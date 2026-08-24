"""Deterministic synthetic reconstruction for the CART-TRACE access-gating extension.

This module is intentionally non-operational. It reconstructs retrospective
administrative access states from synthetic event streams and must not be used
to determine patient eligibility, insurance coverage, or treatment readiness.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Mapping, Sequence

ACCESS_GATING_VERSION = "0.1.0"
ACCESS_METRIC_CONTRACT_VERSION = "1.0.0"

DENIAL_STATUSES = {
    "denied_medical_necessity",
    "denied_benefit_exclusion",
    "denied_network_or_site",
    "denied_missing_authorization",
    "final_denial",
}

GATE_DOMAINS = {
    "A0": "referral",
    "A1": "clinical_review",
    "A2": "clinical_review",
    "A3": "hospital",
    "A4": "network",
    "A5": "payer",
    "A6": "medicare",
    "A7": "financial",
    "A8": "access",
}

DECISION_ACTORS = {
    "A0": "referring_clinician",
    "A1": "dartmouth_program",
    "A2": "dartmouth_program",
    "A3": "dartmouth_program",
    "A4": "benefit_administrator",
    "A5": "payer",
    "A6": "payer",
    "A7": "financial_services",
    "A8": "research_derivation",
}

STATUS_PRECEDENCE = {
    "not_started": 0,
    "required_not_submitted": 10,
    "submitted_pending": 20,
    "additional_information_requested": 30,
    "peer_to_peer_pending": 40,
    "appeal_pending": 50,
    "denied_medical_necessity": 60,
    "denied_benefit_exclusion": 60,
    "denied_network_or_site": 60,
    "denied_missing_authorization": 60,
    "overturned_on_reconsideration_or_appeal": 70,
    "partially_approved": 80,
    "approved": 90,
    "final_denial": 90,
    "expired": 100,
    "pending": 20,
    "satisfied": 90,
    "not_satisfied": 90,
    "not_applicable": 90,
    "unknown": 90,
}


def _parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _event_time(event: Mapping[str, Any]) -> float:
    """Return a comparable hour value for compact or schema-native events."""
    if "hour" in event:
        return float(event["hour"])
    timestamp = event.get("status_timestamp") or event.get("decision_timestamp")
    if timestamp is None:
        raise ValueError("access event requires hour or status/decision timestamp")
    return _parse_timestamp(str(timestamp)).timestamp() / 3600.0


def _elapsed_hours(later: Mapping[str, Any], earlier: Mapping[str, Any]) -> float:
    return _event_time(later) - _event_time(earlier)


def _event_sort_key(event: Mapping[str, Any]) -> tuple[Any, ...]:
    """Return an input-order-independent key with semantic same-time ordering."""
    status = str(event.get("status", ""))
    return (
        _event_time(event),
        str(event.get("gate_id", "")),
        STATUS_PRECEDENCE.get(status, 999),
        status,
        str(event.get("policy_version", "")),
        str(event.get("event_id", "")),
    )


def _ordered(events: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return sorted(events, key=_event_sort_key)


def _first(events: Sequence[Mapping[str, Any]], gate_id: str, status: str) -> Mapping[str, Any] | None:
    return next((event for event in events if event.get("gate_id") == gate_id and event.get("status") == status), None)


def _last_gate(events: Sequence[Mapping[str, Any]], gate_id: str) -> Mapping[str, Any] | None:
    matches = [event for event in events if event.get("gate_id") == gate_id]
    return matches[-1] if matches else None


def _first_denial(events: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    return next(
        (
            event
            for event in events
            if event.get("gate_id") == "A5" and event.get("status") in DENIAL_STATUSES - {"final_denial"}
        ),
        None,
    )


def _primary_barrier(events: Sequence[Mapping[str, Any]], policy_drift: bool) -> str | None:
    statuses = [event.get("status") for event in events]
    if policy_drift:
        return "policy_change_during_episode"
    if "denied_benefit_exclusion" in statuses:
        return "denied_benefit_exclusion"
    if "denied_network_or_site" in statuses:
        return "denied_network_or_site"
    if "expired" in statuses:
        return "authorization_expired"
    if "appeal_pending" in statuses:
        return "appeal_delay"
    if "peer_to_peer_pending" in statuses and "denied_medical_necessity" in statuses:
        return "initial_medical_necessity_denial"
    if "denied_medical_necessity" in statuses:
        return "denied_medical_necessity"
    if "additional_information_requested" in statuses:
        return "additional_information_requested"
    if any(event.get("gate_id") == "A7" and event.get("status") == "pending" for event in events):
        return "financial_clearance_delay"
    return None


def _iso_from_anchor(anchor_time: str, hour: float) -> str:
    anchor = datetime.fromisoformat(anchor_time.replace("Z", "+00:00"))
    if anchor.tzinfo is None:
        anchor = anchor.replace(tzinfo=timezone.utc)
    return (anchor + timedelta(hours=float(hour))).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def materialize_access_event(
    case_id: str,
    event_index: int,
    compact_event: Mapping[str, Any],
    anchor_time: str,
) -> dict[str, Any]:
    """Expand one compact oracle event into a schema-conformant synthetic record."""
    gate_id = str(compact_event["gate_id"])
    timestamp = _iso_from_anchor(anchor_time, float(compact_event["hour"]))
    policy_version = compact_event.get("policy_version")
    return {
        "patient_research_id": f"SYN-{case_id}",
        "access_episode_id": case_id,
        "event_id": f"{case_id}-E{event_index:03d}",
        "gate_id": gate_id,
        "gate_domain": GATE_DOMAINS[gate_id],
        "status": compact_event["status"],
        "status_timestamp": timestamp,
        "decision_timestamp": timestamp,
        "decision_actor_type": DECISION_ACTORS[gate_id],
        "source_type": "synthetic_fixture",
        "source_record_id": f"SYN-{case_id}-SRC-{event_index:03d}",
        "payer_name": "synthetic_payer" if gate_id in {"A4", "A5", "A6"} else None,
        "plan_product": "synthetic_plan" if gate_id in {"A4", "A5", "A6"} else None,
        "line_of_business": "synthetic" if gate_id in {"A4", "A5", "A6"} else None,
        "servicing_administrator": "synthetic_administrator" if gate_id in {"A4", "A5", "A6"} else None,
        "state_service_area": "NH" if gate_id in {"A4", "A5", "A6"} else None,
        "requested_product": "synthetic_car_t" if gate_id in {"A1", "A2", "A3", "A5", "A6"} else None,
        "policy_id": "SYN-POLICY" if policy_version is not None else None,
        "policy_version": policy_version,
        "policy_effective_date": "2026-01-01" if policy_version is not None else None,
        "reason_code": None,
        "reason_text_original": None,
        "facility_requirement_type": None,
        "evidence_completeness": "complete_for_gate",
        "uncertainty_flag": False,
        "provenance": {
            "synthetic": True,
            "rule_version": ACCESS_GATING_VERSION,
            "source_note": "materialized from compact access-gating oracle event",
        },
    }


def materialize_access_case(case: Mapping[str, Any], anchor_time: str) -> list[dict[str, Any]]:
    """Materialize all compact events for one oracle case in deterministic order."""
    case_id = str(case["case_id"])
    return [
        materialize_access_event(case_id, index, event, anchor_time)
        for index, event in enumerate(_ordered(case["events"]), start=1)
    ]


def reconstruct_access_case(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Derive deterministic administrative access outcomes from compact or schema-native events."""
    if not events:
        raise ValueError("access-gating reconstruction requires at least one event")

    ordered = _ordered(events)
    referral = _first(ordered, "A0", "satisfied")
    terminal_a5 = _last_gate(ordered, "A5")
    terminal_a8 = _last_gate(ordered, "A8")
    submitted = _first(ordered, "A5", "submitted_pending")
    first_denial = _first_denial(ordered)
    overturn = _first(ordered, "A5", "overturned_on_reconsideration_or_appeal")
    info_request = _first(ordered, "A5", "additional_information_requested")
    financial_pending = _first(ordered, "A7", "pending")
    financial_satisfied = _first(ordered, "A7", "satisfied")

    versions: list[str] = []
    for event in ordered:
        version = event.get("policy_version")
        if version is not None and version not in versions:
            versions.append(str(version))
    policy_drift = len(versions) > 1

    result: dict[str, Any] = {
        "terminal_authorization_status": terminal_a5.get("status") if terminal_a5 else None,
        "access_ready": bool(terminal_a8 and terminal_a8.get("status") == "satisfied"),
        "primary_barrier": _primary_barrier(ordered, policy_drift),
        "initial_denial": first_denial is not None,
        "overturned": overturn is not None,
        "policy_versions_observed": versions,
        "policy_drift_flag": policy_drift,
        "event_count": len(ordered),
        "access_gating_version": ACCESS_GATING_VERSION,
    }

    if submitted and terminal_a5 and terminal_a5.get("status") in {
        "approved",
        "denied_medical_necessity",
        "denied_network_or_site",
        "denied_missing_authorization",
        "final_denial",
        "expired",
    }:
        first_decision = next(
            (
                event
                for event in ordered
                if event.get("gate_id") == "A5"
                and _event_time(event) >= _event_time(submitted)
                and event.get("status")
                in {
                    "approved",
                    "denied_medical_necessity",
                    "denied_benefit_exclusion",
                    "denied_network_or_site",
                    "denied_missing_authorization",
                }
            ),
            None,
        )
        if first_decision is not None:
            result["authorization_turnaround_hours"] = _elapsed_hours(first_decision, submitted)

    if info_request is not None:
        resubmission = next(
            (
                event
                for event in ordered
                if event.get("gate_id") == "A5"
                and event.get("status") == "submitted_pending"
                and _event_time(event) > _event_time(info_request)
            ),
            None,
        )
        if resubmission is not None:
            result["information_request_delay_hours"] = _elapsed_hours(resubmission, info_request)

    if first_denial is not None and overturn is not None:
        result["appeal_or_reconsideration_delay_hours"] = _elapsed_hours(overturn, first_denial)

    if financial_pending is not None and financial_satisfied is not None:
        result["financial_clearance_delay_hours"] = _elapsed_hours(financial_satisfied, financial_pending)

    if referral is not None and terminal_a8 is not None:
        elapsed = _elapsed_hours(terminal_a8, referral)
        if terminal_a8.get("status") == "satisfied":
            result["referral_to_access_ready_hours"] = elapsed
        elif terminal_a8.get("status") == "not_satisfied":
            result["referral_to_terminal_hours"] = elapsed

    return result


def _episode_id(events: Sequence[Mapping[str, Any]]) -> str:
    values = {str(event.get("access_episode_id")) for event in events if event.get("access_episode_id")}
    if len(values) == 1:
        return next(iter(values))
    if len(values) > 1:
        raise ValueError("access metric derivation requires one access_episode_id")
    return "synthetic-compact-episode"


def _event_ids(events: Sequence[Mapping[str, Any]]) -> list[str]:
    return [str(event["event_id"]) for event in events if event.get("event_id")]


def _gate_ids(events: Sequence[Mapping[str, Any]]) -> list[str]:
    return list(dict.fromkeys(str(event["gate_id"]) for event in events if event.get("gate_id")))


def _policy_versions(events: Sequence[Mapping[str, Any]]) -> list[str]:
    return list(
        dict.fromkeys(
            str(event["policy_version"])
            for event in events
            if event.get("policy_version") is not None
        )
    )


def _mapping_versions(events: Sequence[Mapping[str, Any]]) -> list[str]:
    versions: list[str] = []
    for event in events:
        provenance = event.get("provenance") or {}
        version = provenance.get("rule_version") if isinstance(provenance, Mapping) else None
        if version is not None and str(version) not in versions:
            versions.append(str(version))
    return versions


def _metric_result(
    episode_id: str,
    metric_id: str,
    status: str,
    value: Any,
    unit: str,
    contributing_events: Sequence[Mapping[str, Any]],
    all_events: Sequence[Mapping[str, Any]],
    missingness_reason: str | None = None,
) -> dict[str, Any]:
    return {
        "access_episode_id": episode_id,
        "metric_id": metric_id,
        "metric_contract_version": ACCESS_METRIC_CONTRACT_VERSION,
        "status": status,
        "value": value,
        "unit": unit,
        "contributing_event_ids": _event_ids(contributing_events),
        "contributing_gate_ids": _gate_ids(contributing_events),
        "policy_versions_observed": _policy_versions(all_events),
        "mapping_rule_versions": _mapping_versions(all_events),
        "synthetic": all(bool((event.get("provenance") or {}).get("synthetic", False)) for event in all_events),
        "uncertainty_flag": any(bool(event.get("uncertainty_flag", False)) for event in contributing_events),
        "missingness_reason": missingness_reason,
    }


def derive_access_metric_results(events: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Return Gate 3 episode-level metric results with explicit provenance and missingness."""
    if not events:
        raise ValueError("access metric derivation requires at least one event")

    ordered = _ordered(events)
    episode_id = _episode_id(ordered)
    referral = _first(ordered, "A0", "satisfied")
    terminal_a8 = _last_gate(ordered, "A8")
    submitted = _first(ordered, "A5", "submitted_pending")
    first_denial = _first_denial(ordered)
    overturn = _first(ordered, "A5", "overturned_on_reconsideration_or_appeal")
    info_request = _first(ordered, "A5", "additional_information_requested")
    financial_pending = _first(ordered, "A7", "pending")
    financial_satisfied = _first(ordered, "A7", "satisfied")

    versions = _policy_versions(ordered)
    policy_drift = len(versions) > 1
    barrier = _primary_barrier(ordered, policy_drift) or "unknown_or_unresolved"
    results: list[dict[str, Any]] = []

    access_ready = bool(terminal_a8 and terminal_a8.get("status") == "satisfied")
    access_events = [event for event in (terminal_a8,) if event is not None]
    results.append(_metric_result(episode_id, "access_ready", "observed", access_ready, "boolean", access_events, ordered))
    results.append(_metric_result(episode_id, "policy_drift_flag", "observed", policy_drift, "boolean", ordered, ordered))
    results.append(_metric_result(episode_id, "primary_barrier", "observed", barrier, "category", ordered, ordered))

    if referral is None:
        results.append(_metric_result(episode_id, "referral_to_access_ready_hours", "not_observable", None, "hours", [], ordered, "missing A0 satisfied referral event"))
        results.append(_metric_result(episode_id, "referral_to_terminal_hours", "not_observable", None, "hours", [], ordered, "missing A0 satisfied referral event"))
    elif terminal_a8 is None:
        results.append(_metric_result(episode_id, "referral_to_access_ready_hours", "insufficient_followup", None, "hours", [referral], ordered, "no explicit A8 terminal event"))
        results.append(_metric_result(episode_id, "referral_to_terminal_hours", "insufficient_followup", None, "hours", [referral], ordered, "no explicit A8 terminal event"))
    else:
        elapsed = _elapsed_hours(terminal_a8, referral)
        status = "observed" if elapsed >= 0 else "invalid_temporal_order"
        if terminal_a8.get("status") == "satisfied":
            results.append(_metric_result(episode_id, "referral_to_access_ready_hours", status, elapsed if elapsed >= 0 else None, "hours", [referral, terminal_a8], ordered, None if elapsed >= 0 else "A8 precedes A0"))
            results.append(_metric_result(episode_id, "referral_to_terminal_hours", "not_applicable", None, "hours", [referral, terminal_a8], ordered, "episode reached access-ready rather than explicit non-progression"))
        elif terminal_a8.get("status") == "not_satisfied":
            results.append(_metric_result(episode_id, "referral_to_access_ready_hours", "not_applicable", None, "hours", [referral, terminal_a8], ordered, "episode ended with explicit A8 not_satisfied"))
            results.append(_metric_result(episode_id, "referral_to_terminal_hours", status, elapsed if elapsed >= 0 else None, "hours", [referral, terminal_a8], ordered, None if elapsed >= 0 else "A8 precedes A0"))
        else:
            results.append(_metric_result(episode_id, "referral_to_access_ready_hours", "unknown", None, "hours", [referral, terminal_a8], ordered, "A8 terminal status is neither satisfied nor not_satisfied"))
            results.append(_metric_result(episode_id, "referral_to_terminal_hours", "unknown", None, "hours", [referral, terminal_a8], ordered, "A8 terminal status is neither satisfied nor not_satisfied"))

    if submitted is None:
        results.append(_metric_result(episode_id, "authorization_turnaround_hours", "not_applicable", None, "hours", [], ordered, "no A5 submitted_pending event"))
    else:
        first_decision = next(
            (
                event for event in ordered
                if event.get("gate_id") == "A5"
                and _event_time(event) >= _event_time(submitted)
                and event.get("status") in {
                    "approved", "denied_medical_necessity", "denied_benefit_exclusion",
                    "denied_network_or_site", "denied_missing_authorization"
                }
            ),
            None,
        )
        if first_decision is None:
            results.append(_metric_result(episode_id, "authorization_turnaround_hours", "insufficient_followup", None, "hours", [submitted], ordered, "no terminal first A5 decision observed"))
        else:
            elapsed = _elapsed_hours(first_decision, submitted)
            results.append(_metric_result(episode_id, "authorization_turnaround_hours", "observed" if elapsed >= 0 else "invalid_temporal_order", elapsed if elapsed >= 0 else None, "hours", [submitted, first_decision], ordered, None if elapsed >= 0 else "A5 decision precedes submission"))

    if info_request is None:
        results.append(_metric_result(episode_id, "information_request_delay_hours", "not_applicable", None, "hours", [], ordered, "no additional-information request observed"))
    else:
        resubmission = next((event for event in ordered if event.get("gate_id") == "A5" and event.get("status") == "submitted_pending" and _event_time(event) > _event_time(info_request)), None)
        if resubmission is None:
            results.append(_metric_result(episode_id, "information_request_delay_hours", "insufficient_followup", None, "hours", [info_request], ordered, "no resubmission observed after information request"))
        else:
            elapsed = _elapsed_hours(resubmission, info_request)
            results.append(_metric_result(episode_id, "information_request_delay_hours", "observed", elapsed, "hours", [info_request, resubmission], ordered))

    if first_denial is None:
        results.append(_metric_result(episode_id, "appeal_or_reconsideration_delay_hours", "not_applicable", None, "hours", [], ordered, "no qualifying initial A5 denial"))
    elif overturn is None:
        results.append(_metric_result(episode_id, "appeal_or_reconsideration_delay_hours", "not_applicable", None, "hours", [first_denial], ordered, "no overturn observed"))
    else:
        elapsed = _elapsed_hours(overturn, first_denial)
        results.append(_metric_result(episode_id, "appeal_or_reconsideration_delay_hours", "observed" if elapsed >= 0 else "invalid_temporal_order", elapsed if elapsed >= 0 else None, "hours", [first_denial, overturn], ordered, None if elapsed >= 0 else "overturn precedes denial"))

    if financial_pending is None:
        results.append(_metric_result(episode_id, "financial_clearance_delay_hours", "not_applicable", None, "hours", [], ordered, "no A7 pending interval"))
    elif financial_satisfied is None:
        results.append(_metric_result(episode_id, "financial_clearance_delay_hours", "insufficient_followup", None, "hours", [financial_pending], ordered, "financial clearance remains unresolved"))
    else:
        elapsed = _elapsed_hours(financial_satisfied, financial_pending)
        results.append(_metric_result(episode_id, "financial_clearance_delay_hours", "observed" if elapsed >= 0 else "invalid_temporal_order", elapsed if elapsed >= 0 else None, "hours", [financial_pending, financial_satisfied], ordered, None if elapsed >= 0 else "financial satisfaction precedes pending state"))

    return results


def expected_subset_matches(result: Mapping[str, Any], expected: Mapping[str, Any]) -> bool:
    """Return True when every frozen oracle expectation matches the derived result."""
    return all(result.get(key) == value for key, value in expected.items())
