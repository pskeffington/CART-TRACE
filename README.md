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

**Gate 6 is PASSED for methodological readiness, conditional on governed authorization.** GitHub Actions run `31829204761` validated the Gate 6 candidate package, and subsequent public scholarly/readiness milestones have remained CI-validated.

**The final public scholarly freeze is declared for the capstone package.** The clean reproducibility audit, scholarly consistency sweep, public release manifest, repository metadata alignment, and final freeze record are complete. The verified pre-freeze release state `f06bd84cbc3bcd7a9a56b934a92d6b21ef8dd788` passed GitHub Actions run `31834081804`.

The public capstone package therefore remains a frozen synthetic scholarly artifact. Any institutional clinical-data application remains separate and may proceed only if approvals and governed data access are independently confirmed.

See [ROADMAP.md](ROADMAP.md) for phase gates and the 21-month capstone execution horizon, [THESIS.md](THESIS.md) for the formal scholarly framing, and `docs/scholarly/final_public_scholarly_freeze.md` for the final freeze record.

## Research extension — administrative access gating

A separate synthetic research extension examines how referral, program review, facility, network, payer, Medicare, financial-clearance, and derived access states can be represented as auditable longitudinal administrative events.

This extension is **outside the required capstone scope** and does not modify the frozen post-infusion trajectory package. Its purpose is retrospective methods research: defining source-to-event mappings, deterministic reconstruction rules, provenance, uncertainty handling, and synthetic test cases for administrative access pathways.

The current extension includes:

- a bounded access-event model spanning gates `A0` through `A8`;
- synthetic source-to-event mapping rules;
- deterministic reconstruction of administrative access states and delays;
- explicit policy-version and policy-drift handling;
- synthetic oracle cases and validation controls;
- Gate 2B governed-source readiness, provenance, reporting, CLI, and review tooling;
- a frozen Gate 3 retrospective metric contract for delay, attrition, barrier classification, denominator semantics, missingness, and provenance.

**Current extension status:** Access Gate 1 and Gate 2A are passed. Gate 2B preparation/tooling is passed, while governed source validation remains not started and authorization-dependent. Gate 3A synthetic metric validity is now in progress; Gate 3B governed representation validity remains blocked behind authorization and completion of governed Gate 2B validation.

The access-gating extension does **not** determine whether a patient is clinically eligible for CAR T-cell therapy, whether an insurer must provide coverage, whether treatment is financially approved, or whether a patient is ready for treatment. It is not an authorization engine, utilization-management system, eligibility tool, or clinical decision-support system.

Any future use of institutional, payer, or patient-level administrative data requires separate governance, source authorization, local validation, and domain review.

See `docs/access_gating/dartmouth_health_access_gating_framework.md` for the extension framework and `docs/access_gating/access_gate_3_metric_contract.md` for the current synthetic metric-validity gate.

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
- adjudicate insurance coverage or financial clearance;
- recommend product selection, transfer, escalation, discharge, or treatment;
- infer toxicity severity directly from care location;
- provide prospective alerts or bedside recommendations;
- treat synthetic validation as evidence of external clinical validity.

Any institutional clinical-data application must occur under appropriate governance and approvals, with local source mapping and validation kept separate from public synthetic artifacts.

## Scope boundary

The capstone is intentionally limited to retrospective, descriptive reconstruction and characterization of post-infusion hospital care. Candidate identification, eligibility adjudication, treatment-readiness gating, leukapheresis/bridging decisions, CMC/manufacturing analytics, patient-generated health data, prediction, and prospective decision support are outside the required capstone scope.

The administrative access-gating work is maintained as a separate research extension and should not be interpreted as broadening the capstone endpoint or as evidence of operational eligibility or payer decision-making capability.

## Reproducibility principle

Every major synthetic capstone result remains traceable through:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output -> capstone table/figure`

For future governed work, the analogous chain is:

`approved source field -> local mapping rule -> canonical object -> concordance/adjudication evidence -> metric eligibility -> governed analytic result`

The administrative access extension follows the same principle at a separate research boundary:

`synthetic source-like record -> mapping rule -> access event -> deterministic reconstruction -> validation -> bounded research summary`

The repository prioritizes transparent definitions, versioned transformations, explicit uncertainty, synthetic truth sets, automated tests, reproducible generated outputs, and separation of public synthetic artifacts from governed institutional data.
