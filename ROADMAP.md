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
- [x] Main-text and supplementary scholarly outputs finalized from controlled sources
- [x] Phase 5 scholarly-output gate passed with CI evidence
- [x] Synthetic scholarly prototype frozen
- [ ] Governance/data-readiness package finalized
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** Phase 6 preparation — governance and data readiness  
**Current gate:** the synthetic computational and scholarly prototype is frozen. New work should prepare a governed retrospective application without modifying frozen analytic semantics.

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

## Phases 0–5 — synthetic methodological development

**Status: complete / frozen**

The canonical representation, synthetic oracle, deterministic reconstruction, utilization metrics, reporting layer, and complete scholarly artifact inventory have passed their respective gates. Gate 5 was promoted to **PASSED** after GitHub Actions run `31828145837` completed successfully for commit `6428fda0be4b69f3d29a408d07e3611a69dd4daf`.

See:

- `docs/gates/gate_1_to_2_candidate.md`
- `docs/gates/gate_2_to_3_candidate.md`
- `docs/gates/gate_3_to_4_candidate.md`
- `docs/gates/gate_4_to_5_candidate.md`
- `docs/gates/gate_5_scholarly_prototype_freeze_candidate.md`
- `docs/phase5_rendering_manifest.md`

Any change to frozen care states, interval semantics, source precedence, reconstruction behavior, metric definitions, follow-up rules, or the six-case oracle requires explicit gate-impact review and renewed validation.

---

## Phase 6 preparation — Governance and data readiness

**Status: active / pre-data**

Goal: prepare the frozen CART-TRACE method for an approved retrospective hospital-data application while keeping governed data and institution-specific details out of the public repository.

### Governance/data-readiness deliverables

- [ ] cohort specification defining the therapy episode population and index infusion anchor;
- [ ] minimum source-field inventory for encounter, admission/discharge, location/transfer, disposition, and infusion records;
- [ ] local source-to-canonical mapping protocol with mapping-review and versioning rules;
- [ ] source-data quality profile specification covering timestamp precision, missingness, overlap/conflict burden, and observation completeness;
- [ ] reconstructability classification protocol (`reconstructable`, `reconstructable_with_uncertainty`, `not_reconstructable`);
- [ ] source-concordance/adjudication plan for a governed validation sample;
- [ ] metric-specific follow-up sufficiency and censoring review plan;
- [ ] discrepancy log structure for mapping, timing, reconstruction, and metric disagreements;
- [ ] public/private boundary describing which artifacts may enter the public repository and which remain governed;
- [ ] pre-analysis checklist confirming no frozen analytic rule is changed implicitly during local mapping.

### Gate 6 readiness criteria

A governed-data application may begin only when:

1. approvals and data access are in place;
2. the cohort and infusion-anchor definition are documented;
3. required source domains and fields are identified;
4. local mapping is reviewed and versioned separately from the public synthetic mapping;
5. source-concordance and adjudication procedures are defined;
6. reconstructability, uncertainty, and follow-up sufficiency rules are operationalized for review;
7. no PHI, credentials, local identifiers, or institution-specific confidential mappings are committed publicly;
8. any proposed change to the frozen method is handled through explicit gate-impact review rather than silently embedded in local preprocessing.

**Gate 6 -> governed application: NOT YET PASSED.** Data readiness and governance documentation are the next work products.

### Next focused pass — governance/data-readiness package

Primary task: create a controlled documentation package that can be used to scope and review an eventual governed clinical-data extract without requiring access to actual patient data.

Completion artifacts:

1. `docs/governance/cohort_specification.md`;
2. `docs/governance/source_field_inventory.md`;
3. `docs/governance/local_mapping_protocol.md`;
4. `docs/governance/validation_adjudication_plan.md`;
5. `docs/governance/public_private_boundary.md`;
6. update manuscript Methods/governed-data extension references as appropriate.

This phase is documentation and review design, not new analytic feature development.

---

## 21-month capstone execution horizon

The schedule is organized around three linked claims: **computational validity**, **representation validity**, and **analytic utility**. Computational validity and the synthetic scholarly prototype are now frozen; subsequent work should increasingly emphasize governed-data readiness, empirical validation, descriptive analysis, and scholarly completion.

| Months | Primary objective | Completion products |
|---|---|---|
| 1–4 | Computational foundation | canonical model, synthetic oracle, reconstruction, metric contract, Gates 1–4 |
| 5–7 | Scholarly prototype freeze | generated synthetic tables/figures, reproducibility package, manuscript Methods/Results scaffold, Gate 5 |
| 6–10 | Governance and data readiness | cohort specification, source-field inventory, local mapping protocol, validation/adjudication plan |
| 9–14 | Governed-data application, if feasible | source profiling, mapping coverage, reconstructability, uncertainty and follow-up characterization |
| 12–16 | Empirical validation | source-concordance review, discrepancy analysis, mapping review, sensitivity analyses, metric availability |
| 15–18 | Primary descriptive analysis | patient trajectories, utilization distributions, escalation/de-escalation, discharge and return summaries |
| 18–20 | Scholarly synthesis | final Methods, Results, Discussion, tables, figures, limitations, reproducibility statement |
| 21 | Final freeze and capstone completion | reproducibility audit, repository release, presentation/submission package |

Periods intentionally overlap. Governance preparation may proceed before data access, and writing should continue throughout empirical work rather than being deferred to the final months.

### Work-session completion rule

Each focused work session should define one primary task and one concrete completion artifact. A session is complete when the task supports a named capstone milestone, the artifact is committed or otherwise controlled, frozen semantics are not changed implicitly, validation evidence is added when logic changes, CI is checked before milestone claims, traceability is preserved, synthetic and governed findings remain separated, and the next highest-value task is recorded.

### Scope guardrail

Core-aligned Phase 6 extensions include source mapping, data-quality and reconstructability assessment, source-concordance validation, uncertainty analysis, descriptive trajectory characterization, sensitivity analyses, and publication-quality communication. Prediction, eligibility/readiness logic, prospective decision support, operational forecasting, broad multi-institution platform development, and causal treatment-effect estimation remain outside the required capstone scope unless explicitly re-scoped.

---

## Evidence chain

Every major capstone result should remain traceable through:

`capstone question -> requirement -> schema/function -> synthetic fixture -> automated test -> analytic output -> capstone table/figure`

For governed work, extend this chain with:

`approved source field -> local mapping rule -> canonical object -> concordance/adjudication evidence -> metric eligibility -> governed analytic result`

## Immediate build sequence

1. [x] Complete and freeze synthetic computational Gates 1–4.
2. [x] Complete controlled Phase 5 scholarly rendering and inventory.
3. [x] Pass Gate 5 and freeze the synthetic scholarly prototype.
4. [ ] Define governed cohort and infusion-anchor specification.
5. [ ] Define minimum source-field inventory and data-quality review dimensions.
6. [ ] Define local mapping/versioning protocol and public/private boundary.
7. [ ] Define source-concordance and adjudication plan.
8. [ ] Pass Gate 6 readiness review before any governed application.
9. [ ] Apply the frozen method to governed data if approvals/access permit.
10. [ ] Complete empirical validation, descriptive analysis, and final scholarly synthesis.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
