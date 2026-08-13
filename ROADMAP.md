# CART-TRACE Roadmap

## Research purpose

CART-TRACE is a synthetic-first, non-operational research framework for reconstructing hospital care trajectories following CAR T-cell therapy.

The MS Health Data Science capstone asks:

> **Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?**

The primary unit of analysis is the **therapy episode**, aligned to continuous treatment-relative time with `infusion timestamp = 0 hours`.

## Development status

- [x] Capstone question, scope, aims, and success criterion defined
- [x] Public research/non-operational boundary documented
- [x] Governance/data-use boundary documented
- [x] Canonical care-state vocabulary defined
- [x] Therapy-episode, interval, transition, encounter, and provenance schemas created
- [x] Hour-relative time and `[start, end)` interval semantics frozen
- [x] Machine-readable mapping and precedence rules defined
- [x] Gate 1 canonical model passed with CI evidence
- [x] Six-class synthetic truth set implemented
- [x] Negative/error cases implemented
- [x] Explicit Phase 2 boundary oracle implemented
- [x] Gate 2 synthetic oracle passed with CI evidence
- [x] Deterministic Phase 3 reconstruction implemented
- [x] Gate 3 reconstruction fidelity passed with CI evidence
- [ ] Utilization metric definitions frozen
- [ ] Utilization metric library implemented
- [ ] Gate 4 metric validity passed
- [ ] Cohort characterization implemented
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** Phase 4 — post-infusion hospital utilization measures  
**Current gate:** Gate 4 -> 5 — metric definitions, missingness/censoring behavior, provenance, and fixture expected-value tests must pass before cohort characterization.

## Canonical care states

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` is a transition type, not a state.

## Core temporal model

Primary capstone analytic window:

`infusion timestamp = 0 -> +720 hours (Day +30)`

A limited pre-infusion context may be represented where needed to establish encounter continuity. Continuous relative hours remain canonical; day labels are derived presentation fields only.

## Phase 0 — Scope and governance

**Status: complete**

The capstone is limited to retrospective, descriptive reconstruction and characterization of post-infusion hospital care. Candidate identification, eligibility adjudication, treatment-readiness gating, product selection, leukapheresis/bridging decisions, toxicity prediction, prospective alerts, CMC/manufacturing analytics, and patient-generated health data are outside the core project.

**Gate 0 -> 1: PASSED.**

---

## Phase 1 — Canonical episode/state/transition model

**Status: complete / frozen**

Completed artifacts include the canonical vocabulary, episode/interval/transition/provenance schemas, encounter-input contract, source mapping, continuous hour-relative time semantics, half-open intervals, conflict behavior, Gate 1 hand-worked episode, and schema/semantic tests.

**Gate 1 -> 2: PASSED.** See `docs/gates/gate_1_to_2_candidate.md`.

Changes to frozen Phase 1 semantics require versioning, fixture/test regeneration, and explicit gate-impact review.

---

## Phase 2 — Synthetic oracle

**Status: complete / frozen**

The oracle includes six representative trajectories:

- [x] routine recovery
- [x] prolonged routine inpatient care
- [x] transient intermediate-care escalation/de-escalation
- [x] intensive-care escalation/de-escalation
- [x] discharge followed by early emergency acute-care return
- [x] conflicting/missing location evidence producing explicit `unknown`

Boundary/error coverage includes invalid canonical state, missing infusion anchor, malformed timestamp, reversed interval, equal-priority conflicts, duplicate same-state inputs, missing/open end time, study-window boundary behavior, adjacent intervals, and same-day discharge-to-emergency return.

**Gate 2 -> 3: PASSED.** See `docs/gates/gate_2_to_3_candidate.md`.

---

## Phase 3 — Deterministic reconstruction

**Status: complete / frozen**

The reconstruction implementation includes:

- [x] offset-aware timestamp parsing
- [x] continuous treatment-relative hours
- [x] versioned source-label mapping
- [x] deterministic source sorting
- [x] overlap priority resolution
- [x] equal-priority conflict -> `unknown`
- [x] duplicate same-state suppression
- [x] non-overlapping `[start, end)` interval derivation
- [x] explicit open-end handling
- [x] typed transition derivation
- [x] escalation/de-escalation classification
- [x] discharge and acute-care-return classification
- [x] source-record propagation
- [x] reconstruction audit records
- [x] stable canonical serialization
- [x] exact six-fixture interval/transition oracle agreement
- [x] deterministic repeated-run behavior

GitHub Actions run `31657957588` completed successfully for commit `536724c4cf996b3192f917d11c909a2ea0eb16fd`.

**Gate 3 -> 4: PASSED.** See `docs/gates/gate_3_to_4_candidate.md`.

Changes to reconstruction semantics require complete regression against the frozen Phase 2 oracle and explicit Gate 3 impact review.

---

## Phase 4 — Post-infusion hospital utilization measures

**Status: active / definitions first**

Goal: derive transparent descriptive measures from reconstructed trajectories without contaminating the method with undocumented analysis choices.

### Primary analytic-window rule

Capstone utilization metrics are defined for post-infusion time from `0` through `+720` hours, using a half-open analytic window `[0, 720)`. Pre-infusion intervals may be retained for continuity/reconstruction validation but are clipped out of primary post-infusion utilization measures.

### Planned primary measures

- [ ] total inpatient duration within `[0, 720)`
- [ ] routine inpatient duration
- [ ] intermediate-care duration
- [ ] intensive-care duration
- [ ] high-acuity duration = intermediate + intensive care, if retained
- [ ] number of canonical care-state transitions in the analytic window
- [ ] time from infusion to first escalation
- [ ] time from infusion to first discharge after treatment
- [ ] 7-day post-discharge acute-care return
- [ ] 30-day post-discharge acute-care return
- [ ] unknown-state duration/burden

### Required metric semantics before implementation freeze

- [ ] exact clipping rule for intervals crossing infusion or Day +30
- [ ] zero-versus-missing behavior
- [ ] unknown/uncertain interval handling
- [ ] open-ended/censored interval behavior
- [ ] incomplete follow-up behavior for return metrics
- [ ] treatment of emergency/outpatient time in inpatient-duration metrics
- [ ] definition/version for combined high-acuity duration
- [ ] metric-level provenance linking values to interval/transition IDs
- [ ] expected fixture values recalculated for the post-infusion `[0,720)` window where existing fixtures include pre-infusion time

### Gate 4 -> 5 acceptance target

Every reported metric must have a documented algorithmic definition, version, provenance, zero/missing/censoring behavior, and passing expected-value tests against the frozen synthetic trajectories.

No cohort-level characterization should be treated as a capstone result until Gate 4 passes.

---

## Phase 5 — Capstone characterization and communication

**Status: not started**

Required outputs are expected to include patient-level trajectory examples, cohort-level utilization summaries, validation/fidelity results, missingness/uncertainty reporting, methods diagrams, reproducible figures/tables, and a manuscript-style capstone report or equivalent scholarly product.

Recurring trajectory groups may be explored descriptively if sample size supports them. Clustering and prediction are not required for capstone success.

---

## Phase 6 — Governed clinical-data application

**Status: future / approval dependent**

If approved institutional data are available, the frozen method may be applied in an approved environment with a local source-to-canonical mapping, data-quality assessment, and validation/adjudication plan. No PHI, production endpoint, credential, or institution-specific identifying artifact belongs in the public repository.

Real-data availability strengthens the capstone but does not determine whether the core computational contribution is complete.

---

## Evidence chain

Every major capstone result should remain traceable through:

`capstone question -> requirement -> schema/function -> synthetic fixture -> automated test -> analytic output -> capstone table/figure`

## Immediate build sequence

1. [x] Merge the canonical Gate 1/Phase 2 foundation to `main`.
2. [x] Pass and freeze Gate 2 using the complete synthetic boundary oracle.
3. [x] Implement and validate deterministic Phase 3 reconstruction.
4. [x] Pass Gate 3 -> 4 with exact oracle, provenance, and reproducibility evidence.
5. [ ] Freeze Phase 4 metric definitions and post-infusion clipping rules.
6. [ ] Recalculate fixture expected values for the `[0,720)` analytic window.
7. [ ] Implement versioned metric functions with provenance and missingness behavior.
8. [ ] Pass Gate 4 -> 5 before cohort characterization.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
