# CART-TRACE Aggregate Reconstructability Summary Template

## Status

Template only. No governed patient data are represented in this public artifact.

## Purpose

Summarize cohort-level reconstructability after approved governed execution while preserving the predefined categories and reason codes.

## Cohort summary

| Reconstructability class | Episodes | Percent | Primary reason categories |
|---|---:|---:|---|
| reconstructable |  |  |  |
| reconstructable_with_uncertainty |  |  |  |
| not_reconstructable |  |  |  |

## Reason-code summary

Report aggregate counts for missing or irreconcilable infusion anchor, source gaps, unmapped labels, unresolved temporal conflict, missing interval boundary, timezone ambiguity, provenance failure, and other prespecified reason codes.

## Unknown and uncertainty burden

Report episode-level and interval-level distributions for unknown-state time, uncertain intervals, conflict-derived unknown intervals, and open-ended source records.

## Interpretation rules

1. Reconstructability is determined from prespecified source and data-quality rules, not from outcome knowledge.
2. `reconstructable_with_uncertainty` remains analytically distinct from fully reconstructable episodes.
3. `not_reconstructable` episodes are accounted for explicitly rather than silently removed.
4. Public reporting is aggregate and disclosure-reviewed.
