# CART-TRACE Capstone Submission Checklist

## Purpose

Final submission inventory for the capstone package. This checklist separates public synthetic deliverables from any approval-dependent institutional additions. Checked items below are supported by the current repository record; unchecked items require an explicit final editorial, institutional, or versioning decision.

## Core scholarly files

- [x] `THESIS.md` aligned to final scope.
- [x] `ROADMAP.md` aligned to final milestone state.
- [ ] `docs/scholarly/capstone_manuscript_scaffold.md` tightened to final submission wording.
- [x] `docs/scholarly/capstone_presentation_narrative.md` reviewed against the controlled figure/table order.
- [x] governance/reproducibility statement included in the scholarly package.
- [x] limitations section reflects the current authorization/validation boundary.

## Figures and tables

- [x] Main Figures 1–3 present and synthetic labeling controlled where applicable.
- [x] Main Tables 1–5 present.
- [x] Supplementary Figure S1 present.
- [x] Supplementary Tables S1–S4 present.
- [x] Generated numeric values are traceable to controlled sources through the Phase 5 rendering manifest.
- [x] Public scholarly framing does not imply institutional empirical findings when only synthetic data are shown.

## Presentation

- [x] Capstone question appears early and matches the frozen scope.
- [x] Data-structuring architecture precedes results.
- [x] Synthetic validation strategy precedes synthetic results.
- [x] Gate 6 is presented as methodological readiness, not authorization.
- [x] Governed empirical results remain an approval-dependent insertion point rather than simulated findings.
- [x] Limitations and contribution are distinct presentation sections.
- [ ] Final presentation conclusion reconciled line-by-line against the final submitted manuscript version.

## Reproducibility

- [x] Clean reproducibility audit completed and recorded.
- [ ] Current-head CI green for the latest post-freeze housekeeping commit.
- [x] Generation/rendering commands succeeded in the clean CI audit.
- [x] Automated test suite passed in the clean CI audit.
- [x] Final-freeze commit SHA and Actions run ID recorded.
- [x] Repository release/tag decision recorded: no tag or GitHub Release currently exists; immutable release creation remains optional pending an explicit version identifier.

## Scope and claims

- [x] Project is described as retrospective and descriptive.
- [x] No claim of eligibility determination, treatment readiness, product selection, prospective decision support, toxicity prediction, or causal treatment effect is made.
- [x] Level-of-care trajectory is not described as a direct toxicity or physiologic-severity measure.
- [x] Synthetic validation is not presented as external clinical validity.
- [x] Institutional findings are clearly separated from synthetic results and are not claimed absent governed execution.

## Governed-data branch

If institutional execution occurred:

- [ ] authorization and approved environment documented outside the public repository;
- [ ] local mapping version recorded;
- [ ] data-quality and reconstructability summaries completed;
- [ ] validation/adjudication completed as prespecified;
- [ ] only approved aggregate findings inserted into public scholarly artifacts.

If institutional execution did not occur before submission:

- [ ] final submitted manuscript explicitly states that empirical institutional validation was not performed;
- [x] governed sections remain planned-validation descriptions rather than simulated results;
- [x] public conclusion remains limited to computational validity and methodological readiness.

## Final package

- [ ] final manuscript/report
- [x] presentation narrative
- [x] public repository
- [x] controlled figure/table bundle
- [x] supplementary materials
- [x] reproducibility statement
- [x] governance statement
- [x] final public scholarly freeze record

## Remaining submission decisions

1. Convert the manuscript scaffold into the final submitted manuscript/report wording.
2. Reconcile the final presentation conclusion against that submitted manuscript.
3. Decide whether governed institutional execution will occur before submission; if not, make the non-execution statement explicit in the final manuscript.
4. Choose an immutable release/tag identifier only if a formal GitHub release is desired.
5. Reconfirm current-head CI after the final editorial/release-record commit.

## Completion criterion

The submission package is complete when all public claims are supported by controlled repository evidence, the final manuscript and presentation agree on scope and status, synthetic results remain reproducible, and any governed-data additions have been reviewed for release.
