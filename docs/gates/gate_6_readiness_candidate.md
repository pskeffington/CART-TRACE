# Gate 6 — Governed-Data Methodological Readiness Candidate

## Decision status

**Candidate / pending current-head validation.**

The public CART-TRACE governance and operational-review package is complete enough to support a formal readiness decision. This gate evaluates whether the frozen method has the documentation and controls needed for an approved retrospective hospital-data application. It does **not** certify that institutional approvals, data-use authorization, or governed data access are currently in place.

## Scope of the gate

Gate 6 evaluates methodological and governance readiness only. It does not:

- authorize use of institutional data;
- confirm IRB/privacy/data-use approval;
- confirm access to a governed environment;
- establish external clinical validity;
- permit changes to the frozen analytic method.

## Required readiness artifacts

- [x] `docs/governance/cohort_specification.md`
- [x] `docs/governance/source_field_inventory.md`
- [x] `docs/governance/local_mapping_protocol.md`
- [x] `docs/governance/validation_adjudication_plan.md`
- [x] `docs/governance/public_private_boundary.md`
- [x] `docs/governance/data_quality_profile_template.md`
- [x] `docs/governance/reconstructability_worksheet.md`
- [x] `docs/governance/followup_sufficiency_checklist.md`
- [x] `docs/governance/discrepancy_log_specification.md`
- [x] `docs/governance/preanalysis_checklist.md`

## Readiness controls

- [x] therapy episode and administered infusion timestamp are defined as the cohort/index basis;
- [x] required source domains and minimum semantic fields are specified;
- [x] local mapping is separated from the public synthetic mapping and requires explicit versioning/review;
- [x] source precedence is treated as source authority, not inferred clinical severity;
- [x] source-concordance and adjudication procedures are defined;
- [x] reconstructability categories and structured reason codes are operationalized;
- [x] metric-specific follow-up sufficiency preserves observed/zero/unavailable distinctions;
- [x] data-quality profiling covers timestamps, mapping, overlaps/conflicts, provenance, open ends, and observation completeness;
- [x] discrepancies have controlled categories, resolution classes, and gate-impact escalation;
- [x] the public/private boundary excludes PHI, credentials, local identifiers, restricted mappings, raw governed extracts, and patient-level adjudication evidence;
- [x] pre-analysis review explicitly checks that frozen care states, interval semantics, precedence, metrics, follow-up rules, and oracle expectations have not changed implicitly.

## Frozen-method boundary

Any governed-data issue that appears to require a new canonical state, changed transition semantics, changed `[start,end)` convention, changed precedence/conflict behavior, changed metric definition, changed follow-up interpretation, or changed synthetic oracle expectation must stop and enter explicit gate-impact review. Local preprocessing may not absorb such changes silently.

## External prerequisites

Before governed application begins, the responsible institutional team must document inside the approved environment:

1. required approvals and data-use authorization;
2. approved users and governed environment;
3. actual source-field availability;
4. local mapping review/version;
5. validation/adjudication sample plan;
6. permitted output/disclosure rules;
7. completed pre-analysis readiness decision.

These prerequisites cannot be established by the public repository alone.

## Candidate decision rule

Gate 6 may be marked **PASSED — methodological readiness / awaiting or conditional on governed authorization** when:

1. the current repository head validates successfully;
2. the readiness artifact inventory remains complete and internally consistent;
3. no frozen analytic semantics changed during the readiness pass;
4. the gate decision continues to distinguish methodological readiness from institutional authorization and actual data access.

A successful Gate 6 decision therefore permits transition to governed application **only when** the external prerequisites above are independently satisfied.

## Post-gate work

After methodological readiness passes, the next capstone workstream is governed source profiling and local mapping, followed by source-concordance validation, reconstructability and follow-up characterization, descriptive trajectory analysis, limitations, and final scholarly synthesis. If governed access is unavailable, the frozen synthetic method and governance package remain valid capstone products and the project should proceed with limitations-focused scholarly completion rather than expanding the analytic software.
