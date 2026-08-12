import json

from cart_trace.export import cohort_to_dict, validation_report, write_cohort_json
from cart_trace.synthetic import generate_cohort


def test_cohort_to_dict_serializes_datetimes() -> None:
    cohort = generate_cohort(2, seed=7)
    payload = cohort_to_dict(cohort)
    assert payload[0]["anchor"]["infusion_at"].endswith("+00:00")
    assert payload[0]["events"][0]["observed_at"].endswith("+00:00")


def test_validation_report_is_clean_for_generated_cohort() -> None:
    cohort = generate_cohort(3, seed=7)
    report = validation_report(cohort)
    assert report["valid"] is True
    assert report["patient_count"] == 3
    assert report["missing_source_id_count"] == 0
    assert report["duplicate_source_ids"] == []
    assert report["all_events_synthetic"] is True


def test_write_cohort_json(tmp_path) -> None:
    cohort = generate_cohort(1, seed=7)
    output = write_cohort_json(cohort, tmp_path / "cohort.json")
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data[0]["patient_id"] == "SYN-0001"
