import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
FIXTURES = ROOT / "examples" / "synthetic"


def load_json(path: Path):
    return json.loads(path.read_text())


def validator(schema_name: str):
    schema = load_json(SCHEMAS / schema_name)
    return Draft202012Validator(schema, format_checker=FormatChecker())


MANIFEST = load_json(FIXTURES / "fixture_manifest.json")

FIXTURE_FILES = {
    "routine_recovery": FIXTURES / "phase2_routine_recovery.json",
    "prolonged_routine_inpatient": FIXTURES / "phase2_prolonged_routine_inpatient.json",
    "transient_escalation": FIXTURES / "phase2_transient_escalation.json",
    "icu_escalation": FIXTURES / "gate1_multi_encounter_episode.json",
    "early_acute_care_return": FIXTURES / "phase2_early_acute_care_return.json",
    "conflicting_or_missing_location": FIXTURES / "phase2_conflicting_missing_location.json",
}

REQUIRED_CLASSES = set(FIXTURE_FILES)


def test_manifest_contains_all_required_trajectory_classes():
    names = {item["name"] for item in MANIFEST["fixtures"]}
    assert REQUIRED_CLASSES <= names


def test_manifest_fixture_ids_are_unique():
    ids = [item["fixture_id"] for item in MANIFEST["fixtures"]]
    assert len(ids) == len(set(ids))


def test_all_registered_fixture_files_exist():
    for name, path in FIXTURE_FILES.items():
        assert path.exists(), f"Missing fixture for {name}: {path}"


def test_manifest_entries_have_requirement_coverage():
    for item in MANIFEST["fixtures"]:
        assert item.get("requirements"), f"Fixture {item['name']} lacks requirement coverage"
        assert all(isinstance(req, str) and req for req in item["requirements"])


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
def test_schema_conformant_expected_outputs_where_declared(name, path):
    data = load_json(path)
    interval_validator = validator("care_state_interval.schema.json")
    transition_validator = validator("care_transition.schema.json")

    for interval in _expected_intervals(data):
        if "start_timestamp" in interval:
            interval_validator.validate(interval)

    for transition in _expected_transitions(data):
        if "transition_time" in transition:
            transition_validator.validate(transition)


@pytest.mark.parametrize("name,path", FIXTURE_FILES.items())
def test_fixture_has_expected_metrics_or_gate1_metric_deferment(name, path):
    data = load_json(path)
    if name == "icu_escalation":
        # Gate 1 seed predates the Phase 2 metric truth-set convention.
        # Its metrics are tracked separately until the fixture is normalized.
        assert data.get("expected_canonical_intervals")
    else:
        metrics = data.get("expected_metrics")
        assert isinstance(metrics, dict) and metrics, f"{name} fixture lacks expected metrics"


def test_conflict_fixture_exposes_uncertainty():
    data = load_json(FIXTURE_FILES["conflicting_or_missing_location"])
    intervals = _expected_intervals(data)
    assert any(interval["state"] == "unknown" for interval in intervals)
    assert any(interval.get("uncertain") is True for interval in intervals)


def test_early_return_fixture_encodes_reuse():
    data = load_json(FIXTURE_FILES["early_acute_care_return"])
    metrics = data["expected_metrics"]
    assert metrics["acute_care_reuse_7d"] is True
    assert metrics["acute_care_reuse_30d"] is True


def test_routine_fixture_encodes_no_escalation_or_reuse():
    data = load_json(FIXTURE_FILES["routine_recovery"])
    metrics = data["expected_metrics"]
    assert metrics["time_to_first_escalation_hours"] is None
    assert metrics["acute_care_reuse_7d"] is False
    assert metrics["acute_care_reuse_30d"] is False
