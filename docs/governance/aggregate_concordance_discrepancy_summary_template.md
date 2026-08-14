# CART-TRACE Aggregate Concordance and Discrepancy Summary Template

## Status

Template only. No governed patient data are represented in this public artifact.

## Purpose

Summarize representation-validation findings from the prespecified governed validation sample without exposing patient-level adjudication evidence.

## Concordance summary

| Review domain | Reviewed units | Concordant | Discordant | Indeterminate | Agreement measure if prespecified | Notes |
|---|---:|---:|---:|---:|---:|---|
| Infusion anchor |  |  |  |  |  |  |
| Encounter boundaries |  |  |  |  |  |  |
| Care-state mapping |  |  |  |  |  |  |
| Transition timing |  |  |  |  |  |  |
| Discharge/return interpretation |  |  |  |  |  |  |
| Frozen metric result |  |  |  |  |  |  |

## Discrepancy categories

Report aggregate counts for:

- source ambiguity;
- source missingness;
- mapping disagreement;
- timing mismatch;
- reconstruction discrepancy;
- follow-up-status discrepancy;
- metric-calculation discrepancy;
- provenance deficiency;
- gate-impact candidate.

## Resolution summary

| Resolution class | Count | Notes |
|---|---:|---|
| source clarification |  |  |
| mapping revision within frozen semantics |  |  |
| data-quality limitation retained |  |  |
| adjudication resolved |  |  |
| unresolved/indeterminate |  |  |
| gate-impact review required |  |  |

## Interpretation rules

1. Validation assesses fidelity of the data representation, not quality of clinical care or appropriateness of clinical decisions.
2. Mapping revisions must remain within the frozen canonical state/precedence contract.
3. Patient-specific ad hoc rules are prohibited.
4. Any discrepancy requiring semantic change is escalated to gate-impact review.
5. Only approved aggregate summaries may be used outside the governed environment.
