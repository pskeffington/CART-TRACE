# Supplementary Table S4. Reproducibility artifacts

This table identifies the controlled public artifacts supporting the synthetic CART-TRACE scholarly prototype. Synthetic validation establishes computational fidelity to the specification, not external clinical validity.

| Artifact | Repository path | Version / gate evidence | Purpose | Validation coverage |
|---|---|---|---|---|
| Canonical schemas | `schemas/` | Gates 1–4 frozen | Define episode, interval, transition, provenance, encounter, and metric-result contracts | Schema and semantic tests |
| Synthetic mapping | `config/synthetic_care_state_mapping.json` | mapping version 0.2.0 | Define public source-label mapping, precedence, and conflict rules | Mapping/reconstruction tests |
| Six-fixture truth set | `examples/synthetic/phase2_*.json` | Gate 2 passed | Prespecified representative trajectory oracle | Exact interval/transition and metric validation |
| Fixture manifest | `examples/synthetic/fixture_manifest.json` | version 0.5.0 | Link fixture classes to requirements and edge cases | Inventory/traceability review |
| Boundary/error cases | `examples/synthetic/phase2_boundary_cases.json`, `invalid_phase2_cases.json` | Gate 2 supplement | Exercise duplicate, open-end, window, conflict, and invalid-input behavior | Boundary and negative tests |
| Reconstruction implementation | `cart_trace/reconstruction.py` | Gate 3 passed; Actions run 31657957588 | Deterministic treatment-relative interval/transition reconstruction | Exact oracle and repeatability tests |
| Metric implementation | `cart_trace/metrics.py` | Gate 4 passed; Actions run 31659472624 | Compute versioned post-infusion utilization measures | Expected-value, missingness, follow-up tests |
| Reporting helpers | `cart_trace/reporting.py` | Phase 5 reporting version 0.1.0 | Produce trajectory, cohort, validation, and uncertainty reporting structures | Reporting tests |
| Phase 5 generator | `scripts/generate_phase5_outputs.py` | CI-validated | Generate six controlled machine-readable output classes | Full automated suite |
| Phase 5 renderer | `scripts/render_phase5_outputs.py` | Actions run 31827148476 and subsequent heads | Convert controlled JSON to manuscript-facing quantitative artifacts | Deterministic content and availability controls |
| Rendering manifest | `docs/phase5_rendering_manifest.md` | Phase 5 | Preserve source-to-output paths and freeze boundary | Inventory reconciliation |
| Manuscript scaffold | `docs/manuscript_scaffold.md` | Phase 5 | Scholarly Methods/Results/Discussion structure | Controlled artifact references |
| Roadmap | `ROADMAP.md` | phase/gate record | Track scope, phase completion, and freeze criteria | Manual alignment review |

## Reproduction sequence

```bash
python scripts/generate_phase5_outputs.py
python scripts/render_phase5_outputs.py
pytest -q
```

The public repository contains synthetic research artifacts only. Governed clinical-data application remains a separate approval-dependent phase.
