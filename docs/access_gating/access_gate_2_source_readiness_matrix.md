# CART-TRACE Access Extension — Gate 2 Governed Source Readiness Matrix

**Status:** pre-governed planning / non-operational

## Purpose

This matrix scores whether a proposed governed source is ready for retrospective mapping review. It is a research-readiness instrument, not an authorization instrument. A high score does not grant data access, establish clinical validity, or permit prospective use.

## Readiness dimensions

Each proposed source receives one score per dimension:

- `0 — unknown`: not yet established.
- `1 — blocked`: known issue prevents mapping review.
- `2 — partial`: material exists but is incomplete or unresolved.
- `3 — sufficient`: sufficient for the individual dimension's controlled mapping-review threshold.
- `4 — governed-ready`: strongest documented state for dimensions that require explicit authorization, provenance, linkage, or PHI containment.

A dimension score is not itself a source-level readiness classification. In particular, authorization below `4` remains a hard blocker for governed sample review.

## Scored dimensions

| Dimension | Question | Minimum for governed validation |
|---|---|---|
| Authorization | Is the retrospective research use explicitly covered by the applicable protocol, data-use agreement, or governance approval? | 4 |
| Stewardship | Is the source owner/steward known and available to resolve interpretation questions? | 3 |
| Minimum necessary | Is the smallest required field/date scope documented? | 3 |
| Event-time observability | Are event/decision timestamps known, or is timestamp uncertainty explicitly characterized? | 3 |
| Actor authority | Can the asserting actor or authority be typed without inference? | 3 |
| Status observability | Are candidate statuses explicit enough to map without inventing favorable states? | 3 |
| Provenance | Can each normalized event be traced back to a governed source record and mapping-rule version? | 4 |
| Historical versioning | Are mutable records, payer policy versions, or correction behavior understood? | 3 |
| Linkage | Is episode linkage possible under an approved research-identifier method? | 4 |
| Missingness | Are structural non-capture, lag, or absent fields documented? | 3 |
| Conflict handling | Are likely cross-source conflicts identifiable and preservable? | 3 |
| PHI containment | Are direct identifiers and sensitive text constrained to the governed environment? | 4 |
| Public export | Is the public/deidentified export boundary defined and testable? | 3 |
| Reviewer ownership | Is an authorized person/role assigned to validate source interpretation? | 3 |

## Source-class readiness register

This register is intentionally unscored until source ownership and authorization are known.

| Source class | Candidate gates | Authorization | Stewardship | Minimum necessary | Time | Actor | Status | Provenance | Versioning | Linkage | Missingness | Conflict | PHI | Export | Reviewer | Gate 2B status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Referral/intake | A0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Program/clinical review | A1,A2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Facility/logistics | A3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Benefit/network | A4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Authorization | A5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Medicare policy context | A6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Financial clearance | A7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |
| Derived research | A8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | not assessed |

## Readiness classification

Source-level classification is determined by hard prerequisites first, not by averaging scores.

- **Not assessed:** documentation/register state used before a source metadata record is evaluated.
- **Blocked:** one or more hard prerequisites are below their required threshold, unsupported inference is detected, PHI export risk is detected, or observability defects require correction.
- **Partial:** all hard prerequisites meet threshold, but one or more non-hard readiness dimensions remain below threshold.
- **Governed-ready:** all hard prerequisites and all remaining required thresholds are satisfied.

The executable validator intentionally emits only `blocked`, `partial`, or `governed-ready`. A numerical average must not override a blocked hard prerequisite.

## Gate 2B minimum entry condition

A governed sample review may begin only when the specific source set used in that review is `governed-ready`, or when institutional governance explicitly documents a narrower permitted validation activity.

At minimum:

1. authorization is explicit;
2. source steward is identified;
3. minimum-necessary fields and dates are fixed;
4. research linkage is approved;
5. PHI containment is established;
6. normalized events remain attributable to source record and mapping-rule version;
7. uncertainty and missingness are represented rather than imputed.

## Scope guardrail

This matrix measures data-source and research-process readiness. It does not score a patient's eligibility, likelihood of payer approval, treatment readiness, or clinical suitability.
