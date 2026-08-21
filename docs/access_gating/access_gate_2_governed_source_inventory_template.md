# CART-TRACE Access Extension — Gate 2 Governed Source Inventory Template

**Status:** planning template / non-operational / governed use only

## Purpose

This template inventories governed retrospective sources before any source-to-field implementation begins. It is designed to prevent silent assumptions about observability, authority, retention, linkage, or institutional permission.

No row in this inventory authorizes data access by itself. Institutional approval and source-system authorization remain prerequisites.

## Inventory fields

| Field | Required content |
|---|---|
| `source_inventory_id` | Research-safe identifier for the source class or feed. |
| `source_system_name` | Governed source system or document class. |
| `source_owner` | Institutional owner/steward. |
| `source_class` | referral, program_review, facility_logistics, payer_benefit, authorization, medicare, financial, derived_research, other. |
| `access_authority` | IRB/protocol/data-use/governance basis; record reference, not interpretation. |
| `minimum_necessary_scope` | Smallest retrospective data slice required for the research question. |
| `date_range_available` | Known retrospective coverage period. |
| `event_time_fields` | Candidate fields carrying event or decision timestamps. |
| `actor_fields` | Fields identifying the asserting actor/organization type. |
| `status_fields` | Candidate explicit statuses or disposition fields. |
| `policy_fields` | Payer/product/policy/version/effective-date fields if applicable. |
| `linkage_fields` | Governed fields used to associate records to research episodes. |
| `free_text_present` | yes/no; if yes, define controlled extraction boundary. |
| `phi_present` | yes/no/unknown. |
| `public_export_allowed` | expected no unless separately approved. |
| `gate_candidates` | A0-A8 gates potentially observable from this source. |
| `known_missingness` | Known structural gaps, truncation, lag, or non-capture. |
| `known_conflicts` | Other sources likely to disagree or supersede this source. |
| `retention_or_version_behavior` | Whether historical records can change or be overwritten. |
| `validation_owner` | Person/role responsible for governed source interpretation. |
| `inventory_status` | proposed, approved_for_review, approved_for_mapping, unavailable, retired. |
| `notes` | Research limitations only; no patient-level details. |

## Source inventory table

| source_inventory_id | source_system_name | source_owner | source_class | access_authority | minimum_necessary_scope | date_range_available | event_time_fields | actor_fields | status_fields | policy_fields | linkage_fields | free_text_present | phi_present | public_export_allowed | gate_candidates | known_missingness | known_conflicts | retention_or_version_behavior | validation_owner | inventory_status | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `SRC-TBD-001` | TBD | TBD | referral | TBD | TBD | TBD | TBD | TBD | TBD | n/a | TBD | TBD | yes/unknown | no | A0 | TBD | TBD | TBD | TBD | proposed | Placeholder only. |
| `SRC-TBD-002` | TBD | TBD | program_review | TBD | TBD | TBD | TBD | TBD | TBD | n/a | TBD | TBD | yes/unknown | no | A1,A2 | TBD | TBD | TBD | TBD | proposed | Placeholder only. |
| `SRC-TBD-003` | TBD | TBD | authorization | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | yes/unknown | no | A4,A5,A6 | TBD | TBD | TBD | TBD | proposed | Placeholder only. |
| `SRC-TBD-004` | TBD | TBD | financial | TBD | TBD | TBD | TBD | TBD | TBD | n/a | TBD | TBD | yes/unknown | no | A7 | TBD | TBD | TBD | TBD | proposed | Placeholder only. |
| `SRC-TBD-005` | TBD | TBD | derived_research | governed research workspace | minimum normalized event table | research period | derived timestamps | research_derivation | derived states | copied provenance only | research IDs | no | no | aggregate/deidentified only | A8 | depends on upstream sources | upstream conflicts preserved | versioned derivation | research team | proposed | Must never create new clinical or coverage decisions. |

## Inventory review rules

1. A source is not considered observable merely because a field name appears plausible.
2. Source ownership and authorization must be recorded before governed mapping begins.
3. Free text must not become an unrestricted extraction surface; candidate concepts and minimum-necessary review rules must be specified first.
4. Historical payer and policy sources must document whether prior versions are retained or overwritten.
5. Any source that changes retrospectively must be treated as versioned or mutable evidence.
6. Direct identifiers and sensitive text remain inside the governed environment.
7. A source may support multiple gates, but each mapped event must retain the source authority that asserted it.
8. Absence of a source or field is not evidence that a gate was satisfied or not applicable.

## Gate 2 inventory exit check

The inventory is ready for mapping review only when:

- every proposed source has an owner and authorization basis;
- minimum-necessary scope is specified;
- event timing and actor fields are known or explicitly unavailable;
- source version/retention behavior is documented;
- likely A0-A8 observability is labeled as observed, partial, absent, or unknown;
- public-export constraints are recorded;
- no source is represented as clinical or payer authority beyond its actual institutional role.
