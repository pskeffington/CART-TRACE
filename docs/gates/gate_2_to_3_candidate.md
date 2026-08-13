# Gate 2 -> 3 Candidate Evidence Record

**Proposed transition:** Phase 2 — Synthetic cohort -> Phase 3 — Transition reconstruction

**Current decision:** NOT YET PASSED

Gate 1 has now passed on the corrected canonical semantics. Phase 2 contains six canonical trajectory fixtures, expected intervals/transitions, expected metrics, uncertainty behavior, negative/error cases, and automated validation. GitHub Actions run `31652533891` successfully executed the current full test suite against commit `6d2ce3e1592cec52ab3e2d92f14ebd3a421eea1b`.

That successful run removes CI as the prior blocker. Gate 2 remains open because the stricter current gate definition requires a final oracle-completeness review and explicit coverage of several boundary cases before the truth set is frozen for Phase 3.

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
| Requirement coverage in manifest | Complete | `examples/synthetic/fixture_manifest.json` |
| Canonical expected intervals/transitions | Complete for 6/6 fixtures | fixture files |
| Canonical expected utilization metrics | Complete for 6/6 fixtures | fixture files |
| Negative/error fixtures | Present | `examples/synthetic/invalid_phase2_cases.json` |
| Automated Phase 2 tests | Passing in CI | `tests/test_phase2_fixtures.py`, run `31652533891` |
| Identical-timestamp behavior | Partial | semantic/error cases exist; oracle coverage review required |
| Adjacent interval boundary | Partial | represented in trajectories; explicit assertion should be added |
| Duplicate same-state source event | Missing explicit fixture/test | required before freeze |
| Missing/open end time | Missing explicit fixture/test | required before freeze |
| Study-window boundary event | Missing explicit fixture/test | required before freeze |
| Same-day discharge/acute-care return boundary | Partial | return semantics covered; same-day boundary fixture still required |
| Equal-priority conflicting location sources | Complete | conflict fixture + tests |
| Unknown interval between known states | Complete | conflict fixture |

## Current canonical truth-set coverage

The synthetic cohort now represents:

- routine inpatient recovery;
- prolonged routine inpatient care;
- transient `routine_inpatient -> intermediate_care -> routine_inpatient` escalation/de-escalation;
- `intensive_care` escalation/de-escalation;
- discharge followed by `emergency` care with `transition_type = acute_care_return`;
- equal-priority conflicting care-location evidence represented as `unknown` with explicit uncertainty.

All six fixtures use the Gate 1 hour-relative episode/interval/transition contract.

## Negative/error coverage already present

`examples/synthetic/invalid_phase2_cases.json` currently exercises:

- invalid canonical state labels;
- missing infusion anchor;
- malformed timestamps;
- reversed interval semantics;
- equal-priority overlapping records requiring deterministic/conflict behavior.

## Remaining oracle-closure work

Before Gate 2 passes, add or explicitly test:

1. a duplicate same-state source-event case demonstrating no false transition;
2. a missing/open end-time case demonstrating explicit censor/open-end behavior;
3. a study-window boundary case demonstrating clipping/exclusion semantics;
4. an explicit adjacent-interval assertion at a shared timestamp;
5. a same-day discharge/acute-care-return boundary case;
6. a final requirement-to-fixture coverage check showing that every mandatory Phase 3 reconstruction behavior has an oracle case.

These are oracle-completeness issues, not changes to the Gate 1 canonical semantics.

## Candidate freeze set after passage

When Gate 2 passes, the controlled Phase 2 oracle will include:

- `examples/synthetic/fixture_manifest.json`;
- the six core Phase 2 trajectory fixtures;
- `examples/synthetic/invalid_phase2_cases.json`;
- added boundary/edge-case oracle records;
- expected interval and transition sequences;
- expected uncertainty behavior;
- expected utilization values used downstream.

Changes after passage require explicit Gate 2 impact review and corresponding Phase 3 regression updates.

## Gate passage rule

Gate 2 -> 3 may pass when the six trajectory fixtures and required boundary/error cases collectively allow Phase 3 reconstruction to be judged without inventing missing semantics, and the complete oracle suite executes successfully in CI.
