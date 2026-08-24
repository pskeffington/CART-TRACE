# CART-TRACE Access Extension — Gate 3A Candidate Validation Record

## Status

**CANDIDATE — implementation complete for this pass / CI confirmation pending**

This record applies only to the synthetic retrospective administrative metric layer. It does not establish governed Dartmouth Health source validity, clinical eligibility, payer correctness, treatment readiness, or authorization to process institutional data.

## Candidate head

The Gate 3A implementation pass adds:

- `schemas/access_metric_result.schema.json`;
- `ACCESS_METRIC_CONTRACT_VERSION = 1.0.0`;
- `derive_access_metric_results()` in `cart_trace/access_gating.py`;
- schema and provenance validation tests in `tests/test_access_gating.py`.

## Implemented behavior

The candidate metric layer now produces nine episode-level result records:

1. `referral_to_access_ready_hours`;
2. `authorization_turnaround_hours`;
3. `information_request_delay_hours`;
4. `appeal_or_reconsideration_delay_hours`;
5. `financial_clearance_delay_hours`;
6. `referral_to_terminal_hours`;
7. `access_ready`;
8. `policy_drift_flag`;
9. `primary_barrier`.

Each result carries:

- metric contract version;
- explicit ascertainment state;
- value and unit;
- contributing event IDs;
- contributing gate IDs;
- policy versions observed;
- mapping/rule versions;
- synthetic provenance flag;
- uncertainty flag;
- missingness reason when applicable.

## Candidate safeguards

The implementation explicitly preserves these invariants:

- payer approval alone does not produce access-ready status;
- missing or not-applicable delays are represented as `null`, never zero;
- absence of an A8 terminal event is treated as insufficient follow-up rather than terminal non-progression;
- denial, network/site, benefit, expiration, financial, and policy-drift barriers remain distinct;
- overturned denials preserve the earlier denial event in the event history;
- derived outputs are deterministic under input-order reversal;
- policy versions remain attached to the historical episode rather than being silently rewritten;
- synthetic materialized events remain the validation source for Gate 3A.

## Added validation coverage

The test suite now includes checks for:

- Access Gate 3 metric-result JSON-schema validity across all ten frozen oracle cases;
- exact episode ID and metric-contract version propagation;
- synthetic provenance preservation;
- contributing event and gate provenance for information-request delay;
- explicit A8 requirement for access-ready timing;
- missing metrics remaining null instead of zero;
- policy-version drift preservation;
- deterministic output under reversed input order.

## Remaining Gate 3A work

Before Gate 3A can be marked PASS:

1. confirm the full repository test suite passes on supported Python versions;
2. add cohort-level denominator-aware summaries for access-ready, barrier classes, gate reach, and metric availability;
3. add explicit synthetic fixtures/tests for repeated information-request cycles;
4. add explicit synthetic fixtures/tests for multiple appeal/reconsideration events;
5. add invalid temporal-order fixtures that exercise the metric ascertainment state directly;
6. generate a deterministic synthetic Gate 3 summary artifact;
7. record CI run identifiers and validated commit head.

## Governed boundary

**Access Gate 2B governed source validation:** NOT STARTED / authorization-dependent.

**Access Gate 3B governed representation validity:** NOT STARTED / blocked on Gate 2B governed source validation and institutional authorization.

A future Gate 3A synthetic PASS must not be described as evidence that Dartmouth source fields, payer decisions, clinical criteria, or institutional workflows have been validated.
