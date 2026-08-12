# CART-TRACE research plan

## Phase 0 — scaffold and governance

- establish canonical event and treatment-anchor schemas;
- define institutional boundary and non-clinical-use statement;
- establish endpoint dictionary structure;
- add contribution, licensing, security, and data-governance documents;
- require provenance for all derived features.

**Exit criterion:** package installs, tests pass, synthetic examples run, and governance boundaries are explicit.

## Phase 1 — synthetic longitudinal benchmark

Create a fully synthetic cohort centered on infusion Day 0 with:

- disease and product metadata;
- leukapheresis, lymphodepletion, infusion, encounter, medication, and response events;
- irregular labs and vitals;
- synthetic adjudicated CRS and ICANS outcomes;
- follow-up and survival fields;
- known missingness, duplicate events, and unit errors for QA testing.

**Primary artifact:** a deterministic benchmark dataset generator plus validation report.

## Phase 2 — trajectory engine

Implement research features with explicit window definitions:

- patient-specific baseline;
- absolute and standardized deviation from baseline;
- slopes and rolling change;
- peak and time-to-peak;
- cumulative abnormal burden;
- recovery slope/time;
- change-point candidates;
- observation density and missingness features.

All features should carry source IDs and transformation parameters.

## Phase 3 — statistical methods

Demonstrate:

- descriptive trajectory summaries;
- mixed-effects models;
- time-to-event analyses;
- competing-risk approaches when scientifically justified;
- landmark analyses;
- bootstrap uncertainty;
- temporal validation;
- calibration and subgroup evaluation for any candidate prediction model.

Prediction is deliberately deferred until the data and endpoint layers are stable.

## Phase 4 — interoperability

Build synthetic adapters for selected FHIR resources:

- Patient
- Observation
- Condition
- Procedure
- Encounter
- MedicationAdministration
- DiagnosticReport

Map these resources into the canonical CART-TRACE event representation while retaining source references.

## Phase 5 — patient-generated health data

Add wearable/PGHD support for research streams such as:

- heart rate;
- temperature;
- oxygen saturation;
- respiratory rate;
- activity/motion;
- sleep or recovery proxies where scientifically defensible.

Core engineering requirements: non-wear detection, missing-interval representation, sampling metadata, resampling policy, artifact flags, and source-device provenance.

## Phase 6 — public-health/access layer

Use public or synthetic geographic data to study access to cellular therapy:

- travel distance/time;
- rurality;
- regional availability;
- follow-up burden;
- community/outpatient treatment pathways.

Keep population-access analyses separate from individual clinical outcome models unless a formal research protocol justifies integration.

## Phase 7 — external research application

Only after formal authorization, create a separate application layer for institution-specific research. Requirements should include:

- approved protocol and data-use scope;
- endpoint definitions;
- minimum-necessary data specification;
- versioned cohort logic;
- reproducible analysis plan;
- audit/provenance output;
- clear distinction between exploratory research and clinical decision support.

## Portfolio success criteria

CART-TRACE should eventually provide inspectable evidence of proficiency in:

Python, SQL, clinical data engineering, FHIR concepts, longitudinal statistics, survival analysis, signal processing, patient-specific analytics, data-quality engineering, provenance, reproducibility, testing, CI, technical documentation, and translational research design.
