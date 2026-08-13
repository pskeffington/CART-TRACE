"""Transparent Phase 5 reporting helpers for CART-TRACE.

These functions convert validated canonical trajectories and metric results into
simple, deterministic tabular structures suitable for capstone figures and
summary tables. They do not alter frozen reconstruction or metric semantics.
"""

from __future__ import annotations

from collections import Counter
from statistics import mean, median
from typing import Any, Mapping, Sequence


REPORTING_VERSION = "0.1.0"


def build_patient_trajectory_rows(
    episode: Mapping[str, Any],
    intervals: Sequence[Mapping[str, Any]],
    transitions: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Return deterministic interval rows for patient-level trajectory displays."""
    transition_index = {
        float(item["relative_time_hours"]): item
        for item in transitions
        if item.get("relative_time_hours") is not None
    }
    rows: list[dict[str, Any]] = []
    for sequence, interval in enumerate(intervals, start=1):
        start = interval.get("start_relative_hours")
        end = interval.get("end_relative_hours")
        transition = transition_index.get(float(start)) if start is not None else None
        rows.append({
            "episode_id": episode["episode_id"],
            "sequence": sequence,
            "state": interval["state"],
            "start_relative_hours": start,
            "end_relative_hours": end,
            "duration_hours": None if start is None or end is None else float(end) - float(start),
            "transition_into_state": transition.get("transition_type") if transition else None,
            "uncertain": bool(interval.get("uncertain")),
            "source_record_count": len(interval.get("source_record_ids") or []),
        })
    return rows


def build_metric_validation_rows(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Return one row per expected metric with exact-agreement status."""
    rows = []
    for metric_id in sorted(expected):
        if metric_id == "missingness_reason":
            continue
        rows.append({
            "metric_id": metric_id,
            "expected": expected[metric_id],
            "actual": actual.get(metric_id),
            "exact_match": actual.get(metric_id) == expected[metric_id],
            "status": (actual.get("metric_status") or {}).get(metric_id),
        })
    return rows


def build_reconstruction_validation_summary(
    interval_matches: Sequence[bool],
    transition_matches: Sequence[bool],
) -> dict[str, Any]:
    """Summarize exact reconstruction fidelity without approximate scoring."""
    interval_total = len(interval_matches)
    transition_total = len(transition_matches)
    interval_pass = sum(bool(value) for value in interval_matches)
    transition_pass = sum(bool(value) for value in transition_matches)
    return {
        "reporting_version": REPORTING_VERSION,
        "interval_fixture_count": interval_total,
        "interval_fixture_pass_count": interval_pass,
        "interval_exact_agreement_fraction": interval_pass / interval_total if interval_total else None,
        "transition_fixture_count": transition_total,
        "transition_fixture_pass_count": transition_pass,
        "transition_exact_agreement_fraction": transition_pass / transition_total if transition_total else None,
    }


def _numeric_observed(metric_results: Sequence[Mapping[str, Any]], metric_id: str) -> list[float]:
    values: list[float] = []
    for result in metric_results:
        status = result.get("status", {}).get(metric_id)
        value = result.get("values", {}).get(metric_id)
        if status in {"observed", "observed_zero"} and isinstance(value, (int, float)) and not isinstance(value, bool):
            values.append(float(value))
    return values


def build_cohort_metric_summary(
    metric_results: Sequence[Mapping[str, Any]],
    metric_ids: Sequence[str],
) -> list[dict[str, Any]]:
    """Create denominator-aware descriptive summaries from metric-result objects."""
    rows: list[dict[str, Any]] = []
    total_episodes = len(metric_results)
    for metric_id in metric_ids:
        statuses = Counter(result.get("status", {}).get(metric_id) for result in metric_results)
        values = _numeric_observed(metric_results, metric_id)
        rows.append({
            "metric_id": metric_id,
            "episode_count": total_episodes,
            "available_count": statuses.get("observed", 0) + statuses.get("observed_zero", 0),
            "not_applicable_count": statuses.get("not_applicable", 0),
            "not_calculable_count": statuses.get("not_calculable", 0),
            "incomplete_followup_count": statuses.get("incomplete_followup", 0),
            "mean": mean(values) if values else None,
            "median": median(values) if values else None,
            "minimum": min(values) if values else None,
            "maximum": max(values) if values else None,
        })
    return rows


def build_uncertainty_summary(
    trajectory_rows_by_episode: Mapping[str, Sequence[Mapping[str, Any]]],
    metric_results: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Summarize episode-level unknown/uncertain burden and metric availability."""
    uncertain_episodes = 0
    for rows in trajectory_rows_by_episode.values():
        if any(bool(row.get("uncertain")) or row.get("state") == "unknown" for row in rows):
            uncertain_episodes += 1

    status_counts: Counter[str] = Counter()
    for result in metric_results:
        for status in result.get("status", {}).values():
            if status:
                status_counts[status] += 1

    return {
        "reporting_version": REPORTING_VERSION,
        "episode_count": len(trajectory_rows_by_episode),
        "episodes_with_uncertain_or_unknown_state": uncertain_episodes,
        "metric_status_counts": dict(sorted(status_counts.items())),
    }
