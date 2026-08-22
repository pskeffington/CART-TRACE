# CART-TRACE Access Extension — Gate 2 Provenance Audit Checklist

**Status:** governed-validation prerequisite / retrospective / non-operational

## Purpose

This checklist defines the minimum audit trail required before any governed Dartmouth source-to-event mapping can be treated as analytically usable in Access Gate 2B.

It is intentionally field-level. A mapped event is not considered auditable merely because the source system is known.

## Event-level provenance checks

For every governed normalized event, verify:

- [ ] `patient_research_id` is research-safe and generated under an approved linkage rule.
- [ ] `access_episode_id` can be traced to a versioned episode-construction rule.
- [ ] `event_id` is stable, unique, and reproducible.
- [ ] `source_record_id` points to a governed source record or approved surrogate reference.
- [ ] `source_type` matches the actual source class.
- [ ] `decision_actor_type` reflects the authority that asserted the state.
- [ ] `gate_id` is assigned by a documented mapping rule.
- [ ] `status` is either directly observed or normalized by an explicit rule.
- [ ] `status_timestamp` comes from a known source field or documented fallback.
- [ ] `decision_timestamp` is not silently substituted when unavailable.
- [ ] fallback timing sets `uncertainty_flag=true` where required.
- [ ] `provenance.rule_version` identifies the transformation used.
- [ ] no free-text interpretation silently changes source authority.

## Payer and policy provenance

Where payer/policy fields are populated, verify:

- [ ] payer entity is attributable to the source record.
- [ ] plan/product is preserved separately from payer family.
- [ ] line of business is known or explicitly unknown.
- [ ] servicing administrator is preserved where applicable.
- [ ] state/service area is preserved where relevant.
- [ ] requested CAR-T product is source-grounded rather than inferred from payer family.
- [ ] policy ID is attributable to the contemporaneous source.
- [ ] policy version/effective date reflects the event-time policy state.
- [ ] historical events are not backfilled to a newer policy version.
- [ ] CMS/FDA/payer authority is kept distinct when requirements overlap.

## Authority separation

Confirm that the normalization process does not collapse:

- [ ] Dartmouth program review into payer medical necessity.
- [ ] payer approval into Dartmouth clinical candidacy.
- [ ] payer approval into A8 access readiness.
- [ ] financial clearance into medical eligibility.
- [ ] network/site rules into medical-necessity denial.
- [ ] former FDA REMS status into payer site-of-care requirements.
- [ ] FACT IEC expectations into regulatory certification.
- [ ] research-derived status into a source-authority assertion.

## Missingness and conflict checks

For each field/gate under review:

- [ ] structural missingness is distinguished from true absence.
- [ ] unobservable gates remain absent/unknown rather than satisfied.
- [ ] conflicting source records are retained.
- [ ] corrected/superseding records do not erase earlier history.
- [ ] same-time events remain deterministically ordered without deleting source history.
- [ ] unresolved authority conflicts set uncertainty.
- [ ] incomplete source windows are documented.
- [ ] mutable/overwritten source systems are identified in the source inventory.

## Small-sample governed validation packet

For each hand-reviewed retrospective episode, the validation packet should contain only governed references and approved derivatives:

1. research episode identifier;
2. list of source inventory IDs used;
3. source-record references;
4. normalized event sequence;
5. transformation rule version;
6. field-level uncertainties;
7. conflicts or corrections encountered;
8. reviewer disposition: agree / disagree / insufficient evidence;
9. discrepancy class when reviewer and mapper differ;
10. confirmation that no prospective recommendation was produced.

## Canonical discrepancy taxonomy

Use the discrepancy classes defined in `access_gate_2_discrepancy_review_template.md`. The canonical classes are:

- `SOURCE_MISSING`
- `SOURCE_CONFLICT`
- `TIMESTAMP_CONFLICT`
- `ACTOR_AUTHORITY_CONFLICT`
- `STATUS_NORMALIZATION_ERROR`
- `GATE_ASSIGNMENT_ERROR`
- `POLICY_VERSION_MISMATCH`
- `EPISODE_LINKAGE_ERROR`
- `DERIVATION_ERROR`
- `SCHEMA_ERROR`
- `UNSUPPORTED_INFERENCE`
- `PHI_EXPORT_RISK`
- `NOT_OBSERVABLE`
- `OTHER`

Do not maintain a second discrepancy vocabulary in the provenance audit. A discrepancy may use one primary class and optional secondary classes under the canonical template.

Discrepancies must not be silently corrected by changing the source record or overwriting the first-pass mapped result. The correction path should be auditable and versioned.

## Public-export audit

Before any research derivative leaves the governed environment:

- [ ] no direct identifiers are present.
- [ ] no source free text is exported unless specifically approved.
- [ ] source-record identifiers are removed or replaced by safe research references as required.
- [ ] dates/times follow the approved de-identification or limited-dataset policy.
- [ ] small-cell or rare-event disclosure risk has been reviewed where applicable.
- [ ] payer/member-specific benefit information is not represented as a public coverage determination.
- [ ] output language remains retrospective and non-operational.

## Gate 2B audit acceptance criteria

The provenance audit is acceptable only when:

1. every analytically used field can be traced to source + actor + transformation;
2. uncertainty and missingness are explicit;
3. policy version is event-time aware;
4. authority boundaries remain intact;
5. discrepancies are measured rather than hidden;
6. a small governed sample has documented human review;
7. public-export checks pass;
8. institutional authorization covers the activity.

Passing this checklist would support governed retrospective mapping validity only. It would not establish clinical validity, coverage correctness, treatment readiness, or prospective decision-support authorization.
