# Gate 1 -> 2 Evidence Record

**Transition:** Phase 1 — Canonical episode/state/transition model -> Phase 2 — Synthetic cohort

**Decision:** PASS

Gate 1 is passed on the canonical semantics defined by the current schemas, fixtures, tests, and documentation. The earlier Gate 1 evidence based on legacy state names is superseded by this record.

## Passage evidence

GitHub Actions workflow **Validate Gate 1**, run `31652533891`, completed successfully against commit `6d2ce3e1592cec52ab3e2d92f14ebd3a421eea1b` after the machine-readable Gate 1 model and all six Phase 2 fixtures had been migrated to the canonical semantics.

The successful workflow executed both the dedicated Gate 1 schema tests and the full repository test suite. This is the first Gate 1 passage evidence in this branch that validates the corrected canonical model rather than the legacy ontology.

Subsequent documentation-only commits aligned the vocabulary, episode model, time semantics, requirements, and phase-gate descriptions with the already-tested machine-readable contract.

## Canonical semantics frozen by this gate

### Care states

The exact canonical state set is:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

Legacy values `higher_observation`, `icu`, `inpatient_routine`, and `acute_care_return` as a state are not canonical values.

### Transition types

The controlled transition-type set is:

- `admission`
- `transfer`
- `escalation`
- `deescalation`
- `discharge`
- `acute_care_return`
- `other`
- `unknown`

`acute_care_return` is a transition/event classification. A return encounter retains its actual destination state, such as `emergency`.

### Time and interval semantics

- infusion timestamp defines treatment-relative time 0;
- canonical relative time is continuous hours;
- relative hours are calculated as `(event_timestamp - infusion_timestamp).total_seconds() / 3600`;
- days are derived presentation values only;
- care-state intervals use `[start, end)` boundaries;
- null interval ends require an explicit open/censoring reason;
- overlapping authoritative records are resolved by documented precedence or emitted as `unknown` with explicit uncertainty when irreconcilable.

### Inpatient acuity ranking

For inpatient comparisons only:

- `routine_inpatient` = 1
- `intermediate_care` = 2
- `intensive_care` = 3

Emergency care is not assigned an inpatient acuity rank.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Controlled care-state vocabulary | Complete | `docs/care_state_vocabulary.md` |
| Controlled transition vocabulary | Complete | `schemas/care_transition.schema.json`, vocabulary documentation |
| Therapy-episode schema | Complete | `schemas/therapy_episode.schema.json` |
| Care-state interval schema | Complete | `schemas/care_state_interval.schema.json` |
| Care-transition schema | Complete | `schemas/care_transition.schema.json` |
| Encounter input specification | Complete | `schemas/encounter_input.schema.json` |
| Provenance specification | Complete | `schemas/provenance.schema.json` |
| Continuous treatment-relative time convention | Complete | `docs/time_semantics.md` |
| Half-open interval convention | Complete | `docs/time_semantics.md` |
| Mapping and overlap/conflict rules | Complete | `config/synthetic_care_state_mapping.json` |
| Governance boundary | Complete | `docs/governance.md` |
| Multi-encounter hand-worked episode | Complete | `examples/synthetic/gate1_multi_encounter_episode.json` |
| Canonical expected intervals | Complete | `examples/synthetic/gate1_expected_intervals.json` |
| Canonical expected transitions | Complete | `examples/synthetic/gate1_expected_transitions.json` |
| Provenance truth records | Complete | `examples/synthetic/gate1_provenance.json` |
| Exact-vocabulary regression tests | Complete | `tests/test_gate1_schemas.py` |
| Phase 2 fixtures compatible with Gate 1 semantics | Complete | six `examples/synthetic/phase2_*.json` fixtures |
| Negative/error cases compatible with Gate 1 semantics | Complete | `examples/synthetic/invalid_phase2_cases.json` |
| Full CI execution | PASS | GitHub Actions run `31652533891` |

## Gate-review correction history

An earlier version of this evidence record incorrectly treated a green CI run over legacy semantics as sufficient for Gate 1 passage. Review subsequently identified material semantic debt: `higher_observation` and `icu` remained canonical states, `emergency` was absent, `acute_care_return` was incorrectly represented as a state, and interval/transition objects still used day-relative legacy fields.

Gate 1 was therefore reopened and the machine-readable model, truth sets, Phase 2 fixtures, negative fixtures, tests, and documentation were migrated before passage was re-established. The historical CI run `31648451451` is retained only as development history and is not the evidence supporting the current gate decision.

## Hand-worked episode evidence

The canonical Gate 1 episode demonstrates:

- a single therapy episode containing multiple encounters;
- infusion anchoring with continuous relative hours;
- routine inpatient care;
- embedded higher-priority `intensive_care` exposure;
- de-escalation back to routine inpatient care;
- discharge;
- later emergency care;
- `acute_care_return` as the discharged-to-emergency transition type;
- half-open interval boundaries;
- source-record and derived-artifact provenance.

## Change control

The following are frozen by Gate 1 and require explicit gate-impact review if changed:

- canonical state vocabulary;
- transition-type vocabulary;
- infusion-relative hour calculation;
- half-open interval semantics;
- open-end/censoring semantics;
- encounter minimum input contract;
- source-to-canonical mapping and conflict behavior;
- provenance requirements;
- Gate 1 expected interval and transition truth objects.

A semantic change requires version review, regeneration of affected synthetic fixtures, regression tests, and renewed Gate 1 evidence.

## Authorized next work

Phase 2 synthetic-oracle closure is authorized. Gate 2 -> 3 must still be evaluated independently before Phase 3 reconstruction becomes the authoritative next development phase.
