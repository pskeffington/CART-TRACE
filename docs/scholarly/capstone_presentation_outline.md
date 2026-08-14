# CART-TRACE Capstone Presentation Outline

## Status

Template only. This outline supports the final capstone presentation and must preserve the distinction between synthetic validation, methodological readiness, and governed empirical results.

## Suggested sequence

1. **Clinical-data problem and capstone question** — why post-infusion hospital trajectories are difficult to reconstruct reproducibly.
2. **Scope boundary** — retrospective descriptive health-data-science method; no eligibility/readiness logic, prospective decision support, toxicity inference, or causal treatment-effect estimation.
3. **Canonical representation** — therapy episode, infusion = 0 hours, `[0,720)`, seven care states, transition model.
4. **Data-structuring architecture** — source -> staging -> canonical trajectory -> validation -> analytic representation.
5. **Synthetic truth set and Gates 1–4** — computational validity, boundary/error cases, deterministic reconstruction and metrics.
6. **Scholarly prototype and Gate 5** — reproducible generated figures/tables and frozen synthetic artifact inventory.
7. **Governance/data readiness and Gate 6** — cohort definition, source inventory, local mapping protocol, reconstructability, follow-up, adjudication, public/private boundary.
8. **Governed execution plan** — field-availability matrix, local mapping review, validation sample, aggregate reporting templates.
9. **Empirical results, if authorized** — source quality, reconstructability, representation concordance, descriptive utilization metrics. If unavailable, explicitly state that no governed empirical results were produced.
10. **Limitations** — synthetic versus external validity, source completeness, mapping uncertainty, selection by reconstructability/follow-up, level of care not equal to toxicity severity.
11. **Reproducibility and governance** — audit chain, versioning, frozen-method controls, disclosure boundary.
12. **Conclusion** — whether longitudinal hospital records can be transformed into a transparent and reproducible 30-day level-of-care trajectory representation, within the evidence actually obtained.

## Presentation rule

Every figure or table should be visibly labeled as synthetic, governed aggregate, or schematic. Never visually blend synthetic and observed clinical data as though they are one dataset.
