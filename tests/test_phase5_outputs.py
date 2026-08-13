import json
from pathlib import Path

from scripts.generate_phase5_outputs import COHORT_METRICS, FIXTURE_FILES

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "examples" / "outputs"


def load_json(name: str):
    return json.loads((OUTPUT_DIR / name).read_text())


def test_generated_output_files_exist():
    expected = {
        "phase5_patient_trajectories.json",
        "phase5_metric_results.json",
        "phase5_cohort_summary.json",
        "phase5_metric_validation.json",
        "phase5_reconstruction_validation.json",
        "phase5_uncertainty_summary.json",
    }
    assert expected <= {path.name for path in OUTPUT_DIR.glob("phase5_*.json")}


def test_patient_trajectory_output_covers_all_six_fixtures():
    data = load_json("phase5_patient_trajectories.json")
    assert len(data) == len(FIXTURE_FILES) == 6
    assert all(rows for rows in data.values())


def test_metric_result_output_covers_all_six_fixtures():
    data = load_json("phase5_metric_results.json")
    assert len(data) == 6
    assert all(item["analysis_window_relative_hours"] == {"start": 0.0, "end": 720.0, "boundary": "[start,end)"} for item in data)


def test_cohort_summary_has_expected_metrics_and_denominators():
    data = load_json("phase5_cohort_summary.json")
    assert {row["metric_id"] for row in data} == set(COHORT_METRICS)
    assert all(row["episode_count"] == 6 for row in data)


def test_reconstruction_validation_is_exact_for_all_fixtures():
    data = load_json("phase5_reconstruction_validation.json")
    assert data["interval_fixture_count"] == 6
    assert data["transition_fixture_count"] == 6
    assert data["interval_exact_agreement_fraction"] == 1.0
    assert data["transition_exact_agreement_fraction"] == 1.0


def test_metric_validation_has_no_mismatches():
    data = load_json("phase5_metric_validation.json")
    assert data
    assert all(row["exact_match"] is True for row in data)


def test_uncertainty_summary_identifies_conflict_episode():
    data = load_json("phase5_uncertainty_summary.json")
    assert data["episode_count"] == 6
    assert data["episodes_with_uncertain_or_unknown_state"] == 1
    assert data["metric_status_counts"]["not_calculable"] > 0
    assert data["metric_status_counts"]["incomplete_followup"] > 0
