# CART-TRACE Final Public Scholarly Freeze

## Decision

**FINAL PUBLIC SCHOLARLY FREEZE — DECLARED.**

The public synthetic CART-TRACE research repository has satisfied its computational reproducibility, scholarly consistency, governance-separation, and repository-metadata criteria for final public scholarly freeze.

## Final verified pre-freeze state

- release-state commit: `f06bd84cbc3bcd7a9a56b934a92d6b21ef8dd788`
- GitHub Actions run: `31834081804`
- workflow: `Validate CART-TRACE`
- conclusion: `success`
- repository description verified as:

> Synthetic-first research framework for reproducible reconstruction of 30-day post-CAR-T hospital level-of-care trajectories from longitudinal encounter and location data.

The prior metadata hold is resolved.

## Clean reproducibility evidence

Primary clean audit:

- commit: `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679`
- GitHub Actions run: `31832440738`
- Python 3.11 and Python 3.12 validation jobs: success

Validated workflow steps included:

1. schema tests;
2. controlled Phase 5 JSON generation;
3. scholarly artifact rendering;
4. expected rendered-artifact verification;
5. full automated test suite.

Subsequent release-candidate and release-manifest heads also remained green, including Actions `31832888988`, `31833669828`, `31833799689`, and `31834081804`.

## Frozen analytic contract

The final public freeze preserves:

- unit of analysis: CAR T-cell therapy episode;
- administered infusion timestamp = 0 hours;
- primary analytic window `[0,720)` hours;
- canonical states `outpatient`, `emergency`, `routine_inpatient`, `intermediate_care`, `intensive_care`, `discharged`, and `unknown`;
- `acute_care_return` as a transition type, not a state;
- deterministic interval reconstruction and conflict handling;
- explicit uncertainty and missingness behavior;
- prohibition on treating unavailable, not calculable, incomplete-follow-up, missing, or `unknown` results as zero;
- frozen positive-return versus negative-follow-up semantics;
- the six-case synthetic oracle and associated boundary/error tests.

Any future change to these semantics requires explicit gate-impact review and renewed validation.

## Scholarly claim boundary

This freeze supports claims about:

- deterministic post-infusion hospital trajectory reconstruction;
- computational validity against controlled synthetic truth;
- reproducibility of generated synthetic scholarly outputs;
- methodological readiness for governed retrospective validation.

It does not establish:

- institutional authorization or governed data access;
- hospital-source representation validity;
- external clinical validity;
- toxicity severity from level of care;
- eligibility/readiness determination;
- prospective clinical decision support;
- causal treatment effects.

## Gate status

- Gates 1–5: **PASSED / frozen**.
- Gate 6: **PASSED — methodological readiness / conditional on governed authorization**.

Final public scholarly freeze does not alter Gate 6 or substitute for institutional approval.

## Public scholarly package

The frozen public package includes the controlled main and supplementary figures/tables, near-final manuscript scaffold, capstone presentation narrative, governance/reproducibility controls, final reproducibility audit materials, submission checklist, scholarly consistency sweep, freeze-candidate record, and public release manifest.

## Post-freeze rule

Further public work should be limited to:

1. presentation/editorial corrections that preserve frozen semantics and generated values;
2. immutable release/tag creation when desired;
3. citation/reference completion and submission-format adjustments;
4. separately governed empirical extension only after institutional authorization and approved data access.

No governed patient-level data, identifiers, local sensitive mappings, or unreviewed institutional results belong in the public repository.
