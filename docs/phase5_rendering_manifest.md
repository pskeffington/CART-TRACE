# CART-TRACE Phase 5 Rendering Manifest

This manifest controls the manuscript-facing Phase 5 synthetic scholarly outputs. It separates frozen analytic generation from presentation rendering so that tables and figures do not become a second analytic source of truth.

## Reproduction sequence

Run from the repository root:

```bash
python scripts/generate_phase5_outputs.py
python scripts/render_phase5_outputs.py
pytest -q
```

The generation step produces controlled JSON under `examples/outputs/`. The rendering step consumes those JSON artifacts without reconstructing episodes or recalculating metrics and writes manuscript-facing files under `examples/rendered/`.

## Generated manuscript artifacts

| Scholarly artifact | Rendered path | Controlled source |
|---|---|---|
| Figure 2 — representative synthetic trajectories | `examples/rendered/figure2_representative_trajectories.svg` | `examples/outputs/phase5_patient_trajectories.json` |
| Figure 3 — synthetic utilization and metric availability | `examples/rendered/figure3_utilization_availability.svg` | `examples/outputs/phase5_cohort_summary.json` |
| Supplementary Figure S1 — all six trajectories | `examples/rendered/figure_s1_all_trajectories.svg` | `examples/outputs/phase5_patient_trajectories.json` |
| Table 3 — reconstruction and metric validation | `examples/rendered/table3_validation.md` | `phase5_reconstruction_validation.json`, `phase5_metric_validation.json` |
| Table 4 — synthetic cohort utilization summary | `examples/rendered/table4_cohort_summary.md` | `phase5_cohort_summary.json` |
| Table 5 — missingness, uncertainty, and metric availability | `examples/rendered/table5_uncertainty.md` | `phase5_uncertainty_summary.json` |

## Manuscript integration rule

The manuscript scaffold should reference these generated paths rather than manually copying numeric results into source text. Narrative interpretation may summarize generated results, but numeric values, denominators, agreement fractions, availability counts, and synthetic trajectory displays should remain controlled by the generation-and-render sequence above.

Figure 1 and Tables 1–2 remain specification-oriented scholarly artifacts and may be assembled from frozen schemas, mapping rules, framework documentation, and synthetic fixture definitions because they are descriptive of the method rather than generated quantitative results.

## Validation evidence

GitHub Actions run `31827148476` completed successfully for commit `7aa5b44bf25fab87ac75908252c0cc048ab457fe`. That head included the Phase 5 generation sequence, rendering sequence, Figure 3 availability controls, deterministic rendering tests, and the full automated test suite on supported Python versions.

This evidence establishes reproducible generation and content-level rendering behavior for the current synthetic scholarly artifact layer. It does not establish external clinical validity.

## Freeze boundary

The rendering layer may change layout, labeling, or presentation while preserving controlled source values and frozen analytic semantics. Changes to canonical care states, reconstruction precedence, interval semantics, metric definitions, follow-up rules, or the synthetic oracle require separate gate-impact review and are not presentation-layer changes.
