# CART-TRACE Phase Gates

This document defines the evidence required to advance from one thesis-development phase to the next. A phase is not complete because code exists; it is complete when its exit evidence is reviewable, reproducible, and sufficient to protect downstream validity.

Each gate should produce a completed `docs/gate_evidence_template.md` record.

## Gate policy

A gate may be:

- **PASS** — all mandatory evidence exists and downstream work can rely on it;
- **CONDITIONAL PASS** — a limited residual item remains, but it does not threaten downstream validity and has an explicit closure plan;
- **FAIL / HOLD** — unresolved ambiguity or missing evidence would contaminate downstream implementation or analysis.

A conditional pass is not permitted when the unresolved item changes canonical semantics, time alignment, interval definitions, provenance behavior, or metric formulas used downstream.

Every gate review must also inspect `docs/risk_register.md` and record accepted residual risks.

## Gate 0 -> 1: Scope locked

Required evidence:
- thesis question documented in `THESIS.md`;
- explicit included/excluded domains;
- synthetic-first public-development policy;
- no-PHI and non-operational guardrails;
- thesis success criterion stated;
- initial data domains identified;
- requirements register established;
- minimum necessary data principle documented.

Required review questions:
- can every current thesis aim be answered without CMC/manufacturing data?
- can every current thesis aim be answered without patient-generated health data?
- is the public repository still useful if governed hospital data are delayed?
- is any wording implying bedside utility or clinical recommendations?

Decision rule: all required scope artifacts exist and no mandatory thesis requirement depends on excluded domains or prospective decision support.

Frozen after passage unless formally changed:
- thesis question;
- core aims;
- scope exclusions;
- non-operational boundary.

## Gate 1 -> 2: Canonical model stable enough for fixtures

Required evidence:
- controlled care-state vocabulary;
- therapy-episode schema;
- care-state interval schema;
- care-transition schema;
- minimal encounter input specification;
- provenance specification;
- deterministic treatment-relative time convention;
- interval boundary convention;
- same-timestamp tie-breaking rule;
- one hand-worked example spanning multiple encounters;
- one full synthetic episode that validates across all Phase 1 schemas.

Quality checks:
- local unit names are not embedded in canonical states;
- every derived object can carry source provenance;
- unknown/conflicting states are representable;
- timestamps and interval boundaries are unambiguous;
- schemas do not require fields outside the minimum thesis data footprint;
- multiple encounters can coexist in one episode without ambiguity.

Required tests:
- valid and invalid schema examples;
- study-window boundary examples;
- duplicate-event example;
- conflict/unknown example;
- date-only versus timestamp precision behavior if supported.

Decision rule: every required Phase 2 fixture can be authored using the canonical model without inventing undocumented fields or changing semantics.

Frozen after passage unless versioned:
- core care-state vocabulary;
- interval semantics;
- treatment-relative time convention;
- required canonical identifiers;
- provenance contract.

Regression rule: a post-gate change to these artifacts requires affected fixtures and tests to be regenerated and Gate 1 impact to be reviewed.

## Gate 2 -> 3: Synthetic cohort is testable

Required evidence:
- six required synthetic trajectory classes;
- expected state intervals for each fixture;
- expected transition sequence for each fixture;
- expected utilization measures for each fixture;
- documented edge cases;
- fixture manifest identifying which requirement each case exercises;
- raw event representation for every fixture;
- immutable or versioned truth-set outputs.

Minimum edge-case coverage:
- identical timestamps;
- adjacent intervals;
- overlaps;
- duplicate source events;
- missing end time;
- study-window boundary event;
- discharge and acute-care return on the same day;
- conflicting location sources;
- unknown interval between known states.

Quality checks:
- fixtures do not encode institutional identifiers or real workflow names;
- expected outputs are hand-reviewable;
- no expected result depends on implementation-specific behavior not documented in requirements;
- fixtures collectively exercise all mandatory reconstruction requirements.

Decision rule: fixtures provide a complete enough oracle that reconstruction code can be judged correct or incorrect without subjective interpretation.

Frozen after passage:
- fixture intent;
- expected intervals/transitions;
- metric expected values, subject to explicit metric-version changes.

## Gate 3 -> 4: Reconstruction is trustworthy

Required evidence:
- infusion anchoring implementation;
- treatment-relative time utility;
- deterministic event sorting;
- overlap/conflict resolution rules;
- interval derivation;
- transition derivation;
- provenance propagation;
- uncertainty propagation;
- reconstruction audit output;
- tests demonstrating expected fixture reconstruction.

Quantitative acceptance targets:
- 100% agreement with prespecified synthetic state intervals and transitions for non-conflict fixtures;
- conflict fixtures produce the prespecified `unknown`/uncertainty behavior;
- repeated execution on identical input produces byte-equivalent canonical outputs after stable serialization, excluding intentionally variable metadata;
- no duplicate transition is produced when repeated source events map to the same state.

Required negative tests:
- invalid anchor;
- impossible interval ordering;
- conflicting overlapping records;
- missing required identifier;
- unsupported care-state mapping.

Required auditability:
- each interval lists its source record(s) or derivation provenance;
- each uncertainty state identifies why certainty was not possible;
- transformation version is recorded.

Decision rule: reconstruction behavior is deterministic, explainable, fully exercised by synthetic tests, and sufficiently stable for utilization metrics to rely on it.

Regression rule: any change to reconstruction precedence or interval logic reruns the entire synthetic truth-set suite and triggers Gate 3 impact review.

## Gate 4 -> 5: Utilization metrics are analytically valid

Required evidence:
- metric definitions and formulas;
- handling of partial-day intervals;
- handling of overlapping/unknown intervals;
- 7-day and 30-day acute-care reuse definitions;
- explicit zero-versus-missing behavior;
- metric version identifiers;
- unit tests against fixture-level expected values;
- sensitivity checks for study-window boundaries;
- metric provenance linking values to canonical intervals.

Required metric states:
- observed value;
- observed zero;
- not applicable;
- not calculable because of missing/uncertain data;
- incomplete follow-up/censoring where relevant.

Decision rule: every reported utilization measure has a documented mathematical/algorithmic definition, provenance, missingness behavior, version, and passing expected-value test.

Frozen after passage:
- primary metric definitions used in Aim 2;
- acute-care reuse windows;
- high-acuity aggregation rule.

Regression rule: metric changes after Gate 4 require explicit versioning and rerunning all downstream cohort analyses.

## Gate 5 -> 6: Cohort characterization is reproducible

Required evidence:
- prespecified feature set;
- descriptive grouping method;
- rationale for number/type of groups;
- sample-size adequacy assessment;
- sensitivity analysis plan;
- patient-level traceability from cohort assignment to episode sequence;
- missingness/uncertainty treatment;
- reproducible figures/tables;
- explicit interpretation boundary preventing clinical labeling.

Quality checks:
- grouping does not depend on undocumented manual reassignment;
- method complexity is justified by cohort size;
- alternative reasonable settings are explored in sensitivity analyses;
- uncertain episodes are handled according to a prespecified rule;
- descriptive patterns are not presented as risk scores or management classes.

Decision rule: cohort findings can be reproduced from canonical episode outputs and do not depend on undocumented judgment or post-hoc metric changes.

## Gate 6: Governed hospital-data readiness

Required evidence before real-data execution:
- finalized data dictionary;
- minimum necessary field list;
- source-to-canonical mapping plan;
- infusion-anchor quality definition;
- institutional approvals/data-use agreement as applicable;
- protected working environment;
- validation sampling/adjudication plan;
- no export of PHI into the public repository;
- reproducible environment specification;
- local mapping review by an appropriate institutional stakeholder when required;
- stop criteria defined for inadequate data quality.

Required pilot checks before full cohort execution:
- sample episodes map to canonical states;
- infusion anchor is usable at required precision;
- location data support expected care-state distinctions;
- missingness is quantified;
- no systematic overlap/mapping artifact is evident.

Decision rule: institutional data analysis begins only when governance and data-quality controls are sufficient to prevent invalid trajectory reconstruction.

Stop rule: if source data cannot reliably support the infusion anchor or care-state mapping, Phase 6 analysis pauses and the thesis scope is narrowed rather than forcing unreliable reconstruction.

## Thesis completion gate

The thesis is ready for analysis write-up when:
- Gates 0-5 are complete;
- Gate 6 has either been completed or explicitly documented as unavailable within the thesis period;
- all reported results can be regenerated from versioned code and inputs;
- all figures/tables trace to a versioned analysis artifact;
- limitations include missingness, mapping uncertainty, sample-size constraints, transportability, and the non-operational nature of the work;
- no thesis conclusion overstates descriptive associations as clinical recommendations;
- the risk register has no unresolved high-impact issue that invalidates the primary thesis claim.

## Gate evidence retention

For each passed gate, retain:
- completed gate evidence record;
- relevant requirement IDs;
- commit/PR identifier;
- test result reference;
- known limitations;
- accepted residual risks;
- frozen artifact/version list.

This creates an auditable thesis-development record rather than relying on informal recollection of when methodological decisions were made.
