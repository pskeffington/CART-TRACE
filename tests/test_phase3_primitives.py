from pathlib import Path

import pytest

from cart_trace.reconstruction import (
    canonical_state_for_record,
    load_mapping_config,
    parse_timestamp,
    relative_hours,
    stable_record_sort_key,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "synthetic_care_state_mapping.json"


def test_relative_hours_preserves_negative_fractional_time():
    assert relative_hours("2026-01-08T08:00:00Z", "2026-01-08T10:00:00Z") == -2.0
    assert relative_hours("2026-01-09T18:00:00Z", "2026-01-08T10:00:00Z") == 32.0


def test_parse_timestamp_requires_explicit_offset():
    with pytest.raises(ValueError):
        parse_timestamp("2026-01-08T10:00:00")


def test_mapping_uses_canonical_gate1_states():
    config = load_mapping_config(CONFIG)
    examples = {
        "synthetic_standard_floor": "routine_inpatient",
        "synthetic_stepdown": "intermediate_care",
        "synthetic_intermediate": "intermediate_care",
        "synthetic_icu": "intensive_care",
        "synthetic_emergency": "emergency",
        "synthetic_outpatient": "outpatient",
    }
    for label, expected in examples.items():
        state, _, method = canonical_state_for_record({"source_care_label": label}, config)
        assert state == expected
        assert method == "direct_label_map"


def test_unmapped_label_becomes_unknown_not_guess():
    config = load_mapping_config(CONFIG)
    state, priority, method = canonical_state_for_record(
        {"source_care_label": "synthetic_unmapped", "priority": 7}, config
    )
    assert state == "unknown"
    assert priority == 7
    assert method == "unmapped_source_label"


def test_source_priority_is_preserved_when_present():
    config = load_mapping_config(CONFIG)
    state, priority, _ = canonical_state_for_record(
        {"source_care_label": "synthetic_icu", "priority": 25}, config
    )
    assert state == "intensive_care"
    assert priority == 25


def test_stable_sort_key_uses_source_record_id_for_exact_ties():
    records = [
        {"source_record_id":"SRC-B","encounter_start":"2026-01-08T10:00:00Z","encounter_end":"2026-01-08T12:00:00Z"},
        {"source_record_id":"SRC-A","encounter_start":"2026-01-08T10:00:00Z","encounter_end":"2026-01-08T12:00:00Z"},
    ]
    ordered = sorted(records, key=stable_record_sort_key)
    assert [record["source_record_id"] for record in ordered] == ["SRC-A", "SRC-B"]


def test_open_end_sorts_after_finite_end_at_same_start():
    records = [
        {"source_record_id":"SRC-OPEN","encounter_start":"2026-01-08T10:00:00Z","encounter_end":None},
        {"source_record_id":"SRC-FINITE","encounter_start":"2026-01-08T10:00:00Z","encounter_end":"2026-01-08T12:00:00Z"},
    ]
    ordered = sorted(records, key=stable_record_sort_key)
    assert [record["source_record_id"] for record in ordered] == ["SRC-FINITE", "SRC-OPEN"]
