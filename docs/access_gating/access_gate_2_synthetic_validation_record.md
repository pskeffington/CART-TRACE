# CART-TRACE Access Extension — Gate 2 Synthetic Mapping Validation Record

## Gate scope

**Validation lane:** Access Gate 2A — synthetic source-to-field mapping

**Base:** `main` at merge commit `4fe306161246f17715b178880cd6f45b425d5203`

**Validation date:** 2026-08-21

## Decision

- [x] PASS — synthetic mapping layer
- [ ] CONDITIONAL PASS
- [ ] FAIL

This PASS applies only to the synthetic source-mapping layer. It does **not** mean Access Gate 2 as a governed institutional validation gate has passed.

## Evidence

The validated Gate 2A package contains:

- `docs/access_gating/access_gate_2_source_field_contract.md`
- `docs/access_gating/access_gate_2_governed_source_inventory_template.md`
- `docs/access_gating/access_gate_2_observability_matrix.md`
- `docs/access_gating/access_gate_2_synthetic_source_surrogate_spec.md`
- `examples/synthetic/access_gate_2_source_surrogates.json`
- `cart_trace/access_source_mapping.py`
- `tests/test_access_source_mapping.py`
- `schemas/access_gate_event.schema.json`

## CI evidence

GitHub Actions run `32502337117` validated corrected head `d3a030ef6d2c8432b61e4ca95d9fbee9f1d5fd3e` immediately before merge.

Both validation jobs passed:

- Python 3.11 — PASS
- Python 3.12 — PASS

The validated head was squash-merged to `main` as `4fe306161246f17715b178880cd6f45b425d5203`.

## Defect found and closed during validation

The first Gate 2 mapper run exposed an interface mismatch between two valid event representations:

1. the Gate 1 compact oracle used relative `hour` values;
2. the Gate 2 source mapper emitted schema-native `status_timestamp` / `decision_timestamp` values.

The reconstruction layer originally assumed every event contained `hour`, causing `KeyError: 'hour'` across Gate 2 mapping tests.

Commit `d3a030ef6d2c8432b61e4ca95d9fbee9f1d5fd3e` closed the defect by introducing a common event-time adapter that accepts either compact relative time or schema-native timestamps. Existing compact-oracle behavior remains unchanged.

## Synthetic mapping assertions validated

The current automated contract demonstrates that:

1. synthetic source input maps deterministically to access events;
2. mapped access events validate against `access_gate_event.schema.json`;
3. referral evidence does not imply program acceptance;
4. payer approval does not imply `access_ready`;
5. missing decision timestamps remain uncertain rather than silently invented;
6. conflicting authorization records remain preserved;
7. policy versions remain attached to contemporaneous events;
8. network/site denial remains distinct from medical-necessity denial;
9. financial clearance remains distinct from payer authorization;
10. Dartmouth-program-like and payer-like synthetic authorities remain separate;
11. facility requirements remain authority-typed rather than collapsed into a generic certification flag;
12. absent A7 evidence does not produce inferred financial clearance;
13. non-synthetic input is rejected by the synthetic mapper.

## What this PASS establishes

Gate 2A establishes that the public synthetic transformation contract is internally reproducible and schema-compatible.

It supports the following research-development claim only:

> Source-like synthetic administrative records can be transformed into deterministic, provenance-aware access-gating events without collapsing payer, hospital, financial, and research authorities.

## What this PASS does not establish

It does not establish:

- that Dartmouth Health source systems contain equivalent fields;
- that the proposed source mappings are institutionally valid;
- that payer policies accurately represent a specific member's benefits;
- that Dartmouth clinical candidacy can be inferred from administrative records;
- that administrative `access_ready` equals clinical treatment readiness;
- that any prospective workflow or decision-support use is authorized;
- that governed PHI may be accessed or exported.

## Remaining Gate 2B governed-validation prerequisites

Before governed retrospective validation may begin, the project still requires:

1. an institutionally approved source inventory;
2. documented source ownership/stewardship;
3. approved minimum-necessary data scope;
4. source-to-field mapping review by authorized personnel;
5. explicit observability labels for A0-A8 using real source systems;
6. approved linkage and research-identifier handling;
7. provenance audit from source record to normalized event;
8. uncertainty/conflict review on a small governed sample;
9. no-PHI public-export verification;
10. confirmation that the research remains retrospective and non-operational.

## Gate status

**Access Gate 2A:** PASS

**Access Gate 2B governed source validation:** NOT STARTED / authorization-dependent

**Overall Access Gate 2:** IN PROGRESS
