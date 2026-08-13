"""Deterministic CART-TRACE trajectory reconstruction.

The reconstruction layer converts source-like encounter/location records into
canonical half-open care-state intervals and typed transitions. It implements
the frozen Gate 1 semantics and is tested directly against the Phase 2 oracle.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


CANONICAL_STATES = {
    "outpatient",
    "emergency",
    "routine_inpatient",
    "intermediate_care",
    "intensive_care",
    "discharged",
    "unknown",
}
INPATIENT_STATES = {"routine_inpatient", "intermediate_care", "intensive_care"}
ACUITY_RANK = {"routine_inpatient": 1, "intermediate_care": 2, "intensive_care": 3}
DERIVATION_VERSION = "0.2.0"


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


def _iso(value: datetime) -> str:
    text = value.isoformat()
    return text.replace("+00:00", "Z")


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
    """Map one source record to canonical state, priority, and mapping method."""
    label = record.get("source_care_label")
    rule = _rule_index(config).get(label)
    if rule is None:
        priority = record.get("priority")
        return "unknown", priority if isinstance(priority, int) else 0, "unmapped_source_label"
    priority = record.get("priority")
    resolved_priority = priority if isinstance(priority, int) else rule.priority
    return rule.canonical_state, resolved_priority, "direct_label_map"


def stable_record_sort_key(record: Mapping[str, Any]) -> tuple[datetime, datetime, str]:
    """Return the deterministic source-record ordering key."""
    start = parse_timestamp(record["encounter_start"])
    raw_end = record.get("encounter_end")
    end = parse_timestamp(raw_end) if raw_end is not None else datetime.max.replace(tzinfo=start.tzinfo)
    record_id = record.get("source_record_id")
    if not isinstance(record_id, str) or not record_id:
        raise ValueError("source_record_id is required for deterministic sorting")
    return start, end, record_id


def _record_covers(record: Mapping[str, Any], start: datetime, end: datetime) -> bool:
    record_start = parse_timestamp(record["encounter_start"])
    raw_end = record.get("encounter_end")
    if raw_end is None:
        return record_start <= start
    record_end = parse_timestamp(raw_end)
    return record_start <= start and record_end >= end


def _resolve_active(active: Sequence[Mapping[str, Any]], config: Mapping[str, Any]) -> dict[str, Any]:
    mapped = []
    for record in active:
        state, priority, method = canonical_state_for_record(record, config)
        mapped.append((record, state, priority, method))

    max_priority = max(item[2] for item in mapped)
    top = [item for item in mapped if item[2] == max_priority]
    top_states = {item[1] for item in top}
    all_ids = sorted(str(item[0]["source_record_id"]) for item in mapped)

    if len(top_states) > 1:
        return {
            "state": "unknown",
            "source_type": "encounter_location_conflict",
            "source_record_ids": sorted(str(item[0]["source_record_id"]) for item in top),
            "mapping_method": "equal_priority_conflict_to_unknown",
            "uncertain": True,
            "uncertainty_reason": "equal-priority conflicting canonical states",
        }

    state = next(iter(top_states))
    if len(mapped) == 1:
        method = mapped[0][3]
    elif len({item[1] for item in mapped}) == 1:
        method = "duplicate_same_state_collapse"
    else:
        method = "priority_overlap_resolution"

    uncertain = state == "unknown"
    return {
        "state": state,
        "source_type": "encounter_location",
        "source_record_ids": all_ids,
        "mapping_method": method,
        "uncertain": uncertain,
        "uncertainty_reason": "unmapped source label" if uncertain else None,
    }


def _classify_transition(from_state: str, to_state: str) -> str:
    if to_state == "discharged":
        return "discharge"
    if from_state == "discharged" and to_state in {"emergency", *INPATIENT_STATES}:
        return "acute_care_return"
    if from_state == "unknown" or to_state == "unknown":
        return "unknown"
    if from_state in ACUITY_RANK and to_state in ACUITY_RANK:
        if ACUITY_RANK[to_state] > ACUITY_RANK[from_state]:
            return "escalation"
        if ACUITY_RANK[to_state] < ACUITY_RANK[from_state]:
            return "deescalation"
        return "transfer"
    if from_state in {"outpatient", "emergency"} and to_state in INPATIENT_STATES:
        return "admission"
    return "other"


def reconstruct_intervals(
    episode: Mapping[str, Any],
    encounters: Sequence[Mapping[str, Any]],
    config: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Reconstruct canonical half-open care-state intervals for one episode.

    Finite source records are resolved by a boundary sweep. Gaps following an
    inpatient state are represented as ``discharged`` until the next encounter
    or study-window end. A lone open-ended record is retained explicitly with a
    null end rather than being assigned an invented duration.
    """
    if not encounters:
        return []
    infusion = parse_timestamp(episode["infusion_timestamp"])
    window_end = parse_timestamp(episode["window_end_timestamp"])
    ordered = sorted(encounters, key=stable_record_sort_key)

    if len(ordered) == 1 and ordered[0].get("encounter_end") is None:
        record = ordered[0]
        state, _, method = canonical_state_for_record(record, config)
        return [{
            "episode_id": episode["episode_id"],
            "interval_id": f"INT-{episode['episode_id']}-001",
            "state": state,
            "start_timestamp": record["encounter_start"],
            "end_timestamp": None,
            "start_relative_hours": relative_hours(record["encounter_start"], infusion),
            "end_relative_hours": None,
            "source_type": "encounter_location",
            "source_record_ids": [record["source_record_id"]],
            "mapping_method": method,
            "provenance_id": record.get("provenance_id"),
            "uncertain": True,
            "uncertainty_reason": "source end timestamp missing",
            "open_end_reason": "source_end_missing",
        }]

    boundaries = {parse_timestamp(record["encounter_start"]) for record in ordered}
    boundaries.update(
        parse_timestamp(record["encounter_end"])
        for record in ordered
        if record.get("encounter_end") is not None
    )
    boundaries.add(window_end)
    points = sorted(boundaries)
    intervals: list[dict[str, Any]] = []
    prior_state: str | None = None
    prior_source_ids: list[str] = []

    for start, end in zip(points, points[1:]):
        if start >= window_end or end <= start:
            continue
        active = [record for record in ordered if _record_covers(record, start, end)]
        if active:
            resolved = _resolve_active(active, config)
        elif prior_state in INPATIENT_STATES:
            resolved = {
                "state": "discharged",
                "source_type": "derived_disposition",
                "source_record_ids": prior_source_ids,
                "mapping_method": "derived_after_encounter_end",
                "uncertain": False,
                "uncertainty_reason": None,
            }
        else:
            continue

        state = resolved["state"]
        source_ids = list(resolved["source_record_ids"])
        intervals.append({
            "episode_id": episode["episode_id"],
            "interval_id": f"INT-{episode['episode_id']}-{len(intervals)+1:03d}",
            "state": state,
            "start_timestamp": _iso(start),
            "end_timestamp": _iso(end),
            "start_relative_hours": relative_hours(start, infusion),
            "end_relative_hours": relative_hours(end, infusion),
            "source_type": resolved["source_type"],
            "source_record_ids": source_ids,
            "mapping_method": resolved["mapping_method"],
            "provenance_id": None,
            "uncertain": resolved["uncertain"],
            "uncertainty_reason": resolved["uncertainty_reason"],
            "open_end_reason": None,
        })
        prior_state = state
        prior_source_ids = source_ids

    return intervals


def derive_transitions(episode: Mapping[str, Any], intervals: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Derive typed transitions only when the canonical state changes."""
    infusion = parse_timestamp(episode["infusion_timestamp"])
    transitions: list[dict[str, Any]] = []
    for previous, current in zip(intervals, intervals[1:]):
        if previous["state"] == current["state"]:
            continue
        timestamp = current["start_timestamp"]
        if timestamp is None:
            continue
        uncertain = bool(previous.get("uncertain") or current.get("uncertain"))
        source_ids = list(current.get("source_record_ids") or previous.get("source_record_ids") or [])
        transitions.append({
            "episode_id": episode["episode_id"],
            "transition_id": f"TR-{episode['episode_id']}-{len(transitions)+1:03d}",
            "transition_timestamp": timestamp,
            "relative_time_hours": relative_hours(timestamp, infusion),
            "from_state": previous["state"],
            "to_state": current["state"],
            "transition_type": _classify_transition(previous["state"], current["state"]),
            "source_type": "derived_state_change",
            "source_record_ids": source_ids,
            "provenance_id": None,
            "derived": True,
            "derivation_version": DERIVATION_VERSION,
            "uncertain": uncertain,
            "uncertainty_reason": current.get("uncertainty_reason") if uncertain else None,
        })
    return transitions


def reconstruct_episode(
    episode: Mapping[str, Any],
    encounters: Sequence[Mapping[str, Any]],
    config: Mapping[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    """Return canonical intervals and transitions for one therapy episode."""
    intervals = reconstruct_intervals(episode, encounters, config)
    return {"intervals": intervals, "transitions": derive_transitions(episode, intervals)}
