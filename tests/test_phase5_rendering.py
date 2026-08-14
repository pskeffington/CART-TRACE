from __future__ import annotations

import json
from pathlib import Path

from scripts.render_phase5_outputs import render_all


def _write(path: Path, value: object) -> None:
    path.write_text(json.dumps(value))


def test_render_all_preserves_required_phase5_controls(tmp_path: Path) -> None:
    input_dir = tmp_path / "outputs"
    output_dir = tmp_path / "rendered"
    input_dir.mkdir()

    trajectories = {
        "routine": [
            {
                "episode_id": "routine",
                "sequence": 1,
                "state": "routine_inpatient",
                "start_relative_hours": 0,
                "end_relative_hours": 48,
                "duration_hours": 48,
                "transition_into_state": None,
                "uncertain": False,
                "source_record_count": 1,
            }
        ],
        "intermediate": [
            {
                "episode_id": "intermediate",
                "sequence": 1,
                "state": "intermediate_care",
                "start_relative_hours": 24,
                "end_relative_hours": 72,
                "duration_hours": 48,
                "transition_into_state": "escalation",
                "uncertain": False,
                "source_record_count": 1,
            }
        ],
        "intensive": [
            {
                "episode_id": "intensive",
                "sequence": 1,
                "state": "intensive_care",
                "start_relative_hours": 24,
                "end_relative_hours": 96,
                "duration_hours": 72,
                "transition_into_state": "escalation",
                "uncertain": False,
                "source_record_count": 1,
            }
        ],
        "unknown": [
            {
                "episode_id": "unknown",
                "sequence": 1,
                "state": "unknown",
                "start_relative_hours": 10,
                "end_relative_hours": 20,
                "duration_hours": 10,
                "transition_into_state": None,
                "uncertain": True,
                "source_record_count": 2,
            }
        ],
    }
    cohort = [
        {
            "metric_id": "total_inpatient_hours",
            "episode_count": 4,
            "available_count": 3,
            "not_applicable_count": 0,
            "not_calculable_count": 0,
            "incomplete_followup_count": 1,
            "mean": 56.0,
            "median": 48.0,
            "minimum": 48.0,
            "maximum": 72.0,
        }
    ]
    metric_validation = [
        {
            "episode_id": "routine",
            "metric_id": "total_inpatient_hours",
            "expected": 48,
            "actual": 48,
            "exact_match": True,
            "status": "observed",
        }
    ]
    reconstruction = {
        "reporting_version": "0.1.0",
        "interval_fixture_count": 4,
        "interval_fixture_pass_count": 4,
        "interval_exact_agreement_fraction": 1.0,
        "transition_fixture_count": 4,
        "transition_fixture_pass_count": 4,
        "transition_exact_agreement_fraction": 1.0,
    }
    uncertainty = {
        "reporting_version": "0.1.0",
        "episode_count": 4,
        "episodes_with_uncertain_or_unknown_state": 1,
        "metric_status_counts": {
            "incomplete_followup": 1,
            "observed": 3,
        },
    }

    _write(input_dir / "phase5_patient_trajectories.json", trajectories)
    _write(input_dir / "phase5_cohort_summary.json", cohort)
    _write(input_dir / "phase5_metric_validation.json", metric_validation)
    _write(input_dir / "phase5_reconstruction_validation.json", reconstruction)
    _write(input_dir / "phase5_uncertainty_summary.json", uncertainty)

    paths = render_all(input_dir, output_dir)
    assert len(paths) == 6

    table3 = (output_dir / "table3_validation.md").read_text()
    table4 = (output_dir / "table4_cohort_summary.md").read_text()
    table5 = (output_dir / "table5_uncertainty.md").read_text()
    figure2 = (output_dir / "figure2_representative_trajectories.svg").read_text()
    figure3 = (output_dir / "figure3_utilization_availability.svg").read_text()
    figure_s1 = (output_dir / "figure_s1_all_trajectories.svg").read_text()

    assert "Metric expected values" in table3
    assert "Agreement fraction" in table3
    assert "Incomplete follow-up n" in table4
    assert "total_inpatient_hours" in table4
    assert "Episodes with uncertain or unknown state" in table5
    assert "Metric status: incomplete_followup" in table5
    assert "analytic boundary = 720 h" in figure2
    assert "unknown" in figure2
    assert 'stroke-dasharray="5 3"' in figure2
    assert "Synthetic cohort utilization and metric availability" in figure3
    assert "available 3/4" in figure3
    assert "IFU 1" in figure3
    assert "not-calculable" in figure3
    for episode_id in trajectories:
        assert episode_id in figure_s1


def test_render_all_is_content_deterministic(tmp_path: Path) -> None:
    input_dir = tmp_path / "outputs"
    output_a = tmp_path / "rendered-a"
    output_b = tmp_path / "rendered-b"
    input_dir.mkdir()

    _write(
        input_dir / "phase5_patient_trajectories.json",
        {
            "episode": [
                {
                    "episode_id": "episode",
                    "sequence": 1,
                    "state": "routine_inpatient",
                    "start_relative_hours": 0,
                    "end_relative_hours": 24,
                    "duration_hours": 24,
                    "transition_into_state": None,
                    "uncertain": False,
                    "source_record_count": 1,
                }
            ]
        },
    )
    _write(input_dir / "phase5_cohort_summary.json", [])
    _write(input_dir / "phase5_metric_validation.json", [])
    _write(
        input_dir / "phase5_reconstruction_validation.json",
        {
            "interval_fixture_count": 1,
            "interval_fixture_pass_count": 1,
            "interval_exact_agreement_fraction": 1.0,
            "transition_fixture_count": 1,
            "transition_fixture_pass_count": 1,
            "transition_exact_agreement_fraction": 1.0,
        },
    )
    _write(
        input_dir / "phase5_uncertainty_summary.json",
        {
            "episode_count": 1,
            "episodes_with_uncertain_or_unknown_state": 0,
            "metric_status_counts": {},
        },
    )

    render_all(input_dir, output_a)
    render_all(input_dir, output_b)

    assert {
        path.name: path.read_text() for path in output_a.iterdir()
    } == {
        path.name: path.read_text() for path in output_b.iterdir()
    }
