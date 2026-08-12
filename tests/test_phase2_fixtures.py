import json
from datetime import datetime
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
FIXTURES = ROOT / "examples" / "synthetic"

CANONICAL_STATES = {
    "outpatient",
    "emergency",
    "routine_inpatient",
    "intermediate_care",
    "intensive_care",
    "discharged",
    "unknown",
}
LEGACY_STATES = {"higher_observation", "icu", "acute_care_return", "inpatient_routine"}


def load_json(path: Path):
    return json.loads(path.read_text())


def validator(schema_name: str):
    schema = load_json(SCHEMAS / schema_name)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def parse_timestamp(value: str):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


MANIFEST = load_json(FIXTURES / "fixture_manifest.json")

FIXTURE_FILES = {
    "routine_recovery": FIXTURES / "phase2_routine_recovery.json",
    "prolonged_routine_inpatient": FIXTURES / "phase2_prolonged_routine.json",
    "transient_escalation": FIXTURES / "phase2_transient_escalation.json",
    "icu_escalation": FIXTURES / "phase2_icu_escalation.json",
    "early_acute_care_return": FIXTURES / "phase2_early_return.json",
    "conflicting_or_missing_location": FIXTURES / "phase2_conflicting_location.json",
}

REQUIRED_CLASSES = set(FIXTURE_FILES)


def test_manifest_contains_all_required_trajectory_classes():
    names = {item["name"] for item in MANIFEST["fixtures"]}
    assert REQUIRED_CLASSES <= names


def test_manifest_fixture_ids_are_unique():
    ids = [item["fixture_id"] for item in MANIFEST["fixtures"]]
    assert len(ids) == len(set(ids))


def test_manifest_artifacts_match_registered_paths():
    for item in MANIFEST["fixtures"]:
        expected = ROOT / item["artifact"]
        assert expected == FIXTURE_FILES[item["name"]]


def test_all_registered_fixture_files_exist():
    for name, path in FIXTURE_FILES.items():
        assert path.exists(), f"Missing fixture for {name}: {path}"


def test_manifest_entries_have_requirement_coverage():
    for item in MANIFEST["fixtures"]:
        assert item.get("requirements"), f"Fixture {item['name']} lacks requirement coverage"
        assert all(isinstance(req, str) and req for req in item["requirements"])


def test_manifest_uses_only_canonical_states():
    for item in MANIFEST["fixtures"]:
        assert set(item["expected_patterns"]) <= CANONICAL_STATES
        assert not (set(item["expected_patterns"]) & LEGACY_STATES)


@pytest.mark.parametrize("name,path", FIXTURE_FILES.items())
def test_episode_and_encounter_objects_validate(name, path):
    data = load_json(path)
    episode = data.get("episode") or data.get("therapy_episode")
    assert episode is not None, f"{name} fixture has no therapy episode object"
    validator("therapy_episode.schema.json").validate(episode)

    encounters = data.get("encounters", [])
    assert encounters, f"{name} fixture has no encounters"
    enc_validator = validator("encounter_input.schema.json")
    for encounter in encounters:
        enc_validator.validate(encounter)


def _expected_intervals(data):
    return data.get("expected_intervals") or data.get("expected_canonical_intervals") or []


def _expected_transitions(data):
    return data.get("expected_transitions") or []


@pytest.mark.parametrize("name,path", FIXTURE_FILES.items())
def test_expected_state_patterns_match_manifest(name, path):
    data = load_json(path)
    intervals = _expected_intervals(data)
    assert intervals, f"{name} fixture has no expected interval truth set"
    actual_states = [interval["state"] for interval in intervals]
    manifest_item = next(item for item in MANIFEST["fixtures"] if item["name"] == name)
    assert actual_states == manifest_item["expected_patterns"]


@pytest.mark.parametrize("name,path", FIXTURE_FILES.items())
def test_all_expected_outputs_are_schema_conformant(name, path):
    data = load_json(path)
    interval_validator = validator("care_state_interval.schema.json")
    transition_validator = validator("care_transition.schema.json")

    intervals = _expected_intervals(data)
    transitions = _expected_transitions(data)
    assert intervals, f"{name} fixture has no interval truth set"
    assert transitions, f"{name} fixture has no transition truth set"

    for interval in intervals:
        interval_validator.validate(interval)
    for transition in transitions:
        transition_validator.validate(transition)


def test_all_fixture_outputs_use_only_canonical_states():
    for path in FIXTURE_FILES.values():
        data = load_json(path)
        states = {i["state"] for i in _expected_intervals(data)}
        transition_states = {
            s
            for transition in _expected_transitions(data)
            for s in (transition["from_state"], transition["to_state"])
        }
        assert states <= CANONICAL_STATES
        assert transition_states <= CANONICAL_STATES
        assert not ((states | transition_states) & LEGACY_STATES)


@pytest.mark.parametrize("name,path", FIXTURE_FILES.items())
def test_fixture_has_expected_metrics(name, path):
    data = load_json(path)
    metrics = data.get("expected_metrics")
    assert isinstance(metrics, dict) and metrics, f"{name} fixture lacks expected metrics"
    assert "higher_observation_hours" not in metrics
    assert "icu_hours" not in metrics


def test_conflict_fixture_exposes_uncertainty():
    data = load_json(FIXTURE_FILES["conflicting_or_missing_location"])
    intervals = _expected_intervals(data)
    assert any(interval["state"] == "unknown" for interval in intervals)
    assert any(interval.get("uncertain") is True for interval in intervals)


def test_early_return_fixture_encodes_reuse_and_transition_type():
    data = load_json(FIXTURE_FILES["early_acute_care_return"])
    metrics = data["expected_metrics"]
    assert metrics["acute_care_reuse_7d"] is True
    assert metrics["acute_care_reuse_30d"] is True
    transition = next(t for t in data["expected_transitions"] if t["transition_type"] == "acute_care_return")
    assert transition["from_state"] == "discharged"
    assert transition["to_state"] == "emergency"


def test_routine_fixture_encodes_no_escalation_or_reuse():
    data = load_json(FIXTURE_FILES["routine_recovery"])
    metrics = data["expected_metrics"]
    assert metrics["time_to_first_escalation_hours"] is None
    assert metrics["acute_care_reuse_7d"] is False
    assert metrics["acute_care_reuse_30d"] is False


def test_icu_fixture_encodes_expected_high_acuity_exposure():
    data = load_json(FIXTURE_FILES["icu_escalation"])
    metrics = data["expected_metrics"]
    assert metrics["total_inpatient_hours"] == 78.0
    assert metrics["routine_inpatient_hours"] == 66.0
    assert metrics["intensive_care_hours"] == 12.0
    assert metrics["time_to_first_escalation_hours"] == 32.0
    assert metrics["acute_care_reuse_7d"] is True


def test_invalid_schema_cases_fail_validation():
    cases = load_json(FIXTURES / "invalid_phase2_cases.json")["cases"]
    validators = {
        "care_state_interval": validator("care_state_interval.schema.json"),
        "therapy_episode": validator("therapy_episode.schema.json"),
        "encounter_input": validator("encounter_input.schema.json"),
    }
    for case in cases:
        if case["expected_failure"] != "schema":
            continue
        with pytest.raises(ValidationError):
            validators[case["kind"]].validate(case["record"])


def test_reversed_interval_is_semantically_invalid():
    cases = load_json(FIXTURES / "invalid_phase2_cases.json")["cases"]
    case = next(item for item in cases if item["case_id"] == "REVERSED-INTERVAL-001")
    record = case["record"]
    validator("care_state_interval.schema.json").validate(record)
    assert parse_timestamp(record["end_timestamp"]) <= parse_timestamp(record["start_timestamp"])
    assert record["end_relative_hours"] <= record["start_relative_hours"]


def test_equal_priority_overlap_requires_explicit_conflict_handling():
    cases = load_json(FIXTURES / "invalid_phase2_cases.json")["cases"]
    case = next(item for item in cases if item["case_id"] == "AMBIGUOUS-PRIORITY-001")
    records = case["records"]
    enc_validator = validator("encounter_input.schema.json")
    for record in records:
        enc_validator.validate(record)
    assert records[0]["priority"] == records[1]["priority"]
    assert records[0]["encounter_start"] == records[1]["encounter_start"]
    assert records[0]["encounter_end"] == records[1]["encounter_end"]
    assert sorted(record["source_record_id"] for record in records) == ["SRC-AMB-001", "SRC-AMB-002"]


def test_conflict_fixture_prespecifies_unknown_for_equal_priority_disagreement():
    data = load_json(FIXTURE_FILES["conflicting_or_missing_location"])
    conflict = next(i for i in data["expected_intervals"] if i["state"] == "unknown")
    assert conflict["mapping_method"] == "equal_priority_conflict_to_unknown"
    assert set(conflict["source_record_ids"]) == {"SRC-CONFLICT-002", "SRC-CONFLICT-003"}
