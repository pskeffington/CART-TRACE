# CART-TRACE Scholarly Consistency Sweep

## Status

Completed public documentation consistency review prior to final reproducibility freeze.

## Scope reviewed

The sweep compared the current public framing across:

- `README.md`;
- `THESIS.md`;
- `ROADMAP.md`;
- `docs/requirements.md`;
- `docs/clinical_data_structuring_framework.md`;
- governance/readiness artifacts;
- near-final manuscript scaffold;
- near-final capstone presentation narrative;
- controlled scholarly figure/table inventory;
- GitHub repository metadata.

## Findings

### 1. Core research question — aligned

The public scholarly materials consistently center the same question: whether longitudinal encounter and location data surrounding CAR T-cell infusion can be transformed into reproducible hospital level-of-care trajectories during the first 30 days after infusion.

### 2. Unit and time model — aligned

The primary unit remains the CAR T-cell therapy episode. The administered infusion timestamp remains time zero and the frozen primary analytic window remains `[0,720)` hours.

### 3. Canonical state model — aligned

The frozen canonical state vocabulary remains:

- `outpatient`;
- `emergency`;
- `routine_inpatient`;
- `intermediate_care`;
- `intensive_care`;
- `discharged`;
- `unknown`.

`acute_care_return` remains a transition type, not a state.

### 4. Missingness, uncertainty, and follow-up — aligned

Public materials consistently preserve `unknown`, missing, unavailable, not-calculable, and incomplete-follow-up semantics. These values are not silently converted to zero.

### 5. Clinical interpretation guardrails — aligned

Care location is treated as a trajectory/utilization representation, not a direct toxicity or physiologic-severity measure. The project does not perform eligibility/readiness adjudication, treatment selection, prospective decision support, prediction, or causal treatment-effect estimation.

### 6. Synthetic versus governed evidence — aligned

The public package consistently distinguishes:

1. synthetic computational validity;
2. governed representation fidelity;
3. descriptive empirical findings;
4. external clinical validity.

Gate 6 certifies methodological readiness only and does not establish institutional authorization or data access.

### 7. Patient-generated health data references — exclusions only

References to patient-generated health data in current requirements, thesis, and README appear only as explicit out-of-scope statements. No active CART-TRACE method depends on patient-generated data.

### 8. README status — corrected

The README previously lagged the roadmap by describing the project primarily as a two-branch post-Gate-6 state without reflecting completion of the near-final manuscript, presentation narrative, and audit/submission controls. It has been updated to match the current near-final scholarly synthesis stage.

### 9. GitHub repository description — outstanding metadata mismatch

The repository-level GitHub description still uses an older broad formulation mentioning patient-generated data, toxicity, recovery, and response. This wording conflicts with the narrowed capstone scope.

Recommended replacement:

> Synthetic-first research framework for reproducible reconstruction of 30-day post-CAR-T hospital level-of-care trajectories from longitudinal clinical records.

The current connector exposes repository metadata retrieval but not a repository-description update action, so this remains a manual metadata correction and does not affect the controlled scholarly artifacts or frozen method.

## Freeze impact

No inconsistency identified in this sweep requires a change to frozen care states, interval semantics, source precedence, reconstruction logic, metric definitions, follow-up rules, or synthetic oracle expectations.

The project may proceed to final reproducibility audit and scholarly freeze once current-head CI is green and remaining submission-language refinements are complete.
