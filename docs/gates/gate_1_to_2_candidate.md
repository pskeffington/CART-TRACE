# Gate 1 -> 2 Candidate Evidence Record

**Proposed transition:** Phase 1 — Episode and transition schema -> Phase 2 — Synthetic cohort

**Current decision:** CONDITIONAL / NOT YET PASSED

The canonical model artifacts now exist, but Gate 1 -> 2 should remain open until the schemas are validated together and the hand-worked episode is shown to conform to the model without undocumented assumptions.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Controlled care-state vocabulary | Complete | `docs/care_state_vocabulary.md` |
| Therapy-episode schema | Complete | `schemas/therapy_episode.schema.json` |
| Care-state interval schema | Complete | `schemas/care_state_interval.schema.json` |
| Care-transition schema | Complete | `schemas/care_transition.schema.json` |
| Encounter input specification | Complete | `schemas/encounter_input.schema.json` |
| Provenance specification | Complete | `schemas/provenance.schema.json` |
| Treatment-relative time convention | Complete | `docs/time_semantics.md` |
| Interval-boundary convention | Complete | `docs/time_semantics.md` |
| Identical-timestamp tie-breaking | Documented | `docs/time_semantics.md` |
| Overlap/conflict behavior | Documented conceptually | `docs/time_semantics.md`, `docs/care_state_vocabulary.md` |
| Governance boundary | Complete | `docs/governance.md` |
| Multi-encounter hand-worked episode | Complete | `examples/synthetic/gate1_multi_encounter_episode.json` |
| Cross-schema validation | Pending | automated validation required |
| Machine-testable overlap precedence | Pending | Phase 1 closure task |

## Requirements addressed

This evidence materially advances:

- `SCOPE-001` through `SCOPE-003`
- `DATA-001` through `DATA-005`
- `MODEL-001` through `MODEL-005`
- `TIME-001` through `TIME-004`
- `PROV-001` through `PROV-004`
- `GOV-001` through `GOV-004`

## Hand-worked episode review

The Gate 1 synthetic episode demonstrates:

- a single therapy episode containing multiple encounters;
- infusion anchoring at Day 0;
- routine inpatient care with an embedded higher-priority ICU interval;
- return from ICU to routine inpatient care;
- discharge;
- later acute-care return;
- expected care-state intervals with half-open boundaries;
- expected transition sequence;
- source-record traceability.

The fixture intentionally contains an overlapping ICU location record within a broader inpatient encounter to exercise precedence logic.

## Remaining blockers

### 1. Automated schema validation

The episode, encounter inputs, canonical intervals, transitions, and provenance examples must be validated against their schemas in a reproducible test.

### 2. Provenance instances

The hand-worked fixture currently references provenance IDs but does not yet include full provenance objects for every source and derived artifact. Add these before Gate passage.

### 3. Machine-testable mapping/precedence configuration

The documentation states that higher-authority or configured higher-priority source records can override broader encounter records. The public model still needs a small machine-readable mapping/precedence example so the behavior is not only prose.

### 4. Expected canonical objects must conform exactly

The hand-worked expected intervals currently function as a truth-set description. They should be converted or mirrored into objects conforming exactly to `care_state_interval.schema.json` and `care_transition.schema.json`.

## Gate passage rule

Gate 1 -> 2 may pass when:

1. all core schemas validate;
2. one complete multi-encounter synthetic episode validates end to end;
3. every expected interval and transition has provenance;
4. deterministic mapping/precedence behavior is represented in testable configuration or code;
5. no undocumented field or inference is required to produce the expected canonical trajectory.

Until those conditions are met, Phase 2 fixture expansion may be prototyped, but the Phase 1 semantics should not be considered frozen.
