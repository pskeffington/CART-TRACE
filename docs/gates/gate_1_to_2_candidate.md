# Gate 1 -> 2 Candidate Evidence Record

**Proposed transition:** Phase 1 — Episode and transition schema -> Phase 2 — Synthetic cohort

**Current decision:** CONDITIONAL / NOT YET PASSED

Gate 1 is now close to closure. The canonical schemas, governance boundary, time semantics, machine-readable mapping rules, schema-conformant truth sets, and validation tests are present. The remaining requirement is to execute the test suite in a reproducible environment and resolve any failures before freezing Phase 1 semantics.

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
| Identical-timestamp tie-breaking | Complete | `docs/time_semantics.md`, `config/synthetic_care_state_mapping.json` |
| Overlap/conflict precedence | Machine-readable | `config/synthetic_care_state_mapping.json` |
| Governance boundary | Complete | `docs/governance.md` |
| Multi-encounter hand-worked episode | Complete | `examples/synthetic/gate1_multi_encounter_episode.json` |
| Schema-conformant expected intervals | Complete | `examples/synthetic/gate1_expected_intervals.json` |
| Schema-conformant expected transitions | Complete | `examples/synthetic/gate1_expected_transitions.json` |
| Provenance truth records | Complete for Gate 1 evidence | `examples/synthetic/gate1_provenance.json` |
| Automated validation tests authored | Complete | `tests/test_gate1_schemas.py` |
| Reproducible test environment declared | Complete | `pyproject.toml` |
| Validation tests executed successfully | Pending | execution/CI evidence required |

## Requirements addressed

This evidence covers the Phase 1 requirements associated with:

- `SCOPE-001` through `SCOPE-003`
- `DATA-001` through `DATA-005`
- `MODEL-001` through `MODEL-005`
- `TIME-001` through `TIME-004`
- `PROV-001` through `PROV-004`
- `GOV-001` through `GOV-004`

The authored tests specifically verify schema validity, canonical vocabulary consistency, and that mapping configuration targets only valid canonical states.

## Semantic defect corrected during gate review

Gate review identified an inconsistency in `care_transition.schema.json`: the transition schema used `inpatient_routine` while the canonical vocabulary and interval schema use `routine_inpatient`.

The transition schema has been corrected to use the canonical `routine_inpatient` state and now includes provenance and uncertainty fields aligned with the broader model.

This is exactly the type of cross-artifact inconsistency Gate 1 is intended to catch before the vocabulary becomes frozen.

## Hand-worked episode review

The Gate 1 synthetic episode demonstrates:

- a single therapy episode containing multiple encounters;
- infusion anchoring at Day 0;
- a broad routine-inpatient encounter;
- an embedded higher-priority ICU record;
- deterministic ICU precedence during overlap;
- return from ICU to routine inpatient care;
- discharge;
- later acute-care return;
- half-open interval boundaries;
- source-record and derived-artifact provenance.

The expected canonical trajectory is now separated into schema-conformant interval and transition truth sets so later reconstruction code can be compared directly against a fixed oracle.

## Machine-readable precedence contract

`config/synthetic_care_state_mapping.json` establishes a public test configuration with:

- source-label-to-canonical-state mappings;
- explicit numeric priorities;
- higher-priority-overlap behavior;
- deterministic tie-breaking by lexicographic source record ID;
- explicit `unknown` behavior for unmapped or irreconcilable records.

The configuration is synthetic-only. It demonstrates the contract without encoding institutional unit names.

## Automated validation contract

`tests/test_gate1_schemas.py` is intended to verify:

1. the therapy episode validates;
2. each encounter input validates;
3. all interval truth records validate;
4. all transition truth records validate;
5. provenance truth records validate;
6. the care-state vocabulary is identical across interval and transition schemas;
7. mapping targets are members of the canonical vocabulary.

## Remaining blocker

### Execute the Gate 1 test suite

Gate passage requires actual test evidence. The current repository contains the test contract but this evidence record does not claim the tests have executed successfully.

Required command in a clean development environment:

`python -m pip install -e '.[dev]'`

followed by:

`pytest`

If the tests fail, Phase 1 remains open until the schema, fixture, or semantic defect is corrected. If they pass, the evidence should be recorded here or in CI and Gate 1 may be evaluated for PASS.

## Candidate freeze set after passage

If Gate 1 passes, the following become controlled Phase 1 semantics:

- canonical care-state vocabulary;
- infusion-relative time convention;
- half-open interval semantics;
- encounter minimum input contract;
- provenance contract;
- synthetic mapping/precedence semantics used by the truth set;
- Gate 1 expected interval and transition objects.

Changes to these artifacts after gate passage require an explicit gate-impact review and corresponding fixture/test updates.

## Gate passage rule

Gate 1 -> 2 may pass when:

1. all Gate 1 schema and consistency tests execute successfully in a clean environment;
2. the hand-worked episode requires no undocumented semantic assumption;
3. expected intervals/transitions and their required provenance validate;
4. deterministic mapping/precedence behavior remains machine-testable;
5. the freeze set is explicitly accepted.

Until test execution evidence exists, Phase 2 fixture design may continue experimentally, but Phase 1 is not formally frozen.
