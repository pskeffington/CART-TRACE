# CART-TRACE Time Semantics

This document defines the temporal conventions used by the canonical episode, interval, and transition models.

## Infusion anchor

The CAR T-cell infusion timestamp is the primary temporal anchor and defines treatment-relative time zero.

If only an infusion date is available in governed data, precision loss must be represented explicitly. Analyses requiring sub-day timing must not claim greater precision than the source supports.

## Canonical treatment-relative time

For an event at timestamp `t` and infusion timestamp `t0`:

`relative_hours = (t - t0).total_seconds() / 3600`

Treatment-relative hours are continuous and may be negative before infusion. No flooring is applied to the canonical value.

Treatment-relative days, when useful for presentation, are derived as:

`relative_days = relative_hours / 24`

Examples:

- 12 hours before infusion: `-12 h`, `-0.5 d`
- infusion timestamp: `0 h`, `0 d`
- 36 hours after infusion: `36 h`, `1.5 d`

Integer treatment-day labels are presentation fields only and must not replace the underlying continuous time representation.

## Interval boundary convention

Care-state intervals use half-open boundaries:

`[start, end)`

A state is active at `start` and ceases to be active at `end`. Adjacent intervals may share the same boundary timestamp without overlap or double-counting.

Example:

`routine_inpatient [08:00, 14:00)`

`intensive_care [14:00, 22:00)`

This represents an instantaneous transition at 14:00.

## Missing or censored end times

An interval with no defensible end must not be assigned an arbitrary duration. The canonical interval may retain `end_timestamp = null` and `end_relative_hours = null` only when an explicit `open_end_reason` is recorded.

Permitted handling includes:

1. closing the interval at a later authoritative event when a documented reconstruction rule supports the inference;
2. clipping to a configured study-window boundary while explicitly recording censoring/truncation provenance;
3. leaving duration-derived metrics missing when no defensible end exists.

## Simultaneous events and tie-breaking

Events sharing a timestamp require deterministic handling. The ordering principle is:

1. explicit end/discharge events close the prior interval;
2. explicit location/care-state starts establish candidate new states;
3. configured source precedence resolves unequal-priority conflicts;
4. equally authoritative irreconcilable evidence produces `unknown` with uncertainty rather than an arbitrary state choice.

Implementation tests must verify these semantics.

## Overlap semantics

Canonical care-state intervals must not silently overlap. When source encounters or location records overlap:

- normalize each source record;
- apply documented mapping and precedence rules;
- preserve all contributing source identifiers;
- emit `unknown`/uncertainty when equally authoritative evidence remains irreconcilable.

Overlap resolution is a reconstruction rule, not an assertion that a source record was clinically incorrect.

## Study window

The development model can retain a limited pre-infusion context window, typically approximately Day -7, while the primary capstone analysis focuses on the first 30 days after infusion.

The exact episode bounds are stored as:

- `window_start_timestamp`
- `window_end_timestamp`
- `window_start_relative_hours`
- `window_end_relative_hours`

Source events outside the configured analysis window are excluded from capstone utilization calculations, although they may remain available as governed source context where permitted.

## Duration calculations

Duration metrics are calculated from elapsed timestamp differences or their exact continuous-hour equivalents, not by counting calendar dates or discrete day labels.

For non-overlapping intervals, exposure is the sum of interval durations after any explicitly documented study-window clipping.

## Time-zone handling

Timestamps must be normalized to a consistent timezone or offset-aware representation before elapsed-time computation. Naive and offset-aware timestamps must not be mixed silently.

Public synthetic fixtures use explicit UTC timestamps to make tests deterministic.

## Precision and uncertainty

CART-TRACE must not manufacture timestamp precision. Date-only, rounded, or otherwise imprecise source data must retain that limitation in provenance or uncertainty metadata. Analyses dependent on precise escalation timing may require exclusion or sensitivity analysis for such episodes.

## Change control

After Gate 1 passage, changes to infusion anchoring, hour-relative calculation, interval boundaries, open-end behavior, or tie-breaking rules require documentation, version impact review, affected fixture regeneration, regression testing, and explicit Gate 1 impact review.
