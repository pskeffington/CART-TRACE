# CART-TRACE Scholarly Integration — Limitations Template

## Status

Template only. This document defines limitations that should remain visible regardless of whether governed validation is completed.

## Core methodological limitations

1. Synthetic truth-set validation establishes deterministic computational behavior under controlled cases, not external clinical validity.
2. Level of care is a representation of hospital utilization and cannot be assumed to equal toxicity severity or physiologic acuity.
3. Source encounter/location data may be incomplete, delayed, overwritten, or administratively coded in ways that do not perfectly reflect bedside care location.
4. Local source-to-canonical mapping introduces institution-specific interpretation that requires versioning and validation.
5. Reconstructability and follow-up requirements may introduce selection into empirical analyses.
6. Unknown and uncertain intervals may remain even after adjudication and should be reported rather than hidden.
7. The 30-day `[0,720)` window is a prespecified analytic boundary and does not capture the full clinical course.
8. Descriptive trajectory summaries do not support causal claims about treatment, escalation, discharge, or outcomes.

## Governance and access limitations

If governed access is unavailable, state that external representation validation and empirical hospital-utilization characterization were not performed. Do not substitute expanded synthetic simulation for actual clinical validation.

If governed access is available, describe residual source completeness, mapping uncertainty, validation-sample size, adjudication burden, and disclosure constraints.

## Generalizability

A validated local mapping and source model may not transfer directly across institutions. Cross-site reproducibility would require independent source inventory, mapping review, and representation validation without changing the frozen canonical contract silently.
