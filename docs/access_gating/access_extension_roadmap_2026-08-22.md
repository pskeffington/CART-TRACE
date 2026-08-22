# CART-TRACE Access Extension Roadmap — 2026-08-22

## Purpose

This roadmap governs the retrospective, descriptive CAR-T access extension without changing the frozen MS Health Data Science capstone core.

The extension studies how administrative, institutional, payer, financial, and source-data events can be represented reproducibly. It does not adjudicate clinical candidacy, treatment readiness, medical necessity, member benefits, prior authorization, or prospective care decisions.

## Current state

- Core CART-TRACE capstone: Gate 6 methodological readiness PASSED; public synthetic scholarly package frozen.
- Access Gate 1: PASS.
- Access Gate 2A synthetic mapping: PASS.
- Access Gate 2B readiness/schema/reporting/CLI preparation: PASS.
- Access Gate 2B governance intake: review-ready.
- Governed source validation: NOT STARTED; institutional authorization required.

## Research opportunity

Recent literature documents substantial CAR-T access barriers across referral, financial clearance, payer authorization, geographic access, center capacity, and treatment logistics. However, many studies measure aggregate delays or barriers rather than reconstructing a traceable event-level administrative trajectory with explicit actor authority, policy version, missingness, and provenance.

The extension therefore asks a narrower methodological question:

> Can retrospective administrative and institutional events surrounding CAR-T access be transformed into a reproducible, provenance-aware sequence of access states without inferring clinical eligibility or payer decisions that are not directly observable?

## Phase A — Governance and provenance closure

**Status: active**

Objectives:

1. finalize governance-intake controls;
2. require authoritative authorization evidence before governed review;
3. preserve source-level stewardship and reviewer ownership;
4. separate governance confirmation from readiness scoring;
5. fail closed on expired, revoked, ambiguous, or scope-mismatched evidence;
6. ensure access-gating documentation changes trigger CI.

Completion artifact:

- review-ready governance-intake package with exact-head CI.

Exit condition:

- package is methodologically complete, but governed-data work remains unopened unless institutional authorization exists.

## Phase B — Literature and construct map

**Status: active / public-data feasible**

Objectives:

1. maintain a current CAR-T access literature review;
2. classify barriers by patient, provider, institution, payer, and policy level;
3. map published constructs to A0-A8 only where the literature supports the concept;
4. distinguish directly observable administrative events from inferred states;
5. identify fields that require local institutional confirmation;
6. document evidence gaps and potential publication questions.

Completion artifacts:

- `docs/access_gating/access_extension_literature_review_2026-08-22.md`;
- source-to-construct evidence matrix in a later pass.

Exit condition:

- each A0-A8 construct has either literature support, local-governance dependency, or an explicit unresolved status.

## Phase C — Synthetic administrative trajectory validation

**Status: partially complete**

Objectives:

1. expand synthetic fixtures for referral, program acceptance, payer, financial, and administrative-hold events;
2. test missing, contradictory, late-entered, superseded, and policy-versioned events;
3. enforce actor-authority separation;
4. prohibit arbitrary gate assignment or unsupported inference;
5. validate deterministic event-to-gate transformation and reporting.

Priority engineering issue:

- tighten `access_source_mapping.py` so any `target_gate` override cannot fabricate an unsupported A0-A8 assignment.

Exit condition:

- synthetic event mapping fails closed under malformed, unsupported, or authority-conflicting inputs.

## Phase D — Governed source observability review

**Status: blocked pending authorization**

If institutional authorization is obtained, perform metadata-first source review before patient-level analysis.

Objectives:

1. confirm source inventory and stewardship;
2. profile source/date/field coverage;
3. assess direct, normalized, partial, derived, absent, and unknown observability;
4. validate historical policy/version availability;
5. confirm research linkage and PHI containment;
6. conduct a bounded governed sample review under institutional oversight.

No source may be treated as governed-ready because another source in the same system family is approved.

Exit condition:

- each source is classified `blocked`, `partial`, or `governed-ready` using evidence specific to that source.

## Phase E — Descriptive access trajectory analysis

**Status: future / authorization-dependent**

Potential descriptive measures, only if observable and authorized:

- referral-to-program-review interval;
- program-review-to-financial-clearance interval;
- authorization submission-to-initial-decision interval;
- initial decision-to-final administrative resolution interval;
- frequency and duration of administrative holds;
- payer/network/financial agreement delays;
- proportion of episodes with unresolved or unobservable access states;
- source concordance and discrepancy classes.

These measures describe administrative process. They do not establish treatment eligibility, quality of clinical decisions, causality, or patient-specific coverage entitlement.

## Phase F — Scholarly synthesis

**Status: public-data work may proceed now**

Potential outputs:

1. methods paper on provenance-aware reconstruction of CAR-T access trajectories;
2. health-services paper on observable versus inferred access barriers;
3. institutional case study, only if governed data and approvals permit;
4. reproducible public synthetic supplement.

## 21-month alignment

The extension should remain subordinate to capstone completion rather than becoming a second capstone.

| Horizon | Core capstone | Access extension |
|---|---|---|
| Months 1-10 | synthetic method + Gate 6 readiness | synthetic access model + literature/governance |
| Months 9-14 | governed application if feasible | metadata/source observability if separately authorized |
| Months 12-18 | empirical validation + descriptive analysis | bounded descriptive access analysis only if feasible |
| Months 18-21 | capstone synthesis and final freeze | optional extension manuscript / future-work package |

## Priority sequence from 2026-08-22

1. Merge governance-intake package after explicit authorization to merge.
2. Complete literature source-to-construct matrix.
3. Tighten synthetic source-to-gate mapping and add regression tests.
4. Add policy-version and actor-authority conflict fixtures.
5. Build a metadata-only governed-source intake template tied to the readiness schema.
6. Do not begin patient-level governed validation until institutional authorization is documented.
7. If authorization does not arrive within the capstone window, freeze the access extension as a synthetic/public methodological package and preserve the core capstone completion path.

## Success criterion

The access extension succeeds if it demonstrates a transparent and reproducible way to represent observable CAR-T access-process events while preserving provenance, actor authority, policy version, missingness, and governance boundaries—and while refusing to infer clinical or payer decisions that the data do not directly support.
