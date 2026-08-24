# CART-TRACE Access Extension — Gate 3 Retrospective Metric Contract

## Status

**Synthetic-first research specification / non-operational / governed validation pending**

This contract defines the next unblocked phase of the Dartmouth Health CAR-T administrative access extension. It does not change the frozen MS Health Data Science capstone and does not determine clinical eligibility, insurance coverage, prior-authorization entitlement, financial approval, or treatment readiness.

Access Gate 2B governed source validation remains authorization-dependent. Gate 3 may therefore proceed only as a synthetic and methodological specification until approved institutional source data and local mappings are available.

## Gate 3 research question

> Can versioned longitudinal administrative access events be transformed into reproducible, provenance-preserving measures of delay, attrition, and barrier type without converting the framework into prospective eligibility or authorization decision support?

## Unit of analysis

The primary unit is the **administrative access episode**, identified by `access_episode_id` and beginning at the first valid `A0 = satisfied` referral/case-entry event.

An episode may terminate in:

- `A8 = satisfied` — access-ready administrative milestone reached;
- `A8 = not_satisfied` — terminal administrative non-progression explicitly recorded;
- payer terminal state without A8 resolution;
- authorization expiration;
- loss of observable follow-up;
- unresolved/unknown status.

No terminal state may be inferred from absence alone.

## Frozen metric families

### M1 — Referral-to-access-ready time

**Definition**

`referral_to_access_ready_hours = first A8 satisfied timestamp - first A0 satisfied timestamp`

**Eligible when**

- at least one valid `A0 = satisfied` event exists;
- at least one valid `A8 = satisfied` event exists;
- event ordering is non-negative after normalization.

**Not eligible when**

- no A8 satisfied event exists;
- referral timestamp is unavailable;
- temporal provenance is invalid or unresolved.

This metric must never be calculated by substituting payer approval for A8.

### M2 — Authorization turnaround time

**Definition**

`authorization_turnaround_hours = first terminal A5 decision after first submitted_pending - first A5 submitted_pending`

Terminal first-decision states include:

- `approved`;
- `denied_medical_necessity`;
- `denied_benefit_exclusion`;
- `denied_network_or_site`;
- `denied_missing_authorization`.

The primary turnaround metric measures the initial payer decision interval. Later appeal/reconsideration time is measured separately.

### M3 — Information-request delay

**Definition**

`information_request_delay_hours = first A5 resubmitted_pending after additional_information_requested - first A5 additional_information_requested`

If multiple information-request cycles occur, preserve each component interval in governed implementations and report both episode count and cumulative delay. The synthetic Gate 3 baseline may begin with the first frozen cycle while retaining an explicit extension path for repeated cycles.

### M4 — Appeal or reconsideration delay

**Definition**

`appeal_or_reconsideration_delay_hours = first overturned_on_reconsideration_or_appeal - first qualifying A5 denial`

The initial denial event remains append-only and must not be overwritten by the later approval.

### M5 — Financial-clearance delay

**Definition**

`financial_clearance_delay_hours = first A7 satisfied after A7 pending - first A7 pending`

Financial delay is an administrative access measure and must never be encoded as clinical ineligibility or payer medical-necessity denial.

### M6 — Referral-to-terminal administrative disposition

**Definition**

`referral_to_terminal_hours = first explicit A8 not_satisfied timestamp - first A0 satisfied timestamp`

This metric requires an explicit terminal non-progression event. Lack of A8 satisfaction alone is not a terminal disposition.

### M7 — Barrier classification

Each episode may retain multiple observed barriers, but the primary synthetic summary must preserve at minimum these mutually distinguishable classes:

- `denied_medical_necessity`;
- `denied_benefit_exclusion`;
- `denied_network_or_site`;
- `denied_missing_authorization`;
- `authorization_expired`;
- `additional_information_requested`;
- `appeal_delay`;
- `initial_medical_necessity_denial`;
- `financial_clearance_delay`;
- `policy_change_during_episode`;
- `unknown_or_unresolved`.

A barrier class describes the administrative record. It does not imply clinical candidacy, causal attribution, or fault.

### M8 — Access-ready proportion

**Episode-level indicator**

`access_ready = true` only when `A8 = satisfied` is explicitly present.

**Cohort summary**

`access_ready_proportion = count(access_ready = true) / count(episodes eligible for the defined cohort denominator)`

The denominator definition must be declared before analysis and must not silently exclude unresolved episodes.

### M9 — Stage reach / attrition

For each access gate `A0` through `A8`, report:

- number and proportion of cohort episodes with at least one observable event for the gate;
- number and proportion satisfying the gate when the gate uses satisfaction semantics;
- number and proportion with explicit non-satisfaction/denial/expiration when applicable;
- number and proportion unresolved or unobservable.

Progression between gates must not be interpreted as a clinical funnel unless the governed Dartmouth workflow validates that interpretation.

### M10 — Policy-version drift

**Definition**

`policy_drift_flag = true` when more than one non-null policy version is observed within an episode for the policy-governed decision pathway being analyzed.

Historical events must remain associated with the contemporaneous version. Re-analysis against the newest policy must be a separately labeled sensitivity analysis rather than silent rewriting.

## Missingness and uncertainty states

Every metric must resolve to one of:

- `observed` — calculable from valid source events;
- `not_applicable` — metric does not apply to the episode;
- `not_observable` — required source domain is unavailable;
- `insufficient_followup` — episode could still progress but follow-up is incomplete;
- `invalid_temporal_order` — timestamps contradict required event order;
- `unresolved_mapping` — source-to-event mapping is not validated;
- `unknown` — evidence is insufficient for a more specific state.

Numeric zero is a valid value only when the timestamps support a true zero-duration interval. Missing or unknown values must never be coerced to zero.

## Cohort denominator contract

Every aggregate report must state:

1. cohort entry rule;
2. observation window;
3. source systems included;
4. governed mapping version;
5. policy-version handling rule;
6. minimum follow-up rule;
7. exclusion rules, if any;
8. unresolved episode count;
9. metric-specific eligible denominator.

Aggregate rates without an explicit denominator and missingness accounting fail Gate 3.

## Provenance requirements

Every episode-level metric result should preserve or link to:

- `access_episode_id`;
- metric identifier and metric-contract version;
- contributing event IDs;
- contributing gate IDs;
- source-system provenance;
- source policy ID/version/effective date when relevant;
- mapping-rule version;
- calculation timestamp/version;
- uncertainty/missingness state;
- synthetic/governed provenance flag.

## Synthetic Gate 3 validation requirements

Gate 3 synthetic validation should demonstrate:

1. exact agreement with the frozen oracle expectations for existing delay metrics;
2. order-invariant deterministic output;
3. explicit A8 requirement for access-ready status;
4. preservation of initial denials after overturn;
5. distinct benefit, network/site, medical-necessity, expiration, and financial barriers;
6. correct policy-drift detection;
7. no conversion of unknown/missing metrics to zero;
8. explicit denominator reporting for cohort summaries;
9. stable results across repeated runs;
10. no patient identifiers, real authorization numbers, or PHI in synthetic fixtures.

## Gate 3 pass criteria

### Gate 3A — synthetic metric validity

May be marked **PASS** when:

- the metric contract is frozen and versioned;
- episode-level metrics are implemented against synthetic fixtures;
- cohort-level summaries use explicit denominators and missingness states;
- all frozen oracle cases pass exact expected-value tests;
- deterministic/order-invariance tests pass;
- provenance links from metric results to contributing events are test-covered;
- CI passes on supported Python versions.

### Gate 3B — governed representation validity

Remains **NOT STARTED / AUTHORIZATION-DEPENDENT** until:

- Access Gate 2B governed source validation is complete;
- approved local mappings establish which source events can support each metric;
- domain reviewers confirm event semantics and denominator interpretation;
- governed temporal/discrepancy review is completed;
- permitted aggregate output rules are confirmed.

A Gate 3A synthetic PASS must not be represented as Gate 3B governed validity.

## Immediate implementation backlog

1. Add a versioned episode-level `access_metric_result` representation.
2. Refactor current reconstruction outputs into named metric results without changing frozen oracle expectations.
3. Add explicit metric missingness/ascertainment states.
4. Add cohort summarization for access-ready, barrier classes, gate reach, and metric availability.
5. Add provenance links from each derived metric to contributing synthetic event IDs.
6. Add tests for unresolved follow-up, absent A8, repeated information requests, multiple appeal events, and invalid temporal order.
7. Generate a deterministic synthetic Gate 3 summary artifact.
8. Record CI evidence in an Access Gate 3A validation record.
9. Keep Gate 3B blocked until governed source authorization and Gate 2B validation are complete.

## Scope boundary

Gate 3 measures retrospective administrative process behavior. It does not predict access, recommend an appeal, determine whether a payer should approve therapy, establish clinical eligibility, or determine treatment readiness.
