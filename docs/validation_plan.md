# CART-TRACE Validation Plan

The thesis requires evidence that CART-TRACE reconstructs hospital care trajectories correctly before any cohort-level interpretation is trusted. Validation therefore proceeds from schema verification to synthetic truth sets and, only if approved data become available, source-record validation.

## Validation layers

### Layer 1 — Schema and contract validation

Purpose: verify structural correctness.

Requirements:
- all canonical JSON objects validate against versioned schemas;
- required identifiers and timestamps are present;
- care-state values are valid vocabulary members;
- interval end is not before interval start;
- invalid or incomplete records fail with interpretable errors.

Acceptance target: 100% of valid synthetic fixtures pass and deliberately invalid fixtures fail as expected.

### Layer 2 — Temporal utility validation

Purpose: verify treatment-relative alignment.

Test cases:
- timestamp exactly at infusion;
- one second/minute/hour before and after infusion;
- day-boundary behavior;
- timezone-aware timestamp conversion;
- date-only infusion anchor behavior if supported;
- study-window start/end inclusion rules.

Acceptance target: all boundary cases match the documented relative-time convention.

### Layer 3 — Synthetic trajectory truth-set validation

Purpose: verify trajectory reconstruction against known truth.

Required fixture classes:
1. routine recovery;
2. prolonged routine inpatient stay;
3. transient escalation/de-escalation;
4. ICU escalation;
5. discharge with early acute-care return;
6. conflicting/missing location records.

Each fixture shall define:
- raw source-like input records;
- expected normalized intervals;
- expected transitions;
- expected uncertainty flags;
- expected utilization metrics.

Acceptance target:
- exact interval/transition agreement for deterministic fixtures;
- prespecified uncertainty output for conflict fixtures;
- no false transitions caused by duplicate same-state records.

### Layer 4 — Metric validation

Purpose: verify that utilization measures are mathematically and semantically correct.

Tests include:
- total inpatient duration;
- duration by care state;
- transition count;
- time to first escalation;
- high-acuity duration;
- time to discharge;
- 7-day and 30-day acute-care reuse;
- explicit missing result when follow-up is insufficient.

Acceptance target: exact agreement with hand-calculated expected metrics for all synthetic fixtures.

### Layer 5 — Reproducibility validation

Purpose: verify that results do not depend on run order or hidden state.

Requirements:
- repeated execution on identical input/configuration yields identical canonical outputs;
- deterministic sorting is enforced;
- software/environment versions are recorded;
- generated reports are reproducible from canonical outputs.

Acceptance target: reproducible outputs across repeated clean runs, excluding intentionally variable metadata.

### Layer 6 — Governed source-record validation

Only applicable if approved institutional data become available.

Purpose: evaluate validity against real source records.

Proposed design:
- select an approved validation sample spanning uncomplicated and complex episodes;
- compare reconstructed encounter boundaries, care-state intervals, transfers, discharge, and acute-care returns with source records;
- classify disagreements as source ambiguity, mapping error, reconstruction error, or missing data;
- adjudicate according to a prespecified process;
- revise mapping/reconstruction rules only with versioned documentation.

Possible measures:
- proportion of source transitions correctly represented;
- timestamp disagreement distribution;
- proportion of episode time assigned to correct/non-unknown state;
- unknown-state burden;
- episode-level agreement on ICU exposure and acute-care reuse.

No numerical performance threshold should be claimed until source-data characteristics and sample size are known. Thresholds for real-data acceptance should be prespecified with the thesis committee before final validation.

## Error taxonomy

Validation failures should use a stable taxonomy:
- `schema_error`
- `missing_anchor`
- `invalid_interval`
- `mapping_conflict`
- `overlap_conflict`
- `unknown_state`
- `transition_mismatch`
- `metric_mismatch`
- `insufficient_followup`
- `source_ambiguity`

This taxonomy is for research quality control, not clinical event classification.

## Sensitivity analyses

Where data permit, thesis analyses should evaluate sensitivity to:
- alternative episode-window boundaries;
- higher-observation classification choices;
- treatment of short gaps between encounters;
- inclusion/exclusion of uncertain intervals;
- follow-up completeness for reuse measures.

## Validation reporting

A thesis-ready validation report should include:
1. fixture coverage matrix;
2. schema-test results;
3. reconstruction-test results;
4. metric-test results;
5. missingness and uncertainty summary;
6. real-data validation results if available;
7. unresolved failure modes;
8. version identifiers for schemas, mappings, and reconstruction code.

## Stop conditions

Cohort characterization should not proceed if:
- core synthetic trajectories fail reconstruction tests;
- interval overlap handling is nondeterministic;
- metric definitions remain ambiguous;
- missingness is silently converted to zero;
- source mappings cannot be audited.

These conditions require remediation in the preceding development phase before analysis continues.
