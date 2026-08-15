# CART-TRACE Public Release Manifest

## Status

**Final public scholarly freeze declared and CI-validated.**

This manifest consolidates the public capstone evidence required for a reproducible scholarly release. It does not establish institutional authorization or governed clinical-data execution.

## Scope anchor

Primary question:

> Can longitudinal encounter and location data surrounding CAR T-cell infusion be transformed into a reproducible representation of hospital level-of-care trajectories during the first 30 days after infusion?

Primary unit: CAR T-cell therapy episode.  
Treatment anchor: administered infusion timestamp = 0 hours.  
Primary analytic window: `[0,720)` hours.  
Design: retrospective, descriptive, synthetic-first health-data-science methodology.

## Frozen canonical states

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` remains a transition type, not a state.

## Gate evidence

| Gate | Status | Key evidence |
|---|---|---|
| Gate 1 | PASSED / frozen | canonical model and schema validation |
| Gate 2 | PASSED / frozen | six-case synthetic oracle and boundary/error fixtures |
| Gate 3 | PASSED / frozen | Actions `31657957588`, commit `536724c4cf996b3192f917d11c909a2ea0eb16fd` |
| Gate 4 | PASSED / frozen | Actions `31659472624`, commit `b5ecb78071f2b194ede887fbb2d3dbd260068416` |
| Gate 5 | PASSED / frozen | Actions `31828145837`, commit `6428fda0be4b69f3d29a408d07e3611a69dd4daf` |
| Gate 6 | PASSED — methodological readiness / conditional on governed authorization | Actions `31829204761`, commit `2f63a3d35825e615598f3030b64253abffc86818` |

Post-gate public validation anchors include Actions `31830669600`, `31830978074`, `31831222408`, `31831407553`, `31832440738`, `31832888988`, `31833669828`, `31833799689`, `31834081804`, `31848508218`, `31849398353`, and `31853659240`.

## Clean reproducibility anchor

Clean audit commit: `4b2e64a178a8e47bb28e7fc9c54952ff29fe8679`  
GitHub Actions run: `31832440738`

Both Python 3.11 and 3.12 jobs successfully completed:

1. repository checkout;
2. dependency installation;
3. schema tests;
4. controlled Phase 5 JSON generation;
5. scholarly rendering;
6. expected rendered-artifact verification;
7. full automated test suite.

Final public scholarly freeze was subsequently recorded and validated. The finalized manuscript and submission-checklist heads also remained green.

## Reproduction commands

Run from repository root:

```text
python scripts/generate_phase5_outputs.py
python scripts/render_phase5_outputs.py
pytest -q
```

## Main scholarly artifacts

- Figure 1 — `examples/rendered/figure1_data_structuring_architecture.svg`
- Figure 2 — `examples/rendered/figure2_representative_trajectories.svg`
- Figure 3 — `examples/rendered/figure3_utilization_availability.svg`
- Table 1 — `examples/rendered/table1_canonical_model.md`
- Table 2 — `examples/rendered/table2_synthetic_truth_set.md`
- Table 3 — `examples/rendered/table3_validation.md`
- Table 4 — `examples/rendered/table4_cohort_summary.md`
- Table 5 — `examples/rendered/table5_uncertainty.md`

Supplement:

- Figure S1 — `examples/rendered/figure_s1_all_trajectories.svg`
- Table S1 — `examples/rendered/supplementary_table_s1_metric_matrix.md`
- Table S2 — `examples/rendered/supplementary_table_s2_mapping_rules.md`
- Table S3 — `examples/rendered/supplementary_table_s3_boundary_negative_tests.md`
- Table S4 — `examples/rendered/supplementary_table_s4_reproducibility_artifacts.md`

The authoritative table/figure source mapping remains `docs/phase5_rendering_manifest.md`.

## Scholarly synthesis artifacts

- `THESIS.md`
- `ROADMAP.md`
- `docs/scholarly/capstone_manuscript_scaffold.md`
- `docs/scholarly/capstone_presentation_narrative.md`
- `docs/scholarly/reproducibility_audit_checklist.md`
- `docs/scholarly/capstone_submission_checklist.md`
- `docs/scholarly/scholarly_consistency_sweep.md`
- `docs/scholarly/final_scholarly_freeze_candidate.md`
- `docs/scholarly/final_public_scholarly_freeze.md`

The freeze-candidate record is retained as historical provenance; `final_public_scholarly_freeze.md` is the controlling final status record.

## Governance package

The public governance package prespecifies cohort definition, infusion anchor, field availability review, local mapping/versioning, reconstructability, follow-up sufficiency, source-concordance validation, adjudication, discrepancy logging, aggregate reporting, and public/private separation.

Gate 6 certifies methodological readiness only. It does **not** establish IRB/privacy/data-use approval, governed environment access, local source availability, representation validity on hospital data, or empirical clinical findings.

## Claim boundary

The public release may support claims about:

- deterministic reconstruction methodology;
- computational validity against the controlled synthetic oracle;
- reproducibility of generated synthetic scholarly outputs;
- methodological readiness for a governed validation branch.

It must not claim:

- institutional empirical validation unless completed;
- external clinical validity from synthetic tests;
- toxicity severity from care location;
- eligibility/readiness determination;
- prospective decision support;
- causal treatment effects.

## Repository metadata and release state

The GitHub repository description is aligned to the narrowed capstone scope:

> Synthetic-first research framework for reproducible reconstruction of 30-day post-CAR-T hospital level-of-care trajectories from longitudinal encounter and location data.

The prior metadata hold is closed. The public scholarly package is frozen and CI-validated. A formal GitHub tag or Release remains optional and should be created only after an explicit version identifier is chosen.
