# CART-TRACE Phased Implementation Plan

This document turns the roadmap into an executable implementation sequence. Each phase is organized around inputs, work products, verification, and a release artifact suitable for thesis review.

## Phase 0 — Scope and governance

### Inputs
- thesis question and aims;
- public-repository constraints;
- institutional research and privacy expectations.

### Implementation work
- maintain `THESIS.md`, `ROADMAP.md`, and `docs/requirements.md` as controlling documents;
- document synthetic-first development and no-PHI constraints;
- define what is explicitly out of scope;
- define provenance and reproducibility expectations before real-data work.

### Required artifacts
- `docs/governance.md`;
- requirement traceability for all `SCOPE-*` and `GOV-*` items;
- repository review confirming no operational/clinical claims.

### Verification
- documentation review;
- repository content scan for PHI-like examples, credentials, or local identifiers;
- confirmation that no mandatory thesis requirement depends on excluded domains.

### Phase release
`v0-scope-locked`

---

## Phase 1 — Canonical episode model

### Inputs
- care-state vocabulary;
- therapy episode definition;
- source encounter/location concepts;
- temporal and provenance requirements.

### Implementation work
1. finalize canonical schemas;
2. define minimal encounter input contract;
3. define provenance schema;
4. freeze treatment-relative time semantics;
5. create one hand-worked multi-encounter episode;
6. validate relationships among episode, state intervals, and transitions.

### Required artifacts
- `schemas/therapy_episode.schema.json`;
- `schemas/care_state_interval.schema.json`;
- `schemas/care_transition.schema.json`;
- `schemas/provenance.schema.json`;
- `schemas/encounter_input.schema.json` or equivalent contract;
- `docs/time_semantics.md`;
- one canonical hand-worked example.

### Verification
- schema validation;
- explicit check that all derived objects can carry provenance;
- no ambiguity in inclusive/exclusive interval boundaries;
- local hospital unit labels never appear as canonical states.

### Phase release
`v1-canonical-model`

---

## Phase 2 — Synthetic truth set

### Inputs
- frozen canonical model;
- phase-gate requirements;
- known edge cases.

### Implementation work
Create deterministic synthetic episodes representing:
1. routine recovery;
2. prolonged routine hospitalization;
3. transient higher-observation escalation;
4. ICU escalation and de-escalation;
5. discharge with early acute-care return;
6. missing/conflicting location records.

Each fixture should contain raw-like input events plus a manually specified truth set.

### Required artifacts
- fixture manifest;
- source-like synthetic events;
- expected canonical intervals;
- expected transitions;
- expected utilization metrics;
- edge-case annotations.

### Verification
- all fixtures validate against schemas;
- expected outputs are hand-reviewable;
- fixture coverage maps to `DATA-*`, `MODEL-*`, `TIME-*`, `PROV-*`, and `RECON-*` requirements.

### Phase release
`v2-synthetic-truth-set`

---

## Phase 3 — Trajectory reconstruction engine

### Inputs
- source-like synthetic fixtures;
- canonical model;
- frozen temporal semantics.

### Implementation work
Recommended modules:

```text
src/cart_trace/
  timeline/
    relative_time.py
  normalize/
    care_state.py
  transitions/
    reconstruct.py
    overlap.py
  provenance/
    records.py
```

Functions should:
- anchor to infusion;
- normalize source locations/encounter classes;
- deterministically sort events;
- resolve duplicate and overlapping records;
- create non-overlapping care-state intervals;
- derive transitions only on state change;
- propagate provenance and uncertainty.

### Required artifacts
- executable reconstruction library;
- stable canonical serialization;
- unit tests and fixture-based integration tests;
- reconstruction diagnostics for conflicts and missingness.

### Verification
- 100% agreement with non-conflict synthetic truth sets;
- prescribed uncertainty behavior for conflict fixtures;
- repeated runs produce equivalent canonical outputs;
- no hidden inference from physiologic measurements into care state.

### Phase release
`v3-reconstruction-engine`

---

## Phase 4 — Hospital utilization layer

### Inputs
- validated care-state intervals and transitions.

### Implementation work
Implement documented metrics for:
- inpatient exposure;
- time by care state;
- number and timing of transitions;
- first escalation;
- higher-observation and ICU duration;
- time to discharge;
- 7-day and 30-day acute-care reuse;
- missing/undefined metric reasons.

Recommended module:

```text
src/cart_trace/utilization/
  metrics.py
  definitions.py
```

### Required artifacts
- metric dictionary;
- formulas/algorithms;
- tested implementation;
- fixture-level expected values;
- sensitivity tests for window boundaries and partial days.

### Verification
- all `METRIC-*` requirements have tests;
- zero and missing are never conflated;
- metric outputs retain episode and transformation provenance.

### Phase release
`v4-utilization-layer`

---

## Phase 5 — Cohort characterization

### Inputs
- validated episode-level metrics;
- patient-level trajectory sequences;
- missingness summaries.

### Implementation work
1. prespecify interpretable features;
2. define descriptive grouping/phenotyping strategy;
3. generate patient-level trajectory plots;
4. produce cohort-level utilization tables and figures;
5. perform sensitivity analysis;
6. ensure every cohort assignment remains traceable to patient-level sequences.

### Required artifacts
- analysis specification;
- cohort report generator;
- patient trajectory visualization;
- missingness/uncertainty report;
- reproducible notebook or scripted analysis.

### Verification
- analysis regenerates from canonical outputs;
- group labels remain descriptive rather than clinical;
- cohort findings are robust to prespecified sensitivity checks.

### Phase release
`v5-cohort-characterization`

---

## Phase 6 — Governed hospital-data execution

### Inputs
- approved institutional extract;
- source-to-canonical mapping specification;
- protected research environment;
- validated reconstruction pipeline.

### Implementation work
1. map local fields to the public canonical model;
2. run data-quality and reconstructability assessment;
3. reconstruct hospital trajectories;
4. validate a prespecified sample against source records;
5. quantify disagreement and missingness;
6. produce hospital-relevant descriptive results;
7. document local mapping separately from the portable public framework.

### Required artifacts
- governed mapping specification;
- data-quality report;
- validation/adjudication log;
- cohort results;
- limitations and transportability analysis.

### Verification
- approved data never enter the public repository;
- validation performance is reported transparently;
- conclusions remain descriptive and proportional to data quality/sample size.

### Phase release
`v6-governed-study`

## Cross-phase implementation rules

1. **No forward dependency leakage.** A phase may prepare interfaces for later work but should not require later-phase functionality to satisfy its own gate.
2. **Requirements precede implementation.** New functions or metrics require a requirement ID or documented rationale.
3. **Synthetic truth precedes real-data interpretation.** Reconstruction and metrics are validated first against known truth.
4. **Canonical model precedes local mapping.** Institution-specific workflows belong in adapters/configuration, not the core model.
5. **Every derived result is auditable.** Transformation version and source provenance remain available throughout the pipeline.
6. **Clinical interpretation is separated from engineering validation.** Algorithm correctness does not establish clinical utility.

## Implementation cadence

A practical development cadence is:

- one branch per phase or coherent phase sub-gate;
- one reviewable PR per gate advancement;
- update `ROADMAP.md` checkboxes in the same PR that supplies acceptance evidence;
- tag phase releases only after gate evidence is satisfied;
- freeze thesis-analysis definitions before executing the final governed cohort analysis.
