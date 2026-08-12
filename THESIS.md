# CART-TRACE MS HSE Thesis Scaffold

## Working title

**CART-TRACE: Longitudinal Characterization of Hospital Care Trajectories Following CAR T-Cell Therapy**

## Primary research question

How can longitudinal clinical data be used to characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy?

## Thesis premise

CAR T-cell treatment produces a time-dependent hospital care episode in which patients may move between outpatient care, routine inpatient care, higher-observation settings, intensive care, discharge, and early readmission. These transitions are clinically meaningful but are often distributed across encounter, location, laboratory, medication, and utilization records.

The engineering problem is to build a reproducible temporal representation of these care trajectories that preserves patient-level sequence, supports cohort-level analysis, and makes hospital utilization patterns measurable without functioning as a bedside decision-support system.

## Specific aims

### Aim 1 - Reconstruct the hospital episode

Develop a reproducible method for aligning CAR T-cell events to a common treatment-relative timeline anchored on infusion day (`day 0`). Represent care setting, encounter state, and transitions throughout the acute episode and early follow-up period.

Primary outputs:
- canonical episode table;
- treatment-relative event timeline;
- care-location sequence;
- transition table;
- provenance for each derived state.

### Aim 2 - Characterize utilization trajectories

Quantify hospital utilization across CAR T-cell episodes.

Candidate measures:
- total inpatient days;
- days by care level;
- number and timing of transfers;
- ICU or other high-acuity escalation;
- discharge timing;
- 7-day and 30-day acute-care reuse;
- unplanned readmission;
- monitoring intensity by treatment-relative day.

### Aim 3 - Identify recurrent hospital care phenotypes

Determine whether recurrent patterns of hospital use can be identified from the reconstructed trajectories.

Candidate descriptive phenotypes:
- uncomplicated routine recovery;
- prolonged routine inpatient care;
- transient escalation and de-escalation;
- sustained high-acuity care;
- discharge followed by early acute-care reuse.

Phenotypes will be descriptive research constructs and must not be presented as diagnostic labels or treatment recommendations.

## Primary unit of analysis

The primary unit is the **CAR T-cell therapy episode**, not the individual encounter.

Minimum episode window for initial development:

`infusion day -7 -> infusion day +30`

This window may be revised based on available research data and advisor input.

## Core data domains

The thesis core is intentionally limited to hospital-relevant clinical and system data:

1. therapy episode identifiers and treatment anchors;
2. encounters and admission/discharge events;
3. care location and level-of-care states;
4. transfers between care settings;
5. routinely collected laboratory and vital-sign timestamps where useful for contextualizing care intensity;
6. recorded toxicity events where available;
7. discharge and acute-care reuse.

CMC/manufacturing attributes and patient-generated data are out of scope for the primary thesis.

## Primary outcomes

The initial analysis should prioritize outcomes measurable from hospital data:

- length of stay;
- high-acuity care exposure;
- time to first escalation;
- number of level-of-care transitions;
- time from last escalation to discharge;
- 7-day readmission or emergency acute-care return;
- 30-day readmission or emergency acute-care return.

## Methodological contribution

The thesis contribution is the design and evaluation of a reproducible patient-level temporal model for hospital care trajectories around CAR T-cell therapy.

The project should emphasize:
- temporal alignment;
- explicit state definitions;
- deterministic transformation rules;
- provenance;
- missingness;
- validation against source events;
- interpretable cohort summaries.

Prediction is not required for thesis success.

## Validation plan

### Synthetic validation

Before governed institutional data are used, the repository should contain synthetic episodes representing:

1. routine inpatient recovery;
2. transient escalation with return to routine care;
3. ICU escalation;
4. prolonged hospitalization;
5. discharge followed by early readmission;
6. incomplete or missing location records.

### Research-data validation

If institutional data become available under appropriate approvals:
- compare reconstructed transitions against source encounter/location records;
- quantify disagreement and missingness;
- manually review a small validation sample under the approved protocol;
- document all adjudication rules.

## Guardrails

CART-TRACE is a research framework.

It will not:
- issue clinical alerts;
- diagnose CRS, ICANS, or other toxicity from raw signals;
- recommend escalation, transfer, discharge, or treatment;
- claim prospective clinical utility without separate validation;
- include PHI in the public repository.

## Near-term build sequence

1. Define the care-state vocabulary.
2. Define the episode schema.
3. Implement treatment-relative time conversion.
4. Implement transition reconstruction.
5. Create synthetic episodes covering core hospital trajectories.
6. Implement utilization metrics.
7. Add validation tests.
8. Produce a cohort-level descriptive report.
9. Refine phenotype definitions based on data availability and advisor review.

## Thesis success criterion

A successful thesis will demonstrate that heterogeneous hospital records surrounding CAR T-cell therapy can be transformed into a transparent, reproducible, patient-level sequence of care states and transitions that supports meaningful characterization of hospital utilization across a cohort.
