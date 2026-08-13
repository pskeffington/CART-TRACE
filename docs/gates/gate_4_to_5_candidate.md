# Gate 4 -> 5 Evidence Record

**Transition:** Phase 4 — Post-infusion hospital utilization measures -> Phase 5 — Capstone characterization and communication

**Decision:** PASS

Gate 4 passes on the versioned Phase 4 metric contract and the complete synthetic trajectory oracle. GitHub Actions run `31659472624` completed successfully for commit `b5ecb78071f2b194ede887fbb2d3dbd260068416`.

## Acceptance evidence

| Requirement | Status | Evidence |
|---|---|---|
| Primary analytic window explicitly defined | PASS | `[0,720)` hours relative to infusion |
| Pre-infusion continuity context excluded from primary utilization totals | PASS | fixture expected values and Phase 4 tests |
| Total inpatient duration implemented | PASS | `cart_trace/metrics.py` |
| State-specific routine/intermediate/intensive duration implemented | PASS | `cart_trace/metrics.py` |
| High-acuity duration implemented | PASS | intermediate + intensive care |
| Transition count implemented | PASS | canonical transitions in `[0,720)` |
| Time to first escalation implemented | PASS | first `escalation` transition after infusion |
| Time to discharge implemented | PASS | first post-infusion discharge transition |
| 7-day acute-care return implemented | PASS | discharge-relative follow-up-aware logic |
| 30-day acute-care return implemented | PASS | discharge-relative follow-up-aware logic |
| Unknown-state burden implemented | PASS | explicit `unknown_state_hours` |
| Zero versus missing behavior defined | PASS | per-metric status contract |
| Incomplete follow-up behavior defined | PASS | negative return requires complete horizon after discharge |
| Positive return with incomplete later follow-up handled | PASS | observed return remains positive when documented |
| Open/uncertain duration behavior defined | PASS | non-calculable where attribution is indefensible |
| Metric definitions versioned | PASS | `config/metric_definitions.json` and metric implementation version |
| Metric result schema present | PASS | `schemas/metric_result.schema.json` |
| Metric provenance present | PASS | interval, transition, and source-record identifiers retained |
| Synthetic expected values use post-infusion window | PASS | all six core fixtures updated |
| Exact expected-value tests | PASS | Phase 4 fixture regression suite |
| CI execution | PASS | GitHub Actions run `31659472624` |

## Metric interpretation rules frozen at passage

### Analytic window

Primary utilization measures use the half-open interval `[0,720)` hours relative to CAR T-cell infusion. Negative-time records may remain in the reconstructed trajectory for continuity but are excluded from primary post-infusion duration totals.

### Duration metrics

Duration is calculated from canonical interval overlap with `[0,720)`. Routine, intermediate, intensive, high-acuity, and total inpatient duration are not imputed through unresolved `unknown` intervals when those intervals could change state attribution.

### Missingness and status

Metric outputs distinguish:

- `observed`;
- `observed_zero`;
- `not_applicable`;
- `not_calculable`;
- `incomplete_followup`.

Missing or uncertain information is not silently converted to zero.

### Acute-care return

Acute-care return is defined from canonical `acute_care_return` transitions after a qualifying discharge. A documented qualifying return establishes a positive result even before the entire negative-ascertainment horizon has elapsed. A negative result requires observation through the complete 7-day or 30-day horizon after discharge.

This distinction is required because a Day +30 infusion-relative analysis window does not necessarily provide 30 days of post-discharge follow-up.

## Metric-result provenance contract

Every structured metric result records:

- episode identifier;
- metric implementation version;
- analytic-window bounds;
- observation-end relative time;
- scalar metric values;
- per-metric status;
- missingness reason where applicable;
- contributing interval identifiers;
- contributing transition identifiers;
- contributing source-record identifiers.

This preserves the evidence chain:

`source record -> canonical trajectory -> metric algorithm -> metric result -> capstone output`

## Synthetic oracle result

The Phase 4 tests require exact agreement with prespecified metric values for all six core trajectory fixtures, including:

- post-infusion clipping of encounters beginning before infusion;
- routine recovery;
- prolonged routine inpatient care;
- intermediate-care escalation/de-escalation;
- intensive-care escalation/de-escalation;
- early acute-care return;
- unresolved equal-priority location conflict.

The conflict fixture demonstrates the intended distinction between measurable unknown burden and non-calculable state-attributed duration.

## Interpretation boundary

Gate 4 passage establishes internal mathematical, semantic, reproducibility, and provenance validity against the synthetic oracle. It does not establish external clinical validity, causal interpretation, or transportability to a specific institution.

Any future governed-data application requires local source mapping, data-quality review, and validation under the approved governance process.

## Frozen Phase 4 artifacts

The following are controlled after passage:

- analytic-window definition;
- metric definition contract;
- duration clipping behavior;
- high-acuity definition;
- zero/missing/status semantics;
- follow-up sufficiency rules;
- acute-care-return ascertainment logic;
- metric-result schema;
- metric provenance contract;
- post-infusion synthetic expected values.

Changes require versioning, fixture regeneration where affected, regression testing, and explicit Gate 4 impact review.

## Authorized next phase

Phase 5 — Capstone characterization and communication is authorized.

Phase 5 may construct descriptive patient-level and cohort-level outputs from validated canonical trajectories and metric results. Appropriate next artifacts include:

1. synthetic patient-level trajectory figures;
2. a cohort-style synthetic utilization summary table;
3. reconstruction fidelity and metric validation tables;
4. missingness/uncertainty summaries;
5. a methods/data-flow figure;
6. manuscript-style Methods and Results scaffolding.

Prediction, clustering, capacity forecasting, prospective clinical alerts, and clinical decision support are not required for Gate 5 or capstone completion.
