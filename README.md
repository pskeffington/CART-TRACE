# CART-TRACE

**CART-TRACE** is a synthetic-first, non-operational research framework for reconstructing post-infusion hospital care trajectories following CAR T-cell therapy.

The current MS Health Data Science capstone asks:

> **Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?**

## Capstone focus

The primary unit of analysis is the **CAR T-cell therapy episode**, aligned to continuous treatment-relative time with `infusion timestamp = 0 hours`.

The core methodological pipeline is:

`source clinical records -> staging representation -> canonical trajectory -> validation/review -> analytic representation`

The project focuses on:

- deterministic reconstruction of care-state intervals and transitions;
- continuous treatment-relative timing;
- explicit `[start, end)` interval semantics;
- provenance-preserving source-to-canonical mapping;
- explicit `unknown`, missingness, and uncertainty behavior;
- post-infusion hospital utilization measures;
- synthetic truth-set validation and reproducibility;
- governed retrospective clinical-data application if approvals and data access are available.

## Current status

CART-TRACE has completed and frozen the canonical episode/state model, synthetic oracle, deterministic reconstruction layer, post-infusion utilization metric contract, and synthetic scholarly prototype through **Gate 5**.

GitHub Actions run `31828145837` completed successfully for the Gate 5 freeze candidate, providing current-head validation evidence for the complete synthetic scholarly artifact inventory.

The project is now in **Phase 6 preparation — governance and data readiness**. Current priorities are:

1. define the governed cohort and infusion-anchor specification;
2. define the minimum encounter/location/transfer/disposition/infusion source-field inventory;
3. establish local source-to-canonical mapping review and versioning rules;
4. define source-concordance, adjudication, reconstructability, uncertainty, and follow-up review procedures;
5. preserve a strict public/private boundary before any governed clinical-data application.

See [ROADMAP.md](ROADMAP.md) for phase gates and the 21-month capstone execution horizon, and [THESIS.md](THESIS.md) for the formal scholarly framing.

## Canonical care states

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` is represented as a transition type, not a care state.

## Temporal model

The primary capstone analytic window is:

`[0, 720)` hours relative to infusion.

Limited pre-infusion context may be retained only to establish encounter continuity and is excluded from primary post-infusion utilization totals unless a metric explicitly states otherwise. Continuous relative hours are canonical; day labels are presentation fields.

## Research guardrails

CART-TRACE is a **research methods project**, not a clinical decision-support system.

The public repository does not:

- contain PHI, production credentials, or identifying free text;
- determine CAR T-cell eligibility or treatment readiness;
- recommend product selection, transfer, escalation, discharge, or treatment;
- infer toxicity severity directly from care location;
- provide prospective alerts or bedside recommendations;
- treat synthetic validation as evidence of external clinical validity.

Any institutional clinical-data application must occur under appropriate governance and approvals, with local source mapping and validation kept separate from public synthetic artifacts.

## Scope boundary

The capstone is intentionally limited to retrospective, descriptive reconstruction and characterization of post-infusion hospital care. Candidate identification, eligibility adjudication, treatment-readiness gating, leukapheresis/bridging decisions, CMC/manufacturing analytics, patient-generated health data, prediction, and prospective decision support are outside the required capstone scope.

## Reproducibility principle

Every major synthetic result remains traceable through:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output -> capstone table/figure`

For future governed work, the analogous chain is:

`approved source field -> local mapping rule -> canonical object -> concordance/adjudication evidence -> metric eligibility -> governed analytic result`

The repository prioritizes transparent definitions, versioned transformations, explicit uncertainty, synthetic truth sets, automated tests, reproducible generated outputs, and separation of public synthetic artifacts from governed institutional data.
