"""Canonical research event schema for CAR T-cell trajectories."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal

EventKind = Literal[
    "lab",
    "vital",
    "medication",
    "procedure",
    "encounter",
    "adverse_event",
    "response",
    "patient_generated",
]


@dataclass(frozen=True)
class ResearchEvent:
    patient_id: str
    observed_at: datetime
    kind: EventKind
    code: str
    value: Any = None
    unit: str | None = None
    source_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TreatmentAnchor:
    patient_id: str
    infusion_at: datetime
    product: str | None = None
    disease: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
