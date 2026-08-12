"""Serialization helpers for synthetic CART-TRACE benchmark cohorts."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .quality import duplicate_source_ids, missing_source_ids
from .synthetic import SyntheticPatient


def patient_to_dict(patient: SyntheticPatient) -> dict[str, Any]:
    """Convert one synthetic patient to a JSON-serializable dictionary."""
    payload = asdict(patient)
    payload["anchor"]["infusion_at"] = patient.anchor.infusion_at.isoformat()
    for event_payload, event in zip(payload["events"], patient.events, strict=True):
        event_payload["observed_at"] = event.observed_at.isoformat()
    return payload


def cohort_to_dict(cohort: tuple[SyntheticPatient, ...]) -> list[dict[str, Any]]:
    """Convert a synthetic cohort to JSON-serializable records."""
    return [patient_to_dict(patient) for patient in cohort]


def write_cohort_json(cohort: tuple[SyntheticPatient, ...], path: str | Path) -> Path:
    """Write the synthetic benchmark cohort to JSON."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(cohort_to_dict(cohort), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output


def validation_report(cohort: tuple[SyntheticPatient, ...]) -> dict[str, Any]:
    """Summarize structural integrity checks for a synthetic cohort."""
    events = tuple(event for patient in cohort for event in patient.events)
    missing = missing_source_ids(events)
    duplicates = sorted(duplicate_source_ids(events))
    return {
        "patient_count": len(cohort),
        "event_count": len(events),
        "missing_source_id_count": len(missing),
        "duplicate_source_ids": duplicates,
        "all_events_synthetic": all(event.metadata.get("synthetic") is True for event in events),
        "valid": not missing and not duplicates,
    }


def write_validation_report(cohort: tuple[SyntheticPatient, ...], path: str | Path) -> Path:
    """Write a machine-readable synthetic benchmark validation report."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(validation_report(cohort), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return output
