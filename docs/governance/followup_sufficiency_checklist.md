# CART-TRACE Metric Follow-up Sufficiency Checklist

## Purpose

This checklist defines how governed episodes are reviewed for metric-specific observation sufficiency, especially post-discharge acute-care return measures. It preserves the frozen Phase 4 distinction between observed outcomes, observed zero, not applicable, not calculable, and incomplete follow-up.

## Episode-level inputs

Record:

- therapy episode identifier;
- infusion timestamp;
- discharge timestamp, if applicable;
- last defensible observation timestamp;
- documented qualifying post-discharge emergency/inpatient return, if present;
- source records supporting discharge, return, and observation horizon;
- reviewer and review version.

## General rules

1. A documented qualifying return is `observed` even if later observation is incomplete.
2. A negative 7-day return requires a complete 7-day post-discharge observation horizon.
3. A negative 30-day return requires a complete 30-day post-discharge observation horizon.
4. Absence of a recorded return is not equivalent to a negative outcome when observation is incomplete.
5. Missing or uncertain discharge timing may make return measures `not_calculable` rather than negative.
6. Follow-up status is metric-specific and must not automatically exclude the entire episode.

## 7-day return checklist

- [ ] defensible discharge timestamp is present;
- [ ] observation horizon extends through 7 days after discharge, or a qualifying return is documented earlier;
- [ ] emergency/inpatient return sources were included in the approved extract;
- [ ] return event timing is source-traceable;
- [ ] status assigned as `observed`, `observed_zero`, `not_applicable`, `not_calculable`, or `incomplete_followup`;
- [ ] structured reason recorded when status is not observed/observed-zero.

## 30-day return checklist

- [ ] defensible discharge timestamp is present;
- [ ] observation horizon extends through 30 days after discharge, or a qualifying return is documented earlier;
- [ ] emergency/inpatient return sources were included in the approved extract;
- [ ] return event timing is source-traceable;
- [ ] status assigned as `observed`, `observed_zero`, `not_applicable`, `not_calculable`, or `incomplete_followup`;
- [ ] structured reason recorded when status is not observed/observed-zero.

## Recommended structured reasons

- `no_discharge_in_window`;
- `discharge_time_uncertain`;
- `observation_horizon_lt_7d`;
- `observation_horizon_lt_30d`;
- `return_source_domain_unavailable`;
- `return_event_time_uncertain`;
- `source_conflict`;
- `other_documented_limitation`.

## Reporting requirement

Cohort summaries must report metric-specific denominators and counts of unavailable statuses. Incomplete follow-up must never be silently converted to `false` or zero.

## Completion criterion

Follow-up review is complete when every return metric has a defensible status, supporting observation-horizon evidence, and a structured reason whenever a negative outcome cannot be established.
