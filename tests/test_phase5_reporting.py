import json
from pathlib import Path

from cart_trace.metrics import build_metric_result
from cart_trace.reconstruction import load_mapping_config, reconstruct_episode
from cart_trace.reporting import (
    build_cohort_metric_summary,
    build_metric_validation_rows,
    build_patient_trajectory_rows,
    build_reconstruction_validation_summary,
    build_uncertainty_summary,
)

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


def reconstructed_and_metric_result(path: Path):
    data = load_json(path)
    reconstructed = reconstruct_episode(data["episode"], data["encounters"], CONFIG)
    result = build_metric_result(
        data["episode"],
        reconstructed["intervals"],
        reconstructed["transitions"],
    )
    return data, reconstructed, result


def test_patient_trajectory_rows_preserve_state_order_and_transition_context():
    data, reconstructed, _ = reconstructed_and_metric_result(FIXTURES / "phase2_icu_escalation.json")
    rows = build_patient_trajectory_rows(data["episode"], reconstructed["intervals"], reconstructed["transitions"])
    assert [row["state"] for row in rows] == [
        "routine_inpatient",
        "intensive_care",
        "routine_inpatient",
        "discharged",
        "emergency",
    ]
    assert rows[1]["transition_into_state"] == "escalation"
    assert rows[2]["transition_into_state"] == "deescalation"
    assert rows[3]["transition_into_state"] == "discharge"
    assert rows[4]["transition_into_state"] == "acute_care_return"


def test_metric_validation_rows_report_exact_fixture_agreement():
    data, _, metric_result = reconstructed_and_metric_result(FIXTURES / "phase2_transient_escalation.json")
    actual = {**metric_result["values"], "metric_status": metric_result["status"]}
    rows = build_metric_validation_rows(data["expected_metrics"], actual)
    assert rows
    assert all(row["exact_match"] for row in rows)


def test_reconstruction_validation_summary_reports_perfect_synthetic_fidelity():
    summary = build_reconstruction_validation_summary([True] * 6, [True] * 6)
    assert summary["interval_exact_agreement_fraction"] == 1.0
    assert summary["transition_exact_agreement_fraction"] == 1.0


def test_cohort_metric_summary_reports_denominators_and_incomplete_followup():
    metric_results = []
    for path in FIXTURE_PATHS:
        _, _, result = reconstructed_and_metric_result(path)
        metric_results.append(result)

    rows = build_cohort_metric_summary(
        metric_results,
        ["total_inpatient_hours", "acute_care_reuse_30d", "unknown_state_hours"],
    )
    by_metric = {row["metric_id"]: row for row in rows}

    total = by_metric["total_inpatient_hours"]
    assert total["episode_count"] == 6
    assert total["available_count"] == 5
    assert total["not_calculable_count"] == 1

    return_30d = by_metric["acute_care_reuse_30d"]
    assert return_30d["episode_count"] == 6
    assert return_30d["incomplete_followup_count"] >= 1


def test_uncertainty_summary_exposes_conflict_episode_and_metric_statuses():
    trajectory_rows_by_episode = {}
    metric_results = []
    for path in FIXTURE_PATHS:
        data, reconstructed, result = reconstructed_and_metric_result(path)
        trajectory_rows_by_episode[data["episode"]["episode_id"]] = build_patient_trajectory_rows(
            data["episode"], reconstructed["intervals"], reconstructed["transitions"]
        )
        metric_results.append(result)

    summary = build_uncertainty_summary(trajectory_rows_by_episode, metric_results)
    assert summary["episode_count"] == 6
    assert summary["episodes_with_uncertain_or_unknown_state"] == 1
    assert summary["metric_status_counts"].get("not_calculable", 0) > 0
