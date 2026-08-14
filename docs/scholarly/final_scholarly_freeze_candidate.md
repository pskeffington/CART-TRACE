# CART-TRACE Final Scholarly Freeze Candidate

## Decision

**FREEZE CANDIDATE — computational and scholarly reproducibility criteria satisfied; one non-semantic repository-metadata hold remains.**

## Audit anchor

- audited commit: `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679`
- GitHub Actions run: `31832440738`
- workflow: `Validate CART-TRACE`
- matrix: Python 3.11 and Python 3.12
- conclusion: success for both validation jobs

## Reproduction evidence

The clean current-head workflow completed the following in both supported Python environments:

1. checkout;
2. project/test dependency installation;
3. Gate 1 schema tests;
4. controlled Phase 5 JSON generation;
5. Phase 5 scholarly artifact rendering;
6. expected rendered-artifact verification;
7. full automated test suite.

All steps completed successfully.

## Frozen analytic-core review

The repository-wide scholarly consistency sweep found no semantic drift in:

- canonical care states;
- `acute_care_return` transition semantics;
- `[0,720)` primary analytic window;
- half-open interval behavior;
- source precedence/conflict handling;
- missing/unknown/unavailable/incomplete-follow-up handling;
- positive-return versus negative-follow-up semantics;
- six-case synthetic oracle;
- separation of synthetic computational validity from governed representation validity and empirical clinical findings.

No gate-impact change is required.

## Scholarly package review

The public package contains:

- aligned README, ROADMAP, THESIS, and requirements;
- controlled synthetic figures/tables and supplementary inventory;
- near-final manuscript scaffold;
- near-final capstone presentation narrative;
- governance/reproducibility language;
- governed-result insertion points that remain explicitly unpopulated absent approved execution;
- reproducibility and submission checklists;
- scholarly consistency sweep record.

No synthetic value is represented as an institutional empirical result.

## Governance boundary

Gate 6 remains **PASSED — methodological readiness / conditional on governed authorization**. This freeze candidate does not establish institutional authorization, governed access, representation validity on hospital data, or empirical clinical findings.

## Outstanding hold

The GitHub repository description still reflects an older, broader scope and mentions patient-generated data, toxicity, recovery, and response. The repository files themselves are aligned to the narrowed post-infusion hospital trajectory-reconstruction capstone, but final public freeze should not be declared until the repository description is updated or the metadata exception is explicitly accepted.

Suggested repository description:

> Synthetic-first research framework for reproducible reconstruction of 30-day post-CAR-T hospital level-of-care trajectories from longitudinal encounter and location data.

## Freeze rule

Until the metadata hold is resolved, this document is a freeze **candidate**, not the final scholarly freeze record. No analytic-core change is permitted without explicit gate-impact review. Presentation-only edits must preserve generated values, frozen semantics, and synthetic-versus-governed claim boundaries.
