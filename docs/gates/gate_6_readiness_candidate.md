# Gate 6 — Governed-Data Methodological Readiness

## Decision status

**PASSED — methodological readiness / conditional on governed authorization.**

GitHub Actions run `31829204761` completed successfully for commit `2f63a3d35825e615598f3030b64253abffc86818`, validating the complete public CART-TRACE governance and operational-review package.

This decision certifies that the frozen method has a documented, controlled process for an approved retrospective hospital-data application. It does **not** certify that institutional approvals, data-use authorization, governed-environment access, or actual source-data availability are in place.

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

## Validation evidence

GitHub Actions run `31829204761` completed successfully for head `2f63a3d35825e615598f3030b64253abffc86818`. The validated head contained the complete readiness artifact inventory and the Gate 6 candidate decision logic.

## Frozen-method boundary

Any governed-data issue that appears to require a new canonical state, changed transition semantics, changed `[start,end)` convention, changed precedence/conflict behavior, changed metric definition, changed follow-up interpretation, or changed synthetic oracle expectation must stop and enter explicit gate-impact review. Local preprocessing may not absorb such changes silently.

## External prerequisites for governed execution

Before governed application begins, the responsible institutional team must document inside the approved environment:

1. required approvals and data-use authorization;
2. approved users and governed environment;
3. actual source-field availability;
4. local mapping review/version;
5. validation/adjudication sample plan;
6. permitted output/disclosure rules;
7. completed pre-analysis readiness decision.

These prerequisites are external to the public repository and remain mandatory despite this methodological-readiness pass.

## Post-gate work

Two capstone branches are now legitimate without reopening the frozen method:

1. **Governed execution branch** — if approvals/access exist, perform source profiling, local mapping, reconstructability and follow-up characterization, source-concordance validation, descriptive trajectory analysis, and governed results reporting.
2. **Scholarly synthesis branch** — if governed access is unavailable or delayed, complete the capstone with the frozen synthetic method, governance package, limitations, reproducibility statement, and manuscript/presentation synthesis rather than expanding the software.
