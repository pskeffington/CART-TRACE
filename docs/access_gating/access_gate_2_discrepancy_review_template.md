# CART-TRACE Access Extension — Gate 2 Discrepancy Review Template

**Status:** pre-governed validation template / non-operational

## Purpose

This template standardizes review of disagreements between source records, normalized access events, and reconstructed episode states during future governed retrospective validation.

A discrepancy is evidence about mapping quality or source ambiguity. It must not be resolved by inventing a clinical or payer decision.

## Discrepancy classes

Use one primary class and optional secondary classes.

- `SOURCE_MISSING` — expected source evidence is absent or inaccessible.
- `SOURCE_CONFLICT` — two source records assert incompatible states.
- `TIMESTAMP_CONFLICT` — event or decision times disagree materially.
- `ACTOR_AUTHORITY_CONFLICT` — the asserting authority cannot be resolved or differs across records.
- `STATUS_NORMALIZATION_ERROR` — mapped status does not faithfully represent source assertion.
- `GATE_ASSIGNMENT_ERROR` — source event mapped to wrong A0-A8 gate.
- `POLICY_VERSION_MISMATCH` — event linked to wrong or uncertain policy version/effective date.
- `EPISODE_LINKAGE_ERROR` — record attached to wrong or uncertain access episode.
- `DERIVATION_ERROR` — deterministic research rule applied incorrectly.
- `SCHEMA_ERROR` — normalized event violates schema contract.
- `UNSUPPORTED_INFERENCE` — favorable/adverse state inferred without source support.
- `PHI_EXPORT_RISK` — source text/identifier would exceed governed export boundary.
- `NOT_OBSERVABLE` — gate or field cannot be established from available governed sources.
- `OTHER` — requires explicit explanation.

## Review record

| Field | Value |
|---|---|
| discrepancy_id | |
| review_packet_id | |
| access_episode_id | research-safe identifier only |
| event_id | |
| gate_id | A0-A8 / unknown |
| primary_class | |
| secondary_classes | |
| source_record_ids | governed identifiers or research-safe surrogates |
| source_classes | |
| normalized_value | |
| expected_or_reviewed_value | |
| source_authority | |
| mapper_rule_version | |
| policy_id_version | |
| uncertainty_before_review | true/false |
| reviewer_role | |
| review_date | |
| disposition | confirmed_mapping / mapper_defect / source_ambiguity / not_observable / governance_question / excluded_from_analysis |
| corrective_action | |
| code_or_rule_change_required | yes/no |
| fixture_or_test_added | yes/no/not_applicable |
| residual_uncertainty | |
| public_export_safe | yes/no/not_applicable |
| notes | no direct identifiers or unnecessary source text |

## Disposition rules

### Confirmed mapping

Use only when source evidence and mapping rule agree after review. This is not confirmation that the underlying payer or clinical decision was substantively correct; it confirms faithful retrospective representation.

### Mapper defect

Use when deterministic transformation logic is wrong. Required actions:

1. preserve the original discrepant case;
2. correct the mapping/reconstruction rule;
3. add a regression fixture/test where allowed;
4. rerun affected validation;
5. version the rule if semantics changed materially.

### Source ambiguity

Use when records conflict or are insufficient and no authoritative resolution is available. Preserve both source events where appropriate and retain `uncertainty_flag=true`.

### Not observable

Use when the governed source set cannot support the target gate/field. Do not impute the value. Observability documentation should be updated.

### Governance question

Use when interpretation depends on institutional policy, source stewardship, protocol scope, data-use authority, or whether a source may be linked/used. No mapping change should substitute for governance review.

### Excluded from analysis

Use only under a prespecified research rule, with the exclusion reason retained. Exclusion must not be used to remove inconvenient discordant cases.

## Review packet minimum contents

A hand-review packet should contain only the minimum necessary governed evidence:

1. research-safe episode identifier;
2. target gate/event;
3. attributable source record references;
4. mapped values and rule version;
5. relevant source timestamps and authority types;
6. policy/version context when applicable;
7. discrepancy class proposed by the mapper/researcher;
8. reviewer disposition and residual uncertainty.

Direct identifiers and unrestricted narrative text should not be copied into the review log unless institutional governance explicitly requires and permits them.

## Aggregate discrepancy metrics

For a governed validation sample, report at minimum:

- number of mapped events reviewed;
- number and proportion with any discrepancy;
- discrepancy count by class;
- discrepancy count by gate A0-A8;
- mapper-defect rate;
- source-ambiguity rate;
- not-observable rate;
- policy-version mismatch rate;
- unsupported-inference count;
- residual-uncertainty rate after review.

These are mapping-quality measures, not patient outcome or payer-performance measures.

## Gate 2B review threshold principle

No universal numerical pass threshold is declared in advance without governed pilot evidence. Gate 2B should instead require:

- zero unresolved `UNSUPPORTED_INFERENCE` defects in the reviewed mapping rules;
- zero unresolved PHI/public-export boundary violations;
- all mapper defects corrected or explicitly bounded before promotion;
- source ambiguity and not-observable rates reported rather than hidden;
- reviewer agreement/disagreement documented where multiple reviewers are used;
- any proposed quantitative threshold justified from governed pilot results and research purpose.

## Scope guardrail

Discrepancy review assesses whether CART-TRACE faithfully reconstructs retrospective administrative evidence. It does not adjudicate clinical eligibility, payer medical necessity, member benefits, or prospective treatment readiness.