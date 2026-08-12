# Gate 2 -> 3 Candidate Evidence Record

**Proposed transition:** Phase 2 — Synthetic cohort -> Phase 3 — Transition reconstruction

**Current decision:** CONDITIONAL / NOT YET PASSED

Phase 2 now contains the six required trajectory classes and automated fixture-coverage tests. Gate 2 remains open until all fixtures conform fully to the canonical truth-set contract and the test suite executes successfully in CI.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Six trajectory classes represented | Complete | `examples/synthetic/fixture_manifest.json` |
| Routine recovery fixture | Complete | `examples/synthetic/phase2_routine_recovery.json` |
| Prolonged routine inpatient fixture | Complete | `examples/synthetic/phase2_prolonged_routine_inpatient.json` |
| Transient escalation fixture | Complete | `examples/synthetic/phase2_transient_escalation.json` |
| ICU escalation fixture | Complete as Gate 1 seed | `examples/synthetic/gate1_multi_encounter_episode.json` |
| Early acute-care return fixture | Complete | `examples/synthetic/phase2_early_acute_care_return.json` |
| Conflicting/missing location fixture | Complete | `examples/synthetic/phase2_conflicting_missing_location.json` |
| Requirement coverage in manifest | Complete | `examples/synthetic/fixture_manifest.json` |
| Fixture coverage tests authored | Complete | `tests/test_phase2_fixtures.py` |
| Expected utilization metrics | Complete for 5/6 fixtures | fixture files |
| Canonical interval/transition schema conformity | Partial | normalization still needed for Gate 1 seed fields |
| Invalid fixtures for negative/error testing | Pending | Phase 2 closure task |
| CI execution of Phase 2 tests | Pending | workflow evidence required |

## Current strengths

The truth set now covers the principal hospital trajectory patterns required by the thesis:

- uncomplicated routine inpatient recovery;
- prolonged routine inpatient care;
- transient escalation to intermediate/higher-observation care and return;
- ICU escalation and de-escalation;
- discharge followed by early acute-care return;
- incomplete/conflicting care-location evidence producing explicit uncertainty.

Each manifest entry is linked to requirement IDs so the fixture set can function as both an engineering oracle and a requirements-coverage artifact.

## Remaining blockers

### 1. Normalize the ICU seed fixture

The Gate 1 seed uses legacy truth-set field names such as `start`, `end`, `relative_start_hours`, and compact transition objects. Before Gate 2 passage, this fixture should either be normalized to the canonical interval/transition schemas or mirrored by schema-conformant Phase 2 expected objects.

### 2. Add expected metrics for the ICU fixture

The ICU fixture should have the same metric truth-set structure as the other Phase 2 fixtures, including inpatient duration, ICU duration, transition count, time to first escalation, and reuse indicators where applicable.

### 3. Add invalid/error fixtures

Phase 2 should include a small negative-test set for conditions such as:

- invalid care-state label;
- end before start;
- missing required episode anchor;
- duplicate/ambiguous priority without tie-break key;
- malformed timestamp;
- unsupported/unmapped label producing explicit `unknown` behavior where appropriate rather than silent success.

### 4. Execute Phase 2 tests in CI

The authored fixture tests must pass in the reproducible environment before Gate 2 is frozen.

## Gate passage rule

Gate 2 -> 3 may pass when:

1. all six fixtures expose source-like inputs plus prespecified canonical intervals, transitions, uncertainty behavior, and expected metrics;
2. every expected interval/transition object conforms to its schema;
3. fixture requirement coverage is complete and non-empty;
4. negative/error fixtures exist for schema/reconstruction failure behavior;
5. automated fixture tests execute successfully in CI;
6. no Phase 3 reconstruction code needs to invent missing fixture semantics.

Until then, Phase 3 code may be prototyped only if it treats the current truth set as provisional rather than frozen.
