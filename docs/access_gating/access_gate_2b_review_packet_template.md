# CART-TRACE Access Extension — Gate 2B Governed Review Packet Template

**Status:** governed-validation preparation / non-operational

## Purpose

This packet structures a small retrospective governed review once institutional authorization exists. It is intended to make each reviewed episode auditable without turning the research workflow into clinical, payer, or operational decision support.

## Packet header

- `review_packet_id`:
- `protocol_or_governance_reference`:
- `review_date`:
- `reviewer_role`:
- `source_inventory_ids`:
- `mapping_rule_version`:
- `schema_version`:
- `research_environment`:
- `public_export_permitted`: yes / no / restricted

## Source scope confirmation

Before any episode review, confirm:

- [ ] source set is covered by institutional authorization;
- [ ] minimum-necessary fields and dates are documented;
- [ ] source steward/owner is identified;
- [ ] approved research identifier/linkage method is in use;
- [ ] PHI remains inside the governed environment;
- [ ] mapping rules are versioned;
- [ ] no prospective workflow or patient-facing output is generated.

## Episode review block

### Research identifiers

- `patient_research_id`:
- `access_episode_id`:
- `episode_date_range`:

### Source records reviewed

| source_record_id | source_inventory_id | source_class | source_timestamp | actor/authority | source_version | notes |
|---|---|---|---|---|---|---|
| | | | | | | |

### Mapped events

| event_id | gate_id | mapped_status | status_timestamp | decision_actor_type | source_record_id | policy_version | uncertainty_flag | mapping_rule_version |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### Gate observability summary

| Gate | observed | partial | absent | unknown | supporting source(s) | reviewer note |
|---|---:|---:|---:|---:|---|---|
| A0 | | | | | | |
| A1 | | | | | | |
| A2 | | | | | | |
| A3 | | | | | | |
| A4 | | | | | | |
| A5 | | | | | | |
| A6 | | | | | | |
| A7 | | | | | | |
| A8 | | | | | | |

## Discrepancy review

For every disagreement between source evidence and mapped output, create a row in `access_gate_2_discrepancy_review_template.md`.

- `discrepancy_count`:
- `critical_discrepancy_present`: yes / no
- `unsupported_inference_present`: yes / no
- `policy_version_error_present`: yes / no
- `authority_misattribution_present`: yes / no
- `phi_export_risk_present`: yes / no

## Reviewer conclusions

- `mapping_traceable`: yes / no / partial
- `actor_authority_preserved`: yes / no / partial
- `missingness_explicit`: yes / no / partial
- `conflicts_preserved`: yes / no / partial
- `policy_version_event_time_aligned`: yes / no / not_applicable
- `a5_approval_kept_separate_from_a8`: yes / no / not_applicable
- `clinical_eligibility_inference_detected`: yes / no
- `member_specific_coverage_inference_detected`: yes / no

## Episode disposition for research validation

Choose exactly one:

- [ ] acceptable for governed mapping validation
- [ ] acceptable with documented discrepancy
- [ ] exclude from validation because source evidence is insufficient
- [ ] exclude because source authorization/scope is not adequate
- [ ] stop review because a privacy/governance issue was identified

## Required sign-off fields

- `reviewer_role`:
- `source_steward_role`:
- `methodological_reviewer_role`:
- `decision_date`:
- `decision_rationale`:

## Scope guardrail

This packet evaluates whether retrospective source records can be mapped reproducibly into research events. It does not evaluate whether a patient should receive CAR-T, whether a payer should approve treatment, or whether treatment is clinically ready to proceed.