# CART-TRACE Data Requirements

This document defines the minimum data needed to answer the thesis question and separates required fields from optional contextual fields. It is not an institutional extraction specification and contains no local system identifiers.

## Principle: minimum necessary data

The thesis should prefer the smallest data footprint capable of reconstructing hospital care trajectories. Additional clinical variables should be added only when they support validation, interpretation, or a prespecified secondary analysis.

## Tier 1 — Required for episode reconstruction

### Episode anchor
Required:
- research episode identifier;
- infusion date/time or infusion date;
- configurable study-window start/end.

Rationale: treatment-relative time cannot be constructed without an infusion anchor.

### Encounters
Required where available:
- research encounter identifier;
- episode linkage;
- encounter start timestamp;
- encounter end timestamp;
- encounter type/category;
- source-system identifier or source table/record reference.

### Location / level-of-care events
Required:
- event or interval start timestamp;
- end timestamp when represented as an interval;
- source location/category;
- source record identifier;
- sufficient information to map to the CART-TRACE care-state vocabulary.

### Discharge / acute-care return
Required:
- discharge timestamp or encounter end representing discharge;
- subsequent emergency, observation, or inpatient encounter timing during the follow-up window.

## Tier 2 — Required for trustworthy provenance and validation

Recommended as mandatory in governed research extracts:
- source table/domain;
- source record key or research-safe surrogate;
- extraction/version date;
- mapping/version identifier;
- encounter/location status where available;
- cancellation/deletion/error flags where available;
- admission/discharge disposition when needed to interpret encounter boundaries.

These fields support auditability but should not be exposed in public synthetic examples as institutional identifiers.

## Tier 3 — Optional contextual variables

These are not required to reconstruct care trajectories but may support secondary interpretation:
- recorded CRS grade;
- recorded ICANS grade;
- selected timestamps of major interventions;
- selected laboratory/vital-sign timestamps;
- diagnosis category;
- disease indication;
- age band or approved demographic covariates;
- mortality status where relevant to episode censoring.

These variables must not be used to infer care state when authoritative location data are available.

## Explicitly out of scope for the thesis core

Not required:
- manufacturing/CMC variables;
- product-release attributes;
- wearable/device streams;
- patient-generated home observations;
- free-text clinical notes;
- imaging content;
- genomic data;
- operational staffing or bed-management feeds;
- real-time alert feeds.

## Source-to-canonical mapping contract

For each institutional source field used later, the governed mapping document should record:

1. source system/domain;
2. source field;
3. source datatype/unit;
4. canonical CART-TRACE field;
5. transformation rule;
6. allowable values;
7. null/missing semantics;
8. precedence/conflict rule;
9. effective dates/version;
10. validation evidence.

## Care-state mapping requirements

Institution-specific locations should be mapped into:
- `outpatient`
- `routine_inpatient`
- `higher_observation`
- `icu`
- `discharged`
- `acute_care_return`
- `unknown`

Mapping should be table-driven or configuration-driven. Hard-coded institutional unit names in public source code are prohibited.

## Data quality dimensions

The thesis should measure at minimum:

### Completeness
- fraction of episodes with an infusion anchor;
- fraction with complete encounter boundaries;
- fraction of observed episode time assigned to a non-unknown care state.

### Consistency
- overlapping encounter/location intervals;
- contradictory state assignments at identical timestamps;
- discharge followed by continued inpatient location records;
- impossible negative-duration intervals.

### Timeliness is not a thesis requirement
Because CART-TRACE is retrospective research infrastructure, real-time latency is not a required quality dimension.

### Validity
- timestamps parse correctly;
- end times do not precede start times unless flagged as source error;
- canonical state values belong to the controlled vocabulary;
- source-to-canonical mappings use a documented mapping version.

## Data sufficiency rule

An episode may be:
- **reconstructable** — sufficient timing/location data exist to derive the intended trajectory;
- **partially reconstructable** — portions require `unknown` states or uncertain boundaries;
- **not reconstructable** — infusion anchor or essential encounter/location information is absent.

The cohort report should state counts in each category. Excluding non-reconstructable episodes must be documented rather than performed silently.

## Institutional-data readiness checklist

Before requesting or analyzing real hospital data:
- [ ] thesis variables mapped to minimum necessary source fields;
- [ ] no unnecessary free text requested;
- [ ] research-safe identifiers specified;
- [ ] mapping ownership and review process identified;
- [ ] date/time zone conventions documented;
- [ ] source-system historical changes considered;
- [ ] follow-up availability for 7/30-day reuse assessed;
- [ ] validation subset plan defined;
- [ ] required approvals confirmed.
