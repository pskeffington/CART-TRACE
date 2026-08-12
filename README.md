# CART-TRACE

**CAR T-cell Treatment, Response, Analytics, Clinical Trajectories & Evidence**

CART-TRACE is an open, research-oriented scaffold for studying longitudinal CAR T-cell therapy data with reproducible clinical-data engineering, patient-centered time alignment, statistical analysis, signal processing, and evidence provenance.

> **Status:** early research scaffold. This repository is not a clinical decision-support system and is not intended for diagnosis, prognosis, treatment selection, or bedside use.

## Research objective

> How can heterogeneous longitudinal clinical and patient-generated data be transformed into reproducible patient-level trajectories for studying CAR T-cell treatment, toxicity, recovery, and response?

The project is organized around a common treatment-relative time axis:

`baseline -> leukapheresis -> manufacturing/bridging -> lymphodepletion -> Day 0 infusion -> acute monitoring -> early recovery -> response/follow-up`

## What the scaffold demonstrates

- clinical and translational data engineering
- treatment-relative longitudinal alignment
- laboratory and physiologic time-series analysis
- patient-specific baselines and deviation features
- survival and repeated-measures methods
- candidate CRS/ICANS research endpoints
- data quality, provenance, and reproducibility
- FHIR-to-research-schema interoperability concepts
- synthetic-data benchmarking
- research reporting with explicit limitations

## Repository structure

```text
src/cart_trace/
  schema.py          canonical research event model
  timeline.py        treatment-relative time alignment
  quality.py         validation and data-quality rules
  features.py        longitudinal feature engineering
  provenance.py      analysis provenance records
docs/
  research_review.md current domain and methodological review
  research_plan.md   staged scientific roadmap
tests/
  test_timeline.py   initial behavioral tests
```

## Design principles

1. **Day 0 is an analytical anchor, not a biological simplification.** Original timestamps are retained while treatment-relative time is derived.
2. **Raw and derived data remain distinguishable.** Derived features carry provenance to source observations and transformation parameters.
3. **Missingness is data.** CART-TRACE does not silently impute or interpolate clinical observations.
4. **Research endpoints are explicit.** CRS, ICANS, response, progression, admission, and survival variables require documented definitions and adjudication rules.
5. **Patient-specific and cohort-level inference are separated.** Within-person trajectories are not presented as validated clinical predictions.
6. **Synthetic/public data first.** Human-subject data should only enter governed research workflows with appropriate institutional authorization.

## Quick example

```python
from datetime import datetime, timezone
from cart_trace.timeline import relative_day

infusion = datetime(2026, 1, 10, tzinfo=timezone.utc)
observation = datetime(2026, 1, 13, 12, tzinfo=timezone.utc)

print(relative_day(observation, infusion))  # 3.5
```

## Planned workstreams

- **Cohort model:** disease, product, prior therapy, treatment milestones, labs, vitals, medications, adverse events, response, survival.
- **Trajectory engine:** patient baselines, slopes, peaks, recovery measures, cumulative abnormal burden, and change points.
- **Signal layer:** irregular sampling, artifact flags, resampling policies, wearable/PGHD adapters, and uncertainty-aware feature extraction.
- **Statistics:** mixed-effects models, survival analysis, competing risks, landmark analyses, bootstrap uncertainty, calibration, and subgroup evaluation.
- **Interoperability:** synthetic FHIR `Patient`, `Observation`, `Condition`, `Procedure`, `Encounter`, and `MedicationAdministration` adapters.
- **Research reporting:** cohort-flow, endpoint dictionary, provenance manifest, validation report, and reproducible figures/tables.

## Institutional boundary

CART-TRACE is an independent open-source research project. Any future Dartmouth/Dartmouth Health application should be represented as a distinct, formally authorized research application rather than implying institutional sponsorship of this repository.

## Research review

See [`docs/research_review.md`](docs/research_review.md) for the initial review of CAR T-cell therapy, toxicity, longitudinal analytics, and research opportunities.

## License and governance

License, contribution rules, data-governance documentation, and a formal model-use statement will be added before the project is described as release-ready.
