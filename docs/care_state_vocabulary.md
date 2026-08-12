# Care-State Vocabulary

CART-TRACE uses a small research vocabulary to normalize institution-specific locations into interpretable hospital care states.

The vocabulary is intentionally descriptive. It does not imply clinical severity, appropriateness of placement, or a recommendation to transfer a patient.

## Core states

### `outpatient`
The patient is receiving care without an inpatient admission.

Examples may include clinic, infusion-center, scheduled outpatient evaluation, or other ambulatory care settings represented in the source data.

### `routine_inpatient`
The patient is admitted to a standard inpatient care setting that does not meet the source-defined criteria for higher-observation or intensive-care classification.

### `higher_observation`
The patient is admitted to an intermediate or higher-observation setting between routine inpatient care and ICU-level care.

This is a generic research state. Institution-specific unit names must be mapped through documented configuration rather than hard-coded into CART-TRACE.

### `icu`
The source record indicates an intensive-care setting.

CART-TRACE records the state as observed in hospital data; it does not infer ICU need from physiologic variables.

### `discharged`
The acute inpatient episode has ended and the patient is no longer represented as occupying an inpatient care state.

This state does not imply full clinical recovery.

### `acute_care_return`
A new emergency, observation, or inpatient acute-care encounter occurs after discharge within the study follow-up window.

The source encounter type should remain available so analyses can distinguish emergency evaluation, observation, and readmission where data quality permits.

### `unknown`
The care state cannot be assigned confidently because source records are absent, conflicting, or insufficiently specific.

Unknown states should remain visible rather than being silently imputed.

## Mapping principles

1. Preserve the original source location or encounter category in provenance.
2. Map local unit names to the smallest common vocabulary needed for the thesis question.
3. Do not use physiologic measurements to infer a care state when an authoritative location record exists.
4. When source records conflict, apply a documented precedence rule and retain an uncertainty flag.
5. Do not equate care state with toxicity grade or disease severity.
6. Keep institutional unit names and identifiers out of public synthetic examples.

## Transition semantics

A transition occurs when a patient's normalized care state changes at a documented timestamp.

Examples:

`outpatient -> routine_inpatient`

`routine_inpatient -> higher_observation`

`higher_observation -> icu`

`icu -> routine_inpatient`

`routine_inpatient -> discharged`

`discharged -> acute_care_return`

Repeated source events that do not change normalized state should not generate duplicate transitions.

## Research use

This vocabulary supports reproducible characterization of:

- time spent in each care state;
- timing and frequency of escalation/de-escalation;
- high-acuity exposure;
- discharge timing;
- early acute-care reuse;
- recurrent descriptive hospital care trajectories.

It is not a clinical ontology and should not be used to automate patient placement or escalation decisions.
