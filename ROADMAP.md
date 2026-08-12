# CART-TRACE Roadmap

## Research purpose

CART-TRACE is a research-oriented framework for transforming heterogeneous longitudinal data into reproducible patient-level trajectories around CAR T-cell and cellular immunotherapy. The repository is intentionally non-clinical and non-operational: it is designed for retrospective research, methods development, reproducible analysis, and future protocol design rather than bedside decision-making.

The near-term design assumption is an academic health system preparing for greater inpatient capacity, higher-acuity care, and increasingly integrated cancer and cellular-therapy services. CART-TRACE should therefore answer hospital-relevant research questions while remaining portable, privacy-conscious, and suitable for synthetic or properly governed de-identified data.

## Hospital-centered research questions

1. **Patient trajectory:** What happens from referral and collection through infusion, acute toxicity, discharge, recovery, response, and longer-term follow-up?
2. **Capacity and utilization:** Which portions of a CAR T episode drive inpatient days, ICU transfer, emergency care, readmission, or prolonged monitoring?
3. **Toxicity and recovery:** How do CRS, ICANS, cytopenias, infections, organ dysfunction, and functional recovery evolve over time?
4. **Manufacturing-to-outcome linkage:** How can CMC and product attributes be represented alongside clinical outcomes without conflating product quality research with clinical decision support?
5. **Rural access:** How do travel distance, referral timing, local monitoring, telehealth, and transitions back to regional care affect the treatment pathway?
6. **Data continuity:** Which clinically meaningful signals are lost when patients move between outpatient oncology, inpatient units, ICU-level care, home monitoring, and regional facilities?
7. **Reproducibility:** Can a patient-level trajectory be reconstructed from source data with explicit provenance, definitions, missingness, and versioned transformations?

## Core longitudinal episode model

CART-TRACE should organize research data around a treatment episode rather than a single encounter.

`referral -> eligibility/workup -> leukapheresis -> manufacturing interval -> lymphodepletion -> infusion -> acute monitoring -> toxicity/recovery -> discharge -> early follow-up -> response -> survivorship/relapse`

Each phase should support four linked data layers:

- **Clinical:** diagnoses, labs, medications, vitals, procedures, adverse events, encounters, disease response.
- **Product / CMC:** collection characteristics, manufacturing milestones, release attributes, cell dose, viability, potency or other available product-level variables.
- **Patient-generated:** symptoms, wearable/device measurements, home observations, patient-reported outcomes, where available and governed.
- **System:** care location, level of care, transfer, length of stay, readmission, travel/access measures, telehealth, and regional handoffs.

## Phased development

### Phase 0 - Research foundation

**Goal:** establish a credible, reproducible, non-operational research scaffold.

Deliverables:
- repository scope and governance statement;
- explicit synthetic/de-identified-data policy;
- canonical CAR T episode timeline;
- data dictionary template;
- provenance and missingness conventions;
- reproducible environment and tests;
- literature and regulatory source registry.

Exit criteria:
- no PHI or production credentials in the repository;
- one synthetic patient can be represented end-to-end;
- every derived variable has a documented definition and provenance field.

### Phase 1 - Common data model

**Goal:** create a patient-episode schema capable of joining clinical, product, and system data.

Minimum entities:
- `patient`
- `therapy_episode`
- `encounter`
- `observation`
- `laboratory_result`
- `medication_exposure`
- `toxicity_event`
- `disease_response`
- `cell_product`
- `manufacturing_event`
- `patient_generated_observation`
- `care_transition`
- `provenance`

Design requirements:
- timestamp plus treatment-relative time (`day 0 = infusion`);
- source-system and transformation provenance;
- explicit units and reference ranges;
- missingness reason where known;
- support for multiple CAR T episodes per patient;
- no assumption that a variable is clinically actionable merely because it is available.

Exit criteria:
- validated synthetic fixtures for typical and complicated treatment courses;
- schema validation tests;
- deterministic conversion from raw synthetic inputs to canonical tables.

### Phase 2 - Trajectory reconstruction

**Goal:** turn event tables into research-grade longitudinal trajectories.

Initial features:
- treatment-relative timeline;
- daily laboratory and vital summaries with raw-value traceability;
- CRS and ICANS event windows as recorded/abstracted, not algorithmically diagnosed;
- care-location trajectory (outpatient, inpatient, ICU-level care, home/regional follow-up);
- discharge and readmission windows;
- missing-data visualization;
- manufacturing interval and product release milestones.

Primary outputs:
- machine-readable trajectory tables;
- patient-level research timeline plots;
- cohort-level episode summaries;
- provenance report for every generated trajectory.

### Phase 3 - Hospital operations research layer

**Goal:** study service needs associated with cellular therapy without building an operational command system.

Research measures:
- inpatient days per episode;
- ICU transfer and ICU days;
- time from referral to collection and infusion;
- discharge destination;
- 7/30/90-day acute-care utilization;
- unplanned readmissions;
- outpatient visit burden;
- regional-to-tertiary care transitions;
- travel burden and rural access proxies;
- monitoring intensity by treatment-relative day.

Hospital-facing questions:
- when in the CAR T timeline is high-acuity capacity most frequently required?
- which transitions create fragmented data or duplicated work?
- what monitoring could plausibly occur closer to home and which questions require prospective study?
- which data should follow the patient across physical care settings?

Exit criteria:
- reproducible cohort reports using synthetic or governed research data;
- analyses clearly separated from real-time operational recommendations.

### Phase 4 - CMC-to-clinical research linkage

**Goal:** provide a structured research interface between cell-product characteristics and longitudinal outcomes.

Candidate variables, subject to availability and governance:
- collection cell counts/characteristics;
- manufacturing duration and milestones;
- final viable cell dose;
- viability;
- CAR expression/transduction measures;
- vector-related characterization where available;
- phenotype/composition measures;
- release/potency assay outputs;
- out-of-specification or exception flags represented only through approved research fields.

Candidate outcomes:
- expansion/persistence measurements where available;
- CRS and ICANS burden;
- cytopenia and infection trajectories;
- hospital/ICU utilization;
- response depth and timing;
- relapse and survival endpoints.

Guardrail: CART-TRACE should support association, characterization, and hypothesis generation. It should not infer product release suitability or recommend treatment from research correlations.

### Phase 5 - Patient-generated signals and recovery

**Goal:** study the interval between conventional encounters.

Potential research inputs:
- patient-reported symptoms;
- temperature and heart rate;
- activity/sleep summaries;
- blood pressure or oxygen saturation when clinically collected;
- validated device outputs;
- care-team contacts and escalation events.

Research priorities:
- signal quality and missingness;
- adherence and acceptability;
- concordance with clinical events;
- recovery phenotypes after discharge;
- feasibility of rural/home follow-up models.

Any prospective collection belongs behind IRB, privacy, security, device-validation, and clinical-governance review.

### Phase 6 - Prospective translational studies

**Goal:** use findings from earlier phases to formulate testable prospective protocols.

Examples:
- feasibility study of longitudinal post-infusion patient-generated data;
- prospective characterization of recovery trajectories;
- study of rural transitions and local follow-up after cellular therapy;
- validation of specific trajectory features against prespecified outcomes;
- implementation-science study of data continuity across new and existing care environments.

This phase should produce protocols and evidence, not autonomous clinical decision support.

## Research architecture principles

- **Patient-level first:** preserve the individual trajectory before cohort aggregation.
- **Time-relative:** align events to clinically meaningful anchors, especially infusion day.
- **Source-preserving:** derived data must be traceable to original research inputs.
- **FHIR/OMOP aware, not dependent:** map where useful, but keep the research model understandable on its own.
- **Synthetic-first development:** examples and tests should run without institutional data.
- **Privacy by design:** no PHI, secrets, or identifying free text in the public repository.
- **Reproducibility over prediction:** definitions, provenance, validation, and rerunnable pipelines precede modeling.
- **No bedside claims:** research outputs must not be presented as clinical alarms, diagnoses, or treatment recommendations.

## Suggested repository structure

```text
CART-TRACE/
  README.md
  ROADMAP.md
  docs/
    data_dictionary.md
    governance.md
    episode_model.md
    hospital_questions.md
  schemas/
    patient.schema.json
    therapy_episode.schema.json
    observation.schema.json
    cell_product.schema.json
  src/cart_trace/
    ingest/
    normalize/
    timeline/
    phenotypes/
    provenance/
    reports/
  tests/
  examples/
    synthetic/
  notebooks/
    01_episode_reconstruction.ipynb
    02_utilization_trajectories.ipynb
    03_cmc_outcomes.ipynb
```

## Initial success metrics

CART-TRACE should be considered useful when it can reproducibly answer, from appropriately governed research data:

1. Where was the patient in the treatment pathway on any treatment-relative day?
2. What clinical, product, and patient-generated measurements were available at that point?
3. Which toxicities, responses, and utilization events occurred, and when?
4. What data are missing, and is the reason for missingness represented?
5. Can every plotted or modeled feature be traced to a source field and transformation?
6. Can researchers compare cohorts without losing the underlying patient-level sequence?

## Near-term build order

1. Governance and synthetic-data policy.
2. Episode/time model.
3. Core schema and data dictionary.
4. Synthetic CAR T cohort generator/fixtures.
5. Timeline reconstruction library.
6. Utilization and care-transition metrics.
7. CMC/product linkage schema.
8. Patient-generated signal interface.
9. Reproducible cohort reporting.
10. Prospective-study protocol templates.
