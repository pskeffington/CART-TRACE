# CART-TRACE Roadmap

## Research purpose

CART-TRACE is a synthetic-first, non-operational research framework for reconstructing hospital care trajectories surrounding CAR T-cell therapy.

The current MS HSE thesis is intentionally narrow. The repository should answer one hospital-facing research question well before expanding into broader translational directions.

> **How can longitudinal clinical data be used to characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy?**

The primary unit of analysis is the **therapy episode**, aligned to treatment-relative time with `day 0 = infusion`.

## Thesis scope

### Included

- encounter timing;
- admission and discharge;
- care location;
- level-of-care state;
- transfer and escalation/de-escalation events;
- length of stay;
- high-acuity exposure;
- early acute-care reuse;
- selected routinely collected clinical observations when useful for contextualizing care intensity;
- provenance, missingness, and deterministic transformation rules.

### Excluded from the thesis core

- CMC/manufacturing attributes;
- product release analytics;
- patient-generated health data;
- remote monitoring;
- treatment recommendation;
- real-time prediction or clinical alerting.

These may be considered later as separate research programs if the thesis foundation proves useful.

## Core episode model

Initial research window:

`day -7 -> infusion day 0 -> acute hospitalization -> discharge -> day +30`

The window is a development default rather than a fixed clinical claim and may be revised based on advisor input and governed data availability.

The canonical episode should preserve:

1. patient/episode identifier;
2. infusion timestamp;
3. encounter boundaries;
4. care-state intervals;
5. transitions between care states;
6. discharge and acute-care return;
7. source and transformation provenance;
8. explicit missing or uncertain states.

## Care-state vocabulary

The initial controlled vocabulary should be small and operationally interpretable for research:

- `outpatient`
- `routine_inpatient`
- `higher_observation`
- `icu`
- `discharged`
- `acute_care_return`
- `unknown`

Institution-specific units should map into these research states rather than becoming hard-coded assumptions in the public framework.

## Phased development

### Phase 0 - Scope and governance

**Goal:** maintain a credible public research boundary.

Deliverables:
- thesis question and aims;
- synthetic/de-identified-data policy;
- no-PHI/no-production-credentials rule;
- explicit distinction between research characterization and bedside decision support.

Exit criteria:
- public examples contain synthetic data only;
- all repository-facing claims are descriptive or methodological;
- thesis scope is clearly separated from post-thesis opportunities.

### Phase 1 - Episode and transition schema

**Goal:** define the research objects needed to represent a CAR T hospital episode.

Minimum objects:
- `therapy_episode`
- `encounter`
- `care_state_interval`
- `care_transition`
- `acute_care_return`
- `provenance`

Design requirements:
- absolute timestamp and treatment-relative time;
- deterministic state mapping;
- explicit source record identifiers;
- missingness/uncertainty representation;
- support for multiple encounters within an episode.

Exit criteria:
- schema validation succeeds for all synthetic fixtures;
- one end-to-end synthetic episode can be represented without ambiguity.

### Phase 2 - Synthetic cohort

**Goal:** build realistic synthetic trajectories to drive development and testing.

Required fixtures:
1. routine recovery;
2. prolonged routine inpatient care;
3. transient escalation and de-escalation;
4. ICU escalation;
5. discharge followed by early readmission;
6. incomplete or conflicting location records.

Exit criteria:
- every fixture has an expected transition sequence;
- edge cases are documented;
- no synthetic fixture depends on institutional identifiers or internal workflow names.

### Phase 3 - Transition reconstruction

**Goal:** transform event-level records into patient-level care-state intervals and transitions.

Core functions:
- anchor events to infusion day;
- sort and normalize encounter/location events;
- resolve overlaps according to documented rules;
- derive state intervals;
- derive transition events;
- preserve provenance and uncertainty.

Primary outputs:
- patient-level transition table;
- patient-level care-state intervals;
- treatment-relative timeline;
- validation report comparing derived output with expected synthetic states.

### Phase 4 - Utilization metrics

**Goal:** quantify hospital use from reconstructed trajectories.

Initial measures:
- total inpatient days;
- days by care state;
- number of transfers;
- time to first escalation;
- duration of high-acuity exposure;
- time from last escalation to discharge;
- 7-day acute-care reuse;
- 30-day acute-care reuse;
- unplanned readmission where the source data support that distinction.

These are descriptive research measures, not thresholds for clinical action.

### Phase 5 - Cohort characterization

**Goal:** characterize recurrent hospital care patterns across episodes.

Candidate descriptive patterns:
- uncomplicated routine recovery;
- prolonged routine care;
- transient escalation;
- sustained high-acuity care;
- discharge with early acute-care return.

Methods should prioritize interpretability and sensitivity analysis. Prediction is not required.

Exit criteria:
- cohort summaries are reproducible;
- derived phenotypes can be traced back to patient-level sequences;
- uncertainty and missingness are visible rather than silently imputed away.

### Phase 6 - Governed hospital-data study

**Goal:** evaluate the framework on appropriately approved institutional data, if available.

Possible validation steps:
- compare reconstructed transitions to source encounter/location records;
- quantify disagreement and missingness;
- manually adjudicate a small approved sample;
- assess whether the framework yields hospital-relevant descriptive information about utilization and transitions.

This phase requires applicable institutional approvals and is not assumed by the public repository.

## Thesis deliverables

A defensible MS thesis should be able to produce:

1. a documented episode and care-state model;
2. reproducible transition-reconstruction code;
3. synthetic validation fixtures and tests;
4. utilization metrics derived from care-state sequences;
5. interpretable patient-level and cohort-level visualizations;
6. a validation and missingness analysis;
7. a written discussion of implications for hospital capacity and care-transition research without making operational recommendations.

## Suggested repository structure

```text
CART-TRACE/
  README.md
  THESIS.md
  ROADMAP.md
  docs/
    care_state_vocabulary.md
    data_dictionary.md
    governance.md
    episode_model.md
  schemas/
    therapy_episode.schema.json
    care_state_interval.schema.json
    care_transition.schema.json
  src/cart_trace/
    normalize/
    timeline/
    transitions/
    utilization/
    provenance/
    reports/
  tests/
    fixtures/
      synthetic/
  notebooks/
    01_episode_reconstruction.ipynb
    02_utilization_trajectories.ipynb
```

## Near-term build order

1. Care-state vocabulary.
2. Therapy-episode schema.
3. Care-state interval schema.
4. Treatment-relative time utilities.
5. Synthetic fixtures.
6. Transition reconstruction.
7. Utilization metrics.
8. Validation tests.
9. Cohort reporting.

## Post-thesis opportunities

The following directions are deliberately deferred:

- rural access and distance-to-center analyses;
- patient-generated health signals;
- remote recovery monitoring;
- prospective implementation studies;
- advanced cellular-therapy product/manufacturing research;
- predictive or decision-support models.

They should only be pursued as separate questions after the hospital care-trajectory foundation is established.

## Success criterion

CART-TRACE succeeds as an MS thesis framework if it can transform heterogeneous hospital records surrounding CAR T-cell therapy into a transparent, reproducible, patient-level sequence of care states and transitions that supports meaningful cohort-level characterization of hospital utilization.
