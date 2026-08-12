from cart_trace.quality import duplicate_source_ids, missing_source_ids
from cart_trace.synthetic import generate_cohort, generate_patient
from cart_trace.timeline import relative_day


def test_generate_patient_is_deterministic() -> None:
    first = generate_patient(1, seed=42)
    second = generate_patient(1, seed=42)
    assert first == second


def test_synthetic_events_have_sources() -> None:
    patient = generate_patient(2, seed=42)
    assert missing_source_ids(patient.events) == []
    assert duplicate_source_ids(patient.events) == set()


def test_synthetic_trajectory_spans_pre_and_post_infusion() -> None:
    patient = generate_patient(3, seed=42)
    days = [relative_day(event.observed_at, patient.anchor.infusion_at) for event in patient.events]
    assert min(days) < 0
    assert max(days) >= 90


def test_generate_cohort_size_and_unique_ids() -> None:
    cohort = generate_cohort(12, seed=42)
    assert len(cohort) == 12
    assert len({patient.patient_id for patient in cohort}) == 12


def test_generate_cohort_rejects_nonpositive_size() -> None:
    try:
        generate_cohort(0)
    except ValueError as exc:
        assert "positive" in str(exc)
    else:
        raise AssertionError("generate_cohort should reject nonpositive n")
