# CART-TRACE Access Extension — Gate 2 Synthetic Source Surrogate Specification

**Status:** synthetic-only / non-operational / pre-governed validation

## Purpose

Gate 2 needs a source-like test layer that sits upstream of `access_gate_event.schema.json`. This surrogate specification defines synthetic records that resemble source-system classes closely enough to test mapping, provenance, missingness, conflict handling, and policy-version attachment without containing PHI or reproducing Dartmouth internal workflow content.

The surrogate is not a model of Dartmouth operations. It is a mapping test harness.

## Core boundary

Synthetic source records may test whether transformation rules behave deterministically. They may not be used to claim:

- Dartmouth workflow validity;
- real source-field availability;
- patient clinical eligibility;
- payer coverage correctness;
- authorization correctness;
- financial-clearance correctness;
- treatment readiness.

## Synthetic source classes

Minimum source classes:

1. `synthetic_referral`
2. `synthetic_program_review`
3. `synthetic_facility_logistics`
4. `synthetic_benefit_network`
5. `synthetic_authorization`
6. `synthetic_medicare_policy_context`
7. `synthetic_financial_clearance`
8. `synthetic_research_derivation`

Each record must include:

- `synthetic_source_id`
- `synthetic_patient_id`
- `synthetic_episode_id`
- `source_class`
- `source_timestamp`
- `actor_type`
- `source_status`
- `source_status_code` when applicable
- `policy_version` when applicable
- `source_version`
- `synthetic: true`

Optional source-specific fields may be added only when they support a documented mapping test.

## Required surrogate scenarios

### S2-001 — direct referral mapping

Input: explicit referral-received source event.

Expected mapping:

- A0 event created;
- actor remains `referring_clinician` or appropriate intake actor;
- referral timestamp preserved;
- no A1/A2 status inferred.

### S2-002 — payer approval without access-ready

Input: A5-like authorization approval record with no financial-clearance or A8 milestone evidence.

Expected mapping:

- A5 `approved` event created;
- A8 absent or unresolved;
- `access_ready` remains false/unknown at episode reconstruction.

### S2-003 — missing decision timestamp

Input: authorization record with document timestamp but no explicit decision time.

Expected mapping:

- `status_timestamp` may use documented fallback under mapping rule;
- `decision_timestamp` remains null/unknown;
- `uncertainty_flag=true`.

### S2-004 — conflicting authorization records

Input: same episode contains an approval event followed by a corrected denial record, or vice versa.

Expected mapping:

- both source events preserved;
- provenance retained separately;
- no silent overwrite;
- terminal research state determined by explicit sequencing rule only.

### S2-005 — policy-version drift

Input: authorization history spans policy `v1` and `v2`.

Expected mapping:

- each event retains contemporaneous version;
- drift flag becomes true;
- no historical event is backfilled to current policy.

### S2-006 — network denial distinct from medical necessity

Input: explicit network/site denial.

Expected mapping:

- typed as `denied_network_or_site`;
- not recoded as clinical or medical-necessity failure.

### S2-007 — financial delay after authorization

Input: A5 approval plus A7 pending then satisfied.

Expected mapping:

- authorization remains approved;
- financial delay represented separately;
- A8 may become satisfied only if governed synthetic rule prerequisites are met.

### S2-008 — program acceptance distinct from payer approval

Input: Dartmouth-program-like synthetic review source and separate payer source.

Expected mapping:

- A2 state comes only from program source;
- A5 state comes only from payer source;
- actor authority remains distinct.

### S2-009 — facility requirement authority typing

Input: synthetic source includes a payer site-of-care requirement and a separate FACT expectation.

Expected mapping:

- two typed facility requirement events/attributes;
- never collapsed into generic `certified_center=true`.

### S2-010 — unobservable gate

Input: episode lacks any valid A7 source.

Expected mapping:

- A7 remains absent/unknown;
- mapper does not infer financial clearance from payer approval or scheduling.

## Mapping test requirements

A future Gate 2 mapper should demonstrate:

1. deterministic output for reordered source input;
2. stable source-to-event identifiers;
3. preservation of source authority;
4. preservation of policy version;
5. explicit missingness and uncertainty;
6. conflict preservation;
7. no-PHI fixtures;
8. event-schema validation for every mapped output;
9. no inference of A8 from A5 alone;
10. no clinical-eligibility inference from payer or administrative sources.

## Provenance contract

Every mapped event must carry enough information to reconstruct:

`synthetic source record -> mapping rule version -> normalized access event -> episode reconstruction output`

For the synthetic harness, this should include at minimum:

- `source_record_id`
- `source_type`
- `provenance.synthetic=true`
- `provenance.rule_version`
- source version or fixture version where supported

## Promotion boundary

Passing synthetic surrogate tests means only that the mapping software behaves according to the public research contract. It does not establish that Dartmouth source systems contain equivalent fields or that the same transformations are institutionally valid.

Governed source inventory review and institutional approval remain mandatory before any real-record validation begins.
