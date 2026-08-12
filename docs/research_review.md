# CART-TRACE initial research review

_Last reviewed: 2026-08-12_

## Scope

This review supports the architecture of CART-TRACE as a **research and methods platform** for longitudinal CAR T-cell data. It is not a clinical protocol, bedside monitoring system, or treatment recommendation engine.

## 1. Why CAR T-cell therapy is a strong longitudinal-data domain

CAR T-cell therapy is inherently temporal. Patient care and research commonly span leukapheresis, manufacturing/bridging, lymphodepletion, infusion, acute monitoring, early recovery, response assessment, and longer-term follow-up. A Day-0 infusion anchor therefore provides a useful analytical frame, provided original timestamps and treatment context are preserved.

The National Cancer Institute describes CAR T-cell therapy as a form of T-cell transfer therapy in which a patient's T cells are collected, genetically modified to recognize cancer targets, expanded, and returned to the patient. Dartmouth Cancer Center describes the same treatment pathway and notes post-infusion monitoring for side effects and response.

## 2. Toxicity endpoints require explicit definitions

Two major research outcomes are cytokine release syndrome (CRS) and immune effector cell-associated neurotoxicity syndrome (ICANS). NCI materials describe CRS as a potentially severe inflammatory syndrome after CAR T-cell therapy and ICANS as a neurological toxicity syndrome. These are not interchangeable outcomes and should be represented separately in the data model.

For CART-TRACE, toxicity grades should never be inferred from a single biomarker or vital sign unless a study protocol explicitly defines that derivation. The repository should support storing:

- adjudicated CRS grade and onset/resolution times;
- adjudicated ICANS grade and onset/resolution times;
- the source grading system/version;
- fever, blood pressure, oxygen support, neurologic assessment, medication, and encounter events as separate observations;
- uncertainty or missingness in endpoint ascertainment.

## 3. Longitudinal biomarkers are scientifically plausible but should not be overclaimed

Published work has shown that severe CRS has distinct clinical and biomarker kinetics and that longitudinal cytokine and immune-cell measurements can characterize inflammatory trajectories after CAR T-cell therapy. More recent work in multiple myeloma has examined longitudinal cytokine profiles and circulating immune-cell transcriptional states around CRS.

This supports a CART-TRACE feature layer for slopes, peaks, time-to-peak, cumulative burden, recovery, change points, and patient-specific deviation from baseline. It does **not** by itself establish that any such feature is clinically predictive in a new population.

## 4. Wearables and patient-generated data are a high-value research extension

A recent prospective pilot in patients receiving CAR T-cell therapy for multiple myeloma evaluated wearable monitoring of temperature, oxygen saturation, respiratory rate, heart rate, and motion alongside cytokine profiling for CRS detection. This makes patient-generated health data a particularly relevant extension for the portfolio.

CART-TRACE should therefore treat wearable data as a separate provenance class with explicit handling of:

- device/source identity;
- sampling frequency;
- missing intervals and non-wear;
- calibration and unit normalization;
- resampling policy;
- artifact flags;
- alignment to clinical observations and infusion Day 0.

## 5. Current regulatory context matters

FDA eliminated the REMS requirements for the currently approved autologous CD19- and BCMA-directed CAR T-cell products in June 2025, while product labeling continues to communicate risks including CRS and neurologic toxicities. CART-TRACE documentation should therefore avoid reproducing stale operational assumptions tied to the former REMS structure.

## 6. Dartmouth context creates a legitimate translational frame

Dartmouth Cancer Center operates a CAR T-cell program within its Transplant and Cellular Therapy Program. Dartmouth describes active work in immunology and cancer immunotherapy, including CAR engineering, and has reported expansion of outpatient CAR T-cell care and efforts to improve access for rural patients.

That creates several academically coherent research directions for an eventual formally authorized Dartmouth application:

1. longitudinal toxicity and recovery trajectories;
2. outpatient monitoring and patient-generated data;
3. treatment-response and persistence analyses;
4. reproducible cohort construction across clinical data sources;
5. rural access, travel burden, and follow-up geography;
6. integration of clinical, immune, and patient-generated measurements.

The open-source CART-TRACE repository should remain institutionally neutral. Any Dartmouth-specific study, data use, or institutional endorsement should be represented separately and only after formal authorization.

## 7. Recommended first scientific benchmark

The first benchmark should be a synthetic longitudinal cohort rather than a predictive model. The benchmark should include:

- treatment anchors and disease/product metadata;
- irregularly sampled labs and vitals;
- adjudicated synthetic CRS/ICANS events;
- medication and encounter events;
- response and survival outcomes;
- optional wearable streams;
- known missingness and injected data-quality defects.

Primary methods demonstrations:

- deterministic Day-0 alignment;
- source-preserving provenance;
- baseline and change-from-baseline features;
- trajectory summaries and uncertainty;
- explicit endpoint dictionaries;
- mixed-effects and survival-analysis examples;
- calibration/evaluation framework for any later candidate prediction model.

## 8. Research safeguards

Before any human-subject application, the project should add explicit documentation for IRB/governance boundaries, HIPAA-safe data handling, minimum-necessary fields, data retention, access control, auditability, and separation of exploratory research outputs from clinical decision support.

## Sources reviewed

- National Cancer Institute. "CAR T Cells: Engineering Immune Cells to Treat Cancer." https://www.cancer.gov/about-cancer/treatment/research/car-t-cells
- National Cancer Institute. "T-cell Transfer Therapy." https://www.cancer.gov/about-cancer/treatment/types/immunotherapy/t-cell-transfer-therapy
- U.S. Food and Drug Administration. "FDA Eliminates Risk Evaluation and Mitigation Strategies (REMS) for Autologous Chimeric Antigen Receptor (CAR) T cell Immunotherapies." June 26, 2025. https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/fda-eliminates-risk-evaluation-and-mitigation-strategies-rems-autologous-chimeric-antigen-receptor
- Hay KA, et al. "Kinetics and biomarkers of severe cytokine release syndrome after CD19 chimeric antigen receptor-modified T-cell therapy." Blood. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5701525/
- "Neutrophil activation and clonal CAR-T re-expansion underpinning cytokine release syndrome during ciltacabtagene autoleucel therapy in multiple myeloma." https://pmc.ncbi.nlm.nih.gov/articles/PMC10774397/
- "Detection of cytokine release syndrome using wearables and cytokine profiling following CAR-T therapy for myeloma." https://pmc.ncbi.nlm.nih.gov/articles/PMC13313484/
- Dartmouth Cancer Center. "CAR T-Cell Therapy." https://cancer.dartmouth.edu/blood-marrow/car-t-cell-therapy
- Dartmouth Cancer Center. "Immunology & Cancer Immunotherapy." https://cancer.dartmouth.edu/scientists-researchers/immunology-cancer-immunotherapy
- Dartmouth Cancer Center. "Enhancing Community Access to Cancer Clinical Trials and Care." https://cancer.dartmouth.edu/stories/article/enhancing-community-access-cancer-clinical-trials-and-care

## Review status

This is a portfolio-oriented literature and architecture review, not a systematic review. The next research-review pass should add ASTCT consensus endpoint definitions, product-specific labeling, FHIR/OMOP representation choices, and a structured evidence table with study design, cohort, exposure, outcome, time axis, and limitations.
