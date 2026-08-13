# CART-TRACE Clinical Data Structuring and Validation Framework

## Purpose

This framework defines how CART-TRACE converts heterogeneous longitudinal hospital records into auditable research data suitable for reconstructing post-infusion CAR T-cell hospital care trajectories.

The framework treats clinical-data structuring as a methodological component of the capstone rather than a clerical preprocessing step. Its purpose is to ensure that every analytic result can be traced from source evidence through normalization, canonical representation, validation, and metric derivation.

The framework is descriptive and retrospective. It does not determine treatment eligibility, infer clinical appropriateness, recommend transfer or discharge, predict toxicity, or support prospective bedside decisions.

## Design principle

CART-TRACE uses a layered architecture:

`source clinical data -> staging representation -> canonical trajectory representation -> validation/review -> analytic representation`

Each layer has a distinct purpose and must preserve enough information for the next layer to be audited without erasing the prior layer.

---

## Layer 1 — Source clinical data

### Purpose

Represent the authoritative or source-like records from which hospital care trajectories may be reconstructed.

### Candidate source domains

- encounter start/end records;
- admission/discharge records;
- care-location or unit history;
- emergency encounters;
- transfer/location-change records;
- infusion timestamp;
- source encounter type;
- source disposition information where available.

### Required principles

1. Preserve original timestamps and source labels.
2. Preserve source-record identifiers suitable for governed audit.
3. Do not overwrite source values with canonical values.
4. Retain source ambiguity rather than resolving it informally outside the transformation rules.
5. Do not require excluded capstone domains such as physiologic prediction inputs, CMC data, or patient-generated data.

### Minimum review questions

- Is the infusion anchor present at sufficient precision?
- Are encounter/location boundaries represented?
- Can local locations be mapped to the canonical care-state vocabulary?
- Are source-record identifiers available for provenance?
- Are missing, overlapping, or contradictory records detectable?

---

## Layer 2 — Staging representation

### Purpose

Normalize source records into a deterministic intermediate representation without yet asserting a final patient trajectory.

### Core staging operations

- normalize timestamps to offset-aware values;
- retain continuous absolute time;
- calculate treatment-relative hours without flooring;
- preserve original source labels;
- attach versioned source-to-canonical mapping metadata;
- assign or preserve deterministic precedence values where defined;
- stable-sort records using documented tie-breaking;
- preserve source system/domain and record identifiers.

### Required outputs

For every staged record, the method should retain at minimum:

- `episode_id`;
- source record identifier;
- source start timestamp;
- source end timestamp, including explicit null/open end;
- source care/location label;
- source encounter category where available;
- mapping version;
- precedence/priority information where applicable;
- source provenance.

### Review dimensions

**Conformance:** Does the record satisfy the expected input contract?

**Completeness:** Are required fields for the intended reconstruction question present?

**Temporal plausibility:** Are timestamps offset-aware, ordered, and internally coherent?

**Semantic interpretability:** Can the source label be mapped without undocumented assumptions?

No staged record becomes a canonical care state solely because it is structurally valid.

---

## Layer 3 — Canonical trajectory representation

### Purpose

Transform staged records into an institution-independent, treatment-relative patient-level representation of observed hospital care.

### Canonical episode

The therapy episode is the organizing unit. It includes:

- `episode_id`;
- optional synthetic/research patient identifier;
- infusion timestamp;
- configured study-window timestamps;
- configured study-window relative-hour bounds;
- source/provenance context.

### Canonical care-state intervals

Each interval contains:

- `episode_id`;
- `interval_id`;
- canonical `state`;
- `start_timestamp`;
- nullable `end_timestamp`;
- `start_relative_hours`;
- nullable `end_relative_hours`;
- `source_type`;
- `source_record_ids`;
- `mapping_method`;
- uncertainty metadata;
- explicit open-end reason where needed.

The canonical state vocabulary is:

- `outpatient`;
- `emergency`;
- `routine_inpatient`;
- `intermediate_care`;
- `intensive_care`;
- `discharged`;
- `unknown`.

### Canonical transitions

Each state change is represented separately from the intervals it connects.

Required transition types are:

- `admission`;
- `transfer`;
- `escalation`;
- `deescalation`;
- `discharge`;
- `acute_care_return`;
- `other`;
- `unknown`.

`acute_care_return` is a transition type, never a care state.

### Temporal semantics

- treatment-relative time is continuous elapsed time from infusion;
- canonical duration calculations use timestamps or continuous relative hours;
- care-state intervals use half-open boundaries `[start, end)`;
- adjacent intervals may share a boundary timestamp without overlap;
- open ends remain explicit when no defensible end can be established;
- source overlap is resolved only through documented deterministic rules;
- irreconcilable equal-priority canonical disagreement produces `unknown` with uncertainty.

### Provenance requirement

Every canonical interval and transition must be auditable to one or more source records or to an explicit documented derivation rule.

---

## Layer 4 — Validation and review

### Purpose

Determine whether the structured representation is fit for the intended research use.

Schema validity alone is insufficient. CART-TRACE separates structural validity from temporal validity, semantic validity, reconstruction fidelity, and reproducibility.

### Dimension A — Structural conformance

Question: Does the object conform to the expected schema and vocabulary?

Checks include:

- required identifiers;
- allowed canonical states;
- allowed transition types;
- timestamp types;
- required provenance fields;
- explicit nullable/open-end behavior.

### Dimension B — Completeness

Question: Is enough information available to answer the intended post-infusion trajectory question?

Checks include:

- usable infusion anchor;
- sufficient encounter/location coverage;
- availability of source identifiers;
- follow-up completeness for return measures;
- proportion of episode time represented as known versus unknown.

Completeness is evaluated relative to the research question, not as a generic EHR property.

### Dimension C — Temporal plausibility

Question: Is the reconstructed sequence internally coherent?

Checks include:

- interval end after start;
- monotonic ordering;
- no silent overlaps;
- deterministic handling of identical timestamps;
- correct study-window clipping;
- reproducible treatment-relative timing;
- no manufactured timestamp precision.

### Dimension D — Semantic validity

Question: Is the source-to-canonical interpretation defensible?

Checks include:

- local labels map through documented configuration;
- mapping version is recorded;
- institution-specific terms do not become canonical labels;
- equal-priority disagreement is not silently resolved;
- source encounter type is preserved where analytically relevant.

### Dimension E — Reconstruction fidelity

Question: Does the algorithm reproduce the prespecified patient trajectory?

Synthetic validation requires:

- exact interval agreement for deterministic fixtures;
- exact transition agreement for deterministic fixtures;
- prespecified `unknown` behavior for conflict fixtures;
- no false transitions from duplicate same-state records;
- correct handling of open ends and boundary cases.

If governed data become available, fidelity review may additionally compare reconstructed intervals/transitions with source records or an approved adjudication sample.

### Dimension F — Reproducibility

Question: Does the same valid input/configuration produce the same canonical output?

Checks include:

- deterministic source ordering;
- stable serialization;
- explicit mapping/transformation versions;
- repeat-run equivalence;
- no hidden dependence on input order or runtime state.

### Dimension G — Analytic fitness

Question: Can the reconstructed episode support the intended utilization measure without overstating the available evidence?

A metric is analytically fit only if:

- the required interval boundaries are known or defensibly censored;
- the analytic window is defined;
- uncertainty behavior is prespecified;
- zero can be distinguished from missing/not-calculable;
- follow-up is sufficient for the measure;
- the metric can be traced to canonical intervals/transitions.

---

## Layer 5 — Analytic representation

### Purpose

Derive transparent, versioned post-infusion hospital-utilization measures from validated canonical trajectories.

The primary analytic window is:

`[0, 720)` hours relative to infusion.

Limited negative-time records may be used to establish encounter continuity but are excluded from primary post-infusion utilization totals unless a metric explicitly states otherwise.

### Planned core measures

- total inpatient duration;
- routine inpatient duration;
- intermediate-care duration;
- intensive-care duration;
- combined high-acuity duration if retained;
- transition count;
- time to first escalation;
- treatment-relative time to discharge;
- 7-day acute-care return;
- 30-day acute-care return;
- unknown-state burden.

### Metric-state model

Each metric should distinguish at minimum:

- observed value;
- observed zero;
- not applicable;
- not calculable because of missing/uncertain data;
- incomplete follow-up/censoring.

Metrics must not silently coerce unknown or incomplete information to zero.

---

## Episode-level data-quality status

CART-TRACE should expose an episode-level quality classification in addition to object-level schema validity.

Recommended research statuses are:

### `reconstructable`

All intervals needed for the intended analysis are deterministically reconstructable, with no unresolved interval that invalidates the relevant metric.

### `reconstructable_with_uncertainty`

A trajectory can be generated, but one or more intervals, transitions, mappings, or boundaries carry explicit uncertainty. Some metrics may remain valid while others are not calculable.

### `not_reconstructable`

The infusion anchor, temporal boundaries, or location evidence are insufficient to construct a defensible trajectory for the intended analysis.

The classification should include machine-readable reasons rather than a free-text-only judgment.

---

## Separation of uncertainty dimensions

Uncertainty should not be treated as a single generic flag when governed data introduce more complex limitations.

Where feasible, later schema versions may distinguish:

- **temporal uncertainty** — start/end timing is imprecise or missing;
- **mapping uncertainty** — source label cannot be mapped confidently;
- **source conflict** — authoritative records disagree;
- **follow-up uncertainty** — observation time is insufficient for a downstream measure.

The current canonical `uncertain` and `uncertainty_reason` fields remain valid for the synthetic framework; these dimensions define the review model for future governed-data work.

---

## Standards relationship

CART-TRACE is analysis-specific and does not require source data to arrive in FHIR or OMOP form.

FHIR and OMOP may be used as interoperability and harmonization reference models because they reinforce several design principles relevant to this work, including encounter/location hierarchy, temporal periods, source-value preservation, and provenance.

CART-TRACE remains a smaller research representation optimized for deterministic treatment-anchored trajectory reconstruction rather than a general-purpose clinical data model.

---

## Review checklist for governed-data application

Before a governed episode contributes to capstone analysis, review should establish:

1. infusion-anchor availability and precision;
2. source encounter/location completeness across the analytic window;
3. source-label mapping coverage;
4. timestamp and timezone coherence;
5. overlap/conflict burden;
6. unknown-state burden;
7. open-end/censoring behavior;
8. source-record traceability;
9. reconstruction reproducibility;
10. metric-specific follow-up sufficiency.

Episodes should be excluded from a specific metric when the required evidence is not defensible, rather than excluded globally when other measures remain valid.

---

## Framework-to-capstone traceability

The framework supports the capstone evidence chain:

`source record -> staging rule -> canonical object -> validation check -> metric eligibility -> analytic output -> capstone table/figure`

This chain is the principal audit structure for the project.

## Formal methodological claim

CART-TRACE evaluates whether heterogeneous longitudinal hospital records can be transformed into a reproducible, provenance-preserving, treatment-relative representation of post-CAR-T hospital care.

Accordingly, the capstone's primary methodological contribution is not merely extraction of EHR data. It is the specification and validation of a structured longitudinal research representation that separates source evidence, deterministic transformation, uncertainty, validation, and downstream utilization analysis.
