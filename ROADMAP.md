# CART-TRACE Roadmap

## Research purpose

CART-TRACE is a synthetic-first, non-operational research framework for reconstructing hospital care trajectories surrounding CAR T-cell therapy.

The current MS HSE thesis asks:

> **How can longitudinal clinical data be used to characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy?**

The primary unit of analysis is the **therapy episode**, aligned to treatment-relative time with `day 0 = infusion`.

This roadmap is controlled by four supporting specifications:

- [Requirements](docs/requirements.md) — testable system and research requirements;
- [Phase gates](docs/phase_gates.md) — evidence required before advancing phases;
- [Data requirements](docs/data_requirements.md) — minimum hospital data and source-to-canonical mapping expectations;
- [Validation plan](docs/validation_plan.md) — staged verification from schemas through governed source-record validation.

## Development status

- [x] Thesis question, aims, and success criterion defined
- [x] Public research/non-operational boundary documented
- [x] Governance/data-use document completed
- [x] Controlled care-state vocabulary defined
- [x] Therapy-episode schema created
- [x] Care-state interval schema created
- [x] Care-transition schema created
- [x] Provenance schema completed
- [x] Encounter input contract completed
- [x] Treatment-relative time and interval semantics frozen
- [x] Machine-readable mapping and precedence rules defined
- [x] Complete hand-worked Gate 1 episode validated
- [x] Gate 1 -> 2 passed with CI evidence
- [x] Six-class synthetic cohort implemented
- [x] Phase 2 fixture coverage tests implemented
- [x] Normalized ICU escalation fixture with expected metrics implemented
- [x] Negative/error fixture set implemented
- [ ] Phase 2 CI evidence recorded and Gate 2 -> 3 passed
- [ ] Transition reconstruction implemented
- [ ] Utilization metrics implemented as production research functions
- [ ] Cohort characterization implemented
- [ ] Governed hospital-data validation initiated

**Current phase:** Phase 2 — Synthetic cohort  
**Current gate:** Gate 2 -> 3 — synthetic truth set must be complete, schema-conformant, and CI-validated before reconstruction semantics are frozen.

## Thesis scope

### Included

- encounter timing;
- admission and discharge;
- care location;
- level-of-care state;
- transfer and escalation/de-escalation events;
- length of stay;
- high-acuity exposure;
- early acute-care reuse;
- selected routinely collected observations when useful for contextualizing care intensity;
- provenance, missingness, and deterministic transformation rules.

### Excluded from the thesis core

- CMC/manufacturing attributes;
- product release analytics;
- patient-generated health data;
- remote monitoring;
- treatment recommendation;
- real-time prediction or clinical alerting.

These remain post-thesis research opportunities.

## Core episode model

Initial development window:

`day -7 -> infusion day 0 -> acute hospitalization -> discharge -> day +30`

The canonical episode preserves patient/episode identity, infusion timestamp, encounter boundaries, care-state intervals, transitions, discharge/acute-care return, provenance, and explicit uncertainty.

## Phase 0 — Scope and governance

**Status: complete**

Goal: establish a credible public research boundary and lock the thesis question before implementation expands.

### Completed
- [x] Define thesis question and aims
- [x] Define thesis success criterion
- [x] Establish synthetic-first development policy
- [x] Establish no-PHI/no-production-credentials rule
- [x] Separate descriptive research from bedside decision support
- [x] Separate thesis scope from post-thesis extensions
- [x] Define minimum-necessary data principle
- [x] Define institutional approval gate for real-data use
- [x] Add `docs/governance.md`
- [x] Document research-data lifecycle expectations
- [x] Document public/private artifact separation
- [x] Document minimum institutional approval assumptions without embedding institution-specific policy

**Gate 0 -> 1 status: PASSED.**

---

## Phase 1 — Episode and transition schema

**Status: complete / semantics frozen**

Goal: define the canonical research objects and semantics needed to represent a CAR T hospital episode without relying on institution-specific workflow names.

### Completed
- [x] Controlled care-state vocabulary
- [x] Episode-model documentation
- [x] `therapy_episode` schema
- [x] `care_state_interval` schema
- [x] `care_transition` schema
- [x] `provenance` schema
- [x] Minimal encounter input schema/contract
- [x] Treatment-relative time convention
- [x] Half-open interval-boundary semantics
- [x] Deterministic identical-timestamp behavior
- [x] Machine-readable overlap/conflict precedence rules
- [x] Hand-worked multi-encounter episode
- [x] Schema-conformant expected intervals and transitions
- [x] Provenance truth records
- [x] Automated schema/consistency tests
- [x] Reproducible CI execution

**Gate 1 -> 2 status: PASSED.** See `docs/gates/gate_1_to_2_candidate.md` for the evidence record.

Changes to frozen Phase 1 semantics require explicit gate-impact review and corresponding fixture/test updates.

---

## Phase 2 — Synthetic cohort

**Status: active / gate closure pending CI**

Goal: create a deterministic truth set that functions as the oracle for reconstruction and metric testing.

### Required trajectory fixtures
- [x] routine recovery
- [x] prolonged routine inpatient care
- [x] transient escalation and de-escalation
- [x] ICU escalation
- [x] discharge followed by early acute-care return
- [x] incomplete/conflicting location records

### Fixture contract
- [x] source-like encounter/location inputs
- [x] expected normalized state intervals
- [x] expected transition sequence
- [x] expected uncertainty behavior
- [x] expected utilization metrics
- [x] requirement IDs exercised by each fixture
- [x] edge-case annotations in the manifest

### Validation and failure behavior
- [x] requirement-coverage tests authored
- [x] manifest-to-artifact consistency tests authored
- [x] expected interval/transition schema tests authored
- [x] invalid care-state test case
- [x] malformed timestamp test case
- [x] missing infusion-anchor test case
- [x] reversed interval test case
- [x] deterministic equal-priority overlap case
- [ ] additional boundary fixtures may be added during Phase 3 if they expose previously undocumented reconstruction ambiguity

### Gate 2 -> 3 evidence required
- [x] six trajectory classes implemented
- [x] expected outputs prespecified
- [x] fixture requirement coverage complete
- [x] ICU fixture normalized to the Phase 2 contract
- [x] expected metrics available for all six fixtures
- [x] invalid/error fixtures available
- [x] automated Phase 2 tests authored
- [ ] successful CI execution of the current Phase 2 truth set
- [ ] Gate 2 evidence record changed from conditional to PASS

**Gate 2 -> 3 status: CONDITIONAL / CI PENDING.** See `docs/gates/gate_2_to_3_candidate.md`.

---

## Phase 3 — Transition reconstruction

**Status: next phase / not yet authorized for semantic freeze**

Goal: convert event-level records into deterministic patient-level care-state intervals and transitions that exactly reproduce the frozen synthetic truth set.

### Implementation requirements
- [ ] infusion anchoring and continuous treatment-relative hours
- [ ] timezone normalization
- [ ] deterministic event sorting
- [ ] identical-timestamp tie-breaking
- [ ] source-label-to-canonical-state mapping interface
- [ ] duplicate same-state suppression
- [ ] overlap/conflict resolution
- [ ] interval derivation using `[start, end)` semantics
- [ ] transition derivation only on canonical state changes
- [ ] discharge semantics
- [ ] acute-care-return semantics
- [ ] provenance propagation
- [ ] uncertainty propagation
- [ ] stable canonical serialization

### Validation requirements
- [ ] exact reconstruction of deterministic synthetic fixtures
- [ ] prespecified `unknown`/uncertainty behavior for conflict fixtures
- [ ] repeated runs produce equivalent outputs
- [ ] no false transitions from duplicate same-state records
- [ ] negative inputs fail or resolve exactly as specified by the Phase 2 oracle

### Gate 3 -> 4 acceptance target
- [ ] 100% agreement with prespecified synthetic intervals/transitions for deterministic fixtures
- [ ] all conflict fixtures produce prespecified uncertainty behavior
- [ ] clean reruns are reproducible

**Gate status: NOT STARTED.**

---

## Phase 4 — Hospital utilization metrics

**Status: not started**

Goal: derive transparent, thesis-relevant measures of hospital resource utilization from reconstructed trajectories.

### Required metrics
- [ ] total inpatient duration/days
- [ ] routine inpatient duration
- [ ] higher-observation duration
- [ ] ICU duration
- [ ] combined high-acuity duration where prespecified
- [ ] number of normalized care-state transitions
- [ ] time from infusion to first escalation
- [ ] time from final escalation to discharge
- [ ] treatment-relative time to discharge
- [ ] 7-day acute-care reuse
- [ ] 30-day acute-care reuse
- [ ] unplanned readmission where source data support the distinction

### Required metric semantics
- [ ] partial-day calculation rule
- [ ] inclusive/exclusive interval rule
- [ ] zero-versus-missing rule
- [ ] insufficient-follow-up behavior
- [ ] unknown-state handling
- [ ] study-window censoring behavior
- [ ] provenance for every metric

### Gate 4 -> 5 evidence required
- [ ] formulas/algorithms documented
- [ ] hand-calculated expected fixture values
- [ ] unit tests for each metric
- [ ] window-boundary sensitivity checks

**Gate status: NOT STARTED.**

---

## Phase 5 — Cohort characterization

**Status: not started**

Goal: describe recurrent hospital care patterns across episodes without converting them into predictive or clinical labels.

### Candidate descriptive patterns
- [ ] uncomplicated routine recovery
- [ ] prolonged routine care
- [ ] transient escalation
- [ ] sustained high-acuity care
- [ ] discharge with early acute-care return

### Analysis requirements
- [ ] prespecified feature set derived from Phase 4
- [ ] interpretable grouping strategy
- [ ] rationale for any distance/similarity measure
- [ ] sensitivity analyses
- [ ] uncertainty-aware analysis
- [ ] patient-level traceability from group to trajectory
- [ ] descriptive language only

### Required outputs
- [ ] cohort flow diagram
- [ ] utilization summary table
- [ ] patient-level trajectory examples
- [ ] cohort trajectory visualization
- [ ] missingness/uncertainty report
- [ ] sensitivity-analysis appendix/output

**Gate status: NOT STARTED.**

---

## Phase 6 — Governed hospital-data study

**Status: future / approval dependent**

Goal: evaluate the framework using appropriately approved institutional data and determine whether the synthetic-first methods transfer to real hospital records.

### Readiness requirements
- [ ] finalized data dictionary
- [ ] minimum necessary field list
- [ ] local source-to-canonical mapping plan
- [ ] date/time and timezone conventions
- [ ] approved research/privacy/data-use pathway
- [ ] protected analytic environment
- [ ] validation sample/adjudication plan
- [ ] approved cohort definition
- [ ] follow-up availability assessed for reuse metrics

### Validation activities
- [ ] compare reconstructed encounter boundaries to source records
- [ ] compare reconstructed care-state intervals to source records
- [ ] compare transitions to source records
- [ ] quantify timestamp disagreements
- [ ] quantify `unknown`-state burden
- [ ] classify discrepancies using validation error taxonomy
- [ ] adjudicate approved subset
- [ ] version mapping/reconstruction changes

Numerical real-data acceptance thresholds should be prespecified with the thesis committee after source-data characteristics and feasible validation sample size are known. The public repository should not invent universal clinical-performance thresholds.

**Gate status: APPROVAL DEPENDENT.**

---

## Cross-phase requirement tracking

The implementation maintains the traceability chain:

`thesis aim -> requirement ID -> schema/function -> synthetic fixture -> automated test -> thesis table/figure/result`

### Required artifacts
- [x] `THESIS.md`
- [x] `ROADMAP.md`
- [x] `docs/requirements.md`
- [x] `docs/phase_gates.md`
- [x] `docs/data_requirements.md`
- [x] `docs/validation_plan.md`
- [x] `docs/care_state_vocabulary.md`
- [x] `docs/episode_model.md`
- [x] `docs/governance.md`
- [x] provenance schema
- [x] encounter input schema/contract
- [ ] `docs/data_dictionary.md`
- [ ] `docs/metric_definitions.md`
- [ ] `docs/requirements_traceability.md`

## Thesis deliverables

- [x] thesis question and aims
- [x] documented care-state vocabulary and episode model
- [x] canonical schemas and governance boundary
- [x] testable requirements and formal phase-gate plan
- [x] minimum data requirements and staged validation plan
- [x] synthetic validation cohort substantially complete
- [ ] reproducible transition-reconstruction code
- [ ] utilization metric library
- [ ] interpretable patient-level visualizations
- [ ] cohort-level characterization
- [ ] validation/missingness analysis
- [ ] written discussion of implications for hospital capacity and care-transition research

## Immediate next build sequence

1. [ ] Obtain and record a green CI run for the current Phase 2 fixture/test set.
2. [ ] Mark Gate 2 -> 3 PASS and freeze the synthetic truth set.
3. [ ] Implement the Phase 3 reconstruction module against that frozen oracle.
4. [ ] Require exact interval/transition agreement for deterministic fixtures.
5. [ ] Add explicit tests for reproducibility, duplicate suppression, conflict handling, and provenance propagation.
6. [ ] Pass Gate 3 -> 4 before treating utilization metrics as derived research outputs.

## Post-thesis opportunities

Deferred until the hospital trajectory foundation is established:

- rural access and distance-to-center analyses;
- patient-generated health signals;
- remote recovery monitoring;
- prospective implementation studies;
- cellular-therapy manufacturing/product research;
- predictive or decision-support models.

## Success criterion

CART-TRACE succeeds as an MS thesis framework if it can transform heterogeneous hospital records surrounding CAR T-cell therapy into a transparent, reproducible, patient-level sequence of care states and transitions that supports meaningful cohort-level characterization of hospital utilization.
