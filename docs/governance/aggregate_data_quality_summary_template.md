# CART-TRACE Aggregate Governed Data-Quality Summary Template

## Status

Template only. No governed patient data are represented in this public artifact.

## Purpose

This template defines aggregate data-quality results that may be produced after approved governed execution. It preserves the frozen CART-TRACE method and separates source limitations from analytic findings.

## Cohort accounting

| Measure | Value | Denominator | Notes |
|---|---:|---:|---|
| Candidate therapy episodes |  |  |  |
| Valid infusion anchors |  | candidate episodes |  |
| Episodes with required source coverage |  | valid anchors |  |
| Reconstructable |  | valid anchors |  |
| Reconstructable with uncertainty |  | valid anchors |  |
| Not reconstructable |  | valid anchors |  |

## Source-domain quality

| Domain | Availability | Stable-ID coverage | Missing start | Missing end | Duplicate burden | Conflict/overlap burden | Mapping coverage | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Infusion |  |  |  |  |  |  | n/a |  |
| Encounter |  |  |  |  |  |  |  |  |
| Location/unit history |  |  |  |  |  |  |  |  |
| Admission/discharge |  |  |  |  |  |  |  |  |
| Transfer/location change |  |  |  |  |  |  |  |  |
| Emergency care |  |  |  |  |  |  |  |  |
| Observation horizon |  |  |  |  |  |  | n/a |  |

## Timestamp quality

Report aggregate counts or proportions for exact versus coarse timestamp precision, timezone/offset availability, invalid or reversed intervals, timestamp ties, and open-ended intervals.

## Mapping quality

Report unique local labels reviewed; approved, needs-review, and unmapped coverage; record- and episode-level mapping coverage; mapping changes after validation; and final mapping version.

## Reconstruction quality

Report aggregate distributions of interval count, transition count, unknown-state burden, uncertain-interval burden, unresolved conflict burden, and provenance coverage.

## Interpretation rules

1. Missing, uncertain, or unavailable source information is not treated as zero.
2. Data-quality results describe fitness of the source representation for CART-TRACE, not clinical quality of care.
3. Care location is not interpreted as a direct toxicity or physiologic-severity measure.
4. Any result requiring a change to frozen semantics triggers gate-impact review.
5. Public release requires approved non-identifying aggregation and disclosure review.
