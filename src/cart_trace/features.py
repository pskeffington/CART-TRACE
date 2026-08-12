"""Longitudinal research feature helpers."""

from __future__ import annotations

from collections.abc import Sequence


def baseline_mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean for a declared patient baseline window."""
    if not values:
        raise ValueError("baseline values are required")
    return sum(values) / len(values)


def deviation_from_baseline(value: float, baseline: float) -> float:
    """Return absolute deviation from a patient-specific baseline."""
    return value - baseline


def slope(delta_value: float, delta_days: float) -> float:
    """Return change per day; rejects zero-duration intervals."""
    if delta_days == 0:
        raise ValueError("delta_days must be non-zero")
    return delta_value / delta_days
