# Episode Model

CART-TRACE represents hospital use around CAR T-cell therapy as a treatment-relative episode rather than a collection of disconnected encounters.

## Anchor

The canonical temporal anchor is the CAR T-cell infusion timestamp.

`infusion timestamp = treatment-relative day 0`

For an event occurring at timestamp `t`, the treatment-relative time is the elapsed duration between `t` and the infusion timestamp, expressed in days. Implementations should retain the absolute timestamp as well as the treatment-relative value.

## Initial analysis window

The development default is:

`day -7 through day +30`

This is a research implementation window, not a clinical recommendation. It may be changed for a governed study based on the protocol, available data, and advisor review.

## Episode objects

A minimum episode contains:

1. one `therapy_episode` record;
2. zero or more source encounters/events;
3. a normalized sequence of `care_state_interval` records;
4. transitions between consecutive states;
5. provenance linking derived states to source records.

## Reconstruction rules

The initial reconstruction algorithm should follow these principles:

1. Normalize timestamps to a consistent timezone before calculating relative time.
2. Sort authoritative encounter/location records chronologically.
3. Map each source location to the controlled care-state vocabulary.
4. Collapse consecutive events that map to the same normalized state.
5. Create a transition only when the normalized state changes.
6. Preserve overlapping/conflicting records as an explicit uncertainty condition rather than silently choosing a state without documentation.
7. Preserve source identifiers and mapping provenance for every derived interval and transition.
8. Do not infer toxicity or need for escalation from laboratory/vital data as part of care-state reconstruction.

## Example

A synthetic episode may reconstruct as:

```text
day -1.0   outpatient
day  0.0   routine_inpatient
day  2.3   higher_observation
day  3.1   icu
day  4.8   routine_inpatient
day  7.2   discharged
day 14.4   acute_care_return
day 15.1   discharged
```

This sequence supports descriptive measures such as total inpatient time, high-acuity exposure, number of transitions, time to first escalation, and early acute-care reuse.

## Interpretation boundary

The episode model describes **where and when care occurred**. It does not determine whether a transfer was appropriate, infer a patient's physiologic severity, or recommend future placement decisions.
