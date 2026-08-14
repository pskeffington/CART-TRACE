# CART-TRACE Final Public Capstone Manuscript Scaffold

## Status

Final public scholarly scaffold for the frozen synthetic CART-TRACE package. Synthetic computational findings and methodological-readiness evidence are established. No institutional empirical findings are included in this public version. Governed empirical validation remains a separate approval-dependent extension.

## Working title

**CART-TRACE: Reconstructing Hospital Care Trajectories Following CAR T-Cell Therapy from Longitudinal Clinical Data**

## Abstract

### Background

Longitudinal hospital records surrounding CAR T-cell therapy are distributed across infusion, encounter, admission/discharge, transfer, emergency, and location-history systems. These records do not inherently form a coherent treatment-relative trajectory.

### Objective

To develop and validate a reproducible method for transforming heterogeneous longitudinal hospital records into patient-level level-of-care trajectories during the first 30 days following CAR T-cell infusion.

### Methods

CART-TRACE uses the CAR T-cell therapy episode as the analytic unit and the documented administered infusion timestamp as time zero. Source-like records are normalized into staging objects and transformed into half-open `[start,end)` intervals over seven canonical states: `outpatient`, `emergency`, `routine_inpatient`, `intermediate_care`, `intensive_care`, `discharged`, and `unknown`. Deterministic mapping, precedence, conflict handling, provenance, uncertainty, follow-up sufficiency, and utilization metrics were prespecified. Computational validity was evaluated with a frozen six-case synthetic truth set, negative/boundary cases, automated tests, and reproducible reporting outputs. A governed representation-validation protocol was defined separately for future approved institutional application.

### Results

The synthetic methodological pipeline reproduced the prespecified oracle, generated deterministic trajectories and utilization metrics, and produced a controlled scholarly artifact set through Gate 5. Gate 6 methodological readiness was subsequently passed with documented governance, source-mapping, reconstructability, follow-up, validation/adjudication, disclosure, and pre-analysis controls. No institutional empirical results are included in the frozen public package.

### Conclusions

CART-TRACE demonstrates a transparent and auditable approach to treatment-relative reconstruction of post-CAR-T hospital care trajectories. Synthetic validation establishes computational validity, and Gate 6 establishes methodological readiness for a governed extension. Representation fidelity and descriptive institutional findings require separate approved source-data evaluation.

---

## 1. Introduction

### 1.1 Applied data problem

CAR T-cell therapy creates a temporally dense acute-care episode in which patients may transition among outpatient, emergency, routine inpatient, intermediate, intensive, discharge, and subsequent acute-care settings. The relevant evidence is commonly fragmented across multiple hospital information sources.

The methodological problem is therefore not simply to count encounters. It is to reconstruct a coherent treatment-relative representation while preserving timing, provenance, missingness, uncertainty, and explicit rules for conflicting evidence.

### 1.2 Gap

Conventional encounter-level summaries can obscure sequence, duration, and transition structure. A reproducible patient-level trajectory representation requires explicit state definitions, temporal boundary rules, source-to-canonical mapping, conflict resolution, and metric eligibility criteria.

### 1.3 Objective and questions

Primary question:

> Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?

Secondary descriptive question:

> What patterns of acute-care utilization, escalation, de-escalation, discharge, and early return are observed in the reconstructed trajectories?

The secondary question is contingent on governed data availability and is descriptive rather than predictive or causal.

---

## 2. Methods

### 2.1 Study design and analytic unit

CART-TRACE is a synthetic-first, retrospective, descriptive health-data-science framework. The primary unit is the CAR T-cell therapy episode rather than the encounter or patient lifetime. Each documented qualifying infusion defines a distinct episode.

### 2.2 Treatment-relative time

The administered infusion timestamp is fixed at `0 hours`. The primary analytic window is `[0,720)` hours after infusion. Limited pre-infusion context may be retained only to establish encounter continuity and is excluded from primary post-infusion utilization totals unless a frozen metric states otherwise.

### 2.3 Clinical data structuring framework

The method separates five layers:

`source clinical data -> staging representation -> canonical trajectory representation -> validation/review -> analytic representation`

This separation makes transformations inspectable and prevents analytic results from depending on undocumented preprocessing.

### 2.4 Canonical care-state model

The frozen canonical states are:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` is represented as a transition type rather than a state. Care location is interpreted as a utilization/trajectory variable, not as a direct measure of toxicity or physiologic severity.

### 2.5 Source normalization and mapping

Source records retain their original identifiers, timestamps, source labels, source domains, and provenance. Staging standardizes timestamps, calculates treatment-relative hours, applies stable ordering, and attaches versioned mapping metadata. Institution-specific labels map into the frozen canonical vocabulary under a separate governed local mapping protocol.

### 2.6 Deterministic reconstruction

Reconstruction uses half-open `[start,end)` intervals, deterministic event ordering, prespecified source precedence, duplicate collapse, overlap handling, and explicit `unknown` behavior. Equal-priority irreconcilable evidence resolves to `unknown` rather than being inferred clinically.

### 2.7 Utilization measures

Frozen measures include inpatient and state-specific duration, transition counts and timing, time to first escalation, time to discharge, 7-day acute-care return, 30-day acute-care return, and uncertainty/unknown burden. Every metric defines analytic-window clipping, missing-versus-zero behavior, follow-up sufficiency, and provenance expectations.

### 2.8 Synthetic truth-set validation

The synthetic oracle contains six controlled trajectory classes covering routine recovery, prolonged inpatient care, transient escalation, ICU escalation, early acute-care return, and conflicting/missing location evidence. Additional negative and boundary tests cover duplicates, missing ends, exact 720-hour boundaries, adjacent intervals, same-day return, equal-priority conflict, invalid states, missing infusion anchor, malformed timestamps, and reversed intervals.

Validation requires exact deterministic agreement with expected intervals, transitions, uncertainty behavior, and metric outputs. Repeated generation/rendering must remain reproducible.

### 2.9 Scholarly reporting layer

Controlled reporting generates patient trajectories, metric validation outputs, cohort summaries, uncertainty summaries, validation tables, and figures directly from frozen synthetic sources. Numeric values are not manually maintained when a generated source can provide them.

### 2.10 Governed-data readiness and validation protocol

Gate 6 defines methodological readiness for approved retrospective application. Governed execution, if authorized, requires:

1. approval/data-use authorization and approved users/environment;
2. field-availability review;
3. reviewed/versioned local mapping;
4. prespecified reconstructability classification;
5. metric-specific follow-up sufficiency review;
6. source-concordance validation sample;
7. discrepancy/adjudication logging;
8. disclosure review for any aggregate scholarly output.

These controls do not themselves authorize data use.

### 2.11 Governance and reproducibility

The public repository contains synthetic and generic methodological artifacts only. PHI, institution-specific identifiers, raw governed extracts, restricted mappings, credentials, and patient-level adjudication evidence remain inside approved environments. Any proposed change to frozen states, interval semantics, precedence, reconstruction behavior, metric definitions, follow-up rules, or oracle expectations triggers explicit gate-impact review.

---

## 3. Results

### 3.1 Computational foundation

Gates 1–4 established the canonical model, synthetic oracle, deterministic reconstruction, and utilization metric validity under automated testing. The frozen implementation preserves explicit unknown/missing behavior and source-to-output traceability.

### 3.2 Scholarly prototype

Gate 5 established a complete synthetic scholarly prototype with generated patient trajectories, metric results, cohort summaries, uncertainty summaries, validation matrices, and controlled main/supplementary figures and tables. Reproduction is driven by the project generation and rendering scripts followed by the automated test suite.

### 3.3 Methodological readiness

Gate 6 established a governed-data readiness package covering cohort/anchor specification, source-field inventory, local mapping/versioning, validation/adjudication, public/private boundaries, data-quality profiling, reconstructability, follow-up sufficiency, discrepancy logging, pre-analysis review, execution templates, and aggregate reporting templates.

### 3.4 Governed empirical status

No institutional empirical findings are included in the frozen public CART-TRACE package. Institutional source availability, reconstructability, follow-up sufficiency, source-concordance, and descriptive utilization have not been represented as completed public results.

If governed execution is authorized in the future, those findings should be reported only through the prespecified aggregate templates and only after disclosure review.

---

## 4. Discussion

### 4.1 Principal contribution

The primary contribution of CART-TRACE is a deterministic clinical-data structuring and temporal reconstruction framework rather than a predictive model. It makes the transformation from heterogeneous source-like records to patient-level trajectories inspectable, versioned, and reproducible.

### 4.2 Why the representation matters

The canonical trajectory retains sequence, duration, transitions, provenance, and uncertainty that encounter counts alone can obscure. This creates a defensible analytic substrate for descriptive post-infusion utilization research.

### 4.3 Computational validity versus clinical validity

Synthetic truth-set agreement demonstrates that the implementation behaves as specified. It does not demonstrate that institutional source data are complete, that local mappings are semantically correct, or that reconstructed trajectories are externally clinically valid. Those claims require governed source-concordance evaluation.

### 4.4 Governance as part of the method

CART-TRACE treats source mapping, data fitness, reconstructability, follow-up sufficiency, adjudication, and disclosure boundaries as scientific-method components rather than implementation afterthoughts. This is essential because apparently minor preprocessing choices can alter trajectory and denominator interpretation.

### 4.5 Potential empirical interpretation

If governed data become available, empirical results should be interpreted as descriptive characteristics of hospital utilization conditional on source completeness, reconstructability, and follow-up. The framework is not designed to attribute observed care states to toxicity severity or treatment effects.

### 4.6 Future work

Future work may assess transferability across institutions, compare alternative source systems, or evaluate additional descriptive applications. Prediction, eligibility/readiness adjudication, prospective alerts, and causal inference remain outside the current capstone scope unless explicitly re-scoped.

---

## 5. Limitations

1. Synthetic validation establishes computational correctness under prespecified scenarios but cannot establish external clinical validity.
2. Governed source completeness and semantic mapping may differ from synthetic assumptions.
3. Reconstructability requirements may introduce selection into empirical cohorts.
4. Negative return outcomes depend on complete observation through the relevant horizon.
5. `unknown` and uncertainty can affect state-duration and transition summaries and must remain visible.
6. Level of care is an imperfect utilization representation and is not a direct toxicity/severity measure.
7. Institution-specific mappings may limit transportability despite the institution-independent canonical state model.
8. The frozen public capstone package does not include institutional empirical validation; the governed layer remains a prespecified future validation protocol unless separately authorized and executed.

---

## 6. Reproducibility and governance statement

The public CART-TRACE repository contains the frozen canonical model, synthetic truth set, deterministic reconstruction and metric logic, automated tests, generated synthetic scholarly outputs, governance/data-readiness documentation, and disclosure-safe templates. Governed clinical records, local identifiers, restricted mappings, raw extracts, and patient-level adjudication evidence are excluded from the public repository. All public empirical claims must be traceable to generated synthetic outputs or approved aggregate governed outputs.

---

## 7. Conclusion

CART-TRACE provides a transparent, auditable, and reproducible method for transforming longitudinal hospital records surrounding CAR T-cell infusion into treatment-relative care-state trajectories and transitions. The frozen public package establishes computational validity and methodological readiness for governed application. Institutional representation fidelity and descriptive utilization findings remain a separate approval-dependent empirical question.

---

## Controlled figure/table integration

Main-text artifacts:

- Figure 1 — clinical data structuring architecture
- Figure 2 — representative synthetic trajectories
- Figure 3 — synthetic cohort utilization and metric availability
- Table 1 — canonical model
- Table 2 — synthetic truth set
- Table 3 — validation results
- Table 4 — cohort utilization summary
- Table 5 — uncertainty summary

Supplementary artifacts:

- Figure S1 — all synthetic trajectories
- Table S1 — metric-result matrix
- Table S2 — mapping rules
- Table S3 — boundary/negative-test inventory
- Table S4 — reproducibility artifact inventory

Any future governed empirical tables or figures must be added only after authorization and disclosure review and must remain clearly distinguished from the frozen synthetic artifacts.
