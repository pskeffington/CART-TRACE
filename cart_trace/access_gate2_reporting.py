"""Deterministic Gate 2B readiness report generation.

This module renders metadata-only readiness results. It must not process patient
records or be used for clinical, payer, or treatment decisions.
"""

from __future__ import annotations

from typing import Any, Mapping

from cart_trace.access_gate2_readiness import validate_gate2b_source_set

REPORT_VERSION = "0.1.0"


def build_gate2b_readiness_report(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Build a stable machine-readable report from readiness metadata."""
    result = validate_gate2b_source_set(payload["sources"])
    source_results = sorted(
        result["source_results"],
        key=lambda item: str(item.get("source_inventory_id") or ""),
    )
    blockers = sorted(
        {
            blocker
            for source in source_results
            for blocker in source.get("hard_blockers", [])
        }
    )
    return {
        "report_version": REPORT_VERSION,
        "readiness_input_version": payload.get("readiness_input_version"),
        "gate2b_entry_status": result["gate2b_entry_status"],
        "ready_for_governed_sample_review": result["ready_for_governed_sample_review"],
        "source_count": result["source_count"],
        "aggregate_hard_blockers": blockers,
        "source_results": source_results,
        "scope_statement": (
            "Metadata-only retrospective research readiness assessment; "
            "not clinical eligibility, payer adjudication, or treatment readiness."
        ),
    }


def render_gate2b_readiness_markdown(report: Mapping[str, Any]) -> str:
    """Render a stable human-readable readiness summary."""
    lines = [
        "# CART-TRACE Gate 2B Readiness Report",
        "",
        f"**Report version:** {report['report_version']}",
        f"**Input version:** {report.get('readiness_input_version')}",
        f"**Gate 2B entry status:** {report['gate2b_entry_status']}",
        f"**Ready for governed sample review:** {str(report['ready_for_governed_sample_review']).lower()}",
        f"**Source count:** {report['source_count']}",
        "",
        "## Aggregate blockers",
        "",
    ]
    blockers = report.get("aggregate_hard_blockers", [])
    if blockers:
        lines.extend(f"- {item}" for item in blockers)
    else:
        lines.append("- none")

    lines.extend(["", "## Source results", ""])
    for source in report.get("source_results", []):
        lines.extend(
            [
                f"### {source.get('source_inventory_id')}",
                f"- classification: {source['classification']}",
                f"- ready_for_governed_sample_review: {str(source['ready_for_governed_sample_review']).lower()}",
                f"- hard_blockers: {', '.join(source.get('hard_blockers', [])) or 'none'}",
                f"- below_threshold: {', '.join(source.get('below_threshold', [])) or 'none'}",
                f"- observability_defects: {'; '.join(source.get('observability_defects', [])) or 'none'}",
                "",
            ]
        )

    lines.extend(["## Scope", "", report["scope_statement"], ""])
    return "\n".join(lines)
