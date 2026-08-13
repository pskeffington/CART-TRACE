# CART-TRACE Manuscript-Style Capstone Scaffold

## Working title

**CART-TRACE: Reconstructing Hospital Care Trajectories Following CAR T-Cell Therapy from Longitudinal Clinical Data**

## Abstract scaffold

### Background
Longitudinal hospital records surrounding CAR T-cell infusion may contain fragmented encounter, location, transfer, and disposition information. Analyses of post-infusion care therefore require an explicit method for transforming heterogeneous source records into coherent treatment-relative trajectories while preserving provenance, missingness, and uncertainty.

### Objective
Develop and validate a deterministic clinical-data structuring and temporal reconstruction framework for representing post-infusion hospital care trajectories and deriving transparent utilization measures during the first 30 days after CAR T-cell infusion.

### Methods
CART-TRACE uses a layered architecture comprising source preservation, staging normalization, canonical trajectory reconstruction, validation, and analytic representation. Therapy episodes are aligned to continuous time relative to infusion, care is represented as half-open `[start,end)` intervals, source labels are mapped to a small institution-independent state vocabulary, and conflicting equal-priority evidence resolves to explicit `unknown`. Reconstruction logic is evaluated against prespecified synthetic truth sets. Versioned post-infusion utilization metrics are calculated in `[0,720)` hours and include explicit status, follow-up sufficiency, and provenance.

### Results
Report exact interval and transition oracle agreement, metric expected-value agreement, handling of conflict/unknown states, and synthetic descriptive utilization. Clearly state that synthetic examples demonstrate method behavior rather than clinical incidence or external validity.

### Conclusions
CART-TRACE demonstrates whether fragmented longitudinal hospital records can be transformed reproducibly into auditable treatment-relative care trajectories that support descriptive post-infusion utilization analysis. Governed clinical-data validation is a subsequent approval-dependent application.

---

# 1. Introduction

## 1.1 Clinical and data context

Introduce CAR T-cell therapy as a treatment associated with temporally concentrated post-infusion hospital care and possible movement across routine inpatient, intermediate, intensive, emergency, discharge, and return-care settings. Keep this section focused on the data representation problem rather than toxicity prediction or treatment eligibility.

## 1.2 Health-data problem

State that the analytic challenge is not encounter counting alone. Relevant care-state information can be distributed across encounter, admission/discharge, transfer, and location records with potentially overlapping, duplicated, incomplete, or conflicting timestamps.

## 1.3 Methodological gap

Motivate the need for a transparent, versioned, provenance-preserving reconstruction layer between raw longitudinal records and utilization analysis. Existing interoperability models may inform semantics, but the capstone evaluates a purpose-built research representation rather than requiring a particular source standard.

## 1.4 Objective and questions

Primary question:

> Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?

Secondary descriptive question:

> What patterns of acute-care utilization, escalation, de-escalation, discharge, and early return are observed in the reconstructed trajectories?

Explicitly state that prediction, eligibility adjudication, prospective alerts, and treatment recommendation are outside scope.

---

# 2. Methods

## 2.1 Study design

Describe CART-TRACE as a retrospective, synthetic-first methodological study. The primary contribution is development and validation of a clinical-data structuring, trajectory reconstruction, and analytic representation framework. Synthetic data are used to establish computational correctness before any governed clinical application.

## 2.2 Unit of analysis and treatment anchor

The unit of analysis is the CAR T-cell therapy episode. Infusion is the temporal anchor at `0` hours. Continuous relative time is calculated as:

`(event_timestamp - infusion_timestamp).total_seconds() / 3600`

Do not floor negative times. Limited pre-infusion records may be retained only to establish encounter continuity.

## 2.3 Clinical-data structuring architecture

Reference Figure 1.

Describe the five layers:

1. source clinical data;
2. staging representation;
3. canonical trajectory representation;
4. validation/review;
5. analytic representation.

Emphasize that source evidence and derived research objects remain distinguishable throughout the pipeline.

## 2.4 Source and staging representation

Describe preservation of source timestamps, labels, encounter categories, source systems, record identifiers, and provenance. Staging normalizes offset-aware timestamps, calculates continuous relative time, attaches versioned mapping metadata, and provides deterministic ordering without prematurely asserting final care state.

## 2.5 Canonical care-state model

Reference Table 1.

Canonical states:

- `outpatient`;
- `emergency`;
- `routine_inpatient`;
- `intermediate_care`;
- `intensive_care`;
- `discharged`;
- `unknown`.

State that `acute_care_return` is a transition type, not a state.

## 2.6 Temporal and interval semantics

Care-state intervals use `[start,end)` semantics. Adjacent intervals may share a boundary without overlap. Open-ended intervals preserve null end values and an explicit reason rather than inventing duration. Events at exactly `+720` hours are outside the primary analytic window.

## 2.7 Mapping, overlap, and conflict resolution

Describe versioned source-to-canonical mapping, deterministic source ordering, precedence, duplicate same-state suppression, and equal-priority disagreement resolving to `unknown` with uncertainty and contributing source IDs retained.

## 2.8 Transition derivation

Canonical transition types are:

- `admission`;
- `transfer`;
- `escalation`;
- `deescalation`;
- `discharge`;
- `acute_care_return`;
- `other`;
- `unknown`.

Escalation/de-escalation uses the inpatient acuity ordering routine < intermediate < intensive. Emergency care is not treated as an inpatient acuity rank.

## 2.9 Synthetic truth set

Reference Table 2 and Supplementary Figure S1.

Describe the six prespecified trajectory classes:

1. routine recovery;
2. prolonged routine inpatient care;
3. transient intermediate-care escalation/de-escalation;
4. intensive-care escalation/de-escalation;
5. early post-discharge acute-care return;
6. conflicting location evidence producing `unknown`.

Also describe boundary/error cases including duplicate records, open end, adjacent intervals, study-window end, malformed timestamp, missing anchor, reversed interval, and equal-priority ambiguity.

## 2.10 Reconstruction validation

Reference Table 3.

Separate validation domains:

- structural conformance;
- temporal plausibility;
- semantic validity;
- exact reconstruction fidelity;
- reproducibility;
- analytic fitness.

Synthetic reconstruction validation requires exact interval-signature and transition-signature agreement with prespecified oracle outputs. Stable serialization and repeated-run equivalence establish deterministic reproducibility.

## 2.11 Post-infusion utilization measures

The primary analytic window is `[0,720)` hours after infusion. Negative-time continuity context is clipped from primary utilization measures.

Core metrics:

- total inpatient hours;
- routine inpatient hours;
- intermediate-care hours;
- intensive-care hours;
- high-acuity hours = intermediate + intensive;
- canonical transition count;
- time to first escalation;
- time to first post-infusion discharge;
- 7-day post-discharge acute-care return;
- 30-day post-discharge acute-care return;
- unknown-state hours.

Emergency time is not included in inpatient duration.

## 2.12 Missingness, uncertainty, and follow-up sufficiency

Every metric is paired with one of:

- `observed`;
- `observed_zero`;
- `not_applicable`;
- `not_calculable`;
- `incomplete_followup`.

Unknown intervals are not silently treated as zero. If an unknown interval can alter attribution of a duration metric, the affected state-specific and total inpatient values are non-calculable. A negative return result requires observation through the full requested post-discharge horizon; an observed qualifying return remains positive even if later follow-up is incomplete.

## 2.13 Metric provenance

Each metric-result object records the episode, metric version, analytic window, observation end, values, status, missingness reason, contributing interval IDs, transition IDs, and source-record IDs. Reference the metric-result schema and Table 1.

## 2.14 Phase 5 descriptive analysis

Reference Figures 2–3 and Tables 4–5. Synthetic cohort summaries use only `observed` and `observed_zero` numeric values for mean/median/minimum/maximum. Denominators, non-calculable results, not-applicable results, and incomplete follow-up are reported separately.

No inferential population estimates should be calculated from the six synthetic truth-set episodes.

## 2.15 Reproducibility

State that fixtures, schemas, mapping rules, reconstruction code, metric definitions, result schemas, reporting helpers, and automated tests are version controlled. Phase 5 derived output files are generated reproducibly from the frozen synthetic inputs rather than manually maintained.

## 2.16 Governed-data extension

If approved institutional data become available, the frozen framework may be applied using a locally governed source-to-canonical mapping and data-quality/adjudication plan. This requires separate review of source coverage, timestamp precision, mapping validity, conflict burden, follow-up completeness, and source concordance. No governed patient-level data belong in the public repository.

---

# 3. Results

## 3.1 Synthetic truth-set coverage

Report six synthetic therapy episodes covering routine recovery, prolonged routine care, intermediate and intensive escalation/de-escalation, acute-care return, and unresolved location conflict. Make clear these cases were selected for methodological coverage rather than representativeness.

**Insert:** Table 2.

## 3.2 Reconstruction fidelity

Report exact interval and transition agreement from the generated reconstruction-validation artifact.

Suggested wording after final output generation:

> The reconstruction implementation reproduced all prespecified interval signatures and transition signatures across the six core synthetic fixtures, corresponding to an exact-agreement fraction of 1.00 for both validation domains.

Also state that duplicate same-state records did not generate false transitions, adjacent intervals respected shared half-open boundaries, and equal-priority canonical disagreement produced explicit `unknown` rather than an arbitrary state.

**Insert:** Table 3.

## 3.3 Metric validation

Report exact expected-value agreement for all prespecified Phase 4 metrics across the six fixtures. Emphasize the corrected post-infusion clipping rule: negative-time continuity records contribute to reconstruction context but not primary utilization totals.

Include examples only if useful, such as routine recovery totaling 98 post-infusion inpatient hours rather than 100 source-encounter hours, and intensive-care escalation totaling 76 post-infusion inpatient hours with 12 intensive-care hours.

## 3.4 Representative trajectories

Describe the patterns shown in Figure 2 without implying clinical frequency.

Suggested structure:

- routine recovery: uninterrupted routine inpatient care followed by discharge;
- transient escalation: routine -> intermediate -> routine -> discharge;
- intensive escalation/return: routine -> intensive -> routine -> discharge -> emergency return;
- conflict: observed routine care interrupted by an explicit unknown interval caused by equal-priority disagreement.

## 3.5 Synthetic utilization characterization

Populate this section from `phase5_cohort_summary.json` after generation. Report total N=6 and metric-specific available denominators. Numeric summaries should be framed as demonstrations of analytic behavior only.

**Insert:** Table 4 and Figure 3.

## 3.6 Missingness and uncertainty

Populate from `phase5_uncertainty_summary.json`. Report the number of episodes containing uncertainty/unknown state and counts of metric statuses. Explain that unknown-state hours can be directly measured when bounded even when state-attributed inpatient duration is not calculable.

**Insert:** Table 5.

## 3.7 Reproducibility

Report the CI run corresponding to the final frozen Phase 5 output generator and state that the full automated suite passed on supported Python versions. Do not cite a run until the relevant final head has completed successfully.

---

# 4. Discussion

## 4.1 Principal methodological finding

Frame the primary result as demonstration that longitudinal source-like encounter and location records can be transformed through explicit staging, deterministic temporal reconstruction, and validation into auditable patient-level care-state trajectories suitable for descriptive utilization analysis.

## 4.2 Why the structuring layer matters

Discuss preservation of source evidence, deterministic mapping, explicit interval semantics, provenance, and uncertainty as scientific design choices. Emphasize that unreported preprocessing decisions could materially alter duration, transition, and return-care measures.

## 4.3 Validation interpretation

Distinguish computational correctness from clinical validity. Synthetic truth-set agreement demonstrates fidelity to the specification. It does not demonstrate that every future institutional source label is mapped correctly or that the framework captures all clinically meaningful aspects of care.

## 4.4 Analytic implications

Discuss how treatment-relative trajectories support transparent characterization of duration, escalation/de-escalation, discharge, and return care. Avoid claims of causal inference, severity grading, staffing prediction, or capacity forecasting.

## 4.5 Missingness and uncertainty as outputs

Highlight the design choice to expose `unknown`, `not_calculable`, and `incomplete_followup` rather than coercing them to zero or silently excluding episodes.

## 4.6 Strengths

Potential strengths:

- explicit source-to-analysis traceability;
- deterministic and versioned logic;
- prespecified synthetic oracle;
- exact expected-value testing;
- interval and transition provenance;
- explicit uncertainty and follow-up semantics;
- reproducible public synthetic implementation;
- compatibility with heterogeneous source systems without requiring one interoperability standard.

## 4.7 Limitations

Required limitations:

- synthetic validation does not establish external clinical validity;
- care location is not equivalent to physiologic severity or toxicity grade;
- source completeness and timestamp precision may differ across institutions;
- local mapping requires governed review;
- unresolved source conflicts can limit metric calculability;
- 30-day post-discharge outcomes may require observation beyond Day +30 from infusion;
- the framework is retrospective/descriptive and does not provide clinical decision support;
- small synthetic fixtures cannot estimate real-world incidence or resource utilization.

## 4.8 Governed clinical-data transfer

Describe governed real-data application as the next empirical test: assess local mapping coverage, temporal completeness, source concordance, reconstructability status, metric availability, and discrepancies requiring adjudication.

---

# 5. Conclusion scaffold

CART-TRACE provides a formal, deterministic approach for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into treatment-relative care-state intervals, transitions, and versioned utilization measures. The synthetic validation framework establishes reproducibility and exact fidelity to prespecified trajectory and metric oracles while preserving missingness, uncertainty, follow-up sufficiency, and source provenance. The next empirical step is governed application to real hospital data to evaluate source concordance and transportability without changing the frozen core method.

---

# Required main-text output order

1. Figure 1 — data structuring and validation architecture.
2. Table 1 — canonical model and deterministic rules.
3. Table 2 — synthetic truth-set classes.
4. Figure 2 — representative patient trajectories.
5. Table 3 — reconstruction and metric validation.
6. Table 4 — synthetic cohort utilization summary.
7. Figure 3 — utilization and availability visualization.
8. Table 5 — uncertainty/missingness summary.

The final manuscript should pull numeric values from generated machine-readable Phase 5 outputs and should not manually maintain duplicated numeric results.
