"""Minimal research data-quality checks.

These functions flag structural problems. They are not clinical interpretation rules.
"""

from __future__ import annotations

from collections.abc import Iterable

from .schema import ResearchEvent


def missing_source_ids(events: Iterable[ResearchEvent]) -> list[int]:
    """Return positions of events lacking source identifiers."""
    return [i for i, event in enumerate(events) if not event.source_id]


def duplicate_source_ids(events: Iterable[ResearchEvent]) -> set[str]:
    """Return repeated non-empty source identifiers."""
    seen: set[str] = set()
    duplicates: set[str] = set()
    for event in events:
        if not event.source_id:
            continue
        if event.source_id in seen:
            duplicates.add(event.source_id)
        seen.add(event.source_id)
    return duplicates


def unit_mismatch(events: Iterable[ResearchEvent], expected_units: dict[str, str]) -> list[int]:
    """Flag events whose unit does not match a declared code-to-unit mapping."""
    mismatches: list[int] = []
    for i, event in enumerate(events):
        expected = expected_units.get(event.code)
        if expected is not None and event.unit != expected:
            mismatches.append(i)
    return mismatches
