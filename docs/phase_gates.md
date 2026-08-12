# CART-TRACE Phase Gates

This document defines the evidence required to advance from one thesis-development phase to the next. A phase is not complete because code exists; it is complete when its exit evidence is reviewable and reproducible.

## Gate 0 -> 1: Scope locked

Required evidence:
- thesis question documented in `THESIS.md`;
- explicit included/excluded domains;
- synthetic-first public-development policy;
- no-PHI and non-operational guardrails;
- thesis success criterion stated;
- initial data domains identified.

Decision rule: all required scope artifacts exist and no mandatory thesis requirement depends on CMC, patient-generated data, or prospective decision support.

## Gate 1 -> 2: Canonical model stable enough for fixtures

Required evidence:
- controlled care-state vocabulary;
- therapy-episode schema;
- care-state interval schema;
- care-transition schema;
- minimal encounter input specification;
- provenance specification;
- deterministic treatment-relative time convention;
- one hand-worked example spanning multiple encounters.

Quality checks:
- local unit names are not embedded in canonical states;
- every derived object can carry source provenance;
- unknown/conflicting states are representable;
- timestamps and interval boundaries are unambiguous.

Decision rule: a complete synthetic episode can be represented without inventing undocumented fields or semantics.

## Gate 2 -> 3: Synthetic cohort is testable

Required evidence:
- six required synthetic trajectory classes;
- expected state intervals for each fixture;
- expected transition sequence for each fixture;
- expected utilization measures for each fixture;
- documented edge cases;
- fixture manifest identifying which requirement each case exercises.

Decision rule: fixtures provide a sufficient oracle for automated reconstruction testing.

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
- tests demonstrating expected fixture reconstruction.

Quantitative acceptance target:
- 100% agreement with prespecified synthetic state intervals and transitions for non-conflict fixtures;
- conflict fixtures produce the prespecified `unknown`/uncertainty behavior;
- repeated execution on identical input produces byte-equivalent canonical outputs after stable serialization, excluding intentionally variable metadata.

Decision rule: reconstruction behavior is deterministic, explainable, and fully exercised by synthetic tests.

## Gate 4 -> 5: Utilization metrics are analytically valid

Required evidence:
- metric definitions and formulas;
- handling of partial-day intervals;
- handling of overlapping/unknown intervals;
- 7-day and 30-day acute-care reuse definitions;
- explicit zero-versus-missing behavior;
- unit tests against fixture-level expected values;
- sensitivity checks for window boundaries.

Decision rule: every reported utilization measure has a documented mathematical/algorithmic definition, provenance, and test.

## Gate 5 -> 6: Cohort characterization is reproducible

Required evidence:
- prespecified feature set;
- descriptive grouping method;
- rationale for number/type of groups;
- sensitivity analysis plan;
- patient-level traceability from cohort assignment to episode sequence;
- missingness/uncertainty treatment;
- reproducible figures/tables.

Decision rule: cohort findings can be reproduced from canonical episode outputs and do not depend on undocumented manual judgment.

## Gate 6: Governed hospital-data readiness

Required evidence before real-data execution:
- finalized data dictionary;
- minimum necessary field list;
- source-to-canonical mapping plan;
- institutional approvals/data-use agreement as applicable;
- protected working environment;
- validation sampling/adjudication plan;
- no export of PHI into the public repository;
- reproducible environment specification.

Decision rule: institutional data access begins only when governance and validation controls are in place.

## Thesis completion gate

The thesis is ready for analysis write-up when:
- Gates 0-5 are complete;
- Gate 6 has either been completed or explicitly documented as unavailable within the thesis period;
- all reported results can be regenerated from versioned code and inputs;
- limitations include missingness, mapping uncertainty, sample-size constraints, transportability, and the non-operational nature of the work;
- no thesis conclusion overstates descriptive associations as clinical recommendations.
