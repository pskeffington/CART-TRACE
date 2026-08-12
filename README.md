# CART-TRACE

**CART-TRACE** is a research framework for reconstructing reproducible patient-level trajectories around CAR T-cell and cellular immunotherapy.

The central question is:

> How can heterogeneous longitudinal clinical, product/CMC, system, and patient-generated data be transformed into reproducible treatment trajectories for studying CAR T-cell treatment, toxicity, recovery, response, and care delivery?

## Research orientation

CART-TRACE is being developed for retrospective research, methods development, reproducible analytics, and future protocol design. It is **not** a clinical decision-support system and should not be used for bedside diagnosis, alarms, treatment recommendations, product release decisions, or other operational clinical functions.

The project is intentionally designed around questions relevant to an academic hospital and regional cancer system: high-acuity capacity, treatment transitions, cellular-therapy utilization, rural access, longitudinal monitoring, manufacturing-to-outcome research, and continuity of data across inpatient, outpatient, home, and regional care settings.

Development is synthetic-first. Public examples should contain no PHI, institutional secrets, production credentials, or identifying free text.

## Planned data domains

- longitudinal encounters, laboratory results, vitals, medications, procedures, and disease response;
- CAR T toxicity and recovery events;
- cell-product and appropriately governed CMC/manufacturing attributes;
- inpatient, ICU-level, outpatient, emergency, and readmission utilization;
- care transitions across tertiary, regional, and home settings;
- patient-generated health signals and patient-reported observations where available;
- provenance, missingness, and transformation metadata for reproducibility.

## Development roadmap

Development proceeds from a reproducible research foundation to a common episode model, trajectory reconstruction, hospital-operations research, CMC-to-outcome linkage, patient-generated signals, and ultimately prospective translational study designs.

See [ROADMAP.md](ROADMAP.md) for the phased research plan.

## Guiding principle

**Signals into evidence. Evidence into care.**

The repository's role is to strengthen the evidence layer: preserving patient-level sequence, provenance, uncertainty, and reproducibility so that future clinical and health-system studies can be designed on a more rigorous data foundation.
