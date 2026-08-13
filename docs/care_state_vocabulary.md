# Care-State Vocabulary

CART-TRACE uses a small research vocabulary to normalize institution-specific locations into interpretable hospital care states.

The vocabulary is intentionally descriptive. It does not imply clinical severity, appropriateness of placement, or a recommendation to transfer a patient.

## Canonical states

### `outpatient`
The patient is receiving care without an inpatient admission.

Examples may include clinic, infusion-center, scheduled outpatient evaluation, or other ambulatory care settings represented in the source data.

### `emergency`
The patient is receiving care in an emergency setting represented by the source data.

Emergency care is a canonical state because it describes where care occurred. A post-discharge emergency encounter may also generate an `acute_care_return` transition type, but `acute_care_return` is not itself a state.

### `routine_inpatient`
The patient is admitted to a standard inpatient care setting that does not meet the source-defined criteria for intermediate- or intensive-care classification.

### `intermediate_care`
The patient is admitted to an intermediate, stepdown, medical specialty, or higher-observation setting between routine inpatient and intensive care according to documented source-to-canonical mapping.

Institution-specific unit names remain source labels and must not become canonical states.

### `intensive_care`
The source record indicates an intensive-care setting.

CART-TRACE records the observed location state; it does not infer intensive-care need from physiologic variables.

### `discharged`
The acute inpatient episode has ended and the patient is no longer represented as occupying an inpatient care state.

This state does not imply full clinical recovery.

### `unknown`
The care state cannot be assigned confidently because source records are absent, conflicting, or insufficiently specific.

Unknown states remain visible rather than being silently imputed.

## Transition types

Transitions are distinct from states. The controlled transition vocabulary is:

- `admission`
- `transfer`
- `escalation`
- `deescalation`
- `discharge`
- `acute_care_return`
- `other`
- `unknown`

`acute_care_return` describes a transition from `discharged` to a subsequent emergency or inpatient acute-care state within a configured follow-up window. The destination remains the actual canonical care state, such as `emergency` or `routine_inpatient`.

## Mapping principles

1. Preserve original source location or encounter category in provenance.
2. Map local unit names to the smallest common vocabulary needed for the capstone question.
3. Do not use physiologic measurements to infer a care state when authoritative location evidence exists.
4. Apply documented precedence rules when source records overlap.
5. If equally authoritative evidence remains irreconcilable, emit `unknown` with explicit uncertainty rather than selecting a state arbitrarily.
6. Do not equate care state with toxicity grade or disease severity.
7. Keep institutional unit names and identifiers out of public synthetic examples.

## Transition semantics

A transition occurs when the normalized care state changes at a documented timestamp.

Examples:

`outpatient -> routine_inpatient` (`admission`)

`routine_inpatient -> intermediate_care` (`escalation`)

`intermediate_care -> intensive_care` (`escalation`)

`intensive_care -> routine_inpatient` (`deescalation`)

`routine_inpatient -> discharged` (`discharge`)

`discharged -> emergency` (`acute_care_return`, when the configured return-window definition is met)

Repeated source events that do not change normalized state do not generate duplicate transitions.

## Acuity ordering

Acuity rank is defined only for inpatient care-state comparisons:

- `routine_inpatient` = 1
- `intermediate_care` = 2
- `intensive_care` = 3

`emergency`, `outpatient`, `discharged`, and `unknown` are not assigned an inpatient acuity rank.

## Research use

This vocabulary supports reproducible characterization of time spent in each care state, timing and frequency of escalation/de-escalation, high-acuity exposure, discharge timing, early acute-care reuse, and recurrent descriptive hospital care trajectories.

It is not a clinical ontology and must not be used to automate patient placement, eligibility, or escalation decisions.
