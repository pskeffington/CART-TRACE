# CART-TRACE Governed Validation-Sample Protocol

## Purpose

This protocol defines how to select and review a governed sample for source-concordance and reconstruction validation after institutional approvals and data access are in place. It is a methodological template only; it does not specify or expose patient identities, local record identifiers, or protected health information.

## Validation objectives

The governed validation sample should assess whether local source records can support the frozen CART-TRACE representation by evaluating:

1. infusion-anchor correctness;
2. encounter and location-history completeness;
3. local source-to-canonical mapping concordance;
4. temporal ordering and interval boundary fidelity;
5. conflict and `unknown` handling;
6. transition reconstruction;
7. discharge and acute-care-return identification;
8. metric-status correctness, including incomplete follow-up;
9. source-to-derived provenance completeness.

## Sampling principles

Sampling should be prespecified inside the approved environment and should intentionally include episodes likely to exercise important methodological boundaries. At minimum, consider strata for:

- uncomplicated routine inpatient trajectories;
- intermediate-care escalation/de-escalation;
- intensive-care escalation/de-escalation;
- discharge followed by emergency or inpatient return;
- episodes with unmapped or disputed local source labels;
- episodes with overlapping or conflicting source evidence;
- episodes with open-ended or incomplete records;
- episodes with incomplete 7-day or 30-day follow-up;
- repeat-infusion or otherwise complex episode-linkage cases when present.

The sample is for representation validation, not clinical outcome prediction or treatment-effect estimation.

## Review unit

The primary review unit is the therapy episode. Reviewers compare approved source evidence with the derived canonical trajectory and metric results while preserving the source-to-derived audit chain.

## Review form

For each sampled episode, document inside the governed environment:

- governed episode identifier;
- infusion-anchor concordance;
- source coverage reviewed;
- mapping version;
- interval/state concordance;
- transition concordance;
- discharge/return concordance;
- unknown/uncertainty appropriateness;
- metric-result concordance and status;
- discrepancy IDs, if any;
- adjudication status;
- reviewer(s) and review date.

## Concordance categories

Use controlled categories:

- `concordant`
- `minor_discrepancy_no_analytic_impact`
- `material_local_mapping_discrepancy`
- `material_source_data_limitation`
- `possible_implementation_defect`
- `possible_frozen_method_issue`
- `not_evaluable`

Any `possible_frozen_method_issue` must stop local adaptation and enter explicit gate-impact review.

## Adjudication

Disagreements should follow `docs/governance/validation_adjudication_plan.md` and be recorded using the discrepancy-log specification. Resolution must distinguish source correction, local mapping correction, source limitation, implementation defect, and true method-level issue.

## Reporting

Governed validation reporting should include, where permitted:

- sample size and sampling strata;
- proportion concordant;
- discrepancy counts by controlled category;
- mapping revisions arising from review;
- reconstructability distribution;
- follow-up sufficiency distribution;
- unresolved limitations;
- confirmation that frozen analytic semantics were or were not changed.

Only approved non-identifying aggregate results may leave the governed environment.

## Completion criterion

The validation-sample review is complete when prespecified strata have been reviewed, discrepancies are adjudicated or explicitly unresolved, mapping revisions are versioned, provenance is retained, and any potential frozen-method issue has been escalated rather than absorbed into local preprocessing.
