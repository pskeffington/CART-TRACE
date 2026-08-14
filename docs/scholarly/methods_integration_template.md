# CART-TRACE Scholarly Integration — Methods Template

## Status

Template only. This document integrates the frozen public method with the planned governed validation workflow. It does not assert that institutional authorization or governed-data execution has occurred.

## Study design

Describe CART-TRACE as a retrospective, descriptive health-data-science framework for transforming longitudinal hospital encounter and location records surrounding CAR T-cell infusion into reproducible 30-day level-of-care trajectories.

## Unit and anchor

- Primary unit: CAR T-cell therapy episode.
- Treatment-relative anchor: documented administered infusion timestamp = 0 hours.
- Primary window: `[0,720)` hours after infusion.
- Repeated qualifying infusions are distinct therapy episodes.

## Canonical representation

Describe the seven frozen care states: `outpatient`, `emergency`, `routine_inpatient`, `intermediate_care`, `intensive_care`, `discharged`, and `unknown`. State that `acute_care_return` is a transition type rather than a state.

## Data structuring

Document the audit chain:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output`

For governed work, extend with source-field inventory, versioned local mapping, source provenance, reconstructability review, and discrepancy/adjudication controls.

## Reconstruction and metrics

State that interval semantics, source precedence, unknown/conflict handling, deterministic reconstruction, utilization metrics, follow-up rules, and the synthetic oracle were frozen before governed application. Missing or unavailable information is not silently treated as zero.

## Synthetic validation

Summarize the six-case synthetic truth set, deterministic tests, boundary/negative tests, and Gate 1–5 validation. Explicitly state that synthetic validation establishes computational validity, not external clinical validity.

## Governed representation validation

If authorized, describe:

1. source-field availability assessment;
2. reviewed/versioned local source-to-canonical mapping;
3. cohort reconstructability classification;
4. metric-specific follow-up sufficiency;
5. prespecified validation sample;
6. source-concordance review and discrepancy adjudication;
7. approved aggregate reporting.

## Governance

State that PHI, institution-specific identifiers, restricted source mappings, raw extracts, and patient-level adjudication evidence remain in the governed environment. Only approved non-identifying aggregate outputs may enter scholarly/public artifacts.

## Scope limitations

The method does not determine CAR T eligibility/readiness, infer toxicity severity from care location, recommend treatment or disposition, generate prospective alerts, or estimate causal treatment effects.
