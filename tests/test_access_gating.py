import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from cart_trace.access_gating import (
    expected_subset_matches,
    materialize_access_case,
    reconstruct_access_case,
)

ROOT = Path(__file__).resolve().parents[1]
ORACLE = json.loads((ROOT / "examples" / "synthetic" / "access_gating_oracle.json").read_text())
ACCESS_EVENT_SCHEMA = json.loads((ROOT / "schemas" / "access_gate_event.schema.json").read_text())


def cases():
    return ORACLE["cases"]


def test_all_oracle_cases_match_exact_expected_fields():
    failures = []
    for case in cases():
        result = reconstruct_access_case(case["events"])
        if not expected_subset_matches(result, case["expected"]):
            failures.append((case["case_id"], result, case["expected"]))
    assert failures == []


def test_materialized_events_validate_against_access_event_schema():
    validator = Draft202012Validator(ACCESS_EVENT_SCHEMA, format_checker=FormatChecker())
    for case in cases():
        records = materialize_access_case(case, ORACLE["anchor_time"])
        assert len(records) == len(case["events"])
        for record in records:
            validator.validate(record)
            assert record["provenance"]["synthetic"] is True
            assert record["access_episode_id"] == case["case_id"]
            assert record["patient_research_id"].startswith("SYN-")


def test_materialization_is_deterministic_and_order_invariant():
    case = next(item for item in cases() if item["case_id"] == "AG-002-information-request-delay")
    forward = materialize_access_case(case, ORACLE["anchor_time"])
    reordered_case = dict(case)
    reordered_case["events"] = list(reversed(case["events"]))
    reverse = materialize_access_case(reordered_case, ORACLE["anchor_time"])
    assert forward == reverse


def test_materialized_event_ids_are_unique_within_episode():
    for case in cases():
        records = materialize_access_case(case, ORACLE["anchor_time"])
        ids = [record["event_id"] for record in records]
        assert len(ids) == len(set(ids))


def test_materialized_timestamps_are_monotonic():
    for case in cases():
        records = materialize_access_case(case, ORACLE["anchor_time"])
        timestamps = [record["status_timestamp"] for record in records]
        assert timestamps == sorted(timestamps)


def test_policy_drift_materialization_preserves_contemporaneous_versions():
    case = next(item for item in cases() if item["case_id"] == "AG-009-policy-version-change")
    records = materialize_access_case(case, ORACLE["anchor_time"])
    versions = [record["policy_version"] for record in records if record["policy_version"] is not None]
    assert versions == ["v1", "v1", "v2", "v2", "v2"]
    assert all(record["policy_id"] == "SYN-POLICY" for record in records if record["policy_version"] is not None)


def test_approved_does_not_imply_access_ready():
    events = [
        {"gate_id": "A0", "status": "satisfied", "hour": 0},
        {"gate_id": "A5", "status": "submitted_pending", "hour": 24},
        {"gate_id": "A5", "status": "approved", "hour": 48},
    ]
    result = reconstruct_access_case(events)
    assert result["terminal_authorization_status"] == "approved"
    assert result["access_ready"] is False


def test_initial_denial_is_preserved_after_overturn():
    case = next(item for item in cases() if item["case_id"] == "AG-006-peer-to-peer-overturn")
    result = reconstruct_access_case(case["events"])
    assert result["terminal_authorization_status"] == "approved"
    assert result["initial_denial"] is True
    assert result["overturned"] is True
    assert result["appeal_or_reconsideration_delay_hours"] == 60


def test_denial_types_remain_distinct():
    expected = {
        "AG-003-medical-necessity-denial": "denied_medical_necessity",
        "AG-004-benefit-exclusion": "denied_benefit_exclusion",
        "AG-005-network-site-denial": "denied_network_or_site",
    }
    for case_id, barrier in expected.items():
        case = next(item for item in cases() if item["case_id"] == case_id)
        result = reconstruct_access_case(case["events"])
        assert result["primary_barrier"] == barrier


def test_policy_versions_are_order_preserving_and_drift_is_detected():
    case = next(item for item in cases() if item["case_id"] == "AG-009-policy-version-change")
    result = reconstruct_access_case(case["events"])
    assert result["policy_versions_observed"] == ["v1", "v2"]
    assert result["policy_drift_flag"] is True
    assert result["primary_barrier"] == "policy_change_during_episode"


def test_financial_delay_is_not_medical_denial():
    case = next(item for item in cases() if item["case_id"] == "AG-010-financial-clearance-delay")
    result = reconstruct_access_case(case["events"])
    assert result["terminal_authorization_status"] == "approved"
    assert result["financial_clearance_delay_hours"] == 192
    assert result["primary_barrier"] == "financial_clearance_delay"
    assert "denied_medical_necessity" not in [event["status"] for event in case["events"]]


def test_same_time_conflicting_decisive_a5_outcomes_fail_closed():
    events = [
        {"gate_id": "A5", "status": "submitted_pending", "hour": 0},
        {"gate_id": "A5", "status": "approved", "hour": 24},
        {"gate_id": "A5", "status": "final_denial", "hour": 24},
    ]
    try:
        reconstruct_access_case(events)
    except ValueError as exc:
        assert "ambiguous same-time A5 decisive outcomes" in str(exc)
    else:
        raise AssertionError("same-time conflicting decisive A5 outcomes must fail closed")


def test_same_time_duplicate_decisive_a5_status_is_not_conflict():
    events = [
        {"gate_id": "A5", "status": "submitted_pending", "hour": 0},
        {"gate_id": "A5", "status": "approved", "hour": 24, "event_id": "A"},
        {"gate_id": "A5", "status": "approved", "hour": 24, "event_id": "B"},
    ]
    result = reconstruct_access_case(events)
    assert result["terminal_authorization_status"] == "approved"


def test_input_order_does_not_change_output():
    case = next(item for item in cases() if item["case_id"] == "AG-002-information-request-delay")
    forward = reconstruct_access_case(case["events"])
    reverse = reconstruct_access_case(list(reversed(case["events"])))
    assert forward == reverse


def test_empty_event_stream_is_rejected():
    try:
        reconstruct_access_case([])
    except ValueError as exc:
        assert "at least one event" in str(exc)
    else:
        raise AssertionError("empty event stream should raise ValueError")
