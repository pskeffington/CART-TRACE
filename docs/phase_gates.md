# CART-TRACE Phase Gates

This document defines the evidence required to advance from one capstone-development phase to the next. A phase is complete only when its exit evidence is reviewable, reproducible, and sufficient to protect downstream validity.

## Gate policy

A gate may be:

- **PASS** — all mandatory evidence exists and downstream work can rely on it;
- **CONDITIONAL PASS** — a limited residual item remains that does not threaten downstream validity and has an explicit closure plan;
- **FAIL / HOLD** — unresolved ambiguity or missing evidence would contaminate downstream implementation or analysis.

A conditional pass is not permitted when the unresolved item changes canonical semantics, time alignment, interval definitions, provenance behavior, or metric formulas used downstream.

## Gate 0 -> 1: Scope locked

Required evidence includes the capstone question, explicit included/excluded domains, synthetic-first public-development policy, no-PHI and non-operational guardrails, success criterion, initial data domains, requirements register, and minimum-necessary data principle.

Decision rule: all required scope artifacts exist and no mandatory capstone requirement depends on excluded domains or prospective clinical decision support.

Frozen after passage unless formally changed: capstone question, core aims, scope exclusions, and non-operational boundary.

## Gate 1 -> 2: Canonical model stable enough for fixtures

Required evidence:

- controlled care-state vocabulary exactly containing `outpatient`, `emergency`, `routine_inpatient`, `intermediate_care`, `intensive_care`, `discharged`, and `unknown`;
- controlled transition-type vocabulary containing `admission`, `transfer`, `escalation`, `deescalation`, `discharge`, `acute_care_return`, `other`, and `unknown`;
- `acute_care_return` represented only as a transition type, never a state;
- therapy-episode schema with infusion anchor, explicit timestamp window bounds, relative-hour bounds, optional research patient identifier, and provenance/source context;
- care-state interval schema with `interval_id`, `[start,end)` semantics, hour-relative timing, source-record arrays, mapping method, uncertainty, and open-end semantics;
- care-transition schema with `transition_id`, hour-relative timing, transition type, source-record arrays, and provenance;
- minimal encounter input specification;
- provenance specification;
- deterministic treatment-relative time convention using continuous hours;
- same-timestamp and overlap/conflict rules;
- one hand-worked multi-encounter episode represented under the canonical schemas;
- automated tests asserting exact vocabulary and rejecting legacy canonical labels;
- successful CI execution of Gate 1 tests and the full synthetic test suite.

Quality checks:

- local unit names are not embedded as canonical states;
- source ICU labels map to `intensive_care`;
- source stepdown/higher-observation labels map to `intermediate_care`;
- emergency encounters map to `emergency`;
- every derived object can carry source provenance;
- unknown/conflicting states are representable;
- timestamps and interval boundaries are unambiguous;
- multiple encounters can coexist in one episode without undocumented semantics.

Decision rule: every Phase 2 fixture can be authored and validated without inventing fields, using legacy state labels, or changing canonical semantics.

Frozen after passage unless versioned: core care-state vocabulary, transition-type vocabulary, interval semantics, treatment-relative hour convention, required canonical identifiers, provenance contract, and acute-care-return semantics.

Regression rule: a post-gate change to these artifacts requires affected fixtures/tests to be regenerated and Gate 1 impact to be reviewed.

## Gate 2 -> 3: Synthetic cohort is testable

Required evidence:

- six required synthetic trajectory classes;
- expected canonical state intervals for each fixture;
- expected transition sequence and transition types for each fixture;
- expected utilization measures for each fixture;
- documented edge cases;
- fixture manifest identifying requirement coverage;
- source-like event representation for every fixture;
- versioned truth-set outputs;
- all fixtures and negative/error cases validating against the frozen Gate 1 contract;
- successful CI execution of the complete Phase 2 oracle tests.

Minimum edge-case coverage includes identical timestamps, adjacent intervals, overlaps, duplicate events, missing end time, study-window boundary behavior, discharge and acute-care return, conflicting location sources, and unknown intervals between known states.

Decision rule: fixtures provide a sufficiently complete oracle that reconstruction code can be judged correct or incorrect without subjective interpretation.

Frozen after passage: fixture intent, expected intervals/transitions, expected uncertainty behavior, and expected metric values subject to explicit metric-version changes.

## Gate 3 -> 4: Reconstruction is trustworthy

Required evidence includes infusion anchoring, continuous-hour time utility, deterministic sorting, source-to-canonical mapping, overlap/conflict resolution, interval derivation, transition derivation, provenance/uncertainty propagation, stable serialization, audit output, and exact fixture reconstruction tests.

Quantitative acceptance targets:

- 100% agreement with prespecified synthetic intervals/transitions for deterministic fixtures;
- conflict fixtures produce prespecified `unknown`/uncertainty behavior;
- repeated execution produces equivalent canonical outputs after stable serialization, excluding intentionally variable metadata;
- duplicate same-state source records do not create false transitions.

Decision rule: reconstruction is deterministic, explainable, fully exercised by the frozen synthetic oracle, and sufficiently stable for utilization metrics to depend on it.

## Gate 4 -> 5: Utilization metrics are analytically valid

Required evidence includes metric definitions/formulas, partial-interval handling, unknown-state handling, 7-day/30-day acute-care-return definitions, zero-versus-missing rules, censoring/follow-up behavior, metric version identifiers, fixture-level expected-value tests, and provenance to canonical intervals.

Core state-specific metrics use `routine_inpatient`, `intermediate_care`, and `intensive_care`; legacy metric labels such as higher-observation or ICU as canonical state names are not permitted.

Decision rule: every reported utilization measure has a documented definition, provenance, missingness behavior, version, and passing expected-value test.

## Gate 5 -> 6: Cohort characterization is reproducible

Required evidence includes a prespecified feature set, interpretable descriptive grouping strategy if used, sample-size adequacy assessment, sensitivity analysis, patient-level traceability, missingness/uncertainty handling, reproducible figures/tables, and an interpretation boundary preventing descriptive patterns from becoming clinical labels.

Decision rule: cohort findings can be reproduced from canonical episode outputs and do not depend on undocumented judgment or post-hoc metric changes.

## Gate 6: Governed hospital-data readiness

Required evidence before real-data execution includes a finalized data dictionary, minimum necessary field list, local source-to-canonical mapping plan, infusion-anchor quality definition, required approvals/data-use agreements, protected working environment, validation/adjudication plan, and stop criteria for inadequate source-data quality.

Decision rule: institutional data analysis begins only when governance and data-quality controls are sufficient to prevent invalid trajectory reconstruction.

## Capstone completion gate

The capstone is ready for final analysis/write-up when Gates 0-5 are complete; Gate 6 has either been completed or explicitly documented as unavailable within the capstone period; all reported results regenerate from versioned code/inputs; figures and tables trace to versioned artifacts; limitations cover missingness, mapping uncertainty, sample size, transportability, and the non-operational nature of the work; and no conclusion overstates descriptive findings as clinical recommendations.

## Gate evidence retention

For every passed gate retain the evidence record, requirement IDs, commit/PR identifier, CI/test reference, known limitations, accepted residual risks, and frozen artifact/version list. This creates an auditable capstone-development record rather than relying on informal recollection.
