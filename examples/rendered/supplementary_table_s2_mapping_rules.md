# Supplementary Table S2. Synthetic source-to-canonical mapping rules

Synthetic specification artifact only. These rules exercise the public reconstruction framework and are not institution-specific clinical mappings.

| Source care label | Canonical state | Priority | Mapping version |
|---|---|---:|---|
| synthetic_outpatient | outpatient | 5 | 0.2.0 |
| synthetic_standard_floor | routine_inpatient | 10 | 0.2.0 |
| synthetic_emergency | emergency | 10 | 0.2.0 |
| synthetic_stepdown | intermediate_care | 15 | 0.2.0 |
| synthetic_intermediate | intermediate_care | 15 | 0.2.0 |
| synthetic_icu | intensive_care | 20 | 0.2.0 |

## Precedence and conflict rules

| Rule | Controlled behavior |
|---|---|
| Higher numeric priority | Higher-priority mapped state wins during overlap resolution |
| Equal-priority disagreement | Resolve to explicit `unknown` with uncertainty metadata |
| Stable ordering | `source_record_id` is the stable sort key |
| Unmapped / irreconcilable source evidence | Produce canonical `unknown` rather than an undocumented assumption |
| Post-discharge return | A qualifying discharged-to-emergency-or-inpatient transition is typed `acute_care_return`; it is not a care state |

**Controlled source:** `config/synthetic_care_state_mapping.json`.
