import json
from pathlib import Path

import pytest

from cart_trace.reconstruction import load_mapping_config, reconstruct_episode

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "examples" / "synthetic"
CONFIG = load_mapping_config(ROOT / "config" / "synthetic_care_state_mapping.json")

FIXTURE_PATHS = [
    FIXTURES / "phase2_routine_recovery.json",
    FIXTURES / "phase2_prolonged_routine.json",
    FIXTURES / "phase2_transient_escalation.json",
    FIXTURES / "phase2_icu_escalation.json",
    FIXTURES / "phase2_early_return.json",
    FIXTURES / "phase2_conflicting_location.json",
]


def load_json(path: Path):
    return json.loads(path.read_text())


def interval_signature(interval):
    return (
        interval["state"],
        interval["start_timestamp"],
        interval["end_timestamp"],
        interval["start_relative_hours"],
        interval["end_relative_hours"],
        interval["mapping_method"],
        interval["uncertain"],
    )


def transition_signature(transition):
    return (
        transition["from_state"],
        transition["to_state"],
        transition["transition_timestamp"],
        transition["relative_time_hours"],
        transition["transition_type"],
        transition["uncertain"],
    )


@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_reconstruction_matches_frozen_interval_oracle(path):
    data = load_json(path)
    result = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    assert [interval_signature(item) for item in result["intervals"]] == [
        interval_signature(item) for item in data["expected_intervals"]
    ]


@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_reconstruction_matches_frozen_transition_oracle(path):
    data = load_json(path)
    result = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    assert [transition_signature(item) for item in result["transitions"]] == [
        transition_signature(item) for item in data["expected_transitions"]
    ]


def test_reconstruction_is_deterministic_under_input_reordering():
    data = load_json(FIXTURES / "phase2_icu_escalation.json")
    forward = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    reverse = reconstruct_episode(data["episode"], list(reversed(data["encounters"])), CONFIG)
    assert forward == reverse


def test_duplicate_same_state_records_do_not_create_transition():
    boundary = load_json(FIXTURES / "phase2_boundary_cases.json")
    case = next(item for item in boundary["cases"] if item["case_id"] == "DUPLICATE-SAME-STATE-001")
    episode = {
        "episode_id": "SYN-BOUNDARY-DUP",
        "infusion_timestamp": "2026-04-01T10:00:00Z",
        "window_end_timestamp": "2026-04-01T18:00:00Z",
    }
    result = reconstruct_episode(episode, case["encounters"], CONFIG)
    assert [item["state"] for item in result["intervals"]] == ["routine_inpatient"]
    assert result["transitions"] == []
    assert result["intervals"][0]["mapping_method"] == "duplicate_same_state_collapse"


def test_open_end_remains_explicit_and_uncertain():
    boundary = load_json(FIXTURES / "phase2_boundary_cases.json")
    case = next(item for item in boundary["cases"] if item["case_id"] == "MISSING-END-001")
    episode = {
        "episode_id": "SYN-BOUNDARY-OPEN",
        "infusion_timestamp": "2026-04-01T10:00:00Z",
        "window_end_timestamp": "2026-05-01T10:00:00Z",
    }
    result = reconstruct_episode(episode, case["encounters"], CONFIG)
    interval = result["intervals"][0]
    assert interval["end_timestamp"] is None
    assert interval["end_relative_hours"] is None
    assert interval["open_end_reason"] == "source_end_missing"
    assert interval["uncertain"] is True


def test_same_day_return_is_transition_not_state():
    data = load_json(FIXTURES / "phase2_early_return.json")
    result = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    assert "acute_care_return" not in {item["state"] for item in result["intervals"]}
    transition = next(item for item in result["transitions"] if item["transition_type"] == "acute_care_return")
    assert transition["from_state"] == "discharged"
    assert transition["to_state"] == "emergency"


def test_conflicting_equal_priority_sources_produce_unknown():
    data = load_json(FIXTURES / "phase2_conflicting_location.json")
    result = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    conflict = next(item for item in result["intervals"] if item["state"] == "unknown")
    assert conflict["mapping_method"] == "equal_priority_conflict_to_unknown"
    assert conflict["uncertain"] is True
    assert set(conflict["source_record_ids"]) == {"SRC-CONFLICT-002", "SRC-CONFLICT-003"}
