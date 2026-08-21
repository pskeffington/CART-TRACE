import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from cart_trace.access_gating import reconstruct_access_case
from cart_trace.access_source_mapping import map_synthetic_source_case

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = json.loads((ROOT / "examples" / "synthetic" / "access_gate_2_source_surrogates.json").read_text())
SCHEMA = json.loads((ROOT / "schemas" / "access_gate_event.schema.json").read_text())


def cases():
    return FIXTURES["cases"]


def test_all_mapped_events_validate_against_access_event_schema():
    validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
    for case in cases():
        mapped = map_synthetic_source_case(case["records"])
        for event in mapped:
            validator.validate(event)
            assert event["provenance"]["synthetic"] is True
            assert event["source_record_id"] == event["event_id"]


def test_mapping_is_input_order_invariant():
    for case in cases():
        forward = map_synthetic_source_case(case["records"])
        reverse = map_synthetic_source_case(list(reversed(case["records"])))
        assert forward == reverse


def test_s2_001_maps_referral_only():
    case = next(c for c in cases() if c["case_id"] == "S2-001-direct-referral")
    mapped = map_synthetic_source_case(case["records"])
    assert [event["gate_id"] for event in mapped] == ["A0"]
    assert reconstruct_access_case(mapped)["access_ready"] is False


def test_s2_002_approval_does_not_create_access_ready():
    case = next(c for c in cases() if c["case_id"] == "S2-002-approval-not-ready")
    mapped = map_synthetic_source_case(case["records"])
    result = reconstruct_access_case(mapped)
    assert [event["gate_id"] for event in mapped] == ["A5"]
    assert result["terminal_authorization_status"] == "approved"
    assert result["access_ready"] is False


def test_s2_003_missing_decision_time_sets_uncertainty():
    case = next(c for c in cases() if c["case_id"] == "S2-003-missing-decision-time")
    mapped = map_synthetic_source_case(case["records"])
    assert mapped[0]["decision_timestamp"] is None
    assert mapped[0]["uncertainty_flag"] is True


def test_s2_004_conflicting_authorization_records_are_preserved():
    case = next(c for c in cases() if c["case_id"] == "S2-004-conflicting-authorization")
    mapped = map_synthetic_source_case(case["records"])
    assert len(mapped) == 2
    assert [event["status"] for event in mapped] == ["approved", "denied_medical_necessity"]
    result = reconstruct_access_case(mapped)
    assert result["terminal_authorization_status"] == "denied_medical_necessity"


def test_s2_005_policy_versions_remain_contemporaneous():
    case = next(c for c in cases() if c["case_id"] == "S2-005-policy-drift")
    mapped = map_synthetic_source_case(case["records"])
    assert [event["policy_version"] for event in mapped] == ["v1", "v2"]
    result = reconstruct_access_case(mapped)
    assert result["policy_versions_observed"] == ["v1", "v2"]
    assert result["policy_drift_flag"] is True


def test_s2_006_network_denial_remains_network_denial():
    case = next(c for c in cases() if c["case_id"] == "S2-006-network-denial")
    mapped = map_synthetic_source_case(case["records"])
    assert mapped[0]["status"] == "denied_network_or_site"
    assert reconstruct_access_case(mapped)["primary_barrier"] == "denied_network_or_site"


def test_s2_007_financial_delay_remains_separate_from_authorization():
    case = next(c for c in cases() if c["case_id"] == "S2-007-financial-delay")
    mapped = map_synthetic_source_case(case["records"])
    assert [event["status"] for event in mapped if event["gate_id"] == "A7"] == ["pending", "satisfied"]
    result = reconstruct_access_case(mapped)
    assert result["terminal_authorization_status"] == "approved"
    assert result["access_ready"] is False


def test_s2_008_program_and_payer_authority_remain_distinct():
    case = next(c for c in cases() if c["case_id"] == "S2-008-program-vs-payer")
    mapped = map_synthetic_source_case(case["records"])
    assert [(event["gate_id"], event["decision_actor_type"]) for event in mapped] == [
        ("A2", "dartmouth_program"),
        ("A5", "payer"),
    ]


def test_s2_009_facility_requirements_remain_typed():
    case = next(c for c in cases() if c["case_id"] == "S2-009-facility-authority")
    mapped = map_synthetic_source_case(case["records"])
    assert [event["facility_requirement_type"] for event in mapped] == [
        "fact_iec_expectation",
        "payer_site_of_care",
    ]


def test_s2_010_missing_financial_source_does_not_infer_a7_or_ready():
    case = next(c for c in cases() if c["case_id"] == "S2-010-unobservable-financial-gate")
    mapped = map_synthetic_source_case(case["records"])
    assert all(event["gate_id"] != "A7" for event in mapped)
    assert reconstruct_access_case(mapped)["access_ready"] is False


def test_non_synthetic_source_is_rejected():
    record = dict(cases()[0]["records"][0])
    record["synthetic"] = False
    try:
        map_synthetic_source_case([record])
    except ValueError as exc:
        assert "synthetic records only" in str(exc)
    else:
        raise AssertionError("non-synthetic source should be rejected")
