# Gate 2 -> 3 Evidence Record

**Transition:** Phase 2 — Synthetic cohort -> Phase 3 — Transition reconstruction

**Decision:** PASS

Gate 2 is passed. The Phase 2 oracle now contains six canonical trajectory fixtures plus explicit boundary/error cases sufficient to begin deterministic reconstruction without inventing new trajectory semantics.

GitHub Actions run `31657333214` completed successfully on commit `60fa21200d5948833763aef28556984026902dfb` using the repository validation workflow. That run includes the canonical schemas, six Phase 2 fixtures, negative/error cases, and the Phase 2 boundary-case assertions.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Six trajectory classes represented | Complete | `examples/synthetic/fixture_manifest.json` |
| Routine recovery fixture | Complete | `examples/synthetic/phase2_routine_recovery.json` |
| Prolonged routine inpatient fixture | Complete | `examples/synthetic/phase2_prolonged_routine.json` |
| Transient escalation/de-escalation fixture | Complete | `examples/synthetic/phase2_transient_escalation.json` |
| Intensive-care escalation fixture | Complete | `examples/synthetic/phase2_icu_escalation.json` |
| Early acute-care-return fixture | Complete | `examples/synthetic/phase2_early_return.json` |
| Conflicting/missing-location fixture | Complete | `examples/synthetic/phase2_conflicting_location.json` |
| Canonical expected intervals/transitions | Complete | six trajectory fixtures |
| Canonical expected utilization values | Complete | six trajectory fixtures |
| Negative/error cases | Complete | `examples/synthetic/invalid_phase2_cases.json` |
| Duplicate same-state oracle | Complete | `examples/synthetic/phase2_boundary_cases.json` |
| Missing/open-end oracle | Complete | `examples/synthetic/phase2_boundary_cases.json` |
| Study-window boundary oracle | Complete | `examples/synthetic/phase2_boundary_cases.json` |
| Adjacent-interval oracle | Complete | `examples/synthetic/phase2_boundary_cases.json` |
| Same-day discharge/return oracle | Complete | `examples/synthetic/phase2_boundary_cases.json` |
| Equal-priority conflict behavior | Complete | conflict fixture + tests |
| Unknown interval between known states | Complete | conflict fixture + tests |
| Automated oracle validation | PASS | `tests/test_phase2_fixtures.py`, run `31657333214` |

## Frozen Phase 2 oracle

The controlled Phase 2 oracle consists of:

- `examples/synthetic/fixture_manifest.json`;
- the six `phase2_*.json` trajectory fixtures;
- `examples/synthetic/invalid_phase2_cases.json`;
- `examples/synthetic/phase2_boundary_cases.json`;
- prespecified canonical intervals and transitions;
- prespecified uncertainty/conflict behavior;
- expected utilization values used as downstream test oracles.

The oracle uses the Gate 1 canonical states and transition types. `acute_care_return` remains a transition type, never a care state. Treatment-relative timing remains continuous hours, and intervals remain half-open `[start, end)`.

## Phase 3 implementation contract

Phase 3 reconstruction must be judged against this frozen oracle. In particular, implementation must demonstrate:

1. deterministic source-label mapping and stable event ordering;
2. exact interval reconstruction for deterministic fixtures;
3. prespecified `unknown` behavior for irreconcilable equal-priority conflicts;
4. duplicate same-state suppression;
5. explicit open/censored interval behavior when end time is not defensible;
6. `[start, end)` boundary behavior and study-window clipping/exclusion;
7. transitions only when the canonical state changes;
8. `discharged -> emergency/inpatient` classification as `acute_care_return` when the configured return-window condition is met;
9. source-record provenance propagation;
10. reproducible stable outputs across repeated runs.

## Change control

Changes to expected Phase 2 intervals, transitions, uncertainty behavior, or boundary semantics require explicit Gate 2 impact review and corresponding Phase 3 regression updates. Metric-value changes additionally require metric-version review once Phase 4 begins.

## Authorized next phase

**Phase 3 — Transition reconstruction is authorized.**

The first Phase 3 work should implement treatment-relative time normalization, source-label mapping, deterministic sorting/precedence, interval reconstruction, transition derivation, and provenance propagation directly against the frozen oracle.
