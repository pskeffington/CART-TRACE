# CART-TRACE Roadmap

## Research purpose

CART-TRACE is a synthetic-first, non-operational research framework for reconstructing hospital care trajectories surrounding CAR T-cell therapy.

The current MS HSE thesis asks:

> **How can longitudinal clinical data be used to characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy?**

The primary unit of analysis is the **therapy episode**, aligned to treatment-relative time with `day 0 = infusion`.

## Development status

- [x] Thesis question narrowed to hospital care trajectories
- [x] Thesis aims and success criterion defined
- [x] Public research/non-operational boundary documented
- [x] Controlled care-state vocabulary defined
- [x] Therapy-episode schema created
- [x] Care-state interval schema created
- [x] Care-transition schema created
- [ ] Governance/data-use document completed
- [ ] Treatment-relative time utilities implemented
- [ ] Synthetic cohort fixtures implemented
- [ ] Transition reconstruction implemented
- [ ] Utilization metrics implemented
- [ ] Validation test suite implemented
- [ ] Cohort characterization implemented
- [ ] Governed hospital-data validation initiated

**Current phase:** Phase 1 - Episode and transition schema

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

## Phased development

### Phase 0 - Scope and governance

**Status: substantially complete**

Goal: establish a credible public research boundary.

- [x] Define thesis question and aims
- [x] Define thesis success criterion
- [x] Establish synthetic-first development policy
- [x] Establish no-PHI/no-production-credentials rule
- [x] Separate descriptive research from bedside decision support
- [x] Separate thesis scope from post-thesis extensions
- [ ] Add `docs/governance.md` with data-use, privacy, provenance, and institutional-approval expectations

**Exit criterion:** governance documentation is complete and public examples remain synthetic-only.

---

### Phase 1 - Episode and transition schema

**Status: active / near completion**

Goal: define the core research objects required to represent a CAR T hospital episode.

- [x] Define controlled care-state vocabulary
- [x] Document episode model and treatment-relative representation
- [x] Create `therapy_episode` schema
- [x] Create `care_state_interval` schema
- [x] Create `care_transition` schema
- [ ] Define provenance object/schema
- [ ] Define encounter input contract or minimal schema
- [ ] Validate schema relationships using a complete synthetic episode

Design requirements:

- [x] preserve absolute timestamps
- [x] support treatment-relative time
- [x] avoid institution-specific unit names in the canonical model
- [x] represent missingness/uncertainty explicitly
- [x] preserve source identifiers/provenance fields
- [ ] demonstrate multiple encounters within one episode

**Exit criterion:** one end-to-end synthetic episode validates across all core schemas without ambiguity.

---

### Phase 2 - Synthetic cohort

**Status: not started**

Goal: build deterministic synthetic trajectories for development and validation.

Required fixtures:

- [ ] routine recovery
- [ ] prolonged routine inpatient care
- [ ] transient escalation and de-escalation
- [ ] ICU escalation
- [ ] discharge followed by early acute-care return
- [ ] incomplete or conflicting location records

For each fixture:

- [ ] define expected state intervals
- [ ] define expected transitions
- [ ] define expected utilization metrics
- [ ] document edge cases
- [ ] confirm no institutional identifiers/workflow names are embedded

**Exit criterion:** all fixtures have known expected outputs suitable for automated testing.

---

### Phase 3 - Transition reconstruction

**Status: not started**

Goal: transform event-level records into reproducible care-state intervals and transitions.

- [ ] implement infusion-day anchoring
- [ ] implement treatment-relative time conversion
- [ ] normalize encounter/location events
- [ ] sort events deterministically
- [ ] resolve overlapping records using documented precedence rules
- [ ] derive care-state intervals
- [ ] derive transition events
- [ ] preserve source provenance
- [ ] preserve uncertainty/conflict flags
- [ ] generate a patient-level timeline table

Primary outputs:

- [ ] patient-level care-state interval table
- [ ] patient-level transition table
- [ ] treatment-relative timeline
- [ ] reconstruction validation report

**Exit criterion:** synthetic fixtures reconstruct to their prespecified expected trajectories.

---

### Phase 4 - Hospital utilization metrics

**Status: not started**

Goal: quantify hospital use from reconstructed trajectories.

- [ ] total inpatient days
- [ ] days by care state
- [ ] number of transfers
- [ ] time to first escalation
- [ ] duration of high-acuity exposure
- [ ] time from final escalation to discharge
- [ ] 7-day acute-care reuse
- [ ] 30-day acute-care reuse
- [ ] unplanned readmission where source data support the distinction
- [ ] metric-level provenance and missingness reporting

These remain descriptive research measures, not clinical thresholds.

**Exit criterion:** every synthetic fixture produces deterministic, tested utilization measures.

---

### Phase 5 - Cohort characterization

**Status: not started**

Goal: determine whether recurrent hospital care patterns are visible across episodes.

Candidate descriptive patterns:

- [ ] uncomplicated routine recovery
- [ ] prolonged routine care
- [ ] transient escalation
- [ ] sustained high-acuity care
- [ ] discharge with early acute-care return

Method development:

- [ ] establish interpretable feature set from Phase 4
- [ ] define descriptive grouping strategy
- [ ] perform sensitivity analyses
- [ ] retain patient-level traceability from group summaries
- [ ] visualize missingness and uncertainty
- [ ] avoid predictive/clinical labeling claims

**Exit criterion:** cohort summaries are reproducible and every group assignment can be traced back to the underlying episode sequence.

---

### Phase 6 - Governed hospital-data study

**Status: future / approval dependent**

Goal: evaluate CART-TRACE on appropriately governed institutional data.

- [ ] define institutional data requirements
- [ ] obtain required research/privacy approvals
- [ ] map local encounter/location data into the canonical model
- [ ] compare reconstructed transitions against source records
- [ ] quantify missingness and disagreement
- [ ] manually adjudicate an approved validation subset
- [ ] characterize hospital utilization using the validated pipeline
- [ ] document limitations and transportability

**Exit criterion:** demonstrate whether the framework can reproducibly characterize real hospital care trajectories without making operational recommendations.

## Thesis deliverables

- [x] thesis question and aims
- [x] documented care-state vocabulary
- [x] documented episode model
- [x] initial core schemas
- [ ] reproducible transition-reconstruction code
- [ ] synthetic validation cohort and tests
- [ ] utilization metric library
- [ ] interpretable patient-level visualizations
- [ ] cohort-level characterization
- [ ] validation/missingness analysis
- [ ] written discussion of implications for hospital capacity and care-transition research

## Near-term build order

- [x] Care-state vocabulary
- [x] Therapy-episode schema
- [x] Care-state interval schema
- [x] Care-transition schema
- [ ] Provenance and encounter input definitions
- [ ] Treatment-relative time utilities
- [ ] Synthetic fixtures
- [ ] Transition reconstruction
- [ ] Utilization metrics
- [ ] Validation tests
- [ ] Cohort reporting

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
