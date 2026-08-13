# Episode Model

CART-TRACE represents hospital use around CAR T-cell therapy as a treatment-relative episode rather than a collection of disconnected encounters.

## Anchor

The canonical temporal anchor is the CAR T-cell infusion timestamp.

`infusion timestamp = treatment-relative time 0`

For an event occurring at timestamp `t`, treatment-relative time is:

`relative_hours = (t - infusion_timestamp).total_seconds() / 3600`

Days, when needed for presentation, are derived as `relative_hours / 24`. Continuous relative hours remain the canonical analytic representation.

## Initial analysis window

The development default is approximately:

`day -7 through day +30`

The episode object stores both explicit timestamp boundaries and their corresponding relative-hour values. This is a research implementation window, not a clinical recommendation.

## Episode objects

A minimum episode contains:

1. one `therapy_episode` record;
2. zero or more source encounter/location records;
3. a normalized sequence of `care_state_interval` records;
4. `care_transition` records between consecutive states;
5. provenance linking every derived interval and transition to source evidence or a documented derivation rule.

## Canonical states

The canonical state vocabulary is:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` is a transition type, not a state.

## Interval semantics

Care-state intervals use half-open boundaries:

`[start_timestamp, end_timestamp)`

Each interval carries an `interval_id`, absolute timestamps, continuous treatment-relative hours, source type, contributing source-record identifiers, mapping method, provenance, and explicit uncertainty/open-end metadata.

A null end is permitted only when the interval is genuinely open/censored and an explicit reason is retained. Arbitrary imputation of an end time is not allowed.

## Transition semantics

A transition is emitted only when canonical state changes. Each transition carries a `transition_id`, timestamp, relative time in hours, `from_state`, `to_state`, transition type, source-record identifiers, provenance, and uncertainty where applicable.

Controlled transition types are `admission`, `transfer`, `escalation`, `deescalation`, `discharge`, `acute_care_return`, `other`, and `unknown`.

A post-discharge acute-care return is represented by the actual destination state plus `transition_type = acute_care_return`; for example:

`discharged -> emergency`

## Reconstruction rules

The reconstruction method follows these principles:

1. Normalize timestamps to a consistent offset-aware representation before relative-time computation.
2. Sort authoritative encounter/location records deterministically.
3. Map source labels to the controlled canonical state vocabulary.
4. Apply documented precedence rules to overlaps.
5. If equally authoritative source evidence remains irreconcilable, emit `unknown` with explicit uncertainty and preserve all contributing source identifiers.
6. Collapse consecutive records that map to the same canonical state.
7. Create a transition only when canonical state changes.
8. Preserve provenance for every interval and transition.
9. Do not infer toxicity, eligibility, or need for escalation from laboratory/vital data as part of care-state reconstruction.

## Hand-worked example

A synthetic episode may reconstruct as:

```text
-2 h    routine_inpatient
32 h    intensive_care
44 h    routine_inpatient
76 h    discharged
167 h   emergency   [transition_type = acute_care_return]
```

This representation supports descriptive measures such as inpatient duration, intermediate/intensive-care exposure, number and timing of transitions, time to first escalation, discharge timing, and early acute-care reuse.

## Interpretation boundary

The episode model describes **where and when care occurred**. It does not determine treatment eligibility, infer physiologic severity, evaluate whether a transfer was appropriate, or recommend future placement or treatment decisions.
