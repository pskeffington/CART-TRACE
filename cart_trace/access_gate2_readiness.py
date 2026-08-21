"""Gate 2B metadata-only readiness validation for CART-TRACE.

This module evaluates research-governance and source-observability metadata only.
It must not ingest patient records or be used for clinical, payer, or treatment
readiness decisions.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

READINESS_VERSION = "0.1.0"

DIMENSION_MINIMUMS = {
    "authorization": 4,
    "stewardship": 3,
    "minimum_necessary": 3,
    "event_time_observability": 3,
    "actor_authority": 3,
    "status_observability": 3,
    "provenance": 4,
    "historical_versioning": 3,
    "linkage": 4,
    "missingness": 3,
    "conflict_handling": 3,
    "phi_containment": 4,
    "public_export": 3,
    "reviewer_ownership": 3,
}

HARD_PREREQUISITES = {
    "authorization",
    "provenance",
    "linkage",
    "phi_containment",
}

VALID_OBSERVABILITY = {"direct", "normalized", "partial", "derived", "absent", "unknown"}


def _scores(source: Mapping[str, Any]) -> Mapping[str, Any]:
    scores = source.get("scores")
    if not isinstance(scores, Mapping):
        raise ValueError("source readiness record requires a scores mapping")
    missing = sorted(set(DIMENSION_MINIMUMS) - set(scores))
    if missing:
        raise ValueError(f"missing readiness dimensions: {', '.join(missing)}")
    for dimension, value in scores.items():
        if dimension in DIMENSION_MINIMUMS and (not isinstance(value, int) or value < 0 or value > 4):
            raise ValueError(f"invalid readiness score for {dimension}: {value}")
    return scores


def validate_observability_rows(rows: Sequence[Mapping[str, Any]]) -> list[str]:
    """Return metadata-only observability defects that require review."""
    defects: list[str] = []
    for index, row in enumerate(rows, start=1):
        state = str(row.get("observability", "unknown"))
        if state not in VALID_OBSERVABILITY:
            defects.append(f"row {index}: invalid observability state {state}")
        if row.get("unsupported_inference") is True:
            defects.append(f"row {index}: unsupported inference")
        if state in {"direct", "normalized", "derived"} and not row.get("source_inventory_id"):
            defects.append(f"row {index}: observable field lacks source inventory id")
        if state == "derived" and not row.get("mapping_rule_version"):
            defects.append(f"row {index}: derived field lacks mapping rule version")
        if state in {"absent", "unknown"} and row.get("mapped_as_satisfied") is True:
            defects.append(f"row {index}: absent/unknown evidence mapped as satisfied")
    return defects


def classify_source_readiness(source: Mapping[str, Any]) -> dict[str, Any]:
    """Classify one source from governance/readiness metadata, failing closed."""
    scores = _scores(source)
    observability_defects = validate_observability_rows(source.get("observability_rows", []))

    hard_blockers = [
        dimension
        for dimension in sorted(HARD_PREREQUISITES)
        if int(scores[dimension]) < DIMENSION_MINIMUMS[dimension]
    ]
    if source.get("unsupported_inference_detected") is True:
        hard_blockers.append("unsupported_inference")
    if source.get("phi_export_risk_detected") is True:
        hard_blockers.append("phi_export_risk")
    if observability_defects:
        hard_blockers.append("observability_defect")

    below_threshold = [
        dimension
        for dimension, minimum in DIMENSION_MINIMUMS.items()
        if int(scores[dimension]) < minimum
    ]

    if hard_blockers:
        classification = "blocked"
    elif below_threshold:
        classification = "partial"
    else:
        classification = "governed-ready"

    return {
        "source_inventory_id": source.get("source_inventory_id"),
        "classification": classification,
        "hard_blockers": sorted(set(hard_blockers)),
        "below_threshold": sorted(below_threshold),
        "observability_defects": observability_defects,
        "ready_for_governed_sample_review": classification == "governed-ready",
        "readiness_version": READINESS_VERSION,
    }


def validate_gate2b_source_set(sources: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    """Evaluate whether a source set may enter governed sample review."""
    if not sources:
        raise ValueError("Gate 2B readiness validation requires at least one source metadata record")
    results = [classify_source_readiness(source) for source in sources]
    ready = all(result["ready_for_governed_sample_review"] for result in results)
    return {
        "source_results": results,
        "source_count": len(results),
        "ready_for_governed_sample_review": ready,
        "gate2b_entry_status": "ready" if ready else "not_ready",
        "readiness_version": READINESS_VERSION,
    }
