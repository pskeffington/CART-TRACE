# CART-TRACE Reconstructability Review Worksheet

## Purpose

This worksheet defines the episode-level review required before governed data contribute to CART-TRACE analyses. It operationalizes the existing statuses `reconstructable`, `reconstructable_with_uncertainty`, and `not_reconstructable` without changing the frozen reconstruction logic.

## Episode review fields

Record, within the governed environment:

- governed episode identifier;
- infusion-anchor status and precision;
- encounter/location coverage status;
- source-label mapping coverage;
- timestamp/timezone coherence;
- overlap/conflict burden;
- open-end/censoring burden;
- unknown-state burden;
- source-record provenance coverage;
- observation-horizon sufficiency;
- final reconstructability category;
- structured reason code(s);
- reviewer and review date/version.

## Classification rules

### `reconstructable`

Use when the episode can be deterministically reconstructed for the intended analysis and no unresolved interval, transition, mapping, or boundary limitation invalidates the relevant metric set.

### `reconstructable_with_uncertainty`

Use when a defensible trajectory can be produced but one or more intervals, mappings, conflicts, boundaries, or follow-up dimensions carry explicit uncertainty. Metric-level eligibility must be evaluated separately; this category does not imply that every metric is calculable.

### `not_reconstructable`

Use when the infusion anchor, temporal boundaries, source evidence, or mapping information is insufficient to construct a defensible trajectory for the intended analysis.

## Structured reason codes

Recommended reason codes include:

- `missing_infusion_anchor`;
- `ambiguous_infusion_anchor`;
- `insufficient_location_coverage`;
- `unmapped_source_label`;
- `irreconcilable_source_conflict`;
- `missing_required_timestamp`;
- `timezone_or_precision_unresolved`;
- `open_end_affects_required_metric`;
- `provenance_incomplete`;
- `followup_incomplete`;
- `other_documented_limitation`.

Multiple reason codes may apply.

## Metric-specific review

Do not globally exclude an episode merely because one metric is unavailable. For each metric, record one of:

- `eligible_observed`;
- `eligible_observed_zero`;
- `not_applicable`;
- `not_calculable`;
- `incomplete_followup`.

The classification must preserve the distinction between zero and unavailable information.

## Escalation to adjudication

Escalate an episode for source-concordance review when:

- the infusion anchor is ambiguous;
- source domains disagree on a boundary or care location;
- mapping status is `needs_review` or `unmapped` for evidence affecting the trajectory;
- a local data artifact appears to violate frozen temporal assumptions;
- provenance cannot support a derived interval or transition.

Adjudication may clarify source interpretation but must not silently introduce new canonical states, precedence rules, metric definitions, or follow-up semantics.

## Completion criterion

An episode is review-complete when its reconstructability category, structured reasons, metric-specific eligibility, provenance sufficiency, and any required adjudication outcome are recorded reproducibly.
