# CART-TRACE Access Extension — Gate 2B Source Observability Worksheet

**Status:** governed-validation preparation / non-operational

## Purpose

This worksheet records what a governed source can actually show for A0-A8 before mapping rules are promoted beyond synthetic validation. It is designed to prevent the research model from treating unavailable, ambiguous, or indirectly inferred information as observed fact.

## Source header

- `source_inventory_id`:
- `source_system_name`:
- `source_owner_or_steward`:
- `authorization_reference`:
- `date_range_reviewed`:
- `reviewer_role`:
- `review_date`:

## Observability scale

Use one label per concept:

- `direct`: explicit structured or documented value is present.
- `normalized`: source contains the concept, but controlled normalization is required.
- `partial`: only part of the required concept/timing/actor context is available.
- `derived`: value can be produced only by a documented research rule from attributable evidence.
- `absent`: source does not capture the concept.
- `unknown`: observability has not yet been established.

`derived` is not equivalent to `direct`, and `absent` must never be converted into a favorable status.

## Gate observability worksheet

| Gate | Research meaning | Observability | Native source concept/field | Timestamp available | Actor/authority available | Candidate status mapping | Known missingness | Prohibited inference | Reviewer confidence |
|---|---|---|---|---|---|---|---|---|---|
| A0 | Referral/case entry | unknown | | | | | | diagnosis alone does not establish referral | |
| A1 | Product-indication evidence available | unknown | | | | | | research algorithm does not establish clinical eligibility | |
| A2 | Dartmouth program review/acceptance | unknown | | | | | | payer approval does not establish program acceptance | |
| A3 | Facility/service pathway feasibility | unknown | | | | | | former REMS or generic certification does not establish current pathway feasibility | |
| A4 | Network/benefit applicability | unknown | | | | | | payer-family name alone does not establish member network/benefit status | |
| A5 | Medical necessity/prior authorization | unknown | | | | | | clinical candidacy does not establish payer authorization | |
| A6 | Medicare-specific coverage logic | unknown | | | | | | current FDA labeling alone does not establish Medicare administrative state | |
| A7 | Financial clearance | unknown | | | | | | authorization or scheduling does not establish financial clearance | |
| A8 | Access-ready research milestone | unknown | | | | | | A5 approval alone does not establish access-ready | |

## Field observability worksheet

| Target field | Observability | Source-native concept | Direct/normalized/derived | Missingness behavior | Authority | Validation method | Notes |
|---|---|---|---|---|---|---|---|
| patient_research_id | unknown | | | | research linkage | | |
| access_episode_id | unknown | | derived | | research derivation | | |
| source_record_id | unknown | | direct | | source system | | |
| gate_id | unknown | | derived | | research mapping | | |
| status | unknown | | | | source authority preserved | | |
| status_timestamp | unknown | | | | source system | | |
| decision_timestamp | unknown | | | | source authority | | |
| decision_actor_type | unknown | | | | source context | | |
| payer_name | unknown | | | | payer/benefit source | | |
| plan_product | unknown | | | | payer/benefit source | | |
| servicing_administrator | unknown | | | | payer/benefit source | | |
| policy_id | unknown | | | | payer/policy source | | |
| policy_version | unknown | | | | payer/policy source | | |
| policy_effective_date | unknown | | | | payer/policy source | | |
| reason_code | unknown | | | | asserting authority | | |
| facility_requirement_type | unknown | | | | asserting authority | | |
| evidence_completeness | unknown | | derived | | research derivation | | |
| uncertainty_flag | unknown | | derived | | research derivation | | |

## Timing review

For each source, document whether timestamps represent:

- event occurrence time;
- decision time;
- order/submission time;
- note/document creation time;
- ingestion/extraction time;
- later correction/update time.

Do not substitute one timestamp type for another without an explicit mapping rule and uncertainty label.

## Versioning review

- Can records be retrospectively edited? yes / no / unknown
- Is revision history available? yes / no / unknown
- Can historical payer/policy versions be recovered? yes / no / not applicable / unknown
- Can a corrected administrative decision be distinguished from the original decision? yes / no / unknown
- Does the source preserve event-time values or only current state? event-time / current-state / mixed / unknown

## Source-level conclusion

Choose one:

- [ ] observability established for governed review
- [ ] partially observable; mapping restrictions required
- [ ] source unsuitable for one or more proposed gates
- [ ] insufficient evidence to assess observability
- [ ] review blocked by authorization/governance

### Gates considered observable

`A__:`

### Gates considered partial

`A__:`

### Gates considered absent/non-observable

`A__:`

### Required restrictions or follow-up

-

## Scope guardrail

This worksheet describes data observability only. It does not establish clinical eligibility, treatment appropriateness, payer coverage, or readiness for care.