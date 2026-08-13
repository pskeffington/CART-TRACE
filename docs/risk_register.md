# CART-TRACE Risk Register

This register captures risks that could invalidate, delay, or distort the MS HSE thesis implementation. It is intended to be reviewed at each phase gate.

## Risk scale

- Likelihood: Low / Medium / High
- Impact: Low / Medium / High
- Gate consequence: Monitor / Conditional pass / Block

## RISK-001 — Inadequate infusion anchor quality

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** Block Phase 6 analysis if unresolved

If infusion timing is missing, inconsistent, or only available at coarse resolution, treatment-relative reconstruction may be unreliable.

Mitigations:
- require a documented anchor-quality field;
- distinguish date-only versus timestamp precision;
- test sensitivity to anchor precision;
- exclude or separately analyze episodes lacking a trustworthy anchor.

## RISK-002 — Care-location data cannot support canonical mapping

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** Block Phase 6 if systematic

Local location data may be incomplete, free-text, administrative, or inconsistent with actual care level.

Mitigations:
- prespecify authoritative source hierarchy;
- retain raw location values in provenance;
- allow `unknown` rather than forced assignment;
- validate a sample against source records.

## RISK-003 — Intermediate-care semantics differ by institution

**Likelihood:** High  
**Impact:** Medium  
**Gate consequence:** Conditional pass / sensitivity analysis

`higher_observation` may represent different staffing, monitoring, or unit structures across hospitals.

Mitigations:
- define it as a research normalization state, not a clinical equivalence class;
- keep local mapping configuration separate;
- report state-specific results with mapping limitations;
- perform sensitivity analysis combining or separating intermediate care.

## RISK-004 — Overlapping encounter records create false escalation

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** Block Gate 3 -> 4 if unresolved

Administrative overlap may produce impossible simultaneous care states.

Mitigations:
- explicit overlap precedence rules;
- conflict flags;
- synthetic overlap fixtures;
- deterministic audit output.

## RISK-005 — Missingness is informative

**Likelihood:** High  
**Impact:** High  
**Gate consequence:** Monitor through Phases 4-6

Missing location or follow-up data may correlate with patient movement, transfer, outside care, or disease severity.

Mitigations:
- quantify missingness by episode and time;
- avoid zero-imputation;
- include uncertainty metrics in cohort characterization;
- sensitivity analyses excluding high-missingness episodes.

## RISK-006 — Sample size insufficient for stable phenotype discovery

**Likelihood:** Medium  
**Impact:** Medium  
**Gate consequence:** May narrow Aim 3

A small CAR T cohort may not support unsupervised clustering or stable multi-group inference.

Mitigations:
- prioritize descriptive trajectory strata;
- avoid overfitted clustering;
- prespecify minimum support for exploratory grouping;
- treat Aim 3 as descriptive/exploratory if needed.

## RISK-007 — Metric definitions drift during analysis

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** Block Gate 4 -> 5

Changing LOS, high-acuity duration, or reuse definitions after seeing cohort results risks analytic bias.

Mitigations:
- freeze metric definitions before cohort analysis;
- version definitions;
- require impact review for changes;
- rerun all affected fixtures and analyses.

## RISK-008 — Study-window choice drives results

**Likelihood:** Medium  
**Impact:** Medium  
**Gate consequence:** Sensitivity analysis required

The `day -7` to `day +30` development window may not capture all relevant hospitalization or readmission patterns.

Mitigations:
- treat the window as configurable;
- justify the primary window prospectively;
- perform alternative-window sensitivity analyses where feasible.

## RISK-009 — Acute-care return classification is ambiguous

**Likelihood:** Medium  
**Impact:** Medium  
**Gate consequence:** Conditional pass if source type retained

Emergency evaluation, observation, and inpatient readmission may be inconsistently coded.

Mitigations:
- preserve source encounter type;
- use a broad `acute_care_return` canonical concept;
- only label `readmission` when source data support it.

## RISK-010 — Real-data governance delays thesis schedule

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** May prevent Phase 6

Institutional approvals or extraction timelines may exceed the thesis schedule.

Mitigations:
- make Phases 0-5 independently defensible as a methods contribution;
- maintain a complete synthetic validation pathway;
- document Phase 6 as approval-dependent;
- avoid designing the thesis so that no scholarly result exists without real data.

## RISK-011 — Public repository accidentally encodes sensitive institutional detail

**Likelihood:** Low  
**Impact:** High  
**Gate consequence:** Block release

Mitigations:
- synthetic examples only;
- generic canonical states;
- local mappings outside public examples;
- pre-merge review for identifiers, credentials, internal unit names, and free text.

## RISK-012 — Descriptive findings are overinterpreted clinically

**Likelihood:** Medium  
**Impact:** High  
**Gate consequence:** Block thesis/release language until corrected

Mitigations:
- use characterization language;
- distinguish observed utilization from clinical appropriateness;
- avoid treatment or placement recommendations;
- state that prospective validation is required for clinical use.

## RISK-013 — Pipeline is reproducible only on the developer environment

**Likelihood:** Medium  
**Impact:** Medium  
**Gate consequence:** Block thesis-ready implementation

Mitigations:
- lock dependencies;
- provide clean-environment run instructions;
- deterministic seeds where randomness is used;
- automated end-to-end reproduction test.

## RISK-014 — Canonical model changes after synthetic truth sets are written

**Likelihood:** Medium  
**Impact:** Medium  
**Gate consequence:** Gate regression review required

Mitigations:
- version schemas;
- treat Gate 1 as semantic freeze for the thesis baseline;
- update truth sets only through explicit change review;
- maintain backward migration notes if required.

## Gate review rule

At every gate review:

1. identify new risks introduced by the completed phase;
2. reassess likelihood/impact of existing risks;
3. determine whether any risk blocks advancement;
4. assign mitigation evidence to a requirement or validation artifact;
5. document accepted residual risk in the gate evidence record.
