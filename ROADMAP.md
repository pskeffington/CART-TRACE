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
- [x] Cohort and infusion-anchor specification documented
- [x] Source-field inventory documented
- [x] Local mapping/versioning protocol documented
- [x] Validation/adjudication plan documented
- [x] Public/private data boundary documented
- [x] Data-quality profile, reconstructability, follow-up, discrepancy-log, and pre-analysis operational review package finalized
- [x] Gate 6 methodological readiness passed with CI evidence
- [x] Template-only governed-execution work package completed
- [x] Aggregate governed-reporting templates completed
- [x] Scholarly integration templates completed
- [x] Near-final capstone manuscript scaffold completed
- [x] Near-final capstone presentation narrative completed
- [x] Reproducibility audit and submission checklists completed
- [x] Repository-wide scholarly consistency sweep completed
- [x] Clean reproducibility audit completed on `4b2e64a` / Actions `31832440738`
- [x] Final scholarly freeze candidate recorded
- [x] Repository description aligned to narrowed capstone scope
- [x] Public release manifest validated
- [x] Final public scholarly freeze declared
- [ ] Institutional authorization and governed data access confirmed, if pursued
- [ ] Governed hospital-data validation initiated, if feasible

**Current phase:** final public scholarly freeze / governed extension conditional  
**Current gate:** Gate 6 remains **PASSED — methodological readiness / conditional on governed authorization**. The public synthetic scholarly package is frozen. No public artifact establishes or substitutes for institutional approval, data-use authorization, governed data access, hospital-source representation validity, or empirical clinical findings.

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

Any change to frozen care states, interval semantics, source precedence, reconstruction behavior, metric definitions, follow-up rules, or the six-case oracle requires explicit gate-impact review and renewed validation.

---

## Phase 6 — Governance and data readiness

**Status: methodological readiness complete / external authorization conditional**

The public governance package includes cohort/index-event specification, source-field inventory, local mapping/versioning, validation/adjudication, public/private boundaries, data-quality and reconstructability controls, follow-up sufficiency rules, discrepancy logging, and pre-analysis review.

GitHub Actions run `31829204761` completed successfully for commit `2f63a3d35825e615598f3030b64253abffc86818`, validating the complete Gate 6 candidate package. The post-gate documentation head `28b0d12c6e8061f9ee58f57f62e3822f971eab01` was validated in run `31829807836`.

**Gate 6 -> governed application: PASSED FOR METHODOLOGICAL READINESS / GOVERNED AUTHORIZATION REQUIRED.**

### Governed execution templates

Completed template-only execution controls:

- `docs/governance/field_availability_matrix_template.md`;
- `docs/governance/local_mapping_review_sheet.md`;
- `docs/governance/validation_sample_protocol.md`;
- `docs/governance/aggregate_data_quality_summary_template.md`;
- `docs/governance/aggregate_reconstructability_summary_template.md`;
- `docs/governance/aggregate_followup_sufficiency_summary_template.md`;
- `docs/governance/aggregate_concordance_discrepancy_summary_template.md`;
- `docs/governance/governed_results_manuscript_placeholder.md`.

### External prerequisites before governed execution

The governed execution branch may begin only after the responsible institutional team documents inside the approved environment:

1. IRB/privacy/data-use authorization as applicable;
2. approved users and governed environment;
3. actual source-field availability;
4. reviewed/versioned local mapping;
5. prespecified validation sample and adjudication process;
6. permitted output/disclosure rules;
7. completed pre-analysis checklist;
8. confirmation that no frozen method rule changed implicitly.

---

## Scholarly integration package

**Status: final public scholarly freeze declared**

The public scholarly package includes the manuscript scaffold, presentation narrative, audit/submission controls, scholarly consistency sweep, final freeze candidate, public release manifest, and `docs/scholarly/final_public_scholarly_freeze.md`.

The clean reproducibility audit used commit `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679` and GitHub Actions run `31832440738`. Both Python 3.11 and 3.12 validation jobs completed schema tests, controlled JSON generation, scholarly rendering, rendered-artifact verification, and the full test suite successfully.

The verified pre-freeze release state `f06bd84cbc3bcd7a9a56b934a92d6b21ef8dd788` passed GitHub Actions run `31834081804`. The repository description is aligned to the narrowed capstone scope. The prior metadata hold is closed.

The audit found no frozen-semantic drift and no need for gate-impact review. Synthetic computational findings remain explicitly separate from governed representation validation and empirical clinical findings.

---

## 21-month capstone execution horizon

The schedule is organized around three linked claims: **computational validity**, **representation validity**, and **analytic utility**. Computational validity, scholarly prototype completeness, public methodological readiness, and the public scholarly freeze are established; governed empirical validation remains approval-dependent.

| Months | Primary objective | Completion products |
|---|---|---|
| 1–4 | Computational foundation | canonical model, synthetic oracle, reconstruction, metric contract, Gates 1–4 |
| 5–7 | Scholarly prototype freeze | generated synthetic tables/figures, reproducibility package, manuscript Methods/Results scaffold, Gate 5 |
| 6–10 | Governance and data readiness | cohort specification, source-field inventory, local mapping protocol, validation/adjudication plan, operational review templates, Gate 6 |
| 9–14 | Governed-data application, if feasible | source profiling, mapping coverage, reconstructability, uncertainty and follow-up characterization |
| 12–16 | Empirical validation, if feasible | source-concordance review, discrepancy analysis, mapping review, sensitivity analyses, metric availability |
| 15–18 | Primary descriptive analysis, if feasible | patient trajectories, utilization distributions, escalation/de-escalation, discharge and return summaries |
| 18–20 | Scholarly synthesis | manuscript and presentation, figures/tables, limitations, governance/reproducibility statement |
| 21 | Final freeze and capstone completion | clean reproducibility audit, metadata alignment, public scholarly freeze, final presentation/submission package |

### Work-session completion rule

Each focused work session should define one primary task and one concrete completion artifact. A session is complete when the task supports a named capstone milestone, the artifact is committed or otherwise controlled, frozen semantics are not changed implicitly, validation evidence is added when logic changes, CI is checked before milestone claims, traceability is preserved, synthetic and governed findings remain separated, and the next highest-value task is recorded.

### Scope guardrail

Core-aligned extensions include source mapping, data-quality and reconstructability assessment, source-concordance validation, uncertainty analysis, descriptive trajectory characterization, sensitivity analyses, and publication-quality communication. Prediction, eligibility/readiness logic, prospective decision support, operational forecasting, broad multi-institution platform development, and causal treatment-effect estimation remain outside the required capstone scope unless explicitly re-scoped.

---

## Evidence chain

Every major synthetic capstone result remains traceable through:

`capstone question -> requirement -> schema/function -> synthetic fixture -> automated test -> analytic output -> capstone table/figure`

For governed work, extend this chain with:

`approved source field -> local mapping rule -> canonical object -> concordance/adjudication evidence -> metric eligibility -> governed analytic result`

## Immediate build sequence

1. [x] Complete and freeze synthetic computational Gates 1–4.
2. [x] Complete controlled Phase 5 scholarly rendering and inventory.
3. [x] Pass Gate 5 and freeze the synthetic scholarly prototype.
4. [x] Define governed cohort and infusion-anchor specification.
5. [x] Define minimum source-field inventory and data-quality dimensions.
6. [x] Define local mapping/versioning protocol and public/private boundary.
7. [x] Define source-concordance and adjudication plan.
8. [x] Operationalize data-quality, reconstructability, follow-up, discrepancy logging, and pre-analysis review controls.
9. [x] Pass Gate 6 methodological readiness review.
10. [x] Prepare template-only governed execution controls.
11. [x] Prepare aggregate governed-reporting templates.
12. [x] Prepare scholarly integration templates.
13. [x] Build near-final capstone manuscript scaffold.
14. [x] Build near-final capstone presentation narrative.
15. [x] Build reproducibility audit and submission checklists.
16. [x] Complete repository-wide scholarly consistency sweep.
17. [x] Execute clean reproducibility audit and record final scholarly freeze candidate.
18. [x] Align GitHub repository description to narrowed capstone scope.
19. [x] Declare final public scholarly freeze.
20. [ ] Confirm external institutional authorization and governed data access, if pursued.
21. [ ] Apply the frozen method to governed data and complete empirical validation if approvals/access permit.

## Success criterion

CART-TRACE succeeds as an MS Health Data Science capstone if it demonstrates a transparent, auditable, and reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into patient-level care-state trajectories and transitions that support defensible descriptive characterization of post-infusion hospital utilization.
