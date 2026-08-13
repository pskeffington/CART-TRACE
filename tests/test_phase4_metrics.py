import json
from pathlib import Path

import pytest

from cart_trace.metrics import compute_utilization_metrics
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

CORE_KEYS = {
    "total_inpatient_hours",
    "routine_inpatient_hours",
    "intermediate_care_hours",
    "intensive_care_hours",
    "high_acuity_hours",
    "transition_count",
    "time_to_first_escalation_hours",
    "time_to_discharge_hours",
    "acute_care_reuse_7d",
    "acute_care_reuse_30d",
    "unknown_state_hours",
}


def load_json(path: Path):
    return json.loads(path.read_text())


@pytest.mark.parametrize("path", FIXTURE_PATHS)
def test_phase4_metrics_match_post_infusion_fixture_oracle(path):
    data = load_json(path)
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    actual = compute_utilization_metrics(reconstructed["intervals"], reconstructed["transitions"])
    expected = data["expected_metrics"]
    for key in CORE_KEYS:
        assert key in expected, f"{path.name} lacks expected metric {key}"
        assert actual[key] == expected[key], f"{path.name}: mismatch for {key}"

    for key, expected_status in data.get("expected_metric_status", {}).items():
        assert actual["metric_status"][key] == expected_status


def test_preinfusion_context_is_clipped_from_primary_duration():
    data = load_json(FIXTURES / "phase2_routine_recovery.json")
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    metrics = compute_utilization_metrics(reconstructed["intervals"], reconstructed["transitions"])
    assert reconstructed["intervals"][0]["start_relative_hours"] == -2.0
    assert metrics["total_inpatient_hours"] == 98.0
    assert metrics["routine_inpatient_hours"] == 98.0


def test_conflict_preserves_unknown_burden_and_invalidates_duration_metrics():
    data = load_json(FIXTURES / "phase2_conflicting_location.json")
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    metrics = compute_utilization_metrics(reconstructed["intervals"], reconstructed["transitions"])
    assert metrics["unknown_state_hours"] == 8.0
    assert metrics["total_inpatient_hours"] is None
    assert metrics["routine_inpatient_hours"] is None
    assert metrics["high_acuity_hours"] is None
    assert metrics["metric_status"]["total_inpatient_hours"] == "not_calculable"
    assert metrics["missingness_reason"] == "unknown interval prevents complete state-specific duration calculation"


def test_early_return_uses_discharge_relative_elapsed_time():
    data = load_json(FIXTURES / "phase2_early_return.json")
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    metrics = compute_utilization_metrics(reconstructed["intervals"], reconstructed["transitions"])
    assert metrics["hours_from_discharge_to_return"] == 93.0
    assert metrics["acute_care_reuse_7d"] is True
    assert metrics["acute_care_reuse_30d"] is True
    assert metrics["metric_status"]["acute_care_reuse_7d"] == "observed"
    assert metrics["metric_status"]["acute_care_reuse_30d"] == "observed"


def test_negative_return_requires_complete_horizon_after_discharge():
    data = load_json(FIXTURES / "phase2_routine_recovery.json")
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)

    limited = compute_utilization_metrics(
        reconstructed["intervals"], reconstructed["transitions"], observation_end_relative_hours=720.0
    )
    assert limited["acute_care_reuse_7d"] is False
    assert limited["metric_status"]["acute_care_reuse_7d"] == "observed_zero"
    assert limited["acute_care_reuse_30d"] is None
    assert limited["metric_status"]["acute_care_reuse_30d"] == "incomplete_followup"

    complete = compute_utilization_metrics(
        reconstructed["intervals"], reconstructed["transitions"], observation_end_relative_hours=818.0
    )
    assert complete["acute_care_reuse_30d"] is False
    assert complete["metric_status"]["acute_care_reuse_30d"] == "observed_zero"


def test_positive_return_does_not_require_complete_negative_ascertainment_horizon():
    data = load_json(FIXTURES / "phase2_early_return.json")
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    metrics = compute_utilization_metrics(
        reconstructed["intervals"], reconstructed["transitions"], observation_end_relative_hours=200.0
    )
    assert metrics["acute_care_reuse_7d"] is True
    assert metrics["acute_care_reuse_30d"] is True
    assert metrics["metric_status"]["acute_care_reuse_30d"] == "observed"
