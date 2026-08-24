"""Synthetic Gate 2 source-to-event mapping for CART-TRACE access research.

This module is a non-operational test harness. It maps synthetic source-like
records into the public access event schema and must not be used to adjudicate
clinical eligibility, payer coverage, financial clearance, or treatment readiness.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

MAPPING_RULE_VERSION = "0.1.1"

SOURCE_CLASS_TO_GATE = {
    "synthetic_referral": "A0",
    "synthetic_program_review": "A2",
    "synthetic_facility_logistics": "A3",
    "synthetic_benefit_network": "A4",
    "synthetic_authorization": "A5",
    "synthetic_medicare_policy_context": "A6",
    "synthetic_financial_clearance": "A7",
    "synthetic_research_derivation": "A8",
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

SOURCE_TYPES = {
    "synthetic_referral": "referral_record",
    "synthetic_program_review": "clinical_note",
    "synthetic_facility_logistics": "derived_research_record",
    "synthetic_benefit_network": "benefit_document",
    "synthetic_authorization": "authorization_record",
    "synthetic_medicare_policy_context": "payer_policy",
    "synthetic_financial_clearance": "financial_record",
    "synthetic_research_derivation": "derived_research_record",
}


def _gate_for(record: Mapping[str, Any]) -> str:
    source_class = str(record["source_class"])
    if source_class not in SOURCE_CLASS_TO_GATE:
        raise ValueError(f"unsupported synthetic source class: {source_class}")

    canonical_gate = SOURCE_CLASS_TO_GATE[source_class]
    asserted_gate = record.get("target_gate")
    if asserted_gate is not None and str(asserted_gate) != canonical_gate:
        raise ValueError(
            f"target_gate {asserted_gate} conflicts with canonical gate {canonical_gate} "
            f"for source class {source_class}"
        )
    return canonical_gate


def _sort_key(record: Mapping[str, Any]) -> tuple[Any, ...]:
    return (
        str(record["source_timestamp"]),
        _gate_for(record),
        str(record.get("source_status", "")),
        str(record.get("facility_requirement_type", "")),
        str(record["synthetic_source_id"]),
    )


def map_synthetic_source_record(record: Mapping[str, Any]) -> dict[str, Any]:
    """Map one synthetic source-like record into an access event schema record."""
    if record.get("synthetic") is not True:
        raise ValueError("Gate 2 synthetic mapper accepts synthetic records only")

    gate_id = _gate_for(record)
    source_class = str(record["source_class"])
    source_timestamp = str(record["source_timestamp"])
    decision_timestamp = record.get("decision_timestamp")
    uncertainty = bool(record.get("uncertainty_flag", decision_timestamp is None))

    return {
        "patient_research_id": f"SYN-{record['synthetic_patient_id']}",
        "access_episode_id": str(record["synthetic_episode_id"]),
        "event_id": str(record["synthetic_source_id"]),
        "gate_id": gate_id,
        "gate_domain": GATE_DOMAINS[gate_id],
        "status": str(record["source_status"]),
        "status_timestamp": source_timestamp,
        "decision_timestamp": decision_timestamp,
        "decision_actor_type": str(record.get("actor_type", "unknown")),
        "source_type": SOURCE_TYPES.get(source_class, "unknown"),
        "source_record_id": str(record["synthetic_source_id"]),
        "payer_name": record.get("payer_name"),
        "plan_product": record.get("plan_product"),
        "line_of_business": record.get("line_of_business"),
        "servicing_administrator": record.get("servicing_administrator"),
        "state_service_area": record.get("state_service_area"),
        "requested_product": record.get("requested_product"),
        "policy_id": record.get("policy_id"),
        "policy_version": record.get("policy_version"),
        "policy_effective_date": record.get("policy_effective_date"),
        "reason_code": record.get("source_status_code"),
        "reason_text_original": None,
        "facility_requirement_type": record.get("facility_requirement_type"),
        "evidence_completeness": str(record.get("evidence_completeness", "complete_for_gate")),
        "uncertainty_flag": uncertainty,
        "provenance": {
            "synthetic": True,
            "rule_version": MAPPING_RULE_VERSION,
            "source_note": f"mapped from {source_class} source version {record.get('source_version', 'unknown')}",
        },
    }


def map_synthetic_source_case(records: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Map a synthetic source case deterministically, independent of input order."""
    return [map_synthetic_source_record(record) for record in sorted(records, key=_sort_key)]
