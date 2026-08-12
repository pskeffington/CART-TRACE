"""Deterministic synthetic cohort generation for CART-TRACE benchmarks.

The generator creates artificial research events only. It is designed to exercise
longitudinal alignment, endpoint handling, provenance, and data-quality tooling.
It does not simulate validated clinical risk or treatment response.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from random import Random

from .schema import ResearchEvent, TreatmentAnchor


@dataclass(frozen=True)
class SyntheticPatient:
    patient_id: str
    anchor: TreatmentAnchor
    events: tuple[ResearchEvent, ...]
    crs_grade: int
    icans_grade: int
    response_category: str


def _event(
    patient_id: str,
    observed_at: datetime,
    kind: str,
    code: str,
    value: float | str,
    unit: str | None,
    source_id: str,
) -> ResearchEvent:
    return ResearchEvent(
        patient_id=patient_id,
        observed_at=observed_at,
        kind=kind,  # type: ignore[arg-type]
        code=code,
        value=value,
        unit=unit,
        source_id=source_id,
        metadata={"synthetic": True},
    )


def generate_patient(index: int, seed: int = 20260812) -> SyntheticPatient:
    """Create one deterministic synthetic patient trajectory.

    Values are deliberately artificial and should not be interpreted as clinical
    distributions, thresholds, or risk relationships.
    """
    rng = Random(seed + index)
    patient_id = f"SYN-{index:04d}"
    infusion_at = datetime(2026, 1, 15, 12, tzinfo=timezone.utc) + timedelta(days=index)
    anchor = TreatmentAnchor(
        patient_id=patient_id,
        infusion_at=infusion_at,
        product=rng.choice(["synthetic-cd19-a", "synthetic-cd19-b", "synthetic-bcma-a"]),
        disease=rng.choice(["synthetic-b-cell-malignancy", "synthetic-plasma-cell-malignancy"]),
        metadata={"synthetic": True},
    )

    crs_grade = rng.choices([0, 1, 2, 3], weights=[35, 35, 22, 8], k=1)[0]
    icans_grade = rng.choices([0, 1, 2, 3], weights=[68, 18, 10, 4], k=1)[0]
    response_category = rng.choice(["synthetic-response", "synthetic-stable", "synthetic-progression"])

    events: list[ResearchEvent] = []
    sequence = 0
    for day in (-14, -7, -3, 0, 1, 2, 3, 5, 7, 14, 30, 90):
        sequence += 1
        observed_at = infusion_at + timedelta(days=day, hours=rng.uniform(-4, 4))
        inflammatory_shape = max(0.0, 5.0 - abs(day - 3.0))
        crp = 4.0 + inflammatory_shape * (1.0 + 0.35 * crs_grade) + rng.uniform(-1.0, 1.0)
        temperature = 36.8 + max(0.0, 2.0 - abs(day - 2.0)) * 0.25 * crs_grade
        heart_rate = 72.0 + inflammatory_shape * 1.7 + rng.uniform(-4.0, 4.0)

        events.extend(
            [
                _event(patient_id, observed_at, "lab", "crp", round(crp, 2), "mg/L", f"{patient_id}-crp-{sequence}"),
                _event(
                    patient_id,
                    observed_at + timedelta(minutes=5),
                    "vital",
                    "temperature",
                    round(temperature, 2),
                    "Cel",
                    f"{patient_id}-temp-{sequence}",
                ),
                _event(
                    patient_id,
                    observed_at + timedelta(minutes=10),
                    "vital",
                    "heart_rate",
                    round(heart_rate, 1),
                    "beats/min",
                    f"{patient_id}-hr-{sequence}",
                ),
            ]
        )

    events.append(
        _event(
            patient_id,
            infusion_at + timedelta(days=30),
            "response",
            "response_category",
            response_category,
            None,
            f"{patient_id}-response-30",
        )
    )
    events.append(
        ResearchEvent(
            patient_id=patient_id,
            observed_at=infusion_at + timedelta(days=3),
            kind="adverse_event",
            code="crs_grade",
            value=crs_grade,
            source_id=f"{patient_id}-crs",
            metadata={
                "synthetic": True,
                "grading_system": "ASTCT",
                "endpoint_status": "synthetic-adjudicated",
            },
        )
    )
    events.append(
        ResearchEvent(
            patient_id=patient_id,
            observed_at=infusion_at + timedelta(days=5),
            kind="adverse_event",
            code="icans_grade",
            value=icans_grade,
            source_id=f"{patient_id}-icans",
            metadata={
                "synthetic": True,
                "grading_system": "ASTCT",
                "endpoint_status": "synthetic-adjudicated",
            },
        )
    )

    return SyntheticPatient(
        patient_id=patient_id,
        anchor=anchor,
        events=tuple(events),
        crs_grade=crs_grade,
        icans_grade=icans_grade,
        response_category=response_category,
    )


def generate_cohort(n: int, seed: int = 20260812) -> tuple[SyntheticPatient, ...]:
    """Create a deterministic cohort of ``n`` artificial patient trajectories."""
    if n <= 0:
        raise ValueError("n must be positive")
    return tuple(generate_patient(index=i + 1, seed=seed) for i in range(n))
