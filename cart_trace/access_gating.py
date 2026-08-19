"""Deterministic synthetic reconstruction for the CART-TRACE access-gating extension.

This module is intentionally non-operational. It reconstructs retrospective
administrative access states from synthetic event streams and must not be used
to determine patient eligibility, insurance coverage, or treatment readiness.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

ACCESS_GATING_VERSION = "0.1.0"

DENIAL_STATUSES = {
    "denied_medical_necessity",
    "denied_benefit_exclusion",
    "denied_network_or_site",
    "denied_missing_authorization",
    "final_denial",
}


def _ordered(events: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return sorted(events, key=lambda event: (float(event["hour"]), str(event.get("event_id", ""))))


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


def reconstruct_access_case(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Derive deterministic administrative access outcomes from synthetic events."""
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
                and float(event["hour"]) >= float(submitted["hour"])
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
            result["authorization_turnaround_hours"] = float(first_decision["hour"]) - float(submitted["hour"])

    if info_request is not None:
        resubmission = next(
            (
                event
                for event in ordered
                if event.get("gate_id") == "A5"
                and event.get("status") == "submitted_pending"
                and float(event["hour"]) > float(info_request["hour"])
            ),
            None,
        )
        if resubmission is not None:
            result["information_request_delay_hours"] = float(resubmission["hour"]) - float(info_request["hour"])

    if first_denial is not None and overturn is not None:
        result["appeal_or_reconsideration_delay_hours"] = float(overturn["hour"]) - float(first_denial["hour"])

    if financial_pending is not None and financial_satisfied is not None:
        result["financial_clearance_delay_hours"] = float(financial_satisfied["hour"]) - float(financial_pending["hour"])

    if referral is not None and terminal_a8 is not None:
        elapsed = float(terminal_a8["hour"]) - float(referral["hour"])
        if terminal_a8.get("status") == "satisfied":
            result["referral_to_access_ready_hours"] = elapsed
        elif terminal_a8.get("status") == "not_satisfied":
            result["referral_to_terminal_hours"] = elapsed

    return result


def expected_subset_matches(result: Mapping[str, Any], expected: Mapping[str, Any]) -> bool:
    """Return True when every frozen oracle expectation matches the derived result."""
    return all(result.get(key) == value for key, value in expected.items())
