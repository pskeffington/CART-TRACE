import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]

CANONICAL_STATES = {
    "outpatient",
    "emergency",
    "routine_inpatient",
    "intermediate_care",
    "intensive_care",
    "discharged",
    "unknown",
}

TRANSITION_TYPES = {
    "admission",
    "transfer",
    "escalation",
    "deescalation",
    "discharge",
    "acute_care_return",
    "other",
    "unknown",
}

LEGACY_CANONICAL_STATES = {"higher_observation", "icu", "acute_care_return", "inpatient_routine"}


def load_json(path: str):
    return json.loads((ROOT / path).read_text())


def validate_many(schema_path: str, data_path: str):
    schema = load_json(schema_path)
    records = load_json(data_path)
    validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)
    validator = validator_cls(schema, format_checker=jsonschema.FormatChecker())
    for record in records:
        validator.validate(record)


def test_therapy_episode_schema():
    fixture = load_json("examples/synthetic/gate1_multi_encounter_episode.json")
    schema = load_json("schemas/therapy_episode.schema.json")
    jsonschema.validate(fixture["therapy_episode"], schema, format_checker=jsonschema.FormatChecker())
    assert "patient_research_id" in fixture["therapy_episode"]
    assert "patient_id" not in fixture["therapy_episode"]
    assert fixture["therapy_episode"]["window_start_relative_hours"] == -168.0
    assert fixture["therapy_episode"]["window_end_relative_hours"] == 720.0


def test_encounter_input_schema():
    fixture = load_json("examples/synthetic/gate1_multi_encounter_episode.json")
    schema = load_json("schemas/encounter_input.schema.json")
    for encounter in fixture["encounters"]:
        jsonschema.validate(encounter, schema, format_checker=jsonschema.FormatChecker())


def test_expected_interval_truth_set_schema():
    validate_many("schemas/care_state_interval.schema.json", "examples/synthetic/gate1_expected_intervals.json")


def test_expected_transition_truth_set_schema():
    validate_many("schemas/care_transition.schema.json", "examples/synthetic/gate1_expected_transitions.json")


def test_provenance_truth_set_schema():
    validate_many("schemas/provenance.schema.json", "examples/synthetic/gate1_provenance.json")


def test_exact_canonical_state_vocabulary():
    interval_schema = load_json("schemas/care_state_interval.schema.json")
    transition_schema = load_json("schemas/care_transition.schema.json")
    interval_states = set(interval_schema["properties"]["state"]["enum"])
    from_states = set(transition_schema["properties"]["from_state"]["enum"])
    to_states = set(transition_schema["properties"]["to_state"]["enum"])
    assert interval_states == from_states == to_states == CANONICAL_STATES
    assert not (interval_states & LEGACY_CANONICAL_STATES)


def test_exact_transition_type_vocabulary():
    transition_schema = load_json("schemas/care_transition.schema.json")
    assert set(transition_schema["properties"]["transition_type"]["enum"]) == TRANSITION_TYPES


def test_mapping_targets_only_canonical_states():
    mapping = load_json("config/synthetic_care_state_mapping.json")
    targets = {rule["canonical_state"] for rule in mapping["rules"]}
    assert targets <= CANONICAL_STATES
    assert not (targets & LEGACY_CANONICAL_STATES)
    emergency = next(rule for rule in mapping["rules"] if rule["source_care_label"] == "synthetic_emergency")
    assert emergency["canonical_state"] == "emergency"


def test_gate1_return_is_event_not_state():
    intervals = load_json("examples/synthetic/gate1_expected_intervals.json")
    transitions = load_json("examples/synthetic/gate1_expected_transitions.json")
    assert intervals[-1]["state"] == "emergency"
    assert transitions[-1]["from_state"] == "discharged"
    assert transitions[-1]["to_state"] == "emergency"
    assert transitions[-1]["transition_type"] == "acute_care_return"


def test_relative_time_is_hour_based():
    intervals = load_json("examples/synthetic/gate1_expected_intervals.json")
    transitions = load_json("examples/synthetic/gate1_expected_transitions.json")
    assert all("start_relative_hours" in interval for interval in intervals)
    assert all("start_day_relative" not in interval for interval in intervals)
    assert all("relative_time_hours" in transition for transition in transitions)
    assert all("relative_day" not in transition for transition in transitions)
