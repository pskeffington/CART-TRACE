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

- [x] Thesis question narrowed to hospital care trajectories
- [x] Thesis aims and success criterion defined
- [x] Public research/non-operational boundary documented
- [x] Controlled care-state vocabulary defined
- [x] Therapy-episode schema created
- [x] Care-state interval schema created
- [x] Care-transition schema created
- [x] Engineering/research requirements defined
- [x] Phase-gate criteria defined
- [x] Minimum hospital data requirements defined
- [x] Staged validation plan defined
- [ ] Governance/data-use document completed
- [ ] Provenance schema completed
- [ ] Encounter input contract completed
- [ ] Treatment-relative time utilities implemented
- [ ] Complete end-to-end synthetic episode validated
- [ ] Synthetic cohort fixtures implemented
- [ ] Transition reconstruction implemented
- [ ] Utilization metrics implemented
- [ ] Validation test suite implemented
- [ ] Cohort characterization implemented
- [ ] Governed hospital-data validation initiated

**Current phase:** Phase 1 — Episode and transition schema  
**Current gate:** Gate 1 -> 2 — canonical model must become stable enough to support synthetic fixtures.

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

**Status: substantially complete**

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

### Remaining
- [ ] Add `docs/governance.md`
- [ ] Document research-data lifecycle expectations
- [ ] Document public/private artifact separation
- [ ] Document minimum institutional approval assumptions without embedding institution-specific policy

### Gate 0 -> 1 evidence
- [x] thesis question documented
- [x] included/excluded domains documented
- [x] synthetic-first policy documented
- [x] public non-operational boundary documented
- [x] success criterion documented

**Gate status: PASSED**, with governance documentation still required before any real-data phase.

---

## Phase 1 — Episode and transition schema

**Status: active / near completion**

Goal: define the canonical research objects and semantics needed to represent a CAR T hospital episode without relying on institution-specific workflow names.

### Completed
- [x] Controlled care-state vocabulary
- [x] Episode-model documentation
- [x] `therapy_episode` schema
- [x] `care_state_interval` schema
- [x] `care_transition` schema
- [x] Absolute plus treatment-relative time required conceptually
- [x] Missingness/uncertainty required conceptually
- [x] Source provenance required conceptually
- [x] Minimum hospital data requirements specified

### Remaining
- [ ] Define `provenance` schema/object
- [ ] Define minimal encounter input schema/contract
- [ ] Freeze treatment-relative time convention
- [ ] Freeze interval-boundary semantics
- [ ] Define deterministic tie-breaking at identical timestamps
- [ ] Define overlap/conflict precedence rules in machine-readable or testable form
- [ ] Create one hand-worked multi-encounter episode
- [ ] Validate that episode across all schemas

### Gate 1 -> 2 evidence required
- [x] controlled vocabulary
- [x] therapy-episode schema
- [x] care-state interval schema
- [x] care-transition schema
- [ ] encounter input specification
- [ ] provenance specification
- [ ] deterministic relative-time convention
- [ ] complete hand-worked episode

**Gate status: NOT YET PASSED.**

---

## Phase 2 — Synthetic cohort

**Status: not started**

Goal: create a deterministic truth set that can function as the oracle for reconstruction and metric testing.

### Required trajectory fixtures
- [ ] routine recovery
- [ ] prolonged routine inpatient care
- [ ] transient escalation and de-escalation
- [ ] ICU escalation
- [ ] discharge followed by early acute-care return
- [ ] incomplete/conflicting location records

### Every fixture must include
- [ ] source-like encounter/location inputs
- [ ] expected normalized state intervals
- [ ] expected transition sequence
- [ ] expected uncertainty flags
- [ ] expected utilization metrics
- [ ] requirement IDs exercised by the fixture
- [ ] edge-case notes

### Required fixture edge cases
- [ ] duplicate same-state records
- [ ] identical timestamps
- [ ] adjacent intervals
- [ ] overlapping location records
- [ ] missing end time
- [ ] gap in known care state
- [ ] event at infusion boundary
- [ ] event at study-window boundary
- [ ] insufficient post-discharge follow-up

### Gate 2 -> 3 evidence required
- [ ] six trajectory classes implemented
- [ ] expected outputs prespecified
- [ ] fixture requirement-coverage matrix complete
- [ ] invalid fixtures available for schema/error testing

**Gate status: NOT STARTED.**

---

## Phase 3 — Transition reconstruction

**Status: not started**

Goal: convert event-level records into deterministic patient-level care-state intervals and transitions.

### Implementation requirements
- [ ] infusion-day anchoring
- [ ] treatment-relative day/hour conversion
- [ ] timezone convention
- [ ] deterministic event sorting
- [ ] identical-timestamp tie-breaking
- [ ] local-source-to-canonical state mapping interface
- [ ] duplicate suppression
- [ ] overlap/conflict handling
- [ ] interval derivation
- [ ] transition derivation
- [ ] discharge semantics
- [ ] acute-care-return semantics
- [ ] provenance propagation
- [ ] uncertainty propagation
- [ ] stable canonical serialization

### Validation requirements
- [ ] exact reconstruction of deterministic synthetic fixtures
- [ ] expected `unknown`/uncertainty behavior for conflict fixtures
- [ ] repeated runs produce equivalent outputs
- [ ] no false transitions from duplicate same-state records

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

Goal: determine whether recurrent hospital care patterns can be described across episodes without converting them into predictive or clinical labels.

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
- [ ] rationale for number of groups
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

### Gate 5 -> 6 evidence required
- [ ] cohort summaries reproduce from canonical outputs
- [ ] all group assignments trace to episode-level features
- [ ] uncertainty is visible
- [ ] results do not require undocumented manual intervention

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

### Real-data acceptance targets
Numerical thresholds should be prespecified with the thesis committee after source-data characteristics and feasible validation sample size are known. The public repository should not invent universal clinical-performance thresholds.

**Gate status: APPROVAL DEPENDENT.**

---

## Cross-phase requirement tracking

The implementation should maintain traceability between requirements, evidence, and thesis outputs.

### Mandatory traceability chain

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
- [ ] `docs/governance.md`
- [ ] `docs/data_dictionary.md`
- [ ] `docs/metric_definitions.md`
- [ ] `docs/requirements_traceability.md`
- [ ] provenance schema
- [ ] encounter input schema/contract

## Thesis deliverables

- [x] thesis question and aims
- [x] documented care-state vocabulary
- [x] documented episode model
- [x] initial core schemas
- [x] testable requirements specification
- [x] formal phase-gate plan
- [x] minimum data requirements
- [x] staged validation plan
- [ ] reproducible transition-reconstruction code
- [ ] synthetic validation cohort and tests
- [ ] utilization metric library
- [ ] interpretable patient-level visualizations
- [ ] cohort-level characterization
- [ ] validation/missingness analysis
- [ ] written discussion of implications for hospital capacity and care-transition research

## Immediate next build sequence

Before entering Phase 2:

1. [ ] Create `docs/governance.md`.
2. [ ] Create provenance schema.
3. [ ] Create minimal encounter input contract/schema.
4. [ ] Freeze treatment-relative time and interval semantics.
5. [ ] Create one complete hand-worked multi-encounter episode.
6. [ ] Validate all Phase 1 objects together.
7. [ ] Mark Gate 1 -> 2 complete only after the evidence is present.

Then begin Phase 2 synthetic fixtures.

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
