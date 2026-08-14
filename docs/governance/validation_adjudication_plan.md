# CART-TRACE Governed Validation and Adjudication Plan

## Purpose

This plan defines how governed institutional data should be reviewed before reconstructed CAR T hospital-care trajectories are treated as analytically defensible. It operationalizes source concordance, mapping review, discrepancy handling, and metric-specific fitness without changing the frozen CART-TRACE computational specification.

## Validation objectives

Governed validation should determine whether:

1. the infusion anchor is correct and sufficiently precise;
2. encounter/location evidence is temporally complete enough for reconstruction;
3. local source labels are mapped consistently with approved semantic meaning;
4. reconstructed intervals and transitions agree with source evidence;
5. uncertainty/conflict is exposed rather than silently resolved;
6. metric statuses reflect actual calculability and follow-up sufficiency;
7. the same governed input and mapping version reproduce the same outputs.

## Validation domains

### A. Cohort and anchor validation

Review a sample of therapy episodes for:

- correct episode linkage;
- correct infusion timestamp;
- repeat-infusion separation;
- absence of order/scheduling timestamps substituted for administration time;
- correct study-window construction.

### B. Source-to-staging validation

Assess:

- timestamp parsing and timezone coherence;
- retention of source identifiers;
- preservation of source labels;
- duplicate handling before canonicalization;
- missing/open-end representation;
- deterministic ordering for ties.

### C. Mapping validation

Compare approved local mappings with authoritative metadata and/or domain-steward interpretation. Record disagreements by source label and mapping version.

### D. Reconstruction concordance

For sampled episodes, compare reconstructed intervals and transitions against governed source records. Review:

- interval boundaries;
- state assignment;
- escalation/de-escalation transitions;
- discharge boundaries;
- emergency return classification;
- explicit `unknown` intervals;
- provenance coverage.

### E. Metric validation

For sampled episodes, independently review selected metric results against the validated canonical trajectory, including:

- total/routine/intermediate/intensive/high-acuity hours;
- transition count;
- time to escalation;
- time to discharge;
- 7-day and 30-day acute-care return status;
- unknown-state burden;
- follow-up sufficiency/status.

## Sampling approach

The governed validation sample should deliberately include trajectory and data-quality diversity rather than being a simple convenience sample. Where feasible, include:

- routine inpatient recovery;
- intermediate-care exposure;
- intensive-care exposure;
- post-discharge emergency return;
- repeat encounters;
- overlapping records;
- open/missing ends;
- mapping ambiguity;
- explicit `unknown` or conflict;
- incomplete follow-up.

Sample size should be determined by capstone feasibility and governance constraints; the method does not require a fixed universal threshold.

## Adjudication workflow

When a discrepancy is identified:

1. classify the discrepancy domain: anchor, source extraction, timestamp, mapping, precedence, reconstruction, metric, follow-up, or provenance;
2. determine whether the discrepancy reflects source ambiguity, local mapping interpretation, implementation defect, or reviewer disagreement;
3. preserve the original governed evidence and existing result;
4. record the proposed adjudication and rationale;
5. obtain the required reviewer/steward agreement under the governed protocol;
6. if a local mapping changes, version the mapping and regenerate affected governed outputs;
7. if a defect affects frozen public semantics, stop and initiate explicit gate-impact review rather than silently changing the method.

## Discrepancy categories

Use controlled categories where feasible:

- `anchor_mismatch`;
- `missing_source_evidence`;
- `timestamp_discrepancy`;
- `mapping_disagreement`;
- `precedence_disagreement`;
- `interval_boundary_disagreement`;
- `state_disagreement`;
- `transition_disagreement`;
- `metric_value_disagreement`;
- `metric_status_disagreement`;
- `followup_disagreement`;
- `provenance_gap`;
- `reviewer_disagreement`;
- `other_documented`.

## Episode-level review outcome

After validation/adjudication, classify each reviewed episode for the intended analysis as:

- `reconstructable`;
- `reconstructable_with_uncertainty`;
- `not_reconstructable`.

The classification must include reasons and should not imply that every metric shares the same calculability status.

## Validation reporting

Report at minimum, subject to governance approval:

- number of episodes reviewed;
- infusion-anchor agreement;
- mapping coverage and disagreement counts;
- interval/state/transition discrepancy counts;
- episodes with unresolved uncertainty;
- provenance completeness;
- metric disagreement counts;
- metric availability/follow-up limitations;
- mapping versions used;
- number and type of adjudications requiring regeneration.

Avoid presenting synthetic oracle agreement and governed source-concordance results as interchangeable evidence. The former establishes computational fidelity to specification; the latter evaluates transportability and local data validity.

## Reviewer independence and documentation

Where feasible, high-impact semantic disputes should be reviewed by more than one qualified reviewer or by a reviewer plus authoritative data/domain steward. The public repository should document the adjudication method, not sensitive reviewer notes or patient-level evidence.

## Public/private boundary

Patient-level validation records, source screenshots, PHI, institution-specific raw labels where restricted, free-text reviewer notes, and adjudication evidence remain in the governed environment. Public artifacts may include the protocol and approved aggregate concordance/discrepancy summaries.

## Gate 6 readiness criterion

This plan is ready for governed application when reviewer roles, source-access boundaries, discrepancy categories, mapping-version handling, regeneration rules, and aggregate reporting expectations have been defined sufficiently to execute a reproducible validation sample without improvising analytic semantics during review.
