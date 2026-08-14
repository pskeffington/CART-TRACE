# CART-TRACE Governed Field-Availability Matrix Template

## Purpose

This template is completed inside an approved governed environment after data access is authorized. It translates the public source-field inventory into a local availability review without placing institution-specific field names, identifiers, or PHI in the public repository.

## Status vocabulary

Use one of:

- `available_and_interpretable`
- `available_needs_validation`
- `partially_available`
- `not_available`
- `not_yet_assessed`

## Matrix

| Semantic role | Required local evidence | Availability status | Timestamp precision | Timezone behavior | Stable source ID | Completeness notes | Mapping needed | Steward/reviewer | Impact if limited |
|---|---|---|---|---|---|---|---|---|---|
| Therapy episode | episode-level CAR T treatment linkage | not_yet_assessed |  |  |  |  | no |  | cohort definition |
| Infusion anchor | administered infusion timestamp | not_yet_assessed |  |  |  |  | no |  | treatment-relative time cannot be established if absent |
| Encounter | encounter start/end and category | not_yet_assessed |  |  |  |  | yes |  | continuity/reconstructability |
| Location/unit history | source location label with interval/event timing | not_yet_assessed |  |  |  |  | yes |  | care-state reconstruction |
| Admission/discharge | admission/discharge boundary evidence | not_yet_assessed |  |  |  |  | conditional |  | discharge timing/episode continuity |
| Transfer/location change | source/destination or equivalent change event | not_yet_assessed |  |  |  |  | conditional |  | transition concordance |
| Emergency care | emergency encounter/location evidence | not_yet_assessed |  |  |  |  | yes |  | emergency state and return measures |
| Provenance | source system/domain and source-record ID | not_yet_assessed | n/a | n/a |  |  | no |  | auditability |
| Observation horizon | last-known observation or equivalent ascertainment evidence | not_yet_assessed |  |  |  |  | no |  | negative return/follow-up status |

## Review rules

1. The local field name may be recorded only in the governed copy of this template.
2. A field marked `partially_available` or `not_available` must include a reconstructability or metric-availability consequence.
3. No missing field may be replaced by an analytically different proxy without explicit review.
4. The administered infusion timestamp remains the sole treatment-relative anchor.
5. Mapping-readiness and semantic interpretation are reviewed separately from raw technical availability.
6. Any local requirement that appears to change frozen CART-TRACE semantics enters gate-impact review.

## Completion criterion

The matrix is complete when every required semantic role has a local availability determination, responsible reviewer, documented limitation, and explicit consequence for reconstruction or metric status.
