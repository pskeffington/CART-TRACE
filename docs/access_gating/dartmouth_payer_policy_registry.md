# Dartmouth Health CAR-T Payer Policy Registry

## Purpose

This registry is the public, source-grounded index for payer and administrative access evidence relevant to a future retrospective CAR-T access study at Dartmouth Health.

It does **not** assert that any listed plan covers CAR-T for any specific member. Network participation, benefit coverage, prior authorization, medical necessity, and claim payment are separate determinations and must be verified against the member's current plan and the payer's current policy.

**Registry date:** 2026-08-19

## Dartmouth Health public network starting set

Dartmouth Hitchcock Medical Center and Clinics publicly lists participation in the following plan/network families. These names define the first policy-retrieval backlog, not a coverage determination.

| Payer / network family | Public Dartmouth participation signal | CAR-T medical policy captured | Prior authorization source captured | Notes |
|---|---|---:|---:|---|
| Aetna | Listed | [ ] | [ ] | Include commercial and applicable Medicare Advantage products separately. |
| Ambetter | Listed | [ ] | [ ] | Identify NH product/entity and specialty-cell-therapy policy. |
| AmeriHealth Caritas New Hampshire | Listed | [ ] | [ ] | Managed Medicaid. |
| Anthem Blue Cross Blue Shield of New Hampshire | Listed | [ ] | [ ] | Separate commercial, employer, and Medicare Advantage rules. |
| Blue Cross Blue Shield of Vermont | Listed | [ ] | [ ] | Verify VT plan/product and cross-state treatment rules. |
| Cigna | Listed | [ ] | [ ] | Dartmouth notes Cigna-network implications for some MVP members. |
| Community Health Options | Listed | [ ] | [ ] | Verify current network/product geography. |
| First Health | Listed | [ ] | [ ] | Network relationship may not itself define benefit coverage. |
| Harvard Pilgrim Health Care | Listed | [ ] | [ ] | Retrieve current cellular-therapy policy and authorization pathway. |
| Martin's Point Health Care | Listed | [ ] | [ ] | Separate commercial/USFHP/Generations Advantage where applicable. |
| Mass General Brigham Health Plan | Listed | [ ] | [ ] | Formerly AllWays Health Partners. |
| Medicare Traditional | Listed | [x] | [ ] | CMS NCD 110.24 is the national coverage anchor; current implementation must be reconciled with FDA REMS elimination. |
| MultiPlan / PHCS | Listed | [ ] | [ ] | Network status does not establish underlying payer coverage. |
| MVP Health Care | Listed with exclusions/notes | [ ] | [ ] | Dartmouth notes contract limitations as of 2026-04-22; verify product/site-specific network status. |
| New Hampshire Healthy Families | Listed | [ ] | [ ] | Managed Medicaid. |
| New Hampshire Medicaid | Listed | [ ] | [ ] | Retrieve NH Medicaid coverage/authorization rules and any managed-care overlays. |
| UnitedHealthcare / UnitedHealthcare Freedom Plan | Listed | [ ] | [ ] | Separate commercial, employer, Medicaid, and Medicare Advantage products. |
| Vermont Health Partnership | Listed | [ ] | [ ] | Determine underlying payer/benefit administration structure. |
| Vermont Medicaid | Listed | [ ] | [ ] | Retrieve VT Medicaid coverage/authorization rules. |
| WellSense | Listed | [ ] | [ ] | Managed Medicaid and Medicare Advantage products require separate entries. |

## Medicare Advantage starting set

Dartmouth's current public page lists participation in selected 2026 Medicare Advantage products, with geographic and product-specific limitations. Maintain these as separate policy rows because MA coverage and network rules can differ materially from Traditional Medicare.

| Carrier | Dartmouth public 2026 note | Policy capture status |
|---|---|---|
| Aetna Medicare Advantage | Individual plans listed for Hillsborough and Rockingham Counties, NH | [ ] |
| Anthem NH Medicare Advantage | Group Retiree Plans only | [ ] |
| HealthSpring Medicare Advantage | Listed | [ ] |
| Martin's Point Generations Advantage | Maine availability noted | [ ] |
| MVP Health Care Medicare Advantage | New York availability noted | [ ] |
| UnitedHealthcare Medicare Advantage | Selected individual NH counties plus group retiree plans statewide | [ ] |
| WellSense Medicare Advantage | Multiple NH products listed with county-specific availability | [ ] |

## Policy record schema

Create one record per payer + plan/product + policy version.

Required fields:

- `payer_name`
- `payer_entity`
- `plan_or_product`
- `line_of_business`
- `state_or_service_area`
- `network_status_source`
- `network_status_as_of`
- `policy_title`
- `policy_id`
- `policy_url`
- `policy_effective_date`
- `policy_revision_date`
- `policy_retrieved_date`
- `car_t_products_named`
- `diagnoses_named`
- `prior_authorization_required`
- `site_of_care_requirement`
- `center_of_excellence_requirement`
- `network_requirement`
- `clinical_documentation_requirements`
- `prior_therapy_requirements`
- `age_requirements`
- `performance_status_or_organ_function_requirements`
- `reauthorization_or_repeat_treatment_rule`
- `experimental_investigational_exclusions`
- `appeal_or_peer_to_peer_pathway`
- `policy_quotes_prohibited_in_public_dataset` (default `true` unless licensing permits)
- `researcher_interpretation`
- `uncertainty_or_conflict`

## Current national Medicare anchor

### CMS NCD 110.24

Current CMS Medicare Coverage Database text (version 1, effective 2019-08-07) covers FDA-approved autologous CAR-T for a medically accepted indication and still contains the historical condition that treatment be administered at a facility enrolled in the FDA REMS.

### FDA policy change requiring reconciliation

On 2025-06-26, FDA eliminated REMS for the six then-current BCMA- and CD19-directed autologous CAR-T products: Abecma, Breyanzi, Carvykti, Kymriah, Tecartus, and Yescarta. FDA specifically removed the requirement that dispensing hospitals/associated clinics be specially certified under those REMS.

Therefore:

- do not encode `REMS_certified = required` as a timeless Medicare access rule;
- preserve the CMS NCD version/effective date and FDA policy date;
- retrieve current CMS/MAC claims-processing or implementation guidance before using the discrepancy in any analytic eligibility rule;
- classify the issue as `policy_version_conflict_pending_resolution` until authoritative implementation evidence is documented.

## Dartmouth administrative source anchors

Dartmouth's current public referral guidance states that referrals should be for covered services and in-network providers, and that patients should check referral limits. Its precertification guidance directs patients to their insurance card, benefits handbook, or health plan for specific requirements.

For the research model, this supports recording:

- referral requirement;
- referral expiration/visit limit;
- provider/facility network status;
- authorization requirement;
- authorization status;
- source of the requirement;
- effective date.

It does not support inferring a uniform Dartmouth CAR-T authorization rule across insurers.

## Next retrieval order

1. Anthem BCBS New Hampshire CAR-T/cellular therapy medical policy.
2. Harvard Pilgrim / Point32Health CAR-T medical policy.
3. UnitedHealthcare commercial CAR-T medical policy.
4. Aetna CAR-T medical clinical policy bulletin.
5. Cigna CAR-T coverage policy.
6. NH Medicaid and NH managed-Medicaid policies.
7. VT Medicaid and relevant VT commercial policies.
8. Medicare Advantage carrier-specific authorization and network rules.
9. Dartmouth governed authorization-workflow documents, only after institutional approval.

## Evidence quality rule

A payer gate may be classified as evidence-supported only when the applicable plan/product, policy version, effective date, requested CAR-T product, diagnosis/indication, and decision provenance are known. A generic web page or payer-family name is insufficient for patient-level adjudication.

## Public sources

- Dartmouth Hitchcock Medical Center and Clinics, **Insurances Accepted**: https://www.dartmouth-hitchcock.org/patients-visitors/insurance
- Dartmouth Hitchcock Medical Center and Clinics, **Referrals and Precertifications**: https://www.dartmouth-hitchcock.org/patients-visitors/referrals-precertifications
- CMS, **NCD 110.24 — Chimeric Antigen Receptor (CAR) T-cell Therapy**: https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?ncdid=374
- FDA, **FDA Eliminates REMS for Autologous CAR T cell Immunotherapies**, 2025-06-26: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/fda-eliminates-risk-evaluation-and-mitigation-strategies-rems-autologous-chimeric-antigen-receptor
