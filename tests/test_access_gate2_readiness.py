import json
from pathlib import Path

from cart_trace.access_gate2_readiness import (
    classify_source_readiness,
    validate_gate2b_source_set,
    validate_observability_rows,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = json.loads((ROOT / "examples" / "synthetic" / "access_gate_2b_readiness_fixtures.json").read_text())


def source(source_id):
    return next(item for item in FIXTURES["sources"] if item["source_inventory_id"] == source_id)


def test_governed_ready_source_passes_entry_gate():
    result = classify_source_readiness(source("SRC-READY-001"))
    assert result["classification"] == "governed-ready"
    assert result["hard_blockers"] == []
    assert result["ready_for_governed_sample_review"] is True


def test_partial_source_does_not_pass_entry_gate():
    result = classify_source_readiness(source("SRC-PARTIAL-001"))
    assert result["classification"] == "partial"
    assert "event_time_observability" in result["below_threshold"]
    assert "status_observability" in result["below_threshold"]
    assert result["ready_for_governed_sample_review"] is False


def test_missing_authorization_is_hard_blocker():
    result = classify_source_readiness(source("SRC-BLOCKED-AUTH"))
    assert result["classification"] == "blocked"
    assert "authorization" in result["hard_blockers"]


def test_source_classification_vocabulary_has_no_reviewable_state():
    allowed = {"blocked", "partial", "governed-ready"}
    for item in FIXTURES["sources"]:
        result = classify_source_readiness(item)
        assert result["classification"] in allowed
        assert result["classification"] != "reviewable"


def test_unsupported_inference_fails_closed():
    result = classify_source_readiness(source("SRC-BLOCKED-INFERENCE"))
    assert result["classification"] == "blocked"
    assert "unsupported_inference" in result["hard_blockers"]
    assert "observability_defect" in result["hard_blockers"]
    assert any("absent/unknown evidence mapped as satisfied" in defect for defect in result["observability_defects"])


def test_phi_export_risk_fails_closed():
    result = classify_source_readiness(source("SRC-BLOCKED-PHI"))
    assert result["classification"] == "blocked"
    assert "phi_export_risk" in result["hard_blockers"]


def test_source_set_requires_every_source_to_be_governed_ready():
    ready = validate_gate2b_source_set([source("SRC-READY-001")])
    mixed = validate_gate2b_source_set([source("SRC-READY-001"), source("SRC-PARTIAL-001")])
    assert ready["gate2b_entry_status"] == "ready"
    assert mixed["gate2b_entry_status"] == "not_ready"


def test_empty_source_set_is_rejected():
    try:
        validate_gate2b_source_set([])
    except ValueError as exc:
        assert "at least one source metadata record" in str(exc)
    else:
        raise AssertionError("empty source set should raise ValueError")


def test_missing_dimension_is_rejected():
    broken = dict(source("SRC-READY-001"))
    broken["scores"] = dict(broken["scores"])
    broken["scores"].pop("linkage")
    try:
        classify_source_readiness(broken)
    except ValueError as exc:
        assert "missing readiness dimensions" in str(exc)
    else:
        raise AssertionError("missing readiness dimension should raise ValueError")


def test_derived_observability_requires_rule_version():
    defects = validate_observability_rows([
        {
            "field_name": "access_ready",
            "observability": "derived",
            "source_inventory_id": "SRC-X",
        }
    ])
    assert any("derived field lacks mapping rule version" in defect for defect in defects)
