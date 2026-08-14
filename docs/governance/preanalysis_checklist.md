# CART-TRACE Governed Pre-analysis Checklist

## Purpose

This checklist is the final readiness review before applying the frozen CART-TRACE method to an approved governed dataset. Completion does not substitute for institutional approvals or data access authorization.

## Governance and approvals

- [ ] required institutional approvals are documented in the governed environment;
- [ ] approved data-use scope covers the retrospective CART-TRACE research question;
- [ ] approved users and environments are identified;
- [ ] public/private artifact boundaries are understood;
- [ ] no PHI, credentials, local identifiers, or restricted mappings will be committed publicly.

## Cohort and anchor

- [ ] therapy-episode cohort definition is finalized;
- [ ] administered CAR T-cell infusion timestamp is the sole index anchor;
- [ ] repeat-infusion handling is defined;
- [ ] cohort inclusion/exclusion accounting is reproducible;
- [ ] no eligibility or treatment-readiness logic has been introduced.

## Source-field readiness

- [ ] required source domains are identified;
- [ ] required fields have availability statuses;
- [ ] timestamp precision and timezone behavior are documented;
- [ ] stable source-record identifiers are available for provenance;
- [ ] observation-horizon evidence is available for return measures;
- [ ] known missingness, duplication, overlap, and conflict behavior is documented.

## Local mapping readiness

- [ ] local source labels are inventoried;
- [ ] mapping statuses are assigned;
- [ ] mapping reviewers are identified;
- [ ] mapping version is fixed for the analysis run;
- [ ] precedence reflects source authority rather than assumed clinical severity;
- [ ] unmapped or irreconcilable evidence remains explicit rather than forced into a canonical state.

## Validation and adjudication readiness

- [ ] source-concordance review plan is approved;
- [ ] adjudication sample strategy is defined;
- [ ] discrepancy log is operational;
- [ ] reconstructability categories and reason codes are operational;
- [ ] provenance is retained for reviewed intervals/transitions;
- [ ] reviewer roles and resolution procedures are documented.

## Metric and follow-up readiness

- [ ] frozen `[0,720)` primary analytic window is preserved;
- [ ] metric definitions remain unchanged from Gate 4;
- [ ] metric statuses preserve zero versus unavailable information;
- [ ] 7-day and 30-day follow-up sufficiency rules are operational;
- [ ] metric-specific denominators will be reported;
- [ ] unknown-state and uncertainty burden will remain visible.

## Frozen-method integrity

Confirm that local preprocessing does **not** introduce:

- [ ] new canonical care states;
- [ ] new transition semantics;
- [ ] changed `[start,end)` interval behavior;
- [ ] changed precedence/conflict policy;
- [ ] changed utilization metric definitions;
- [ ] changed follow-up interpretation;
- [ ] changed synthetic oracle expectations.

Any required change to these items must be routed through explicit gate-impact review before analysis.

## Readiness decision

Record one of:

- `ready_for_governed_application`;
- `ready_with_documented_limitations`;
- `not_ready`.

The decision must cite unresolved limitations and responsible reviewers.

## Completion criterion

The checklist is complete when governance, cohort, source-field, mapping, validation, reconstructability, follow-up, privacy, and frozen-method integrity controls have all been reviewed and the readiness decision is documented within the governed environment.
