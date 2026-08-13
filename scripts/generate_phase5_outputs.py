"""Generate deterministic synthetic Phase 5 capstone output artifacts.

Run from the repository root:

    python scripts/generate_phase5_outputs.py

The generator consumes the frozen synthetic fixtures, reconstructs trajectories,
computes versioned metric results, and writes capstone-facing JSON artifacts.
No governed or patient-identifying data are used.
"""

from __future__ import annotations

import json
from pathlib import Path

from cart_trace.metrics import build_metric_result, compute_utilization_metrics
from cart_trace.reconstruction import load_mapping_config, reconstruct_episode
from cart_trace.reporting import (
    build_cohort_metric_summary,
    build_metric_validation_rows,
    build_patient_trajectory_rows,
    build_reconstruction_validation_summary,
    build_uncertainty_summary,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "examples" / "synthetic"
OUTPUT_DIR = ROOT / "examples" / "outputs"
MAPPING = load_mapping_config(ROOT / "config" / "synthetic_care_state_mapping.json")

FIXTURE_FILES = [
    "phase2_routine_recovery.json",
    "phase2_prolonged_routine.json",
    "phase2_transient_escalation.json",
    "phase2_icu_escalation.json",
    "phase2_early_return.json",
    "phase2_conflicting_location.json",
]

COHORT_METRICS = [
    "total_inpatient_hours",
    "routine_inpatient_hours",
    "intermediate_care_hours",
    "intensive_care_hours",
    "high_acuity_hours",
    "transition_count",
    "time_to_first_escalation_hours",
    "time_to_discharge_hours",
    "unknown_state_hours",
    "acute_care_reuse_7d",
    "acute_care_reuse_30d",
]


def _write(name: str, value: object) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / name).write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    )


def main() -> None:
    trajectory_rows: dict[str, list[dict[str, object]]] = {}
    metric_results: list[dict[str, object]] = []
    validation_rows: list[dict[str, object]] = []
    interval_matches: list[bool] = []
    transition_matches: list[bool] = []

    for filename in FIXTURE_FILES:
        fixture = json.loads((FIXTURE_DIR / filename).read_text())
        episode = fixture["episode"]
        reconstructed = reconstruct_episode(episode, fixture["encounters"], MAPPING)
        intervals = reconstructed["intervals"]
        transitions = reconstructed["transitions"]
        episode_id = episode["episode_id"]

        trajectory_rows[episode_id] = build_patient_trajectory_rows(
            episode, intervals, transitions
        )
        result = build_metric_result(episode_id, intervals, transitions)
        metric_results.append(result)

        actual = compute_utilization_metrics(intervals, transitions)
        rows = build_metric_validation_rows(fixture["expected_metrics"], actual)
        for row in rows:
            validation_rows.append({"episode_id": episode_id, **row})

        expected_interval_signature = [
            (
                item["state"],
                item["start_relative_hours"],
                item["end_relative_hours"],
                item["uncertain"],
            )
            for item in fixture["expected_intervals"]
        ]
        actual_interval_signature = [
            (
                item["state"],
                item["start_relative_hours"],
                item["end_relative_hours"],
                item["uncertain"],
            )
            for item in intervals
        ]
        interval_matches.append(actual_interval_signature == expected_interval_signature)

        expected_transition_signature = [
            (
                item["from_state"],
                item["to_state"],
                item["relative_time_hours"],
                item["transition_type"],
            )
            for item in fixture["expected_transitions"]
        ]
        actual_transition_signature = [
            (
                item["from_state"],
                item["to_state"],
                item["relative_time_hours"],
                item["transition_type"],
            )
            for item in transitions
        ]
        transition_matches.append(
            actual_transition_signature == expected_transition_signature
        )

    cohort_summary = build_cohort_metric_summary(metric_results, COHORT_METRICS)
    reconstruction_summary = build_reconstruction_validation_summary(
        interval_matches, transition_matches
    )
    uncertainty_summary = build_uncertainty_summary(trajectory_rows, metric_results)

    _write("phase5_patient_trajectories.json", trajectory_rows)
    _write("phase5_metric_results.json", metric_results)
    _write("phase5_cohort_summary.json", cohort_summary)
    _write("phase5_metric_validation.json", validation_rows)
    _write("phase5_reconstruction_validation.json", reconstruction_summary)
    _write("phase5_uncertainty_summary.json", uncertainty_summary)


if __name__ == "__main__":
    main()
