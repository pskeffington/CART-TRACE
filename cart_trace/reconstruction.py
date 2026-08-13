"""Deterministic primitives for CART-TRACE Phase 3 reconstruction.

This module intentionally starts with the smallest frozen building blocks:
offset-aware timestamp parsing, treatment-relative hours, source-label mapping,
and stable source-record ordering. Interval assembly is added only after these
primitives are locked by tests against the Phase 2 oracle.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Mapping


CANONICAL_STATES = {
    "outpatient",
    "emergency",
    "routine_inpatient",
    "intermediate_care",
    "intensive_care",
    "discharged",
    "unknown",
}


@dataclass(frozen=True)
class MappingRule:
    source_care_label: str
    canonical_state: str
    priority: int


def parse_timestamp(value: str) -> datetime:
    """Parse an ISO-8601 timestamp and require an explicit UTC offset."""
    if not isinstance(value, str) or not value:
        raise ValueError("timestamp must be a non-empty string")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must be offset-aware")
    return parsed


def relative_hours(event_timestamp: str | datetime, infusion_timestamp: str | datetime) -> float:
    """Return continuous elapsed hours from infusion without flooring."""
    event = parse_timestamp(event_timestamp) if isinstance(event_timestamp, str) else event_timestamp
    infusion = parse_timestamp(infusion_timestamp) if isinstance(infusion_timestamp, str) else infusion_timestamp
    if event.tzinfo is None or event.utcoffset() is None:
        raise ValueError("event timestamp must be offset-aware")
    if infusion.tzinfo is None or infusion.utcoffset() is None:
        raise ValueError("infusion timestamp must be offset-aware")
    return (event - infusion).total_seconds() / 3600.0


def load_mapping_config(path: str | Path) -> dict[str, Any]:
    """Load and minimally validate the versioned source-label mapping config."""
    config = json.loads(Path(path).read_text())
    if not config.get("mapping_version"):
        raise ValueError("mapping_version is required")
    rules = config.get("rules")
    if not isinstance(rules, list) or not rules:
        raise ValueError("mapping rules are required")
    for raw in rules:
        state = raw.get("canonical_state")
        if state not in CANONICAL_STATES:
            raise ValueError(f"unsupported canonical state in mapping: {state!r}")
        if not isinstance(raw.get("priority"), int):
            raise ValueError("mapping priority must be an integer")
    return config


def _rule_index(config: Mapping[str, Any]) -> dict[str, MappingRule]:
    return {
        raw["source_care_label"]: MappingRule(
            source_care_label=raw["source_care_label"],
            canonical_state=raw["canonical_state"],
            priority=raw["priority"],
        )
        for raw in config["rules"]
    }


def canonical_state_for_record(record: Mapping[str, Any], config: Mapping[str, Any]) -> tuple[str, int, str]:
    """Map one source record to canonical state, priority, and mapping method.

    Unmapped labels are represented explicitly as ``unknown`` rather than
    guessed. If the source record supplies a numeric priority, that value is
    retained; otherwise the mapping rule priority is used.
    """
    label = record.get("source_care_label")
    rule = _rule_index(config).get(label)
    if rule is None:
        priority = record.get("priority")
        return "unknown", priority if isinstance(priority, int) else 0, "unmapped_source_label"
    priority = record.get("priority")
    resolved_priority = priority if isinstance(priority, int) else rule.priority
    return rule.canonical_state, resolved_priority, "direct_label_map"


def stable_record_sort_key(record: Mapping[str, Any]) -> tuple[datetime, datetime, str]:
    """Return the deterministic source-record ordering key.

    Open-ended records sort after finite records sharing the same start time.
    The source record identifier is the final deterministic tie-breaker.
    """
    start = parse_timestamp(record["encounter_start"])
    raw_end = record.get("encounter_end")
    end = parse_timestamp(raw_end) if raw_end is not None else datetime.max.replace(tzinfo=start.tzinfo)
    record_id = record.get("source_record_id")
    if not isinstance(record_id, str) or not record_id:
        raise ValueError("source_record_id is required for deterministic sorting")
    return start, end, record_id
