# CART-TRACE Requirements

This document converts the MS Health Data Science capstone question into explicit, testable requirements. Requirements are intentionally limited to a research system for retrospective reconstruction and characterization of CAR T-cell hospital care trajectories.

## Requirement classes

- `SCOPE` — research boundary and intended use
- `DATA` — minimum source-data capabilities
- `MODEL` — canonical representation
- `TIME` — temporal alignment and interval semantics
- `PROV` — provenance, uncertainty, and missingness
- `RECON` — trajectory reconstruction behavior
- `METRIC` — hospital-utilization measures
- `VALID` — verification and validation
- `REPORT` — research outputs
- `GOV` — privacy and institutional governance

## Scope requirements

### SCOPE-001 — Episode-centered analysis
CART-TRACE shall use the CAR T-cell therapy episode as the primary unit of analysis rather than treating encounters as independent observations.

### SCOPE-002 — Descriptive research boundary
CART-TRACE shall characterize observed care trajectories and utilization without recommending transfer, escalation, discharge, eligibility, treatment, or other patient-management actions.

### SCOPE-003 — Capstone-limited domains
The capstone implementation shall exclude CMC/manufacturing analysis, patient-generated health data, remote monitoring, eligibility adjudication, treatment-readiness gating, treatment selection, and predictive clinical decision support.

## Data requirements

### DATA-001 — Infusion anchor
Each analyzable episode shall contain an infusion timestamp or documented infusion date sufficient to establish treatment-relative time zero.

### DATA-002 — Encounter boundaries
Source inputs shall support encounter start/end times or equivalent boundaries needed to determine inpatient and acute-care exposure.

### DATA-003 — Care location or care level
Source inputs shall provide enough information to map care into the controlled CART-TRACE care-state vocabulary.

### DATA-004 — Source identifiers
Each input record used to derive a trajectory shall retain a non-public research/source identifier sufficient for audit and provenance within the governed environment.

### DATA-005 — Incomplete data support
The pipeline shall accept episodes with missing or conflicting location information and represent uncertainty rather than requiring complete records.

## Canonical model requirements

### MODEL-001 — Therapy episode
A canonical `therapy_episode` object shall identify the episode, optional synthetic/research patient identifier, infusion anchor, explicit timestamp study-window bounds, relative-hour bounds, source type, and provenance context.

### MODEL-002 — Care-state intervals
Care states shall be represented as `[start, end)` intervals with `interval_id`, absolute timestamps, continuous treatment-relative hours, canonical state, source type, contributing source-record identifiers, mapping method, provenance, uncertainty, and explicit open-end reason when applicable.

### MODEL-003 — Care transitions
A transition shall be emitted only when normalized care state changes and shall include `transition_id`, timestamp, treatment-relative hours, from/to states, transition type, source identifiers, and provenance.

### MODEL-004 — Controlled state vocabulary
The canonical state vocabulary shall be exactly:

- `outpatient`
- `emergency`
- `routine_inpatient`
- `intermediate_care`
- `intensive_care`
- `discharged`
- `unknown`

`acute_care_return` shall not be represented as a care state.

### MODEL-005 — Controlled transition vocabulary
Transition type shall be one of:

- `admission`
- `transfer`
- `escalation`
- `deescalation`
- `discharge`
- `acute_care_return`
- `other`
- `unknown`

### MODEL-006 — Institution-independent model
Local unit names shall be mapped through documented configuration or preprocessing and shall not become canonical state labels.

## Temporal requirements

### TIME-001 — Absolute and relative time
Derived records shall preserve absolute timestamps while also providing continuous treatment-relative hours anchored to infusion.

### TIME-002 — Deterministic relative-time rule
Relative time shall be calculated as `(event_timestamp - infusion_timestamp).total_seconds() / 3600`; days, if displayed, are derived as hours divided by 24 and shall not replace the canonical hour-relative value.

### TIME-003 — Ordered intervals
Within an episode, derived intervals shall be temporally ordered, use half-open `[start, end)` boundaries, and shall not silently overlap.

### TIME-004 — Study-window handling
Records outside the configured study window shall be excluded from capstone metrics but may remain available as source provenance where governance permits.

### TIME-005 — Open/censored ends
A null interval end shall be allowed only with an explicit reason; arbitrary end-time imputation is prohibited.

## Provenance and uncertainty requirements

### PROV-001 — Source traceability
Every derived state interval and transition shall be traceable to one or more source records or to a documented derivation rule.

### PROV-002 — Transformation version
Derived outputs shall record the transformation/version identifier used to produce them.

### PROV-003 — Explicit uncertainty
Conflicting or insufficient records shall generate an uncertainty indicator or `unknown` state rather than silent imputation.

### PROV-004 — Missingness accounting
Capstone reports shall quantify missingness relevant to care-state reconstruction.

## Reconstruction requirements

### RECON-001 — Determinism
The same valid input and configuration shall produce the same trajectory output.

### RECON-002 — Stable sorting
When source events share timestamps, the pipeline shall use a documented deterministic tie-breaking rule.

### RECON-003 — Duplicate suppression
Repeated source records that map to the same care state shall not create false transitions.

### RECON-004 — Overlap resolution
Overlapping encounter/location records shall be handled using documented precedence and conflict rules while preserving contributing source identifiers.

### RECON-005 — Discharge semantics
Discharge shall end inpatient occupancy but shall not be interpreted as clinical recovery.

### RECON-006 — Acute-care return semantics
Post-discharge emergency or inpatient acute care within the configured follow-up period shall retain its actual destination state and be identifiable using `transition_type = acute_care_return` when the configured return-window definition is satisfied.

### RECON-007 — Inpatient acuity rank
For inpatient comparisons only, `routine_inpatient = 1`, `intermediate_care = 2`, and `intensive_care = 3`. Emergency care shall not receive an inpatient acuity rank.

## Utilization metric requirements

### METRIC-001 — Total inpatient exposure
The system shall compute total inpatient time within the configured study window.

### METRIC-002 — State-specific exposure
The system shall compute time spent in `routine_inpatient`, `intermediate_care`, and `intensive_care` states.

### METRIC-003 — Transition burden
The system shall count normalized care-state changes and identify escalation/de-escalation timing.

### METRIC-004 — Time to first escalation
Where escalation occurs, the system shall compute time from infusion to the first transition to a higher inpatient acuity rank.

### METRIC-005 — High-acuity duration
The system shall compute `intermediate_care` and `intensive_care` duration separately; any combined high-acuity metric shall have a documented definition.

### METRIC-006 — Discharge timing
The system shall compute treatment-relative time to discharge for episodes with a documented discharge.

### METRIC-007 — Early acute-care reuse
The system shall characterize 7-day and 30-day post-discharge acute-care reuse when follow-up data are available.

### METRIC-008 — Undefined metric behavior
Metrics that cannot be calculated because of missing data shall be explicitly missing with a reason rather than defaulted to zero.

## Validation requirements

### VALID-001 — Synthetic fixture coverage
Synthetic fixtures shall include routine recovery, prolonged hospitalization, transient escalation, intensive-care escalation, early acute-care return, and conflicting/missing records.

### VALID-002 — Expected outputs
Each synthetic fixture shall have prespecified expected intervals, transitions, uncertainty behavior, and utilization metrics.

### VALID-003 — Schema validation
Synthetic inputs/outputs shall validate against applicable JSON schemas.

### VALID-004 — Boundary tests
Tests shall cover infusion boundaries, identical timestamps, adjacent intervals, missing end times, overlaps, study-window boundaries, and acute-care return semantics.

### VALID-005 — Reconstruction accuracy
Before institutional analysis, reconstruction logic shall reproduce all prespecified deterministic synthetic trajectories exactly and conflict fixtures shall produce their prespecified uncertainty states.

### VALID-006 — Governed-data validation
If approved institutional data are available, a validation subset shall compare reconstructed care states/transitions with source records and document disagreement/adjudication.

## Reporting requirements

### REPORT-001 — Patient-level trace
The system shall produce a patient-level trajectory representation sufficient to inspect sequence and provenance.

### REPORT-002 — Cohort summary
The system shall produce reproducible cohort-level summaries of utilization measures.

### REPORT-003 — Missingness report
Research output shall include a missingness/uncertainty summary.

### REPORT-004 — No clinical recommendation layer
Reports shall not present descriptive trajectories or utilization patterns as patient-management recommendations.

## Governance requirements

### GOV-001 — Synthetic-first public repository
Public examples and automated tests shall use synthetic data only.

### GOV-002 — No PHI in public artifacts
Public repository content shall contain no PHI, institutional credentials, production endpoints, or identifying free text.

### GOV-003 — Institutional approval gate
Use of real hospital data shall occur only after required institutional research, privacy, security, and data-use approvals.

### GOV-004 — Minimum necessary research data
Institutional data extraction shall be limited to fields required by the approved capstone question and validation plan.

## Definition of capstone-ready implementation

The implementation is capstone-ready when:

1. canonical semantics are frozen and machine-readable artifacts are internally consistent;
2. all required synthetic fixtures pass schema and expected-output tests;
3. trajectory reconstruction is deterministic and provenance-preserving;
4. utilization metrics have explicit formulas and missing-data behavior;
5. patient-level and cohort-level reports can be reproduced from a clean environment;
6. all claims remain descriptive unless a separate prospective study justifies otherwise.
