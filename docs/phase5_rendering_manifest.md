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

Specification-oriented Figure 1 and Tables 1–2 are controlled directly from frozen framework, schema, mapping, and fixture artifacts because they describe the method rather than quantitative results.

## Main-text scholarly artifacts

| Scholarly artifact | Rendered path | Controlled source |
|---|---|---|
| Figure 1 — data structuring and validation architecture | `examples/rendered/figure1_data_structuring_architecture.svg` | `docs/clinical_data_structuring_framework.md`, schemas, metric contract |
| Table 1 — canonical data model and deterministic rules | `examples/rendered/table1_canonical_model.md` | schemas, mapping config, framework documentation |
| Table 2 — prespecified synthetic trajectory truth set | `examples/rendered/table2_synthetic_truth_set.md` | `examples/synthetic/fixture_manifest.json`, frozen Phase 2 fixtures |
| Figure 2 — representative synthetic trajectories | `examples/rendered/figure2_representative_trajectories.svg` | `examples/outputs/phase5_patient_trajectories.json` |
| Table 3 — reconstruction and metric validation | `examples/rendered/table3_validation.md` | `phase5_reconstruction_validation.json`, `phase5_metric_validation.json` |
| Table 4 — synthetic cohort utilization summary | `examples/rendered/table4_cohort_summary.md` | `phase5_cohort_summary.json` |
| Figure 3 — synthetic utilization and metric availability | `examples/rendered/figure3_utilization_availability.svg` | `examples/outputs/phase5_cohort_summary.json` |
| Table 5 — missingness, uncertainty, and metric availability | `examples/rendered/table5_uncertainty.md` | `phase5_uncertainty_summary.json` |

## Supplementary scholarly artifacts

| Scholarly artifact | Rendered path | Controlled source |
|---|---|---|
| Supplementary Figure S1 — all six trajectories | `examples/rendered/figure_s1_all_trajectories.svg` | `examples/outputs/phase5_patient_trajectories.json` |
| Supplementary Table S1 — complete metric-result matrix | pending | `examples/outputs/phase5_metric_results.json` |
| Supplementary Table S2 — source-to-canonical mapping rules | pending | `config/synthetic_care_state_mapping.json` |
| Supplementary Table S3 — boundary and negative test inventory | pending | `examples/synthetic/phase2_boundary_cases.json`, `invalid_phase2_cases.json`, tests |
| Supplementary Table S4 — reproducibility artifacts | pending | gate candidates, CI evidence, repository paths |

## Manuscript integration rule

The manuscript scaffold should reference these controlled paths rather than manually copying numeric results into source text. Narrative interpretation may summarize generated results, but numeric values, denominators, agreement fractions, availability counts, and synthetic trajectory displays should remain controlled by the generation-and-render sequence above.

Specification-oriented artifacts may summarize frozen semantic definitions, but changes to them must remain consistent with the authoritative framework, schemas, mapping configuration, and fixture manifest.

## Validation evidence

GitHub Actions run `31827148476` completed successfully for commit `7aa5b44bf25fab87ac75908252c0cc048ab457fe`. That head included the Phase 5 generation sequence, rendering sequence, Figure 3 availability controls, deterministic rendering tests, and the full automated test suite on supported Python versions.

This evidence establishes reproducible generation and content-level rendering behavior for the current quantitative synthetic scholarly artifact layer. Figure 1 and Tables 1–2 are specification artifacts and therefore require source-consistency review rather than numeric generation tests. None of this evidence establishes external clinical validity.

## Freeze boundary

The rendering layer may change layout, labeling, or presentation while preserving controlled source values and frozen analytic semantics. Changes to canonical care states, reconstruction precedence, interval semantics, metric definitions, follow-up rules, or the synthetic oracle require separate gate-impact review and are not presentation-layer changes.

## Current inventory status

All planned **main-text** scholarly artifacts now have controlled repository paths. The remaining Phase 5 presentation work is limited to supplementary Tables S1–S4, final inventory reconciliation, and scholarly prototype freeze. These tasks should not expand the analytic model.
