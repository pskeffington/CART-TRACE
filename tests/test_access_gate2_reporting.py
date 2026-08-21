import json
from pathlib import Path

from jsonschema import Draft202012Validator

from cart_trace.access_gate2_reporting import (
    build_gate2b_readiness_report,
    render_gate2b_readiness_markdown,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas" / "access_gate_2b_readiness_input.schema.json").read_text())
FIXTURES = json.loads((ROOT / "examples" / "synthetic" / "access_gate_2b_readiness_fixtures.json").read_text())


def _case(case_id):
    return next(case for case in FIXTURES["cases"] if case["case_id"] == case_id)


def _payload(case):
    return {
        "readiness_input_version": "0.1.0",
        "sources": case["sources"],
    }


def test_readiness_payloads_validate_against_schema():
    validator = Draft202012Validator(SCHEMA)
    for case in FIXTURES["cases"]:
        validator.validate(_payload(case))


def test_governed_ready_report_is_ready_and_has_no_blockers():
    report = build_gate2b_readiness_report(_payload(_case("G2B-001-governed-ready")))
    assert report["gate2b_entry_status"] == "ready"
    assert report["ready_for_governed_sample_review"] is True
    assert report["aggregate_hard_blockers"] == []


def test_blocked_authorization_report_exposes_blocker():
    report = build_gate2b_readiness_report(_payload(_case("G2B-003-authorization-blocked")))
    assert report["gate2b_entry_status"] == "not_ready"
    assert report["ready_for_governed_sample_review"] is False
    assert "authorization" in report["aggregate_hard_blockers"]


def test_report_output_is_stable_when_source_order_changes():
    case = _case("G2B-001-governed-ready")
    payload = _payload(case)
    first = build_gate2b_readiness_report(payload)
    reordered = dict(payload)
    reordered["sources"] = list(reversed(payload["sources"]))
    second = build_gate2b_readiness_report(reordered)
    assert first == second


def test_markdown_report_contains_scope_and_status():
    report = build_gate2b_readiness_report(_payload(_case("G2B-003-authorization-blocked")))
    rendered = render_gate2b_readiness_markdown(report)
    assert "# CART-TRACE Gate 2B Readiness Report" in rendered
    assert "Gate 2B entry status:** not_ready" in rendered
    assert "authorization" in rendered
    assert "not clinical eligibility" in rendered


def test_phi_export_risk_is_visible_in_report():
    report = build_gate2b_readiness_report(_payload(_case("G2B-005-phi-export-risk")))
    assert "phi_export_risk" in report["aggregate_hard_blockers"]
