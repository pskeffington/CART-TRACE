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
- [x] Therapy-episode, interval, transition, encounter, provenance, and metric-result schemas created
- [x] Hour-relative time and `[start, end)` interval semantics frozen
- [x] Machine-readable mapping and precedence rules defined
- [x] Gate 1 canonical model passed with CI evidence
- [x] Six-class synthetic truth set implemented
- [x] Negative/error and boundary cases implemented
- [x] Gate 2 synthetic oracle passed with CI evidence
- [x] Deterministic Phase 3 reconstruction implemented
- [x] Gate 3 reconstruction fidelity passed with CI evidence
- [x] Utilization metric definitions frozen
- [x] Utilization metric library implemented
- [x] Follow-up, zero/missing, uncertainty, and provenance semantics implemented
- [x] Gate 4 metric validity passed with CI evidence
- [ ] Patient-level capstone trajectory outputs implemented
- [ ] Cohort-style synthetic characterization implemented
- [ ] Capstone validation/methods tables finalized
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** Phase 5 — capstone characterization and communication  
**Current gate:** Phase 5 outputs must remain traceable to the frozen reconstruction and metric contracts; governed clinical-data application remains a separate approval-dependent phase.

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

Primary utilization uses `[0,720)`. Limited pre-infusion context may be retained only to establish encounter continuity. Continuous relative hours remain canonical; day labels are derived presentation fields only.

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

The reconstruction implementation includes offset-aware timestamp parsing, continuous treatment-relative hours, versioned source-label mapping, deterministic ordering, overlap resolution, explicit `unknown`, duplicate suppression, non-overlapping `[start,end)` intervals, open-end handling, typed transitions, provenance, stable serialization, exact oracle agreement, and deterministic repeatability.

GitHub Actions run `31657957588` completed successfully for commit `536724c4cf996b3192f917d11c909a2ea0eb16fd`.

**Gate 3 -> 4: PASSED.** See `docs/gates/gate_3_to_4_candidate.md`.

---

## Phase 4 — Post-infusion hospital utilization measures

**Status: complete / frozen**

Primary metric semantics:

- analytic window `[0,720)` hours after infusion;
- pre-infusion continuity context excluded from utilization totals;
- total inpatient, routine, intermediate, intensive, and high-acuity duration;
- transition count;
- time to first escalation;
- time to discharge;
- 7-day and 30-day post-discharge acute-care return;
- unknown-state burden;
- explicit observed/zero/not-applicable/not-calculable/incomplete-follow-up statuses;
- negative return requires complete post-discharge ascertainment horizon;
- positive documented return remains observed even if later follow-up is incomplete;
- metric-result schema and interval/transition/source-record provenance.

GitHub Actions run `31659472624` completed successfully for commit `b5ecb78071f2b194ede887fbb2d3dbd260068416`.

**Gate 4 -> 5: PASSED.** See `docs/gates/gate_4_to_5_candidate.md`.

Changes to frozen Phase 4 semantics require versioning, affected fixture regeneration, regression testing, and explicit Gate 4 impact review.

---

## Phase 5 — Capstone characterization and communication

**Status: active**

Goal: turn validated canonical trajectories and metric results into transparent scholarly outputs without changing the frozen data semantics.

### Priority outputs

- [ ] patient-level synthetic trajectory figures using treatment-relative time;
- [ ] cohort-style synthetic utilization summary table;
- [ ] reconstruction fidelity table;
- [ ] metric validation table;
- [ ] missingness/uncertainty summary;
- [ ] methods/data-flow figure showing source -> staging -> canonical trajectory -> validation -> metrics -> outputs;
- [ ] manuscript-style Methods scaffold;
- [ ] manuscript-style synthetic Results scaffold;
- [ ] limitations and governed-data transfer section.

### Characterization principles

- descriptive rather than predictive;
- distinguish observed zero from unavailable/not-calculable results;
- report denominator and metric availability explicitly;
- show uncertainty/unknown-state burden rather than hiding excluded episodes;
- retain treatment-relative timing in patient-level displays;
- do not infer clinical severity from care location alone;
- do not claim capacity forecasting or prospective decision support;
- keep synthetic demonstration results distinct from future governed clinical findings.

Recurring trajectory groups may be explored descriptively if a future governed sample supports them. Clustering and prediction are not required for capstone success.

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
5. [x] Freeze Phase 4 metric definitions and post-infusion clipping rules.
6. [x] Recalculate fixture expected values for `[0,720)`.
7. [x] Implement versioned metric functions with provenance and missingness/follow-up behavior.
8. [x] Pass Gate 4 -> 5 with exact metric-oracle and schema evidence.
9. [ ] Build synthetic patient-level and cohort-level capstone outputs.
10. [ ] Assemble validation, methods, limitations, and reproducibility reporting for the final scholarly product.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
