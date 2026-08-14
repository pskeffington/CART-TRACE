# CART-TRACE Near-Final Capstone Presentation Narrative

## Status

Near-final public presentation narrative. It is built entirely from frozen synthetic evidence and methodological-readiness artifacts. Governed empirical findings may be inserted only after authorization, execution, and disclosure review.

## Slide 1 — Title and problem

**CART-TRACE: Reconstructing Hospital Care Trajectories Following CAR T-Cell Therapy from Longitudinal Clinical Data**

Opening message: the core problem is not counting encounters; it is reconstructing a coherent, treatment-relative sequence from fragmented hospital records while preserving uncertainty and provenance.

## Slide 2 — Capstone question

Primary question:

> Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?

State the narrow scope: retrospective descriptive reconstruction, not eligibility, toxicity prediction, prospective decision support, or causal inference.

## Slide 3 — Why the representation matters

Show the conceptual contrast between fragmented source records and a patient-level trajectory. Emphasize sequence, duration, transitions, missingness, and provenance.

Recommended artifact: Figure 1, clinical data structuring architecture.

## Slide 4 — Canonical model

Explain the therapy episode, infusion anchor, `[0,720)` analytic window, half-open intervals, seven frozen care states, and `acute_care_return` as a transition rather than a state.

Recommended artifact: Table 1, canonical model.

## Slide 5 — Synthetic-first validation strategy

Explain why the method was frozen against a controlled oracle before any governed application. Present the six synthetic trajectory classes and boundary/error cases.

Recommended artifact: Table 2 and Supplementary Table S3.

## Slide 6 — Deterministic reconstruction

Describe source normalization, versioned mapping, stable ordering, precedence, duplicate collapse, overlap handling, and explicit `unknown` behavior.

Key message: irreconcilable evidence is surfaced, not clinically inferred away.

## Slide 7 — Metric contract

Summarize frozen utilization outputs: state durations, transition counts/timing, time to first escalation, time to discharge, 7-day and 30-day acute-care return, and uncertainty burden.

Explain that unavailable, incomplete-follow-up, and observed-zero are analytically distinct.

## Slide 8 — Synthetic validation results

Show that the implementation reproduces the prespecified synthetic oracle and controlled metric expectations under automated testing.

Recommended artifact: Table 3 and Supplementary Table S1.

Avoid implying external clinical validity.

## Slide 9 — Representative trajectories

Use Figure 2 to illustrate routine recovery, escalation, ICU-level care, return, and uncertainty patterns. Reinforce that these are synthetic examples.

## Slide 10 — Cohort-level synthetic reporting

Use Figure 3, Table 4, and Table 5 to demonstrate generated utilization summaries, metric availability, and uncertainty reporting.

Key message: the scholarly outputs are generated from controlled sources rather than manually maintained.

## Slide 11 — Governance and Gate 6

Explain that Gate 6 certifies methodological readiness, not institutional authorization. Summarize cohort/anchor specification, source inventory, local mapping review, reconstructability, follow-up sufficiency, validation/adjudication, discrepancy logging, and public/private boundaries.

## Slide 12 — Governed validation design

Present the planned sequence if approved data become available:

`approved source fields -> local mapping -> canonical trajectory -> source concordance/adjudication -> metric eligibility -> approved aggregate result`

State explicitly that this branch begins only after institutional authorization and data access.

## Slide 13 — Empirical results insertion point

If governed execution has occurred, insert only disclosure-approved aggregate findings for source availability, reconstructability, concordance, follow-up sufficiency, and descriptive utilization.

If governed execution has not occurred, show the prespecified validation design and state that no institutional empirical results are available.

## Slide 14 — Limitations

Cover synthetic-versus-external validity, source completeness, mapping transportability, reconstructability selection, follow-up requirements, unknown-state burden, and the limitation that level of care is not a direct toxicity or physiologic-severity measure.

## Slide 15 — Contribution

Frame the primary contribution as a deterministic clinical-data structuring, temporal reconstruction, validation, and governance framework for longitudinal hospital data.

The applied CAR T setting demonstrates the method; the project is not a bedside decision-support system.

## Slide 16 — Reproducibility

Show the audit chain:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output -> capstone table/figure`

Mention automated tests, generated artifacts, versioned mapping, frozen gates, and explicit gate-impact review.

## Slide 17 — Conclusion

Closing statement: CART-TRACE demonstrates that post-infusion hospital records can be transformed into a transparent, auditable, treatment-relative trajectory representation under a prespecified synthetic validation framework. Governed empirical validation is a separate, approval-dependent extension.

## Q&A anchors

Be prepared to answer:

- Why therapy episode rather than patient or admission?
- Why `[0,720)`?
- Why include `unknown` as a state?
- How are conflicting source records handled?
- How are zero, missing, unavailable, and incomplete follow-up distinguished?
- Why does synthetic validation matter?
- What does Gate 6 actually certify?
- What would change if local source semantics do not fit the frozen model?
- What claims cannot be made without governed validation?
