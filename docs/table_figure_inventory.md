# CART-TRACE Capstone Table and Figure Inventory

This inventory defines the preferred scholarly outputs for the Phase 5 capstone product. Each item must be generated from controlled trajectory, validation, or metric artifacts and must preserve the distinction between synthetic demonstration results and future governed clinical findings.

## Main-text figures

### Figure 1 — CART-TRACE data structuring and validation architecture

**Purpose:** Show the complete methodological pipeline from heterogeneous source records to capstone outputs.

**Required flow:**

`source clinical records -> staging representation -> canonical trajectory -> validation/review -> metric-result representation -> tables/figures`

**Required annotations:**

- source vocabulary and timestamps preserved;
- infusion defines relative time 0;
- versioned mapping and precedence;
- `[start,end)` interval semantics;
- explicit `unknown` and uncertainty;
- provenance retained across transformations;
- analytic window `[0,720)`;
- metric status/follow-up rules.

**Caption scaffold:**

> **Figure 1. CART-TRACE clinical-data structuring and validation architecture.** Heterogeneous hospital encounter and location records are preserved at the source layer, normalized into a deterministic staging representation, transformed into canonical treatment-relative care-state intervals and transitions, evaluated for reconstruction fidelity and analytic fitness, and converted into versioned utilization metric results with provenance. The framework separates source evidence, transformation logic, validation, and analysis so that downstream results remain auditable.

---

### Figure 2 — Representative synthetic treatment-relative trajectories

**Purpose:** Demonstrate how distinct episode patterns are represented on a common time axis.

**Recommended panels:**

A. Routine recovery.  
B. Intermediate-care escalation/de-escalation.  
C. Intensive-care escalation/de-escalation with early acute-care return.  
D. Conflicting source location evidence resolving to `unknown`.

**X-axis:** hours or derived days relative to infusion, with infusion at 0.  
**Y-axis:** canonical care state or one row per synthetic episode.

**Required design rules:**

- use interval width to encode time spent in state;
- mark escalation/de-escalation/discharge/return transitions;
- visually distinguish `unknown` from observed care states;
- do not label care states as toxicity grades;
- show the Day +30 boundary if the full analytic window is displayed.

**Caption scaffold:**

> **Figure 2. Representative synthetic post-infusion hospital care trajectories.** Canonical care-state intervals are displayed in treatment-relative time for selected synthetic therapy episodes. The examples illustrate routine recovery, escalation and de-escalation, intensive-care exposure followed by early acute-care return, and explicit representation of unresolved conflicting location evidence as `unknown`. These trajectories are prespecified validation examples and are not intended to represent real-world frequency distributions.

---

### Figure 3 — Synthetic cohort utilization and metric availability

**Purpose:** Present descriptive utilization while preserving denominator and missingness information.

**Recommended display:** paired visualization or compact panel showing selected numeric metrics and metric-status availability across the six synthetic episodes.

**Priority metrics:**

- total inpatient hours;
- high-acuity hours;
- time to discharge;
- transition count;
- unknown-state hours;
- 7-day return status;
- 30-day return status/availability.

**Caption scaffold:**

> **Figure 3. Synthetic cohort utilization and metric availability.** Descriptive summaries are calculated only from values with `observed` or `observed_zero` status, with unavailable, non-calculable, and incomplete-follow-up results reported separately. The six synthetic episodes were designed to exercise algorithm behavior rather than estimate population-level utilization.

---

## Main-text tables

### Table 1 — Canonical data model and transformation rules

**Purpose:** Provide a concise methods reference.

**Suggested columns:**

- object/rule;
- definition;
- required fields or states;
- temporal semantics;
- uncertainty/provenance behavior;
- implementation artifact.

**Rows should include:**

- therapy episode;
- encounter input;
- care-state interval;
- transition;
- provenance record;
- metric result;
- infusion-relative time;
- `[start,end)` rule;
- overlap precedence;
- equal-priority conflict -> `unknown`;
- acute-care return transition definition.

**Caption scaffold:**

> **Table 1. CART-TRACE canonical data model and deterministic transformation rules.** The table summarizes the research objects and temporal/semantic rules used to transform source-like hospital records into treatment-relative trajectories and metric results.

---

### Table 2 — Synthetic truth-set trajectory classes and validation targets

**Purpose:** Define what the six synthetic fixtures test.

**Suggested columns:**

- fixture class;
- intended trajectory pattern;
- key edge condition;
- expected transitions;
- principal requirements tested.

**Rows:**

- routine recovery;
- prolonged routine inpatient;
- transient intermediate-care escalation;
- intensive-care escalation;
- early acute-care return;
- conflicting location evidence.

**Caption scaffold:**

> **Table 2. Prespecified synthetic trajectory truth set.** Six synthetic therapy episodes were constructed to evaluate deterministic reconstruction, transition derivation, post-infusion metric calculation, uncertainty handling, and acute-care-return logic across representative trajectory patterns.

---

### Table 3 — Reconstruction and metric validation results

**Purpose:** Present the core quantitative methodological result.

**Suggested sections:**

A. Reconstruction fidelity.  
B. Metric expected-value agreement.  
C. Boundary and uncertainty behavior.

**Suggested fields:**

- validation domain;
- denominator;
- exact matches;
- agreement fraction;
- interpretation.

**Required results:**

- interval-signature agreement across six fixtures;
- transition-signature agreement across six fixtures;
- metric expected-value agreement;
- duplicate suppression behavior;
- `[start,end)` boundary behavior;
- unknown/conflict behavior;
- follow-up sufficiency behavior.

**Caption scaffold:**

> **Table 3. Synthetic reconstruction and metric validation results.** Exact agreement with the prespecified interval, transition, and metric oracle is reported separately from boundary-condition and uncertainty tests. These results establish computational fidelity to the CART-TRACE specification rather than external clinical validity.

---

### Table 4 — Synthetic cohort utilization summary with metric availability

**Purpose:** Demonstrate the downstream analytic representation.

**Suggested columns:**

- metric;
- total episodes;
- available n;
- not applicable n;
- not calculable n;
- incomplete follow-up n;
- mean;
- median;
- minimum;
- maximum.

**Source:** `examples/outputs/phase5_cohort_summary.json`.

**Caption scaffold:**

> **Table 4. Descriptive utilization summary for the synthetic demonstration cohort.** Numeric summaries use only observed values and observed zeros. Availability, non-calculability, and incomplete follow-up are reported explicitly. The synthetic cohort is a methodological demonstration and should not be interpreted as an estimate of clinical incidence or resource use.

---

### Table 5 — Missingness and uncertainty summary

**Purpose:** Make data-quality limitations visible rather than implicit.

**Suggested rows or fields:**

- episodes with `unknown` or uncertain intervals;
- total unknown-state hours;
- number of `not_calculable` metric results;
- number of `incomplete_followup` results;
- number of `not_applicable` results;
- metric-specific examples and reason.

**Caption scaffold:**

> **Table 5. Missingness, uncertainty, and metric availability in the synthetic demonstration cohort.** CART-TRACE distinguishes measurable unknown-state burden from metrics that cannot be defensibly calculated and from negative outcomes that cannot be established because follow-up is incomplete.

---

## Supplementary outputs

### Supplementary Figure S1 — Full six-episode trajectory panel

Display every synthetic episode on a common treatment-relative scale.

### Supplementary Table S1 — Complete metric-result matrix by episode

One row per episode with all scalar values and metric statuses.

### Supplementary Table S2 — Source-to-canonical mapping rules

Document synthetic source labels, canonical states, priorities, and mapping version.

### Supplementary Table S3 — Boundary and negative test inventory

List malformed timestamp, missing anchor, reversed interval, duplicate records, open-end behavior, window boundary, adjacent intervals, same-day return, and equal-priority conflict cases.

### Supplementary Table S4 — Reproducibility artifacts

Suggested columns:

- artifact;
- repository path;
- version/commit or gate;
- purpose;
- test coverage.

---

# Output-to-source traceability

| Scholarly output | Primary controlled source |
|---|---|
| Figure 1 | `docs/clinical_data_structuring_framework.md`, schemas, metric contract |
| Figure 2 | `examples/outputs/phase5_patient_trajectories.json` |
| Figure 3 | `phase5_cohort_summary.json`, `phase5_metric_results.json` |
| Table 1 | schemas, mapping config, framework docs |
| Table 2 | frozen Phase 2 fixtures and manifest |
| Table 3 | `phase5_reconstruction_validation.json`, `phase5_metric_validation.json`, automated tests |
| Table 4 | `phase5_cohort_summary.json` |
| Table 5 | `phase5_uncertainty_summary.json`, metric-result statuses |
| Supplementary Table S1 | `phase5_metric_results.json` |
| Supplementary Table S3 | boundary/error fixtures and tests |

No reported numeric value should be manually maintained when it can be generated from a controlled machine-readable artifact.
