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
- [x] Phase 5 reporting helpers implemented
- [x] Reproducible synthetic output generator implemented and CI-validated
- [x] Manuscript Methods/Results scaffold and table/figure inventory defined
- [x] Patient-level capstone trajectory figures rendered reproducibly
- [x] Cohort-style synthetic characterization table rendered reproducibly
- [x] Capstone validation and uncertainty tables rendered reproducibly
- [x] Figure 3 utilization/availability visualization rendered reproducibly
- [ ] Methods/data-flow Figure 1 finalized
- [ ] Specification-oriented Tables 1–2 finalized
- [ ] Phase 5 scholarly-output gate fully passed
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** Phase 5 — capstone characterization and communication  
**Current gate:** quantitative synthetic scholarly outputs are reproducibly rendered and linked to the manuscript scaffold; the remaining Phase 5 work is specification-oriented Figure 1/Tables 1–2 completion plus final integration/freeze review.

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

**Status: active / quantitative rendering validated**

Goal: turn validated canonical trajectories and metric results into transparent scholarly outputs without changing the frozen data semantics.

### Completed Phase 5 infrastructure

- [x] deterministic patient-level trajectory reporting rows;
- [x] denominator-aware cohort metric summaries;
- [x] reconstruction fidelity summaries;
- [x] expected-versus-actual metric validation rows;
- [x] missingness/uncertainty summaries;
- [x] reproducible generator for six controlled Phase 5 JSON output classes;
- [x] CI validation of generated outputs;
- [x] formal main-text and supplementary table/figure inventory;
- [x] manuscript-style Methods scaffold;
- [x] manuscript-style synthetic Results scaffold;
- [x] limitations and governed-data transfer scaffold;
- [x] deterministic rendering entry point for quantitative Phase 5 artifacts;
- [x] rendering manifest with controlled source-to-output paths;
- [x] manuscript scaffold references generated artifacts rather than manually maintained numeric results.

GitHub Actions run `31827148476` completed successfully for commit `7aa5b44bf25fab87ac75908252c0cc048ab457fe`, validating generation, rendering, Figure 3 availability controls, deterministic rendering behavior, and the full automated suite on supported Python versions.

### Quantitative presentation outputs

- [x] render patient-level synthetic trajectory figures using treatment-relative time;
- [x] render cohort-style synthetic utilization summary table from generated output;
- [x] render reconstruction fidelity and metric validation table from generated output;
- [x] render missingness/uncertainty table from generated output;
- [x] render utilization/metric-availability Figure 3 from generated output;
- [x] link generated quantitative artifacts into the manuscript scaffold without manually duplicating numeric results.

### Remaining specification-oriented outputs

- [ ] finalize Figure 1 showing source -> staging -> canonical trajectory -> validation -> metrics -> outputs;
- [ ] finalize Table 1 summarizing the canonical data model and deterministic transformation rules;
- [ ] finalize Table 2 summarizing the six synthetic truth-set trajectory classes and validation targets;
- [ ] perform one final manuscript-output inventory review confirming every required artifact has a controlled source and explicit synthetic/clinical-validity boundary.

### Phase 5 scholarly-output gate

Phase 5 is complete only when the controlled machine-readable outputs and frozen method specifications have been converted into the planned scholarly artifacts without introducing a second, manually maintained analytic representation.

Gate requirements:

- [x] one deterministic rendering entry point consumes the controlled `examples/outputs/phase5_*.json` artifacts;
- [x] Figure 2 and Supplementary Figure S1 are generated directly from patient-level trajectory output using treatment-relative time;
- [x] Tables 3–5 are generated directly from reconstruction validation, metric validation, cohort summary, and uncertainty outputs;
- [x] Figure 3 reports metric availability alongside descriptive values so unavailable or incomplete-follow-up results cannot be silently treated as zeros;
- [x] generated quantitative artifacts carry a synthetic-demonstration boundary and avoid claims of external clinical validity;
- [x] generated numeric values are not manually duplicated in manuscript source text when a controlled output can supply them;
- [x] repeat rendering from unchanged inputs is deterministic at the data/content level;
- [x] manuscript scaffold references the generated quantitative artifacts and preserves source-to-output traceability;
- [x] CI reproducibility evidence records a successful generation-and-render pass;
- [ ] Figure 1 and Tables 1–2 are finalized from frozen specification sources;
- [ ] final scholarly-output inventory review confirms all main-text and supplementary artifacts are accounted for.

**Gate 5 -> scholarly prototype freeze: PARTIALLY PASSED / quantitative layer validated.** The remaining work is specification-oriented presentation and final freeze review, not expansion of reconstruction or metric logic.

### Next focused pass — specification-oriented scholarly outputs

Primary task: complete Figure 1 and Tables 1–2 directly from frozen method specifications and synthetic fixture definitions.

Completion artifacts for this pass:

1. render or otherwise finalize Figure 1 from `docs/clinical_data_structuring_framework.md`, schemas, mapping config, and metric contract;
2. produce Table 1 from frozen schema objects, interval/transition semantics, mapping/conflict rules, provenance behavior, and implementation paths;
3. produce Table 2 from the six frozen Phase 2 synthetic fixture classes and their validation targets;
4. add artifact paths to `docs/phase5_rendering_manifest.md` and `docs/manuscript_scaffold.md`;
5. perform a final inventory reconciliation against `docs/table_figure_inventory.md`;
6. only then mark the Phase 5 scholarly-output gate passed and freeze the synthetic scholarly prototype.

This pass should not alter frozen care-state semantics, reconstruction precedence, metric definitions, follow-up rules, or the six-case oracle unless a defect is demonstrated and handled through explicit gate-impact review.

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

## 21-month capstone execution horizon

The remaining schedule is organized around three linked claims: **computational validity**, **representation validity**, and **analytic utility**. The first is established primarily through the frozen synthetic gates. Later work should increasingly emphasize governed-data validation, descriptive analysis, and scholarly completion rather than expanding core software architecture.

| Months | Primary objective | Completion products |
|---|---|---|
| 1–4 | Computational foundation | canonical model, synthetic oracle, reconstruction, metric contract, Gates 1–4 |
| 5–7 | Scholarly prototype freeze | generated synthetic tables/figures, reproducibility package, manuscript Methods/Results scaffold |
| 6–10 | Governance and data readiness | cohort specification, source-field inventory, local mapping protocol, validation/adjudication plan |
| 9–14 | Governed-data application, if feasible | source profiling, mapping coverage, reconstructability, uncertainty and follow-up characterization |
| 12–16 | Empirical validation | source-concordance review, discrepancy analysis, mapping review, sensitivity analyses, metric availability |
| 15–18 | Primary descriptive analysis | patient trajectories, utilization distributions, escalation/de-escalation, discharge and return summaries |
| 18–20 | Scholarly synthesis | final Methods, Results, Discussion, tables, figures, limitations, reproducibility statement |
| 21 | Final freeze and capstone completion | reproducibility audit, repository release, presentation/submission package |

Periods intentionally overlap. Governance preparation can begin while the synthetic scholarly prototype is finalized, and writing should continue throughout empirical work rather than being deferred to the final months.

### Work-session completion rule

Each focused work session should define one primary task and one concrete completion artifact. A session is complete when the task supports a named capstone milestone, the artifact is committed or otherwise controlled, frozen semantics are not changed implicitly, validation evidence is added when logic changes, CI is checked before milestone claims, traceability is preserved, synthetic and governed findings remain separated, and the next highest-value task is recorded.

### Monthly alignment review

Review whether current work still supports the primary capstone question; whether it strengthens computational validity, representation validity, or analytic utility; whether uncertainty, denominators, and follow-up limitations are visible; whether outputs remain traceable to controlled inputs; whether governed work is separated from public synthetic artifacts; whether engineering effort is decreasing as the method stabilizes; and whether adequate time remains for validation, writing, revision, and final presentation.

### Scope guardrail

Core-aligned extensions include source mapping, data-quality and reconstructability assessment, source-concordance validation, uncertainty analysis, descriptive trajectory characterization, sensitivity analyses, and publication-quality communication. Prediction, eligibility/readiness logic, prospective decision support, operational forecasting, broad multi-institution platform development, and causal treatment-effect estimation remain outside the required capstone scope unless explicitly re-scoped.

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
9. [x] Implement CI-validated Phase 5 reporting and output-generation infrastructure.
10. [x] Define manuscript structure and controlled table/figure inventory.
11. [x] Implement the controlled Phase 5 rendering entry point and content-level checks.
12. [x] Render quantitative manuscript tables and figures from generated machine-readable outputs.
13. [x] Integrate generated quantitative artifacts into the manuscript scaffold without manual numeric duplication.
14. [ ] Finalize Figure 1 and Tables 1–2 from frozen specification sources.
15. [ ] Reconcile the complete scholarly-output inventory and pass the Phase 5 freeze gate.
16. [ ] Complete final validation, limitations, and reproducibility reporting for the scholarly product.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
