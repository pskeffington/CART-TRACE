# CART-TRACE Time Semantics

This document freezes the initial temporal conventions needed to close Gate 1 -> 2.

## Infusion anchor

The CAR T-cell infusion timestamp is the primary temporal anchor and defines treatment-relative time zero.

If only an infusion date is available in governed data, the episode is not automatically excluded, but precision loss must be represented explicitly and analyses requiring sub-day timing must not claim greater precision than the source supports.

## Treatment-relative time

For an event at timestamp `t` and infusion timestamp `t0`:

- relative hours = `(t - t0)` expressed in elapsed hours;
- relative days = elapsed hours divided by 24.

The canonical representation should preserve the continuous elapsed-time value. Integer treatment-day labels, when displayed, are derived presentation fields and must not replace the underlying elapsed time.

Examples:

- 12 hours before infusion: `-12 h`, `-0.5 d`
- infusion timestamp: `0 h`, `0 d`
- 36 hours after infusion: `36 h`, `1.5 d`

## Day labels

If a discrete day label is required for tables or figures, CART-TRACE should use a documented floor-based convention on elapsed days unless a study protocol specifies another convention.

Under the initial convention:

- `0.0 <= relative_days < 1.0` is Day 0;
- `1.0 <= relative_days < 2.0` is Day +1;
- `-1.0 <= relative_days < 0.0` is Day -1.

The floor-based day label is a convenience for grouping; all duration calculations use timestamps or continuous relative time.

## Interval boundary convention

Care-state intervals use half-open boundaries:

`[start, end)`

A state is active at `start` and ceases to be active at `end`. Adjacent intervals may therefore share the same boundary timestamp without overlap.

Example:

`routine_inpatient [08:00, 14:00)`

`icu [14:00, 22:00)`

This represents an instantaneous transition at 14:00 without double-counting exposure.

## Missing end times

An encounter or state with no end time must not be assigned an arbitrary duration. Handling options are:

1. close the interval at a later authoritative event if the reconstruction rule explicitly supports that inference;
2. truncate at the configured study-window boundary with an uncertainty indicator;
3. leave duration-derived metrics missing when a defensible end cannot be established.

The selected rule must be traceable in provenance.

## Simultaneous events and tie-breaking

Events sharing the same timestamp require deterministic ordering. The initial ordering principle is:

1. explicit end/discharge events close the prior interval;
2. explicit location/care-state start events establish the new state;
3. otherwise apply configured source precedence;
4. if authoritative sources remain irreconcilable, produce `unknown` or an uncertainty flag rather than selecting arbitrarily.

Implementation tests must verify this behavior.

## Overlap semantics

Canonical care-state intervals must not silently overlap. When source encounters overlap:

- normalize each source record;
- apply documented precedence rules;
- preserve all contributing source identifiers;
- emit uncertainty when the overlap cannot be resolved confidently.

Overlap resolution is a reconstruction rule, not an assertion that one source record was clinically incorrect.

## Study window

The initial thesis development window is approximately Day -7 through Day +30 relative to infusion.

The exact configured boundaries must be explicit in the therapy episode. Source events outside the analysis window are excluded from thesis utilization calculations, although they may be retained in governed source context where permitted.

## Duration calculations

Duration metrics are calculated from elapsed timestamp differences, not by counting calendar dates or discrete treatment-day labels.

For a set of non-overlapping intervals, total exposure is the sum of interval durations after clipping to the configured analysis window.

## Time-zone handling

Timestamps should be normalized to a consistent timezone or offset-aware representation before elapsed-time computation. Naive and offset-aware timestamps must not be mixed silently.

The public synthetic cohort should use explicit UTC offsets or UTC timestamps to make tests deterministic.

## Precision and uncertainty

CART-TRACE must not manufacture timestamp precision. If source data are date-only, rounded, or otherwise imprecise, the canonical representation should record that limitation. Analyses dependent on precise escalation timing may require exclusion or sensitivity analysis for such episodes.

## Change control

After Gate 1 -> 2 passes, changes to infusion anchoring, relative-day convention, interval boundary semantics, or tie-breaking rules require:

- documentation of the change;
- version increment;
- review of affected synthetic truth sets;
- regression testing;
- explicit gate-impact review.
