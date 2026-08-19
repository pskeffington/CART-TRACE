# Synthetic CAR-T Access-Gating Oracle Specification

## Purpose

This specification defines the first deterministic truth set for the Dartmouth Health CAR-T hospital/insurance access extension. It mirrors the repository's existing synthetic-first methodology while remaining explicitly outside the frozen MS Health Data Science capstone core.

The oracle is intended to test whether a future retrospective access-reconstruction implementation can reproduce prespecified administrative states, delays, and terminal outcomes from synthetic events. It is not a clinical eligibility model, insurance adjudication engine, or treatment-readiness tool.

## Canonical synthetic assets

- `schemas/access_gate_event.schema.json`
- `examples/synthetic/access_gating_oracle.json`

## Gate vocabulary

- `A0` referral / case entry
- `A1` product-indication evidence available
- `A2` Dartmouth program review / acceptance
- `A3` facility and service-pathway feasibility
- `A4` payer network / benefit applicability
- `A5` medical-necessity / prior-authorization determination
- `A6` Medicare-specific coverage logic when applicable
- `A7` financial clearance
- `A8` aggregate access-ready milestone

## Oracle cases

| Case | Expected terminal condition | Primary analytic feature |
|---|---|---|
| AG-001 | approved / access-ready | straight-through approval |
| AG-002 | approved / access-ready | additional-information delay |
| AG-003 | final denial | medical-necessity denial |
| AG-004 | benefit exclusion | benefit-design barrier |
| AG-005 | network/site denial | site/network barrier |
| AG-006 | approved after reconsideration | peer-to-peer overturn |
| AG-007 | approved after appeal | formal appeal overturn |
| AG-008 | expired / not access-ready | authorization expiration |
| AG-009 | approved under changed policy | policy-version drift |
| AG-010 | approved / access-ready | financial-clearance delay |

## Deterministic derivation rules

### Terminal authorization status

For each episode, select the last observed `A5` status in event-time order. A later `approved` event supersedes a preceding denial only when the record explicitly contains an intervening reconsideration/appeal state or an overturned status.

### Access-ready

`access_ready = true` only when an `A8 = satisfied` event exists.

No algorithm may infer `A8 = satisfied` solely from an `A5 = approved` event because financial, network, or administrative conditions may remain unresolved.

### Authorization turnaround

When defined:

`authorization_turnaround_hours = first terminal A5 decision time - first submitted_pending A5 time`

For cases with additional-information requests or appeals, the total turnaround remains inclusive of those delays unless a component metric is explicitly calculated.

### Information-request delay

For a sequence containing `additional_information_requested` followed by a resubmitted `submitted_pending` event:

`information_request_delay_hours = resubmission time - information request time`

### Appeal/reconsideration delay

For an initial denial followed by eventual overturn/approval:

`appeal_or_reconsideration_delay_hours = overturn time - initial denial time`

### Financial-clearance delay

When financial clearance becomes pending after payer approval:

`financial_clearance_delay_hours = A7 satisfied time - A7 pending time`

### Referral-to-access-ready

`referral_to_access_ready_hours = A8 satisfied time - first A0 satisfied time`

### Policy drift

`policy_drift_flag = true` when more than one non-null `policy_version` is observed in the same access episode.

Every decision event must retain its contemporaneous policy version. The implementation must not rewrite historical decisions against the newest policy.

## Invariants

1. `approved` does not imply `access_ready`.
2. `program acceptance` does not imply payer coverage.
3. `payer denial` does not imply Dartmouth clinical ineligibility.
4. `financial-clearance delay` must never be encoded as medical ineligibility.
5. `network/site denial` must remain distinguishable from medical-necessity denial.
6. `benefit exclusion` must remain distinguishable from medical-necessity denial.
7. An overturned denial must retain the initial denial event; history is append-only.
8. A policy change must preserve both old and new policy versions in the episode history.
9. Former FDA REMS requirements, payer site-of-care restrictions, FACT accreditation expectations, and network-contract constraints must remain typed separately.
10. Synthetic events must never contain real member identifiers, real authorization numbers, or protected health information.

## Expected future validation tests

A future implementation should test at minimum:

- schema validation for all synthetic event objects;
- stable sorting by timestamp and event identifier;
- exact expected terminal status for all ten cases;
- exact expected delay values;
- no false access-ready inference from payer approval alone;
- preservation of initial denial after overturn;
- correct classification of benefit, network/site, medical-necessity, expiration, and financial barriers;
- policy-version drift detection;
- deterministic repeated output across runs.

## Scope boundary

Passing this oracle would establish only that an administrative access-reconstruction algorithm behaves deterministically against synthetic expected cases. It would not establish:

- clinical validity;
- payer-contract correctness;
- Dartmouth workflow validity;
- Medicare claims correctness;
- prospective decision-support safety;
- individual coverage or eligibility.

Those require separate governed validation and appropriate institutional authorization.
