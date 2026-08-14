# CART-TRACE Final Reproducibility Audit Checklist

## Purpose

Pre-submission audit for the public synthetic research repository. This checklist evaluates reproducibility, scholarly consistency, and separation between public artifacts and any future approved institutional work.

## Repository checks

- [ ] `main` is the intended release branch.
- [ ] Current-head GitHub Actions is green.
- [ ] README, ROADMAP, THESIS, gate documents, and manuscript scaffold agree on scope and status.
- [ ] Public repository metadata matches the narrowed post-infusion trajectory-reconstruction scope.
- [ ] Public files contain only disclosure-safe synthetic or generic methodological material.

## Frozen analytic core

- [ ] Canonical care states remain unchanged.
- [ ] `acute_care_return` remains a transition type.
- [ ] Primary analytic window remains `[0,720)` hours relative to infusion.
- [ ] Half-open interval semantics remain unchanged.
- [ ] Reconstruction precedence and conflict behavior remain unchanged.
- [ ] Missing, `unknown`, unavailable, not calculable, and incomplete-follow-up results are not treated as zero.
- [ ] Positive-return and negative-follow-up semantics remain unchanged.
- [ ] Synthetic oracle fixtures and expected outputs remain frozen unless a documented gate-impact review exists.

## Reproduction

Run:

```text
python scripts/generate_phase5_outputs.py
python scripts/render_phase5_outputs.py
pytest -q
```

Verify:

- [ ] generation completes successfully;
- [ ] rendering completes successfully;
- [ ] automated tests pass;
- [ ] repeated rendering is deterministic;
- [ ] controlled outputs match repository expectations;
- [ ] generated numeric results are not contradicted by manually maintained values.

## Scholarly artifact inventory

Main text:

- [ ] Figure 1 — data structuring architecture
- [ ] Figure 2 — representative trajectories
- [ ] Figure 3 — utilization and metric availability
- [ ] Table 1 — canonical model
- [ ] Table 2 — synthetic truth set
- [ ] Table 3 — validation
- [ ] Table 4 — cohort utilization
- [ ] Table 5 — uncertainty

Supplement:

- [ ] Figure S1 — all trajectories
- [ ] Table S1 — metric-result matrix
- [ ] Table S2 — mapping rules
- [ ] Table S3 — boundary and negative-test inventory
- [ ] Table S4 — reproducibility artifacts

## Manuscript consistency

- [ ] Abstract does not imply institutional empirical validation unless it occurred.
- [ ] Methods match the frozen implementation and governance controls.
- [ ] Synthetic Results are explicitly labeled synthetic.
- [ ] Governed-result insertion points are either populated with approved aggregate findings or explicitly left unpopulated.
- [ ] Discussion distinguishes computational validity, representation fidelity, descriptive empirical findings, and external clinical validity.
- [ ] Limitations cover source completeness, mapping transportability, reconstructability selection, follow-up sufficiency, unknown burden, and level-of-care interpretation.
- [ ] No eligibility, readiness, treatment-selection, toxicity-severity, prospective-decision, or causal claims are introduced.

## Governance consistency

- [ ] Gate 6 is described as methodological readiness conditional on authorization.
- [ ] Public and local mapping artifacts remain separate.
- [ ] Governed templates remain generic in the public repository.
- [ ] Any institutional aggregate result is included publicly only after appropriate review.
- [ ] Any semantic change discovered during local application enters gate-impact review rather than being hidden in preprocessing.

## Final freeze record

- release commit SHA: `[insert]`
- GitHub Actions run ID: `[insert]`
- test result: `[insert]`
- generation/rendering result: `[insert]`
- manuscript version/date: `[insert]`
- presentation version/date: `[insert]`
- governed-data status: `[authorized/executed/not available]`
- approved aggregate institutional findings included: `[yes/no/not applicable]`

## Pass criterion

The audit passes when the public repository reproduces its controlled synthetic scholarly outputs from documented code and fixtures, frozen semantics remain intact, scholarly claims match available evidence, and the public/governed boundary is preserved.
