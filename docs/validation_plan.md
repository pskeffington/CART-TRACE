# CART-TRACE Validation Plan

CART-TRACE validation follows the formal clinical data structuring framework defined in `docs/clinical_data_structuring_framework.md`. Validation is therefore not limited to schema checks. The method must establish structural conformance, completeness, temporal plausibility, semantic validity, reconstruction fidelity, reproducibility, and analytic fitness before cohort-level interpretation is trusted.

## Validation dimensions

### 1. Structural conformance

Purpose: verify that source-like, canonical, provenance, and metric objects satisfy their versioned contracts.

Checks include:
- required identifiers and timestamps are present;
- care-state values are canonical vocabulary members;
- transition types are valid;
- provenance arrays are non-empty where required;
- nullable/open-end behavior conforms to schema;
- deliberately invalid fixtures fail with interpretable errors.

Acceptance target: 100% of valid synthetic objects pass applicable schemas and prespecified invalid cases fail as expected.

### 2. Completeness and analytic sufficiency

Purpose: determine whether enough evidence exists for the intended trajectory or metric.

Checks include:
- infusion anchor availability and precision;
- encounter/location coverage across the relevant interval;
- source-record identifiers for audit;
- explicit missing/open end times;
- follow-up availability for acute-care-return metrics;
- burden of `unknown` state within the analytic window.

Completeness is evaluated relative to the metric being reported. An episode may be usable for one metric and not calculable for another.

Recommended episode-level research statuses:
- `reconstructable`;
- `reconstructable_with_uncertainty`;
- `not_reconstructable`.

### 3. Temporal plausibility

Purpose: verify treatment-relative alignment and internally coherent interval ordering.

Test cases include:
- timestamp exactly at infusion;
- negative and positive fractional relative hours;
- timezone-aware timestamp conversion;
- study-window start/end inclusion rules;
- adjacent intervals sharing a timestamp;
- interval end after start;
- deterministic identical-timestamp behavior;
- explicit open-end handling;
- no silent interval overlap.

Acceptance target: all synthetic temporal boundary cases match the documented `[start,end)` and continuous-hour conventions.

### 4. Semantic validity

Purpose: verify that source-to-canonical interpretation uses explicit, reviewable rules.

Checks include:
- source labels map through versioned configuration;
- local/institution-specific labels do not become canonical labels;
- source priority/precedence is explicit;
- equal-priority disagreement produces `unknown` rather than arbitrary selection;
- source encounter category is preserved where relevant;
- `acute_care_return` remains a transition type rather than a state.

Acceptance target: all synthetic mapping cases resolve exactly as specified by the frozen Gate 1/Phase 2 contracts.

### 5. Reconstruction fidelity

Purpose: verify deterministic trajectory reconstruction against prespecified truth.

Required core fixture classes:
1. routine recovery;
2. prolonged routine inpatient stay;
3. transient escalation/de-escalation;
4. intensive-care escalation/de-escalation;
5. discharge with early acute-care return;
6. conflicting/missing location evidence.

Boundary/error cases additionally cover:
- duplicate same-state records;
- missing/open end time;
- study-window boundary;
- adjacent intervals;
- same-day return;
- invalid state;
- malformed timestamp;
- reversed interval;
- missing infusion anchor;
- equal-priority conflict.

Acceptance target:
- exact interval agreement for deterministic fixtures;
- exact transition agreement for deterministic fixtures;
- prespecified `unknown`/uncertainty behavior for conflict cases;
- no false transitions caused by duplicate same-state inputs.

### 6. Reproducibility

Purpose: verify that output does not depend on hidden state or input ordering.

Requirements:
- repeated execution on identical input/configuration yields equivalent canonical outputs;
- deterministic sorting is enforced;
- stable serialization is available;
- transformation and mapping versions are recorded;
- generated reports derive from versioned canonical outputs.

Acceptance target: byte-equivalent stable serialization for repeated synthetic runs, excluding intentionally variable metadata.

### 7. Analytic fitness and metric validation

Purpose: determine whether each utilization metric is mathematically correct and supported by sufficient evidence.

The machine-readable metric contract is `config/metric_definitions.json`.

Primary analytic window:

`[0,720)` hours after infusion.

Negative-time records may establish encounter continuity but are excluded from primary post-infusion utilization totals.

Core metric tests include:
- total inpatient duration;
- routine inpatient duration;
- intermediate-care duration;
- intensive-care duration;
- high-acuity duration where retained;
- transition count;
- time to first escalation;
- time to discharge;
- 7-day acute-care return;
- 30-day acute-care return;
- unknown-state duration.

Each metric result must carry a status distinguishing at minimum:
- `observed`;
- `observed_zero`;
- `not_applicable`;
- `not_calculable`;
- `incomplete_followup`.

Unknown, uncertain, or incomplete data must never be silently converted to zero.

Acceptance target: exact agreement with prespecified post-infusion expected values for synthetic fixtures and exact expected status behavior for missingness/follow-up cases.

## Metric eligibility rules

A metric may be reported only when the evidence required by its machine-readable definition is satisfied.

Examples:
- duration metrics require defensible interval ends after clipping to `[0,720)`;
- state-specific duration is `not_calculable` when an overlapping `unknown` interval could alter allocation;
- time to first escalation is `not_calculable` if unresolved uncertainty precedes or spans the possible first escalation;
- 7-day/30-day return is `incomplete_followup` when observation after discharge is shorter than the required ascertainment window and no return has already been observed;
- observed absence of a qualifying event with complete ascertainment is a valid zero/false result, not missing.

## Governed source-record validation

Only applicable if appropriately approved institutional data become available.

Purpose: evaluate whether the synthetic-validated structuring/reconstruction method transfers to real source records.

Proposed design:
- select an approved sample spanning uncomplicated and complex episodes;
- compare reconstructed encounter boundaries, care-state intervals, transfers, discharge, and acute-care returns with source records;
- record infusion-anchor precision;
- classify disagreements as source ambiguity, mapping error, reconstruction error, missing data, or follow-up insufficiency;
- adjudicate according to a prespecified process;
- revise mapping/reconstruction rules only with versioned documentation and regression testing.

Possible descriptive measures include:
- transition concordance;
- timestamp disagreement distribution;
- proportion of episode time in known versus `unknown` state;
- episode-level agreement on intermediate/intensive-care exposure;
- acute-care-return agreement;
- proportion classified `reconstructable`, `reconstructable_with_uncertainty`, or `not_reconstructable`.

No universal clinical-performance threshold is prespecified. Any governed-data acceptance threshold should be defined with the capstone committee after source-data characteristics and feasible sample size are known.

## Stable error/status taxonomy

Validation and metric processing should use stable machine-readable reasons where possible:
- `schema_error`
- `missing_anchor`
- `invalid_interval`
- `mapping_conflict`
- `overlap_conflict`
- `unknown_state`
- `open_end`
- `transition_mismatch`
- `metric_mismatch`
- `insufficient_followup`
- `source_ambiguity`
- `not_calculable`

This taxonomy is for research quality control, not clinical event classification.

## Sensitivity analyses

Where data permit, analyses should evaluate sensitivity to:
- analytic-window boundaries;
- source-to-intermediate-care mapping choices;
- treatment of short gaps between encounters;
- inclusion/exclusion of uncertain intervals;
- follow-up completeness for return metrics;
- alternative handling of episodes classified `reconstructable_with_uncertainty`.

## Validation reporting

A capstone-ready validation report should include:
1. clinical-data structuring framework diagram;
2. fixture/requirement coverage matrix;
3. schema/conformance results;
4. reconstruction-fidelity results;
5. reproducibility results;
6. metric eligibility/status results;
7. post-infusion metric validation results;
8. missingness and uncertainty summary;
9. governed source-record validation results if available;
10. unresolved failure modes and version identifiers.

## Stop conditions

Cohort characterization should not proceed if:
- core synthetic trajectories fail reconstruction tests;
- interval overlap handling is nondeterministic;
- source mappings cannot be audited;
- Phase 4 metric definitions are not frozen;
- pre-infusion time is included in primary post-infusion totals without an explicit alternative metric definition;
- unknown/missing data are silently converted to zero;
- follow-up sufficiency is ignored for return metrics.

These conditions require remediation in the preceding layer or phase before analysis continues.
