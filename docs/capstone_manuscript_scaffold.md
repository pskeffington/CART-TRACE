# CART-TRACE Capstone Manuscript Scaffold

## Working title

**CART-TRACE: Reconstructing Hospital Care Trajectories Following CAR T-Cell Therapy from Longitudinal Clinical Data**

## Abstract scaffold

### Background

CAR T-cell therapy is followed by a time-dependent period of acute-care utilization in which patients may move among routine inpatient care, intermediate care, intensive care, discharge, and subsequent emergency or inpatient encounters. In longitudinal hospital data, these changes may be distributed across encounter, location, admission/discharge, and transfer records rather than represented as a single coherent trajectory.

### Objective

Develop and validate a reproducible method for transforming heterogeneous longitudinal hospital records surrounding CAR T-cell infusion into treatment-relative patient-level care-state trajectories that support transparent descriptive characterization of hospital utilization during the first 30 days after infusion.

### Methods

CART-TRACE uses a layered transformation architecture: source clinical records -> staging representation -> canonical trajectory representation -> validation -> analytic representation. Episodes are anchored to infusion at 0 hours. Canonical intervals use continuous treatment-relative time and half-open `[start,end)` semantics. A small institution-independent vocabulary represents `outpatient`, `emergency`, `routine_inpatient`, `intermediate_care`, `intensive_care`, `discharged`, and `unknown`. Deterministic overlap, conflict, and transition rules are validated against a prespecified six-episode synthetic truth set. Post-infusion utilization metrics are calculated within `[0,720)` hours with explicit zero, missingness, uncertainty, follow-up, and provenance semantics.

### Results

Synthetic validation should report exact reconstruction agreement, exact metric agreement, uncertainty behavior, and descriptive results from the six-episode demonstration cohort. These results demonstrate computational fidelity and reproducibility rather than external clinical validity.

### Conclusions

The final conclusion should state whether the method provides an auditable and reproducible representation of post-CAR-T hospital trajectories suitable for descriptive utilization analysis, while distinguishing synthetic validation from future governed-data validation.

---

# 1. Introduction

## 1.1 Clinical and data context

Describe the post-infusion hospital episode as a longitudinal sequence rather than a collection of isolated encounters. Establish why encounter counts alone do not preserve timing, escalation, de-escalation, discharge, return, or uncertainty.

## 1.2 Health-data problem

Frame the central technical problem as structuring heterogeneous longitudinal records into a coherent, treatment-relative representation while preserving provenance and ambiguity.

## 1.3 Gap

Emphasize the need for a transparent, deterministic, testable representation that separates source evidence, transformation logic, validation, and analysis. Avoid claims that existing standards or EHR extracts automatically provide this representation.

## 1.4 Objective and questions

Primary question:

> Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?

Secondary descriptive question:

> What patterns of acute-care utilization, escalation, de-escalation, discharge, and early return are observed in the reconstructed trajectories?

State explicitly that prediction, eligibility adjudication, treatment recommendation, and prospective decision support are outside scope.

---

# 2. Methods

## 2.1 Study design

Describe CART-TRACE as a retrospective, synthetic-first health-data methods study. The primary methodological contribution is deterministic clinical-data structuring, temporal reconstruction, and validation. Hospital-utilization characterization is the applied demonstration.

## 2.2 Unit of analysis and treatment anchor

The primary unit is the CAR T-cell therapy episode. Infusion defines relative time 0. Continuous relative hours are calculated from timestamp differences without flooring negative values.

Primary utilization window:

`[0,720)` hours after infusion.

Limited negative-time context may be retained to establish encounter continuity but is excluded from primary post-infusion utilization totals.

## 2.3 Clinical-data structuring architecture

Describe the five layers:

1. source clinical data;
2. staging representation;
3. canonical trajectory representation;
4. validation and review;
5. analytic representation.

Reference the formal framework in `docs/clinical_data_structuring_framework.md`.

## 2.4 Source-level representation

Describe candidate source domains: encounter start/end, admission/discharge, location history, emergency encounters, transfer/location-change records, infusion timestamp, source encounter type, and disposition when available.

State that source labels, timestamps, record identifiers, and provenance are preserved rather than overwritten.

## 2.5 Staging and normalization

Document offset-aware timestamp normalization, stable record ordering, continuous relative time, preserved source vocabulary, versioned mapping metadata, precedence rules, and source identifiers.

Clarify that staging does not itself assert the final care state.

## 2.6 Canonical trajectory model

Canonical states:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

Canonical transitions:

- `admission`
- `transfer`
- `escalation`
- `deescalation`
- `discharge`
- `acute_care_return`
- `other`
- `unknown`

`acute_care_return` is a transition, not a state.

Intervals use `[start,end)` semantics. Shared boundaries are allowed without overlap. Equal-priority disagreement between incompatible canonical states resolves to `unknown` with explicit uncertainty rather than silent selection.

## 2.7 Deterministic reconstruction

Describe the reconstruction sequence: parse -> normalize -> map -> stable sort -> resolve overlap/conflict -> derive intervals -> derive transitions -> preserve provenance -> serialize deterministically.

State that Phase 3 semantics were frozen only after exact agreement with the prespecified synthetic interval and transition oracle.

## 2.8 Synthetic truth set

Describe the six representative trajectory classes:

1. routine recovery;
2. prolonged routine inpatient care;
3. transient intermediate-care escalation/de-escalation;
4. intensive-care escalation/de-escalation;
5. discharge followed by early acute-care return;
6. conflicting location evidence producing explicit `unknown`.

Also summarize boundary/error cases: malformed or missing anchors, reversed intervals, duplicate same-state inputs, open end time, study-window boundary, adjacent intervals, equal-priority conflict, and same-day return.

## 2.9 Validation framework

Separate validation dimensions:

- structural conformance;
- completeness for intended use;
- temporal plausibility;
- semantic validity;
- reconstruction fidelity;
- reproducibility;
- analytic fitness.

Explicitly distinguish schema validity, reconstruction fidelity, and clinical validity.

## 2.10 Utilization metrics

Primary metric definitions are versioned and frozen. Report:

- total inpatient hours;
- routine inpatient hours;
- intermediate-care hours;
- intensive-care hours;
- high-acuity hours = intermediate + intensive care;
- transition count;
- time to first escalation;
- time to discharge;
- 7-day post-discharge acute-care return;
- 30-day post-discharge acute-care return;
- unknown-state hours.

Emergency time is not included in inpatient duration.

## 2.11 Missingness, uncertainty, and follow-up

Metric status values:

- `observed`;
- `observed_zero`;
- `not_applicable`;
- `not_calculable`;
- `incomplete_followup`.

Unknown-state intervals are quantified directly. State-attributed duration is not silently imputed through unresolved unknown intervals when the ambiguity could change the metric.

For acute-care return, an observed qualifying return establishes a positive result immediately. A negative result requires complete ascertainment through the full requested horizon after discharge.

## 2.12 Provenance and reproducibility

Describe source-record propagation through intervals, transitions, metric results, and reporting outputs. State that the expected evidence chain is:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output -> table/figure`

Report versioned schemas, deterministic serialization, synthetic fixtures, automated tests, and CI as reproducibility controls.

## 2.13 Governed-data extension

If approved hospital data are available, describe local source mapping, data-quality review, reconstructability status, source-concordance validation, and adjudication as a separate governed application. Do not mix synthetic validation findings with institutional clinical findings.

---

# 3. Results Scaffold

## 3.1 Synthetic cohort description

State that the demonstration cohort consists of six prespecified synthetic therapy episodes designed to exercise distinct trajectory and uncertainty patterns. Do not present the synthetic cohort as epidemiologically representative.

Suggested first paragraph:

> The synthetic demonstration cohort contained six prespecified CAR T-cell therapy episodes representing routine recovery, prolonged routine hospitalization, intermediate-care escalation, intensive-care escalation, early acute-care return, and conflicting location evidence. The cohort was constructed to test the behavior of the reconstruction and metric algorithms rather than to estimate clinical incidence or prevalence.

## 3.2 Reconstruction fidelity

Report exact interval-signature and transition-signature agreement across all six fixtures. Refer to the generated reconstruction-validation artifact.

Suggested wording when the generated artifact remains at 1.0 agreement:

> Reconstructed care-state intervals and transitions showed exact agreement with the prespecified synthetic oracle across all six trajectory classes. This establishes deterministic computational fidelity to the test specification but does not establish external clinical validity.

## 3.3 Metric validation

Report whether all expected metric values exactly matched generated Phase 4 values. Present metric availability/status separately from numeric agreement.

## 3.4 Patient-level trajectory examples

Show representative treatment-relative trajectories. At minimum include:

- routine recovery;
- intermediate-care escalation/de-escalation;
- intensive-care escalation followed by early return;
- conflict-to-unknown episode.

Describe sequence and timing without interpreting care location as a direct toxicity grade.

## 3.5 Synthetic utilization characterization

Use denominator-aware summaries from generated metric-result objects. Report numeric means/medians only among results with status `observed` or `observed_zero`. Report unavailable and incomplete-follow-up counts alongside numeric summaries.

Do not infer population-level utilization estimates from six deliberately constructed fixtures.

## 3.6 Missingness and uncertainty

Report the number of episodes containing `unknown` or uncertain intervals, unknown-state hours, and counts of `not_calculable` and `incomplete_followup` metric statuses.

Use the conflict fixture to demonstrate why known-state duration and total state-attributed duration are not equivalent when source evidence is contradictory.

## 3.7 Reproducibility result

Report the successful automated test/CI result associated with the final manuscript-output implementation. The final manuscript should cite the most recent relevant passing run, not an earlier development run.

---

# 4. Discussion Scaffold

## 4.1 Principal methodological finding

Discuss whether heterogeneous source-like longitudinal records can be transformed into an auditable treatment-relative trajectory through explicit staging, canonicalization, conflict handling, validation, and provenance.

## 4.2 Why the structuring step matters

Explain that longitudinal data structuring is part of the scientific method because analytic results depend on decisions about temporal boundaries, location semantics, conflict resolution, uncertainty, and follow-up.

## 4.3 Interpretability and auditability

Discuss the value of small canonical vocabularies, source-value preservation, explicit `unknown`, deterministic transformation, and traceability to source records.

## 4.4 Fit-for-purpose validation

Emphasize that schema conformance is necessary but insufficient. Synthetic truth sets establish computational behavior; future governed data are needed to evaluate source-system transfer and clinical concordance.

## 4.5 Applied hospital-utilization relevance

Discuss how reconstructed trajectories support descriptive measures of duration, escalation/de-escalation, discharge, and acute-care return. Avoid capacity-planning or operational-performance claims unless later data specifically support them.

## 4.6 Limitations

Required limitations:

- synthetic fixtures are deliberately constructed and not representative of real-world frequency distributions;
- care location is an operational state and should not be treated as a direct toxicity-severity measure;
- institutional mapping may vary;
- source-record completeness and timestamp precision may differ in real data;
- 30-day post-discharge return may require observation beyond Day +30 from infusion;
- unresolved source conflict can make individual metrics non-calculable;
- synthetic validation demonstrates specification fidelity, not external clinical validity;
- governed clinical-data validation is approval- and access-dependent.

## 4.7 Future work

Prioritize governed retrospective validation, local source mapping, reconstructability assessment, and descriptive application to a real cohort. Prediction, prospective decision support, eligibility gating, and treatment recommendation remain outside the current capstone contribution.

---

# 5. Conclusion Scaffold

The conclusion should remain narrow:

> CART-TRACE specifies a reproducible framework for converting longitudinal hospital encounter and location records surrounding CAR T-cell infusion into treatment-relative care-state trajectories with explicit provenance, uncertainty, and validation. Synthetic truth-set testing demonstrates deterministic reconstruction and metric behavior. The framework provides a defensible basis for descriptive post-infusion hospital-utilization analysis, while transfer to governed clinical data requires institution-specific mapping and source-concordance validation.

---

# Reproducible manuscript inputs

The manuscript-facing analysis should be generated from these controlled artifacts rather than manually transcribed values:

- `examples/outputs/phase5_patient_trajectories.json`
- `examples/outputs/phase5_metric_results.json`
- `examples/outputs/phase5_cohort_summary.json`
- `examples/outputs/phase5_metric_validation.json`
- `examples/outputs/phase5_reconstruction_validation.json`
- `examples/outputs/phase5_uncertainty_summary.json`

These are generated by `scripts/generate_phase5_outputs.py` from the frozen synthetic fixtures and current reconstruction/metric implementations.
