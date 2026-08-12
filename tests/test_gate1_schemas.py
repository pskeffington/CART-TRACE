import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


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
    jsonschema.validate(
        fixture["therapy_episode"],
        schema,
        format_checker=jsonschema.FormatChecker(),
    )


def test_encounter_input_schema():
    fixture = load_json("examples/synthetic/gate1_multi_encounter_episode.json")
    schema = load_json("schemas/encounter_input.schema.json")
    for encounter in fixture["encounters"]:
        jsonschema.validate(
            encounter,
            schema,
            format_checker=jsonschema.FormatChecker(),
        )


def test_expected_interval_truth_set_schema():
    validate_many(
        "schemas/care_state_interval.schema.json",
        "examples/synthetic/gate1_expected_intervals.json",
    )


def test_expected_transition_truth_set_schema():
    validate_many(
        "schemas/care_transition.schema.json",
        "examples/synthetic/gate1_expected_transitions.json",
    )


def test_provenance_truth_set_schema():
    validate_many(
        "schemas/provenance.schema.json",
        "examples/synthetic/gate1_provenance.json",
    )


def test_transition_vocabulary_matches_interval_vocabulary():
    interval_schema = load_json("schemas/care_state_interval.schema.json")
    transition_schema = load_json("schemas/care_transition.schema.json")

    interval_states = set(interval_schema["properties"]["state"]["enum"])
    from_states = set(transition_schema["properties"]["from_state"]["enum"])
    to_states = set(transition_schema["properties"]["to_state"]["enum"])

    assert interval_states == from_states == to_states


def test_mapping_targets_only_canonical_states():
    interval_schema = load_json("schemas/care_state_interval.schema.json")
    mapping = load_json("config/synthetic_care_state_mapping.json")
    canonical_states = set(interval_schema["properties"]["state"]["enum"])

    for rule in mapping["rules"]:
        assert rule["canonical_state"] in canonical_states
