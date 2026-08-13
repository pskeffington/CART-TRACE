# CART-TRACE Gate Evidence Template

Use this template when proposing advancement through a development gate. The purpose is to make phase progression reviewable, evidence-based, and reproducible.

## Gate

**Proposed transition:** `Gate X -> Y`

**Branch / PR:**

**Candidate release tag:**

**Date reviewed:**

## Gate decision

- [ ] PASS
- [ ] CONDITIONAL PASS
- [ ] FAIL / REMAIN IN CURRENT PHASE

A conditional pass must identify the residual item, why it does not threaten downstream validity, and the deadline/phase in which it must be closed.

## Required evidence checklist

For each gate requirement, provide:

| Requirement | Status | Evidence artifact | Test / review result | Notes |
|---|---|---|---|---|
| Example | Complete | `schemas/example.schema.json` | tests passing | — |

## Requirement traceability

List the requirement IDs satisfied by this gate evidence.

Example:

`MODEL-001, MODEL-002, TIME-001, PROV-001`

No gate should advance with an untracked mandatory requirement.

## Verification evidence

### Automated verification

Record applicable test evidence:

- schema validation;
- unit tests;
- integration/fixture tests;
- deterministic output checks;
- metric expected-value tests;
- reproducibility checks.

### Manual review

Record items requiring expert or manual inspection:

- hand-worked episode review;
- mapping-rule review;
- synthetic truth-set review;
- figure/table sanity review;
- governed source-record adjudication.

## Known limitations at gate

Document limitations that remain true even if the gate passes. Examples:

- synthetic data only;
- limited trajectory classes;
- unresolved local mapping questions;
- no external validation;
- no prospective clinical validation.

Passing a gate means the phase objective is sufficiently satisfied to support the next engineering step; it does not imply clinical validity.

## Regression risks

Identify artifacts that must not change silently after gate passage.

Examples:

- care-state vocabulary;
- treatment-relative time convention;
- interval boundary semantics;
- utilization metric formulas;
- synthetic truth-set expected outputs.

Any later change to a frozen artifact should trigger versioning, affected-test updates, and an explicit gate-impact review.

## Reviewer questions

Before approving advancement, reviewers should be able to answer:

1. Is the evidence sufficient to reproduce the claimed phase output?
2. Are assumptions documented rather than embedded implicitly in code?
3. Is missingness or uncertainty represented explicitly?
4. Are outputs traceable back to their inputs and transformation version?
5. Does the work stay inside the thesis scope and non-operational boundary?
6. Would a downstream phase rely on an unresolved ambiguity from this phase?

## Approval record

**Reviewer(s):**

**Decision rationale:**

**Residual actions:**

**Next phase authorized:**
