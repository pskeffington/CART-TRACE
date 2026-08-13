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
- [ ] Deterministic Phase 3 reconstruction implemented
- [ ] Gate 3 reconstruction fidelity passed
- [ ] Utilization metric library implemented
- [ ] Cohort characterization implemented
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** Phase 3 — deterministic transition reconstruction  
**Current gate:** Gate 3 -> 4 — reconstruction must exactly reproduce the frozen synthetic oracle before utilization functions are treated as research outputs.

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

Boundary/error coverage includes:

- [x] invalid canonical state
- [x] missing infusion anchor
- [x] malformed timestamp
- [x] reversed interval
- [x] equal-priority conflicting states
- [x] duplicate same-state source records
- [x] missing/open end time
- [x] study-window end boundary
- [x] adjacent intervals sharing a timestamp
- [x] same-day discharge -> emergency acute-care return

GitHub Actions run `31657333214` completed successfully on the frozen Phase 2 test head.

**Gate 2 -> 3: PASSED.** See `docs/gates/gate_2_to_3_candidate.md`.

---

## Phase 3 — Deterministic reconstruction

**Status: active**

Goal: convert source-like encounter/location records into canonical care-state intervals and transitions that reproduce the frozen Phase 2 oracle.

### Implementation work

- [ ] parse and normalize offset-aware timestamps
- [ ] calculate continuous treatment-relative hours
- [ ] map source labels to canonical states through versioned configuration
- [ ] stable-sort source records/events
- [ ] apply configured priority for overlapping evidence
- [ ] emit `unknown` for irreconcilable equal-priority canonical disagreement
- [ ] suppress duplicate same-state records/transitions
- [ ] derive non-overlapping `[start, end)` intervals
- [ ] preserve explicit open/censored end semantics
- [ ] derive transitions only when canonical state changes
- [ ] classify escalation/de-escalation using inpatient acuity ranks
- [ ] classify discharge
- [ ] classify configured post-discharge acute-care return
- [ ] propagate all contributing source-record IDs and mapping method
- [ ] provide stable canonical serialization

### Gate 3 -> 4 acceptance targets

- [ ] 100% interval agreement for deterministic frozen fixtures
- [ ] 100% transition agreement for deterministic frozen fixtures
- [ ] conflict fixture produces prespecified `unknown`/uncertainty behavior
- [ ] duplicate same-state input produces no false transition
- [ ] boundary cases match frozen Phase 2 behavior
- [ ] repeated runs produce equivalent canonical outputs
- [ ] every interval/transition is auditable to source records or an explicit derivation rule

No Phase 4 metric should be treated as a computed capstone result until Gate 3 passes.

---

## Phase 4 — Post-infusion hospital utilization measures

**Status: not started**

Planned transparent descriptive measures include:

- total inpatient duration within the defined analytic window;
- routine inpatient duration;
- intermediate-care duration;
- intensive-care duration;
- combined high-acuity duration where explicitly defined;
- number and timing of care-state transitions;
- time from infusion to first escalation;
- time to discharge;
- 7-day acute-care return;
- 30-day acute-care return;
- unknown/missing-state burden.

Metric definitions must specify clipping, partial intervals, zero-versus-missing, censoring/follow-up, uncertainty, and provenance before Gate 4 passage.

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
3. [ ] Implement Phase 3 timestamp, mapping, sorting, and interval-building primitives.
4. [ ] Reconstruct the six frozen trajectories from source-like inputs rather than reading expected outputs.
5. [ ] Require exact canonical interval/transition agreement.
6. [ ] Add stable-output, provenance, duplicate-suppression, open-end, conflict, and boundary regression tests.
7. [ ] Pass Gate 3 -> 4 before implementing thesis-facing utilization outputs.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
