# CART-TRACE Final Reproducibility Audit

## Purpose

Completed pre-submission audit for the frozen public synthetic research repository. This record evaluates reproducibility, scholarly consistency, and separation between public artifacts and any future approved institutional work.

## Repository checks

- [x] `main` is the intended public scholarly branch.
- [x] Finalized manuscript head `56307ff845621b8c113d2bd36475e8950ab0ebae` passed GitHub Actions run `31849398353`.
- [x] Submission-checklist head `e691680c18581a5a97dbd2fcf9fbcf5e5d9e9622` passed GitHub Actions run `31853659240`.
- [x] README, ROADMAP, THESIS, gate documents, manuscript, presentation, and freeze records agree on scope and status.
- [x] Public repository metadata matches the narrowed post-infusion trajectory-reconstruction scope.
- [x] Public files contain disclosure-safe synthetic or generic methodological material only.

## Frozen analytic core

- [x] Canonical care states remain unchanged.
- [x] `acute_care_return` remains a transition type.
- [x] Primary analytic window remains `[0,720)` hours relative to infusion.
- [x] Half-open interval semantics remain unchanged.
- [x] Reconstruction precedence and conflict behavior remain unchanged.
- [x] Missing, `unknown`, unavailable, not calculable, and incomplete-follow-up results are not treated as zero.
- [x] Positive-return and negative-follow-up semantics remain unchanged.
- [x] Synthetic oracle fixtures and expected outputs remain frozen.

## Reproduction

Run from repository root:

```text
python scripts/generate_phase5_outputs.py
python scripts/render_phase5_outputs.py
pytest -q
```

Verified by the clean reproducibility audit on commit `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679`, GitHub Actions run `31832440738`, in both Python 3.11 and 3.12:

- [x] generation completed successfully;
- [x] rendering completed successfully;
- [x] automated tests passed;
- [x] repeated rendering was deterministic;
- [x] controlled outputs matched repository expectations;
- [x] generated numeric results were not contradicted by manually maintained values.

## Scholarly artifact inventory

Main text:

- [x] Figure 1 — data structuring architecture
- [x] Figure 2 — representative trajectories
- [x] Figure 3 — utilization and metric availability
- [x] Table 1 — canonical model
- [x] Table 2 — synthetic truth set
- [x] Table 3 — validation
- [x] Table 4 — cohort utilization
- [x] Table 5 — uncertainty

Supplement:

- [x] Figure S1 — all trajectories
- [x] Table S1 — metric-result matrix
- [x] Table S2 — mapping rules
- [x] Table S3 — boundary and negative-test inventory
- [x] Table S4 — reproducibility artifacts

## Manuscript consistency

- [x] Abstract does not imply institutional empirical validation.
- [x] Methods match the frozen implementation and governance controls.
- [x] Synthetic results are explicitly identified as synthetic.
- [x] The public manuscript explicitly states that no institutional empirical findings are included.
- [x] Discussion distinguishes computational validity, representation fidelity, descriptive empirical findings, and external clinical validity.
- [x] Limitations cover source completeness, mapping transportability, reconstructability selection, follow-up sufficiency, unknown burden, and level-of-care interpretation.
- [x] No eligibility, readiness, treatment-selection, toxicity-severity, prospective-decision, or causal claims are introduced.

## Governance consistency

- [x] Gate 6 is described as methodological readiness conditional on authorization.
- [x] Public and local mapping artifacts remain separate.
- [x] Governed templates remain generic in the public repository.
- [x] No institutional aggregate findings are included in the frozen public package.
- [x] Any semantic change discovered during future local application must enter gate-impact review rather than hidden preprocessing.

## Final freeze record

- final public scholarly freeze: declared
- controlling freeze record: `docs/scholarly/final_public_scholarly_freeze.md`
- final-freeze roadmap head: `a7b8325855b8dbcfe6adadf5f7e72b2041daeb48`
- final-freeze GitHub Actions run: `31848508218` — success
- clean reproducibility anchor: `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679` / Actions `31832440738`
- finalized public manuscript head: `56307ff845621b8c113d2bd36475e8950ab0ebae` / Actions `31849398353`
- finalized submission-checklist head: `e691680c18581a5a97dbd2fcf9fbcf5e5d9e9622` / Actions `31853659240`
- governed-data status: not established by the public repository; future execution remains authorization-dependent
- approved aggregate institutional findings included: no
- GitHub tag/Release: not created; optional pending an explicit version identifier

## Audit decision

**PASS — final public scholarly package is reproducible, internally consistent, scope-aligned, and appropriately separated from any future governed institutional execution.**

This audit does not establish institutional approval, governed data access, hospital-source representation validity, or external clinical validity.
