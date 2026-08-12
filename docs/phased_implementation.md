# CART-TRACE Phased Implementation Plan

This document translates the research roadmap into buildable work packages. Each phase has a purpose, implementation package, required artifacts, tests, risks, dependencies, and handoff criteria.

## Phase 0 — Scope and governance

### Purpose
Lock the thesis question, research boundary, and public-development rules before implementation expands.

### Implementation package

- `THESIS.md`
- `README.md`
- `docs/requirements.md`
- `docs/data_requirements.md`
- `docs/validation_plan.md`
- `docs/governance.md`

### Mandatory outputs

- thesis question and aims;
- included/excluded domains;
- synthetic-first policy;
- no-PHI/no-production-credentials policy;
- research-only/non-operational statement;
- minimum necessary institutional data principle;
- real-data approval gate.

### Failure modes to prevent

- scope creep into CMC, monitoring, or predictive decision support;
- public examples that encode real institutional workflows;
- undocumented assumptions about local hospital units;
- premature claims of clinical utility.

### Handoff to Phase 1

Phase 1 starts only when the thesis question is stable enough that schemas can be designed without anticipating excluded domains.

---

## Phase 1 — Canonical episode and care-state model

### Purpose
Create the smallest stable representation capable of expressing the hospital care sequence relevant to the thesis.

### Work package 1A — Care-state semantics

Artifacts:
- `docs/care_state_vocabulary.md`
- mapping principles and conflict semantics

Implementation questions:
- what counts as an inpatient state?
- how is intermediate/high-observation care represented?
- when does discharge become a state versus an event?
- how are emergency/observation returns distinguished from readmission?

### Work package 1B — Core schemas

Artifacts:
- `schemas/therapy_episode.schema.json`
- `schemas/care_state_interval.schema.json`
- `schemas/care_transition.schema.json`
- `schemas/encounter_input.schema.json`
- `schemas/provenance.schema.json`

Schema requirements:
- stable identifiers;
- absolute timestamps;
- treatment-relative time;
- source identifiers;
- uncertainty indicators;
- transformation version;
- support for multiple encounters within one episode.

### Work package 1C — Temporal semantics

Artifacts:
- `docs/time_semantics.md`
- hand-worked example episode

Decisions to freeze:
- timezone handling;
- day-0 anchoring;
- partial-day calculation;
- interval closure convention, preferably half-open `[start, end)`;
- same-timestamp tie-breaking;
- study-window clipping.

### Tests

- schema validation for valid/invalid examples;
- multi-encounter synthetic episode validates end to end;
- timestamp boundary examples;
- unknown/conflicting state examples.

### Handoff to Phase 2

The model must be expressive enough to write all synthetic truth-set cases without schema changes.

---

## Phase 2 — Synthetic cohort and truth sets

### Purpose
Create a deterministic test oracle before writing reconstruction logic.

### Work package 2A — Fixture design

Required trajectory classes:
1. routine recovery;
2. prolonged hospitalization;
3. transient escalation/de-escalation;
4. ICU escalation;
5. discharge followed by early acute-care return;
6. missing/conflicting location data.

### Work package 2B — Truth-set specification

For every fixture define:
- raw input events;
- expected canonical state intervals;
- expected care transitions;
- expected utilization metrics;
- expected uncertainty/missingness flags;
- requirement IDs exercised.

### Work package 2C — Edge-case matrix

At minimum cover:
- identical timestamps;
- adjacent state intervals;
- overlapping source records;
- missing end times;
- duplicate events;
- events exactly at study-window boundaries;
- discharge and return on same calendar day;
- escalation occurring before infusion within the development window;
- unknown state between two known states.

### Tests

Fixtures themselves are specifications. No algorithm is considered correct unless its output matches the truth set.

### Handoff to Phase 3

Every required trajectory class has immutable expected output sufficient to test reconstruction.

---

## Phase 3 — Transition reconstruction engine

### Purpose
Convert source event records into deterministic patient-level care-state intervals and transitions.

### Work package 3A — Normalize

Functions:
- standardize timestamps;
- normalize source encounter types;
- map local care location categories into canonical states;
- preserve raw values in provenance.

### Work package 3B — Time alignment

Functions:
- anchor to infusion;
- calculate treatment-relative hours/days;
- clip or flag out-of-window events;
- preserve absolute time.

### Work package 3C — Event ordering

Functions:
- deterministic stable sort;
- source priority tie-breaking;
- duplicate suppression;
- overlap detection.

### Work package 3D — State derivation

Functions:
- generate intervals;
- resolve or flag conflicts;
- emit `unknown` when required;
- emit transitions only on normalized state change;
- propagate provenance.

### Outputs

- canonical interval table;
- transition table;
- treatment-relative timeline;
- reconstruction audit log/report.

### Acceptance targets

- exact truth-set agreement on all non-conflict fixtures;
- expected uncertainty behavior on conflict fixtures;
- deterministic serialization across repeated runs.

### Handoff to Phase 4

Trajectory reconstruction passes the full synthetic suite and is stable enough that metric calculations can rely on interval semantics.

---

## Phase 4 — Hospital utilization metrics

### Purpose
Convert reconstructed care states into quantitative hospital-use measures relevant to the thesis.

### Work package 4A — Metric specification

Freeze formulas before cohort analysis.

Required metrics:
- total inpatient exposure;
- routine inpatient duration;
- higher-observation duration;
- ICU duration;
- combined high-acuity duration;
- number of transitions;
- number of escalation events;
- time from infusion to first escalation;
- time from last escalation to discharge;
- treatment-relative discharge time;
- 7-day acute-care reuse;
- 30-day acute-care reuse.

### Work package 4B — Missingness semantics

Every metric must distinguish:
- observed zero;
- not applicable;
- not calculable;
- censored/incomplete follow-up where relevant.

### Work package 4C — Metric provenance

Each reported measure should identify:
- source episode;
- metric definition version;
- underlying interval set/version;
- calculation status/missingness reason.

### Tests

- expected-value tests for every synthetic fixture;
- partial-day calculations;
- unknown interval handling;
- window clipping;
- reuse-window boundary checks.

### Handoff to Phase 5

All analytic features used for cohort characterization are defined, tested, and versioned.

---

## Phase 5 — Cohort characterization

### Purpose
Determine whether recurring hospital care patterns can be described across therapy episodes without converting the work into clinical prediction.

### Work package 5A — Prespecified feature matrix

Candidate features:
- inpatient duration;
- high-acuity duration;
- maximum observed care state;
- escalation count;
- transition count;
- discharge time;
- early reuse indicators;
- uncertainty/missingness measures.

### Work package 5B — Descriptive grouping

Potential approaches, selected based on sample size and advisor review:
- rule-based descriptive strata;
- hierarchical clustering;
- sequence-distance clustering;
- latent-class methods if justified by data volume.

Interpretability takes precedence over model complexity.

### Work package 5C — Sensitivity analysis

Assess sensitivity to:
- study-window definition;
- high-acuity grouping choices;
- missingness thresholds;
- alternative grouping parameters;
- inclusion/exclusion of uncertain episodes.

### Required outputs

- patient-level trajectory visualizations;
- cohort utilization distributions;
- descriptive group summaries;
- missingness/uncertainty analysis;
- trace from group assignment back to episode sequence.

### Handoff to Phase 6

Methods and reporting are reproducible on synthetic/demo cohorts and ready to be executed in a governed hospital environment.

---

## Phase 6 — Governed hospital-data study

### Purpose
Evaluate whether the canonical model and pipeline can reconstruct and characterize real hospital care trajectories under appropriate approvals.

### Work package 6A — Institutional mapping

- identify source systems and approved fields;
- document local unit-to-state mapping;
- document encounter-type mapping;
- freeze extraction cohort and study window;
- maintain mapping outside the public repo when necessary.

### Work package 6B — Validation subset

- prespecify sample size or sampling logic;
- compare canonical reconstruction with source records;
- adjudicate disagreements;
- quantify unknown/conflict frequency;
- measure reconstruction agreement.

### Work package 6C — Cohort execution

- run validated transformation;
- generate utilization measures;
- produce cohort characterization;
- perform sensitivity analyses;
- document data limitations and transportability.

### Stop conditions

Pause analysis if:
- infusion anchor quality is inadequate;
- care-location data cannot support canonical mapping;
- missingness materially prevents trajectory reconstruction;
- governance scope does not cover required fields;
- validation reveals systematic mapping errors.

### Thesis handoff

The thesis analysis chapter may proceed when reconstruction validity, metric validity, and data limitations are sufficiently documented for scholarly interpretation.

---

## Cross-phase implementation rules

1. Do not begin a downstream analytic phase while an upstream semantic ambiguity is unresolved.
2. Any change to a frozen schema, time convention, or metric formula must trigger impact review and affected-test updates.
3. Synthetic truth sets remain the baseline regression suite throughout the project.
4. Real-data mapping logic must not silently alter canonical semantics.
5. No phase may introduce clinical recommendation behavior without a separately approved research question and validation program.
6. Every major thesis result should trace to a requirement ID, code version, and reproducible artifact.
