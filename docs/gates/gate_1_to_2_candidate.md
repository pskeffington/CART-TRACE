# Gate 1 -> 2 Evidence Record

**Transition:** Phase 1 — Episode and transition schema -> Phase 2 — Synthetic cohort

**Decision:** PASS

Gate 1 is passed. The canonical schemas, governance boundary, time semantics, machine-readable mapping rules, schema-conformant truth sets, provenance records, and automated validation tests are present. GitHub Actions run `31648451451` completed successfully for commit `942b9864b5454537c091d3a4a322d60b36e75048` using the `Validate Gate 1` workflow.

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
| Provenance truth records | Complete | `examples/synthetic/gate1_provenance.json` |
| Automated validation tests | Complete | `tests/test_gate1_schemas.py` |
| Reproducible test environment | Complete | `pyproject.toml` |
| CI execution | PASS | GitHub Actions run `31648451451` |

## Requirements addressed

This gate closes the Phase 1 requirements associated with:

- `SCOPE-001` through `SCOPE-003`
- `DATA-001` through `DATA-005`
- `MODEL-001` through `MODEL-005`
- `TIME-001` through `TIME-004`
- `PROV-001` through `PROV-004`
- `GOV-001` through `GOV-004`

## Semantic defect corrected during gate review

Gate review identified an inconsistency in `care_transition.schema.json`: the transition schema used `inpatient_routine` while the canonical vocabulary and interval schema used `routine_inpatient`.

The transition schema was corrected before gate passage. This defect is retained in the gate record because it demonstrates the value of semantic freeze review before downstream fixture and reconstruction work.

## Hand-worked episode evidence

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

The expected trajectory is represented as schema-conformant interval and transition truth sets suitable for direct comparison with future reconstruction code.

## Frozen Phase 1 semantics

The following artifacts and semantics are now controlled by Gate 1:

- canonical care-state vocabulary;
- infusion-relative time convention;
- half-open interval semantics;
- encounter minimum input contract;
- provenance contract;
- synthetic mapping/precedence semantics;
- Gate 1 expected interval and transition objects.

Changes to these items require explicit gate-impact review and corresponding fixture/test updates.

## Authorized next phase

Phase 2 — Synthetic cohort is authorized.

Phase 2 should now focus on:

1. completing the six required trajectory truth sets;
2. ensuring every fixture has expected intervals, transitions, uncertainty behavior, and utilization metrics;
3. adding requirement-coverage tests for the fixture manifest;
4. adding invalid/edge-case fixtures for schema and reconstruction failure behavior;
5. preparing Gate 2 -> 3 evidence only when the fixture set functions as a complete oracle for reconstruction testing.
