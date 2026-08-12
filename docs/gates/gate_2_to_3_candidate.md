# Gate 2 -> 3 Candidate Evidence Record

**Proposed transition:** Phase 2 — Synthetic cohort -> Phase 3 — Transition reconstruction

**Current decision:** CONDITIONAL / CI PENDING

Phase 2 now contains six normalized trajectory classes, requirement coverage, expected utilization measures, negative/error fixtures, and automated fixture validation. The only remaining formal blocker is successful CI execution of the updated Phase 2 test suite.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Six trajectory classes represented | Complete | `examples/synthetic/fixture_manifest.json` |
| Routine recovery fixture | Complete | `examples/synthetic/phase2_routine_recovery.json` |
| Prolonged routine inpatient fixture | Complete | `examples/synthetic/phase2_prolonged_routine.json` |
| Transient escalation fixture | Complete | `examples/synthetic/phase2_transient_escalation.json` |
| ICU escalation fixture | Complete / normalized | `examples/synthetic/phase2_icu_escalation.json` |
| Early acute-care return fixture | Complete | `examples/synthetic/phase2_early_return.json` |
| Conflicting/missing location fixture | Complete | `examples/synthetic/phase2_conflicting_location.json` |
| Requirement coverage in manifest | Complete | `examples/synthetic/fixture_manifest.json` |
| Expected utilization metrics | Complete for 6/6 fixtures | fixture files |
| Canonical interval/transition schema conformity | Complete by test contract | `tests/test_phase2_fixtures.py` |
| Invalid fixtures for negative/error testing | Complete | `examples/synthetic/invalid_phase2_cases.json` |
| Fixture coverage and negative tests | Complete | `tests/test_phase2_fixtures.py` |
| CI execution of Phase 2 tests | Pending | workflow evidence required |

## Truth-set coverage

The synthetic cohort represents the core trajectory patterns needed for reconstruction development:

- routine inpatient recovery;
- prolonged routine inpatient care;
- transient escalation and de-escalation;
- ICU escalation and de-escalation;
- discharge followed by early acute-care return;
- incomplete/conflicting care-location evidence with explicit `unknown`/uncertainty behavior.

The ICU trajectory is now represented in the same Phase 2 contract as the other fixtures, including schema-conformant expected intervals/transitions and prespecified utilization metrics.

## Negative/error coverage

`examples/synthetic/invalid_phase2_cases.json` now exercises:

- invalid canonical state labels;
- missing infusion anchor;
- malformed timestamps;
- reversed interval semantics;
- equal-priority overlapping records requiring the frozen deterministic tie-break behavior.

The negative set distinguishes schema-level failure from semantic/reconstruction-level behavior so Phase 3 code can be tested against both categories.

## Automated oracle contract

`tests/test_phase2_fixtures.py` now checks:

1. all required trajectory classes are present;
2. manifest artifact paths resolve to actual fixture files;
3. fixture IDs are unique;
4. every fixture has requirement coverage;
5. episode and encounter inputs validate;
6. expected state sequences match the manifest;
7. all expected intervals/transitions conform to canonical schemas;
8. every fixture exposes expected utilization metrics;
9. conflict, early-return, routine, and ICU-specific expected behavior is explicit;
10. negative schema cases fail validation as expected;
11. semantic-invalid interval and tie-break cases remain machine-testable.

## Remaining blocker

### CI execution

Gate 2 -> 3 should pass only after the updated Phase 2 test suite executes successfully in the repository CI environment.

No Phase 3 reconstruction code should be considered authoritative until this truth set is frozen by successful CI evidence.

## Candidate freeze set after passage

If Gate 2 passes, the following become controlled Phase 2 truth-set artifacts:

- `examples/synthetic/fixture_manifest.json`;
- the six Phase 2 trajectory fixtures;
- `examples/synthetic/invalid_phase2_cases.json`;
- expected interval and transition sequences;
- expected uncertainty behavior;
- expected utilization measures used as downstream test oracles.

Any change to expected trajectory semantics after passage requires gate-impact review and corresponding reconstruction-test updates.

## Gate passage rule

Gate 2 -> 3 may pass when:

1. all six fixtures contain source-like inputs plus prespecified canonical intervals, transitions, uncertainty behavior, and expected metrics;
2. every expected interval/transition object conforms to its schema;
3. fixture requirement coverage is complete and non-empty;
4. negative/error fixtures cover schema and semantic/reconstruction failure behavior;
5. the updated automated fixture tests execute successfully in CI;
6. Phase 3 reconstruction can implement directly against the frozen truth set without inventing missing semantics.
