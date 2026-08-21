# CART-TRACE Access Extension — Gate 2 Source-to-Field Mapping Contract

**Status:** planning artifact / non-operational / governed-validation prerequisite

## Purpose

Access Gate 2 defines how retrospective source records may be mapped into the synthetic access-gating event model without converting the extension into a clinical eligibility engine, payer adjudication tool, or prospective workflow system.

The contract is intentionally source-oriented. It specifies what categories of evidence may populate each field, which transformations are permissible, and which interpretations remain prohibited unless separately governed by Dartmouth Health.

## Core rule

Every populated event field must answer three questions:

1. **What source record supports this value?**
2. **Which actor or authority asserted it?**
3. **Was the value observed, transcribed, normalized, or derived?**

No field may silently change authority during normalization. A payer rule remains a payer rule; a Dartmouth program note remains a Dartmouth program assertion; a financial-services record remains a financial-access record.

## Governed source classes

| Source class | Examples | Primary use | Prohibited interpretation |
|---|---|---|---|
| Referral records | referral order, referral intake, scheduling intake | A0 case entry and timestamps | clinical eligibility |
| Dartmouth clinical/program review | committee note, cellular-therapy program review, specialist assessment | A1/A2 evidence and program-review status | payer coverage |
| Facility/logistics records | treatment-center capability, scheduling/logistics, accreditation documentation | A3 feasibility evidence | universal regulatory certification |
| Payer/benefit records | eligibility response, benefit document, authorization record, denial letter | A4/A5/A6 administrative state | Dartmouth clinical candidacy |
| Financial-services records | financial clearance, assistance workflow, patient-liability review | A7 financial-access state | medical necessity |
| Derived research records | normalized event rows, reconciled status history, calculated intervals | A8/research metrics when rule is explicit | new clinical or coverage decision |

## Field-level contract

### Identity and episode fields

- `patient_research_id`
  - Source: governed study crosswalk only.
  - Transformation: irreversible or governed research identifier.
  - Prohibited: direct identifiers in public fixtures or outputs.
- `access_episode_id`
  - Source: research-derived episode grouping.
  - Transformation: deterministic episode construction rule must be versioned.
- `event_id`
  - Source: research derivation.
  - Transformation: deterministic and unique within episode.

### Gate and status fields

- `gate_id`
  - Source: research mapping from source class and documented event meaning.
  - Rule: A0-A8 meanings are fixed by Access Gate 1.
- `gate_domain`
  - Source: deterministic lookup from `gate_id`.
- `status`
  - Source: explicit source assertion or a narrowly documented normalization rule.
  - Prohibited: inferring favorable status from absence of contrary evidence.
- `status_timestamp`
  - Source: source-event timestamp where available.
  - Fallback: documented record timestamp with uncertainty flag if event time unavailable.
- `decision_timestamp`
  - Source: explicit decision time when present.
  - Prohibited: substituting extraction time for decision time without labeling.

### Authority and provenance

- `decision_actor_type`
  - Source: actor/record context.
  - Rule: actor authority must remain typed.
- `source_type`
  - Source: source-system/document class.
- `source_record_id`
  - Source: governed record identifier or research-safe surrogate.
- `provenance.synthetic`
  - Must be `false` for governed retrospective records and `true` only for fixtures.
- `provenance.rule_version`
  - Required for all derived or normalized events.

### Payer and policy fields

- `payer_name`
- `plan_product`
- `line_of_business`
- `servicing_administrator`
- `state_service_area`
- `requested_product`
- `policy_id`
- `policy_version`
- `policy_effective_date`

Rules:

1. Populate only from an attributable benefit, payer, policy, or authorization source.
2. Preserve plan/product and servicing administrator separately from payer family.
3. Preserve policy version at event time.
4. Do not backfill historical events using the newest available policy version.
5. Unknown plan or policy attributes remain `unknown`/null rather than guessed.

### Barrier and reason fields

- `reason_code`
  - Source: explicit structured code when available, otherwise research normalization from documented text.
- `reason_text_original`
  - Governed environment only; public derivatives should not expose sensitive source text.
- Barrier categories must preserve at least:
  - medical necessity;
  - benefit exclusion;
  - network/site;
  - missing authorization;
  - expiration;
  - financial clearance delay.

A denial must never be recoded as Dartmouth clinical ineligibility unless a separate Dartmouth clinical source explicitly states that conclusion.

### Facility requirement fields

`facility_requirement_type` must distinguish:

- `former_fda_rems`
- `payer_site_of_care`
- `fact_iec_expectation`
- `network_contract`
- `other`

No generic `certified_center=true/false` field should replace these authorities.

### Evidence and uncertainty fields

- `evidence_completeness`
  - `complete_for_gate`, `partial`, `insufficient`, or `unknown`.
- `uncertainty_flag`
  - `true` when timing, actor, status, source conflict, policy version, or episode attribution is unresolved.

Missing records do not establish a satisfied gate.

## Gate-specific candidate mappings

| Gate | Candidate source evidence | Minimum observable event | Not sufficient by itself |
|---|---|---|---|
| A0 Referral/case entry | referral order/intake | referral received or case opened | diagnosis alone |
| A1 Product-indication evidence available | clinical/program review records | documentation sufficient for retrospective comparison | research algorithm saying eligible |
| A2 Dartmouth program review/acceptance | explicit program/committee disposition | review/acceptance status | payer approval |
| A3 Facility/service pathway feasibility | facility/logistics documentation | feasibility/pathway status | former REMS status alone |
| A4 Network/benefit applicability | benefit/network source | explicit network/benefit state | payer-family name alone |
| A5 Medical necessity/prior authorization | auth submission/decision records | submitted, pending, approval, denial, appeal state | clinical candidacy note |
| A6 Medicare-specific coverage logic | Medicare/MAC/NCD-linked evidence | applicable Medicare administrative state | current FDA labeling alone |
| A7 Financial clearance | financial-services workflow | pending/satisfied/not-satisfied financial state | payer authorization alone |
| A8 Access-ready | explicit institutional/admin milestone or documented research derivation | aggregate administrative readiness event | A5 approval alone |

## Conflict-resolution rules

1. Preserve conflicting source events rather than overwriting them.
2. Prefer explicit decision records over inferred narrative interpretation for terminal administrative states.
3. When two authorities disagree, retain both and flag uncertainty; do not adjudicate authority beyond the documented research rule.
4. Same-time events use the Access Gate 1 semantic precedence rules only for deterministic sequence reconstruction; precedence does not erase history.
5. Historical policy state must remain attached to the contemporaneous event.

## Required Gate 2 validation artifacts

Before Gate 2 may pass, the governed extension should have:

- a Dartmouth-approved source inventory;
- a field-to-source mapping table for every populated schema field;
- examples of at least one governed retrospective record path for A0, A2, A5, A7, and A8, or documented evidence that a gate is not observable;
- an uncertainty and conflict-handling review;
- a provenance audit showing traceability from derived event to source record and rule version;
- a no-PHI public-export check;
- explicit confirmation that the workflow remains retrospective and non-operational.

## Gate 2 exit criteria

Access Gate 2 should not pass unless:

1. Every governed field used analytically has an attributable source class and documented transformation.
2. Actor authority is preserved throughout normalization.
3. Missingness and conflicts are explicit.
4. Payer policy versioning is event-time aware.
5. `A8` cannot be inferred from authorization approval alone.
6. No governed mapping introduces prospective patient-specific recommendations or automated coverage determinations.
7. Institutional authorization covers the source systems and retrospective validation activity being performed.

## Scope boundary

This contract is a research data-mapping specification. It does not define clinical eligibility thresholds, medical-necessity thresholds, member benefits, treatment readiness, or recommended care. Those determinations remain with the relevant clinical, payer, and institutional authorities.
