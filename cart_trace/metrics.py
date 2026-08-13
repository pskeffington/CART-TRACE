"""Versioned post-infusion utilization metrics for CART-TRACE Phase 4."""

from __future__ import annotations

from typing import Any, Mapping, Sequence

ANALYSIS_START_HOURS = 0.0
ANALYSIS_END_HOURS = 720.0
INPATIENT_STATES = {"routine_inpatient", "intermediate_care", "intensive_care"}
HIGH_ACUITY_STATES = {"intermediate_care", "intensive_care"}
METRIC_VERSION = "0.2.0"


def _clip_duration(interval: Mapping[str, Any], start: float, end: float) -> float | None:
    raw_start = interval.get("start_relative_hours")
    raw_end = interval.get("end_relative_hours")
    if raw_start is None or raw_end is None:
        return None
    clipped_start = max(float(raw_start), start)
    clipped_end = min(float(raw_end), end)
    return max(0.0, clipped_end - clipped_start)


def _unknown_overlap(intervals: Sequence[Mapping[str, Any]]) -> bool:
    for interval in intervals:
        if interval.get("state") != "unknown":
            continue
        duration = _clip_duration(interval, ANALYSIS_START_HOURS, ANALYSIS_END_HOURS)
        if duration is None or duration > 0:
            return True
    return False


def _state_hours(intervals: Sequence[Mapping[str, Any]], states: set[str]) -> float | None:
    total = 0.0
    for interval in intervals:
        if interval.get("state") not in states:
            continue
        duration = _clip_duration(interval, ANALYSIS_START_HOURS, ANALYSIS_END_HOURS)
        if duration is None:
            return None
        total += duration
    return total


def _status_for_scalar(value: Any, *, not_calculable: bool = False) -> str:
    if not_calculable:
        return "not_calculable"
    if value in (0, 0.0, False):
        return "observed_zero"
    if value is None:
        return "not_applicable"
    return "observed"


def _return_metric(
    first_discharge: float | None,
    return_times: Sequence[float],
    horizon_hours: float,
    observation_end_relative_hours: float,
) -> tuple[bool | None, str]:
    """Classify post-discharge return with explicit follow-up sufficiency.

    An observed qualifying return establishes a positive result even when the
    full negative-ascertainment horizon is not available. A negative result is
    emitted only when observation extends through the complete horizon after
    the qualifying discharge.
    """
    if first_discharge is None:
        return None, "not_applicable"

    qualifying = [
        value for value in return_times
        if first_discharge <= value <= first_discharge + horizon_hours
    ]
    if qualifying:
        return True, "observed"

    required_end = first_discharge + horizon_hours
    if observation_end_relative_hours >= required_end:
        return False, "observed_zero"
    return None, "incomplete_followup"


def compute_utilization_metrics(
    intervals: Sequence[Mapping[str, Any]],
    transitions: Sequence[Mapping[str, Any]],
    *,
    observation_end_relative_hours: float = ANALYSIS_END_HOURS,
) -> dict[str, Any]:
    """Compute Phase 4 metrics from canonical trajectory objects.

    Primary utilization duration is clipped to [0,720) hours after infusion.
    Negative acute-care-return results additionally require complete follow-up
    through the requested horizon after discharge. Positive observed returns
    remain valid even if later follow-up is incomplete.
    """
    unknown_present = _unknown_overlap(intervals)

    routine = None if unknown_present else _state_hours(intervals, {"routine_inpatient"})
    intermediate = None if unknown_present else _state_hours(intervals, {"intermediate_care"})
    intensive = None if unknown_present else _state_hours(intervals, {"intensive_care"})
    high_acuity = None if unknown_present else _state_hours(intervals, HIGH_ACUITY_STATES)
    inpatient = None if unknown_present else _state_hours(intervals, INPATIENT_STATES)
    unknown_hours = _state_hours(intervals, {"unknown"})

    in_window_transitions = [
        transition
        for transition in transitions
        if ANALYSIS_START_HOURS <= float(transition["relative_time_hours"]) < ANALYSIS_END_HOURS
    ]

    escalation_times = [
        float(t["relative_time_hours"])
        for t in in_window_transitions
        if t.get("transition_type") == "escalation"
    ]
    discharge_times = [
        float(t["relative_time_hours"])
        for t in in_window_transitions
        if t.get("transition_type") == "discharge"
    ]
    return_times = [
        float(t["relative_time_hours"])
        for t in in_window_transitions
        if t.get("transition_type") == "acute_care_return"
    ]

    first_discharge = min(discharge_times) if discharge_times else None
    first_return = min(return_times) if return_times else None
    hours_from_discharge_to_return = (
        first_return - first_discharge
        if first_discharge is not None and first_return is not None and first_return >= first_discharge
        else None
    )

    return_7d, return_7d_status = _return_metric(
        first_discharge, return_times, 168.0, observation_end_relative_hours
    )
    return_30d, return_30d_status = _return_metric(
        first_discharge, return_times, 720.0, observation_end_relative_hours
    )

    metrics = {
        "metric_version": METRIC_VERSION,
        "total_inpatient_hours": inpatient,
        "routine_inpatient_hours": routine,
        "intermediate_care_hours": intermediate,
        "intensive_care_hours": intensive,
        "high_acuity_hours": high_acuity,
        "transition_count": len(in_window_transitions),
        "time_to_first_escalation_hours": min(escalation_times) if escalation_times else None,
        "time_to_discharge_hours": first_discharge,
        "acute_care_reuse_7d": return_7d,
        "acute_care_reuse_30d": return_30d,
        "hours_from_discharge_to_return": hours_from_discharge_to_return,
        "unknown_state_hours": unknown_hours,
        "missingness_reason": (
            "unknown interval prevents complete state-specific duration calculation"
            if unknown_present
            else None
        ),
    }
    metrics["metric_status"] = {
        "total_inpatient_hours": _status_for_scalar(inpatient, not_calculable=unknown_present),
        "routine_inpatient_hours": _status_for_scalar(routine, not_calculable=unknown_present),
        "intermediate_care_hours": _status_for_scalar(intermediate, not_calculable=unknown_present),
        "intensive_care_hours": _status_for_scalar(intensive, not_calculable=unknown_present),
        "high_acuity_hours": _status_for_scalar(high_acuity, not_calculable=unknown_present),
        "transition_count": _status_for_scalar(len(in_window_transitions)),
        "time_to_first_escalation_hours": _status_for_scalar(metrics["time_to_first_escalation_hours"]),
        "time_to_discharge_hours": _status_for_scalar(first_discharge),
        "acute_care_reuse_7d": return_7d_status,
        "acute_care_reuse_30d": return_30d_status,
        "hours_from_discharge_to_return": _status_for_scalar(hours_from_discharge_to_return),
        "unknown_state_hours": _status_for_scalar(unknown_hours),
    }
    return metrics
