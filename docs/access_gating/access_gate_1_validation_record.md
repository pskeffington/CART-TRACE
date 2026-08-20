# CART-TRACE Access Extension — Gate 1 Validation Record

## Gate

**Proposed transition:** `Access Gate 0 -> Access Gate 1`

**Branch / PR:** `agent/dartmouth-access-eligibility-gates` / PR #10

**Date reviewed:** 2026-08-20

## Gate decision

- [ ] PASS
- [x] CONDITIONAL PASS
- [ ] FAIL / REMAIN IN CURRENT PHASE

**Condition:** the latest CI failure on materialized-event order invariance must be closed by a successful GitHub Actions run after commit `7160519ac65995d89e7654e8d2861e281548f64e`, which adds an input-order-independent event tie-break rule.

The residual issue is limited to deterministic ordering of same-hour synthetic events. It does not alter the gate vocabulary, access-status semantics, payer/clinical separation, oracle expected outcomes, or schema. Promotion beyond synthetic methodological validation remains prohibited until the CI condition is satisfied.

## Scope of this gate

Access Gate 1 evaluates only whether the public synthetic access-gating extension has a reproducible administrative event model and deterministic oracle-backed reconstruction contract.

Passing this gate does **not** establish:

- clinical eligibility validity;
- Dartmouth Health workflow validity;
- payer contract correctness;
- member-specific coverage;
- Medicare claims correctness;
- authorization decision support;
- prospective treatment-readiness support.

## Required evidence checklist

| Requirement | Status | Evidence artifact | Test / review result | Notes |
|---|---|---|---|---|
| Access-gate vocabulary defined | Complete | `docs/access_gating/dartmouth_health_access_gating_framework.md` | Manual review complete | A0-A8 remain administrative/research constructs. |
| Payer evidence provenance framework | Complete | `docs/access_gating/dartmouth_payer_policy_registry.md`; `payer_policy_evidence_matrix.md` | Manual review complete | Member-specific coverage explicitly excluded. |
| Synthetic oracle | Complete | `examples/synthetic/access_gating_oracle.json` | 10 cases frozen | Includes approval, denial, appeal, expiration, policy drift, financial delay. |
| Event schema | Complete | `schemas/access_gate_event.schema.json` | Schema tests pass in prior CI | Synthetic records only. |
| Deterministic reconstruction | Complete with CI condition | `cart_trace/access_gating.py` | Oracle expected fields matched before materialization extension | Latest same-hour tie-order defect fixed in commit `7160519...`; CI rerun required. |
| Materialized schema records | Complete with CI condition | `materialize_access_event`, `materialize_access_case` | Schema-conformance tests added | Deterministic IDs/timestamps/provenance. |
| Clinical vs administrative separation | Complete | framework + tests | Manual/test review complete | `approved` does not imply `access_ready`. |
| Policy version preservation | Complete | AG-009 oracle case | Test present | Historical decisions retain contemporaneous version. |
| Frozen capstone-core isolation | Complete | PR diff | 0 deletions; additive extension | No changes to frozen core trajectory semantics required. |
| Full branch CI | Pending | GitHub Actions | Prior run failed on deterministic same-hour ordering | Must pass after tie-break fix. |

## Requirement traceability

- `ACCESS-MODEL-001` — A0-A8 administrative gate vocabulary is explicit.
- `ACCESS-MODEL-002` — payer approval and aggregate access readiness are separate states.
- `ACCESS-PROV-001` — each materialized event carries synthetic provenance and transformation version.
- `ACCESS-POLICY-001` — payer, product, line of business, service area, and policy version are separable analytic dimensions.
- `ACCESS-POLICY-002` — policy drift is preserved rather than normalized away.
- `ACCESS-ORACLE-001` — ten synthetic access trajectories have prespecified outputs.
- `ACCESS-ORACLE-002` — denial, benefit, network/site, appeal, expiration, and financial barriers remain typed distinctly.
- `ACCESS-DETERMINISM-001` — event ordering must be independent of input ordering, including same-hour events.
- `ACCESS-SCOPE-001` — the extension remains retrospective, descriptive, non-operational, and outside the frozen capstone core.

## Verification evidence

### Automated verification

The access test suite verifies:

- exact oracle expected-field agreement for all ten synthetic cases;
- no inference of `access_ready` from payer approval alone;
- preservation of initial denial following overturn;
- distinction among medical-necessity, benefit-exclusion, and network/site denials;
- policy-version drift detection;
- financial-clearance delay without medical-ineligibility relabeling;
- schema validation of materialized synthetic events;
- unique deterministic event IDs;
- monotonic materialized timestamps;
- input-order invariance.

### CI finding and corrective action

GitHub Actions run `32322440151` completed with failure in the Python 3.12 matrix. All preceding workflow steps passed, including package installation, Gate 1 schema tests, controlled Phase 5 output generation, rendering, and artifact-presence checks. The full test suite had one failing test:

`tests/test_access_gating.py::test_materialization_is_deterministic_and_order_invariant`

Root cause: compact events at the same hour did not have intrinsic `event_id` values, and the prior sort key used only hour plus optional event ID. Stable sorting therefore retained the caller's input order for ties. In AG-002, `A7=satisfied` and `A8=satisfied` share the same hour, producing different generated ordinal IDs when the input list was reversed.

Corrective action in commit `7160519ac65995d89e7654e8d2861e281548f64e`:

- adds an intrinsic tie-break key using `hour`, `gate_id`, `status`, `policy_version`, and optional `event_id`;
- preserves chronological ordering while making same-hour ordering input-order independent;
- leaves clinical, payer, access-ready, and metric semantics unchanged.

A successful CI run on or after this commit is required to close the conditional pass.

## Manual review

Manual review confirms:

1. The event model is administrative/research-oriented, not a clinical eligibility engine.
2. `A5=approved` and `A8=satisfied` remain independent milestones.
3. Payer-imposed criteria are represented as payer rules, not Dartmouth clinical candidacy criteria.
4. Financial and network barriers remain non-clinical access barriers.
5. Former FDA REMS requirements are not collapsed with payer site-of-care or FACT accreditation expectations.
6. The access extension is additive and remains separate from the frozen post-infusion trajectory thesis core.

## Known limitations at gate

- Synthetic data only.
- No Dartmouth internal authorization-workflow records have been reviewed.
- No member-level payer benefit documents are represented.
- Anthem BCBS New Hampshire CAR-T-specific criteria remain incompletely resolved in the public-source registry.
- Payer policies remain subject to product, plan, state, and effective-date variation.
- No governed retrospective access cohort has been validated.
- No external validation has occurred.
- No clinical or prospective use is authorized.
- The CMS NCD / FDA REMS historical-policy discrepancy remains a versioned research issue rather than an operational rule.

## Regression risks

The following artifacts must not change silently after Access Gate 1 closure:

- A0-A8 gate meanings;
- access status vocabulary;
- rule that payer approval does not imply access readiness;
- denial/barrier taxonomy;
- policy-version preservation behavior;
- synthetic oracle expected outputs;
- materialization provenance fields;
- input-order-independent deterministic event ordering.

Any material change should require versioning, affected-test updates, and a new gate-impact review.

## Promotion criteria for Access Gate 2

Access Gate 2 may begin only after all of the following are true:

1. GitHub Actions passes the full matrix after the deterministic tie-order fix.
2. The ten-case oracle remains exact under repeated execution.
3. All materialized events validate against `access_gate_event.schema.json`.
4. The payer-policy registry records source/effective-date provenance for the targeted Dartmouth-relevant payer set.
5. Any Dartmouth internal workflow mapping is performed only under appropriate institutional authorization.
6. Governed validation remains retrospective and does not create prospective patient-specific authorization or clinical decision support.

## Approval record

**Reviewer(s):** pending

**Decision rationale:** conditional methodological readiness. The synthetic administrative access model, oracle, schema, reconstruction logic, and scope boundaries are sufficiently developed for Gate 1, but the gate cannot be declared fully passed until the latest deterministic-ordering fix is verified by CI.

**Residual actions:** obtain successful GitHub Actions validation on the corrected head; then update this record from `CONDITIONAL PASS` to `PASS` with run ID and head SHA.

**Next phase authorized:** none beyond synthetic validation until the CI condition is closed. After closure, Access Gate 2 may focus on source-to-field mapping and governed retrospective workflow validation planning.
