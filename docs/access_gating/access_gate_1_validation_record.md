# CART-TRACE Access Extension — Gate 1 Validation Record

## Gate

**Proposed transition:** `Access Gate 0 -> Access Gate 1`

**Branch / PR:** `agent/dartmouth-access-eligibility-gates` / PR #10

**Date reviewed:** 2026-08-20

## Gate decision

- [x] PASS
- [ ] CONDITIONAL PASS
- [ ] FAIL / REMAIN IN CURRENT PHASE

**Passing CI evidence:** GitHub Actions run `32323744732`, workflow `Validate CART-TRACE`, completed successfully on 2026-08-20 for branch head `123602350e246d760a77514fca5f300d830e5843`.

Access Gate 1 establishes synthetic methodological readiness only. It does not authorize clinical, payer, or prospective use.

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
| Event schema | Complete | `schemas/access_gate_event.schema.json` | Schema validation passes | Synthetic records only. |
| Deterministic reconstruction | Complete | `cart_trace/access_gating.py` | Oracle expectations pass | Same-time semantic status precedence is explicit. |
| Materialized schema records | Complete | `materialize_access_event`, `materialize_access_case` | Schema-conformance tests pass | Deterministic IDs/timestamps/provenance. |
| Clinical vs administrative separation | Complete | framework + tests | Manual/test review complete | `approved` does not imply `access_ready`. |
| Policy version preservation | Complete | AG-009 oracle case | Test passes | Historical decisions retain contemporaneous version. |
| Frozen capstone-core isolation | Complete | PR diff | Additive extension | No frozen post-infusion trajectory semantics changed. |
| Full branch CI | Complete | GitHub Actions run `32323744732` | PASS | Full matrix validated. |

## Requirement traceability

- `ACCESS-MODEL-001` — A0-A8 administrative gate vocabulary is explicit.
- `ACCESS-MODEL-002` — payer approval and aggregate access readiness are separate states.
- `ACCESS-PROV-001` — each materialized event carries synthetic provenance and transformation version.
- `ACCESS-POLICY-001` — payer, product, line of business, service area, and policy version are separable analytic dimensions.
- `ACCESS-POLICY-002` — policy drift is preserved rather than normalized away.
- `ACCESS-ORACLE-001` — ten synthetic access trajectories have prespecified outputs.
- `ACCESS-ORACLE-002` — denial, benefit, network/site, appeal, expiration, and financial barriers remain typed distinctly.
- `ACCESS-DETERMINISM-001` — event ordering is independent of input ordering, including same-hour events.
- `ACCESS-DETERMINISM-002` — same-time payer statuses follow explicit semantic precedence rather than lexical ordering.
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
- input-order invariance;
- semantic same-time payer status ordering.

### CI findings and closure

Two deterministic-ordering defects were discovered during Gate 1 validation and corrected before passage.

1. Run `32322440151` exposed input-order dependence for same-hour compact events. Commit `7160519ac65995d89e7654e8d2861e281548f64e` added intrinsic tie-breaking.
2. Run `32322755567` exposed an incorrect same-time lexical ordering between `overturned_on_reconsideration_or_appeal` and `approved`. Commit `cda80634fde3d05e33f2fdf344bedd16881ff957` replaced lexical ordering with explicit semantic `STATUS_PRECEDENCE`.
3. Run `32323744732` completed successfully after these corrections, closing the Gate 1 CI condition.

These regressions are retained as part of the gate evidence because they clarify the deterministic contract and future regression surface.

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
- input-order-independent deterministic event ordering;
- same-time status precedence.

Any material change requires versioning, affected-test updates, and a new gate-impact review.

## Promotion criteria for Access Gate 2

Access Gate 2 may focus on governed source-to-field mapping and retrospective workflow validation planning, subject to all of the following:

1. Source classes and candidate fields are documented before governed extraction begins.
2. No source field is interpreted as clinical eligibility unless Dartmouth governance explicitly defines that use.
3. Payer administrative records, clinical records, financial records, and derived research fields retain typed provenance.
4. Missingness, uncertainty, conflicting records, and policy-version ambiguity remain explicit.
5. Any Dartmouth internal workflow mapping occurs only under appropriate institutional authorization.
6. Governed validation remains retrospective and does not create prospective patient-specific authorization or clinical decision support.

## Approval record

**Reviewer(s):** repository methodological review

**Decision rationale:** PASS for synthetic methodological readiness. The administrative access model, schema, oracle, deterministic reconstruction, provenance behavior, and CI evidence are sufficient to support the next retrospective research-design step.

**Residual actions:** none required for Access Gate 1 closure. Known limitations remain active constraints for Access Gate 2.

**Next phase authorized:** Access Gate 2 source-to-field mapping and governed retrospective workflow validation planning only.
