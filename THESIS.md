# CART-TRACE MS Health Data Science Capstone Project

## Working title

**CART-TRACE: Reconstructing Hospital Care Trajectories Following CAR T-Cell Therapy from Longitudinal Clinical Data**

## Capstone objective

Develop and validate a reproducible health-data method for transforming heterogeneous longitudinal hospital records into treatment-relative patient-level trajectories of care during the first 30 days following CAR T-cell infusion.

The capstone is deliberately narrow. Its primary contribution is a transparent and testable data-processing method; hospital utilization after infusion is the applied clinical context in which that method is evaluated.

## Primary capstone question

> **Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?**

## Secondary applied question

> What patterns of acute-care utilization, escalation, de-escalation, discharge, and early return are observed in the reconstructed trajectories?

The secondary question is descriptive. CART-TRACE does not predict eligibility, toxicity, disposition, treatment response, or clinical outcomes.

## Capstone premise

CAR T-cell therapy creates a time-dependent acute-care episode in which patients may move among outpatient care, emergency care, routine inpatient care, intermediate care, intensive care, discharge, and subsequent acute-care encounters. Relevant information can be distributed across encounter, location, admission/discharge, transfer, and utilization records.

The health-data problem is therefore not simply to count encounters. It is to reconstruct a coherent temporal representation of the treatment episode while preserving sequence, provenance, missingness, and uncertainty.

The capstone evaluates whether this reconstruction can be performed deterministically and reproducibly enough to support defensible patient-level and cohort-level utilization analyses.

## Scope boundary

### Included in the capstone core

- CAR T-cell infusion as the treatment anchor;
- continuous treatment-relative time;
- encounter and care-location records;
- canonical hospital care states;
- admission, transfer, escalation, de-escalation, discharge, and acute-care-return transitions;
- interval reconstruction using explicit boundary semantics;
- provenance and source-record traceability;
- explicit missingness and uncertainty;
- post-infusion hospital utilization measures;
- synthetic truth-set validation;
- governed retrospective clinical-data validation if approvals and data access are available.

### Explicitly outside the capstone core

- candidate identification or referral tracking;
- CAR T-cell eligibility adjudication;
- treatment-readiness gating;
- product or therapy selection;
- leukapheresis, bridging, or lymphodepletion decision support;
- toxicity prediction or automated CRS/ICANS detection;
- discharge prediction;
- prospective clinical alerts;
- patient-generated health data;
- CMC/manufacturing analytics;
- treatment recommendation.

These may motivate future work but are not required for capstone completion.

## Unit and analytic window

The primary unit of analysis is the **CAR T-cell therapy episode**, not the individual encounter.

Primary post-infusion analytic window:

`infusion timestamp = time 0 -> day +30`

A limited pre-infusion window may be retained only when necessary to establish encounter continuity around infusion. It is not an eligibility or treatment-readiness study period.

## Canonical care-state model

The capstone uses a small institution-agnostic state vocabulary:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

Institution-specific unit labels are source data that map into these canonical states. Acute-care return is represented as a transition/event, not as a distinct patient state.

## Capstone aims

### Aim 1 — Build the reproducible trajectory representation

Develop a deterministic method that converts source-like longitudinal hospital records into canonical care-state intervals and transitions anchored to CAR T-cell infusion.

Primary products:

- therapy-episode representation;
- canonical care-state intervals;
- transition records;
- treatment-relative timestamps;
- source-record provenance;
- explicit uncertainty and missingness indicators.

### Aim 2 — Validate reconstruction fidelity and reproducibility

Evaluate the method against prespecified synthetic truth sets before applying it to governed clinical data.

Validation targets include:

- exact agreement with deterministic expected intervals and transitions;
- prespecified behavior for conflicting or incomplete records;
- reproducible results across repeated runs;
- no false transitions caused by duplicate same-state records;
- traceability of each derived state to source evidence.

If governed institutional data are available, a separate retrospective validation layer may compare reconstructed outputs with source encounter/location records and an approved adjudication sample.

### Aim 3 — Characterize post-infusion hospital utilization

Apply the validated representation to derive transparent descriptive measures of the hospital episode.

Core measures include:

- total inpatient duration;
- routine inpatient duration;
- intermediate-care duration;
- intensive-care duration;
- number and timing of level-of-care transitions;
- time from infusion to first escalation;
- time to discharge;
- 7-day acute-care return;
- 30-day acute-care return;
- missing/unknown-state burden.

Any recurrent trajectory grouping is exploratory and subordinate to reconstruction and validation. Predictive modeling is not required for capstone success.

## Methodological contribution

The primary academic contribution is a **deterministic temporal/state reconstruction framework for longitudinal hospital data**.

The project emphasizes:

- treatment-relative temporal alignment;
- explicit state definitions;
- half-open interval semantics;
- deterministic conflict and tie-breaking rules;
- source-to-canonical mapping;
- provenance;
- missingness and uncertainty;
- synthetic truth-set testing;
- reproducibility;
- interpretable clinical-data outputs.

The hospital-utilization analysis demonstrates the value of the method; it is not a claim that CART-TRACE is an operational hospital-management or bedside decision-support system.

## Capstone evidence chain

Every major result should be traceable through:

`capstone question -> requirement -> schema/function -> synthetic fixture -> automated test -> analytic output -> capstone table/figure`

This traceability is part of the capstone deliverable rather than an implementation detail.

## Development phases

### Phase 0 — Scope and governance

Define the capstone question, public/non-operational boundary, synthetic-first policy, and requirements for any future governed data use.

### Phase 1 — Canonical model

Define episode, interval, transition, provenance, encounter-input, mapping, and temporal semantics.

### Phase 2 — Synthetic truth set

Prespecify representative post-infusion trajectories and edge cases with expected intervals, transitions, uncertainty behavior, and utilization values.

### Phase 3 — Reconstruction

Implement deterministic conversion from source-like records to canonical trajectories and require exact agreement with the frozen synthetic oracle.

### Phase 4 — Utilization measures

Implement transparent post-infusion hospital-utilization measures from reconstructed trajectories.

### Phase 5 — Capstone analysis and communication

Produce patient-level trajectory examples, cohort summaries, validation results, uncertainty/missingness reporting, methods diagrams, and reproducible capstone figures/tables.

### Phase 6 — Governed clinical-data application, if feasible

Apply the frozen method to appropriately approved institutional records and evaluate transfer from synthetic to real-world hospital data. This phase is approval-dependent and is not allowed to become a prerequisite for demonstrating the core computational method if data access is delayed.

## Capstone deliverables

A complete CART-TRACE capstone should produce:

1. a clearly specified applied health-data question;
2. a documented canonical data model and transformation method;
3. reproducible implementation code;
4. a prespecified synthetic validation cohort;
5. automated reconstruction and schema tests;
6. quantitative reconstruction-validation results;
7. hospital-utilization measures derived from canonical trajectories;
8. interpretable patient-level and cohort-level visualizations;
9. a missingness/uncertainty analysis;
10. a manuscript-style capstone report or equivalent final scholarly product;
11. a public, synthetic-only reproducibility repository, with governed clinical artifacts kept in approved environments.

## Minimum viable capstone

CART-TRACE does **not** depend on completing a large predictive model or gaining immediate access to production hospital data.

The minimum viable scholarly contribution is achieved if the project can demonstrate that heterogeneous source-like hospital records surrounding CAR T-cell infusion can be transformed into a transparent, deterministic, reproducible sequence of care states and transitions; that the method reproduces prespecified truth sets; and that those outputs support defensible post-infusion utilization measures.

Governed real-data validation substantially strengthens the capstone but remains contingent on approvals and data availability.

## Success criterion

The capstone succeeds if CART-TRACE demonstrates a reproducible and auditable method for reconstructing post-CAR-T hospital care trajectories from longitudinal clinical records and shows that the resulting patient-level representation can support meaningful descriptive characterization of hospital utilization during the first 30 days after infusion.

Prediction, clinical eligibility determination, and prospective decision support are not required for success.
