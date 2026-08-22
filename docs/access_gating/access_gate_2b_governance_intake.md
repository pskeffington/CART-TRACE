# CART-TRACE Access Extension — Gate 2B Governance Intake

**Status:** pre-governed authorization intake / retrospective / non-operational

## Purpose

This intake records whether a proposed governed source set has the institutional permissions, stewardship, linkage controls, PHI containment, and reviewer ownership required before any retrospective Gate 2B sample review begins.

Completing this intake does not itself grant access. Evidence must be supplied by the responsible institutional authority or data steward. Unknown or unresolved items remain blockers.

## Intake boundary

This document may contain governance metadata, source-system names, approval identifiers, roles, dates, and minimum-necessary field descriptions. It must not contain patient records, direct identifiers, member-specific coverage determinations, clinical eligibility decisions, or unrestricted source text.

## Governance record

| Field | Value |
|---|---|
| intake_id | |
| intake_date | |
| research_project / protocol reference | |
| responsible investigator | |
| institutional governance authority | |
| data steward(s) | |
| proposed source inventory IDs | |
| proposed retrospective date range | |
| minimum-necessary field set reference | |
| approved research linkage method reference | |
| governed environment / workspace | |
| public-export boundary reference | |
| authorized reviewer role(s) | |
| authorization effective date | |
| authorization expiration / review date | |
| restrictions or conditions | |

## Required authorization evidence

Each item must be recorded as `confirmed`, `not_confirmed`, or `not_applicable`, with a reference or reason.

| Requirement | Status | Evidence / authority reference | Notes |
|---|---|---|---|
| retrospective research use is explicitly authorized | | | |
| proposed source systems are covered by the authorization | | | |
| proposed date range is covered | | | |
| proposed field set is minimum necessary and covered | | | |
| research linkage method is approved | | | |
| governed environment is approved for the source set | | | |
| PHI containment requirements are defined | | | |
| public/deidentified export rules are defined | | | |
| source steward is identified for each source class | | | |
| reviewer ownership is assigned | | | |
| correction / discrepancy escalation path is assigned | | | |
| retention and deletion expectations are documented | | | |

## Source-level governance register

Use one row per proposed source inventory item. Do not infer approval from another source in the same system family.

| source_inventory_id | source_class | steward | authorization status | minimum-necessary scope confirmed | linkage approved | PHI containment confirmed | reviewer owner | restrictions | Gate 2B governance status |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

Allowed Gate 2B governance status values:

- `blocked` — one or more mandatory governance prerequisites are absent, unknown, expired, or unresolved.
- `confirmed` — all mandatory governance prerequisites for the proposed retrospective validation activity are documented.

No intermediate status authorizes governed sample review.

## Fail-closed rules

Gate 2B governed sample review must not begin when any of the following is true:

1. authorization is absent, ambiguous, expired, or does not cover the proposed source/date/field scope;
2. approved research linkage is not documented;
3. PHI containment or governed-environment requirements are unresolved;
4. source stewardship is unknown for a source used analytically;
5. reviewer ownership is not assigned;
6. public-export boundaries are not defined where derivatives may leave the governed environment;
7. an institutional restriction conflicts with the proposed validation activity;
8. governance evidence cannot be traced to an authoritative reference.

## Gate 2B entry decision

| Decision field | Value |
|---|---|
| all required governance evidence confirmed | yes / no |
| all proposed sources governance-confirmed | yes / no |
| unresolved governance questions | |
| permitted activity | none / narrower validation activity / governed retrospective sample review |
| approving authority / role | |
| decision date | |
| next review date | |

A `yes` entry must be supported by authoritative institutional evidence. CART-TRACE must not generate or infer that evidence.

## Relationship to readiness tooling

This governance intake supplies the authoritative basis for metadata values such as `authorization`, `stewardship`, `minimum_necessary`, `linkage`, `phi_containment`, `public_export`, and `reviewer_ownership` in the Gate 2B readiness input.

The readiness CLI and reports remain secondary research controls. They may summarize confirmed governance metadata, but they cannot create authorization, resolve institutional ambiguity, or substitute for human governance review.

## Scope guardrail

This intake concerns research-process authorization only. It does not adjudicate CAR-T clinical candidacy, treatment readiness, payer medical necessity, member benefits, prior authorization, financial clearance, or prospective care decisions.
