# Dartmouth CAR-T Payer Policy Resolution — Pass 2

**Evidence date:** 2026-08-19  
**Status:** public-source research artifact / non-operational

This pass tightens the payer-policy map using current public payer sources. It supersedes any earlier `pending` status below where a stronger source is now documented.

## Point32Health / Harvard Pilgrim Commercial

Point32Health's September 2025 medical-drug program update identifies the following CAR-T products as **existing prior authorization programs** for Harvard Pilgrim Health Care Commercial and other listed Point32Health lines of business:

- Abecma (idecabtagene vicleucel)
- Aucatzyl (obecabtagene autoleucel)
- Breyanzi (lisocabtagene maraleucel)
- Carvykti (ciltacabtagene autoleucel)
- Kymriah (tisagenlecleucel)
- Tecartus (brexucabtagene autoleucel)
- Yescarta (axicabtagene ciloleucel)

The same update removed obsolete language stating that Abecma, Breyanzi, Carvykti, Kymriah, Tecartus, and Yescarta were available only through restricted FDA REMS programs. It also changed immunosuppressive-therapy limitation language for several products.

**Source:** Point32Health, *Medical drug program updates*, effective 2025-09-01.  
https://www.point32health.org/provider/point32health-medical-drug-program-updates-092025

### Research interpretation

For Harvard Pilgrim Commercial, the evidence now supports:

- `prior_authorization_program = present`
- `car_t_product_specific_program = true`
- `former_rems_language_removed = true` for Abecma/Breyanzi/Carvykti/Kymriah/Tecartus/Yescarta
- `direct_product_MNG_criteria = still_to_extract`

The October 2025 Point32Health update separately removed authorized-treatment-center requirements for six CAR-T products for **Tufts Health Together**. That change must not be generalized to Harvard Pilgrim Commercial without a Harvard-Pilgrim-specific source.

## Cigna

Cigna's current Drug Policy A-Z index exposes separate CAR-T injectable oncology policies for:

| Product | Cigna policy ID |
|---|---|
| Abecma | IP0168 |
| Aucatzyl | IP0734 |
| Breyanzi | IP0130 |
| Carvykti | IP0414 |
| Kymriah | IP0197 |
| Tecartus | IP0199 |
| Yescarta | IP0198 |

**Source:** Cigna Healthcare, Drug Policy A-Z Index, retrieved 2026-08-19.  
https://static.cigna.com/assets/chcp/resourceLibrary/coveragePolicies/pharmacy_a-z.html

### Research interpretation

Cigna is no longer classified as `car_t_specific_policy_pending` at the policy-family level. The current state is:

`product_policy_ids_resolved / product_criteria_and_authorization_details_pending`

Each policy must still be opened and versioned before criteria are encoded. A product-policy listing alone does not establish coverage for a specific member.

## Aetna

Aetna's current Clinical Policy Bulletins establish product-specific review and precertification at least for the products verified in this pass:

### Carvykti — CPB 1007

- Commercial medical-plan policy.
- Identified as a Gene-based, Cellular & Other Innovative Therapies (GCIT) product.
- Dedicated Aetna GCIT review for Commercial and Medicare lines of business.
- Precertification required for participating providers and members in applicable plan designs.
- Public policy last review: 2026-03-13.

Source: https://www.aetna.com/cpb/medical/data/1000_1099/1007.html

### Kymriah — CPB 0920

- Commercial medical-plan policy.
- Identified as an Aetna GCIT product.
- Dedicated GCIT review.
- Precertification required for participating providers and members in applicable plan designs.
- Public policy last review: 2026-02-24.

Source: https://www.aetna.com/cpb/medical/data/900_999/0920.html

### Research interpretation

Aetna supports a distinct `payer_review_program` field because the authorization pathway is not merely a generic prior-auth boolean:

`payer_review_program = Aetna_GCIT_National_Medical_Excellence`

Product-specific criteria remain separately versioned.

## UnitedHealthcare / Optum

UnitedHealthcare's current provider clinical-guideline index lists **Chimeric Antigen Receptor T-Cell (CAR T) Therapy — Clinical Guideline**, last published 2026-07-01. UnitedHealthcare also states that clinical guidelines are not a guarantee of coverage and that member-specific benefit-plan documents remain necessary for coverage determination.

**Source:** UnitedHealthcare Provider, Clinical Guidelines.  
https://www.uhcprovider.com/en/policies-protocols/clinical-guidelines.html

### Research interpretation

The current public evidence supports:

- `car_t_clinical_guideline_current = true`
- `guideline_last_published = 2026-07-01`
- `coverage_guarantee_from_guideline = false`
- `member_benefit_plan_required = true`
- `plan_specific_prior_authorization_path = still_to_resolve`

No patient-level authorization status should be inferred from the clinical guideline alone.

## Anthem Blue Cross Blue Shield of New Hampshire

Anthem's current New Hampshire provider prior-authorization page exposes a **New Hampshire Precertification List** and routes medical prior authorization through its provider authorization workflow. Anthem's policy framework further states that federal/state law and contract provisions take precedence over medical policy.

Sources:

- Anthem Provider, Individual & Commercial Prior Authorization: https://www.anthem.com/provider/individual-commercial/prior-authorization
- ADMIN.00001 *Medical Policy Formation*, published 2026-01-06: https://www.anthem.com/medpolicies/abc/active/mp_pw_a044135.html
- ADMIN.00004 *Medical Necessity Criteria*, published 2026-07-01: https://www.anthem.com/medpolicies/abc/active/mp_pw_a044145.html

### Research interpretation

The architecture is now sufficiently clear to distinguish:

- `anthem_nh_precrt_list = present`
- `anthem_general_medical_policy_framework = resolved`
- `anthem_nh_car_t_specific_criteria = still_to_resolve`
- `anthem_nh_car_t_specific_authorization_listing = still_to_resolve`

The next Anthem step is to inspect the NH precertification list and exact CAR-T policy/UM document rather than substitute transplant or generic cellular-therapy policies.

## Normalized policy-key revision

The evidence now supports the following minimum key for payer gate reconstruction:

`payer_entity + plan_product + line_of_business + servicing_administrator + state_service_area + product + policy_id + policy_version_effective_date`

This avoids false equivalence across:

- Harvard Pilgrim plans that may use different administrative/network structures;
- commercial versus Medicare/Medicare Advantage products;
- payer-wide clinical guidelines versus member-plan authorization requirements;
- product-specific CAR-T policies.

## Revised evidence states after Pass 2

| Payer | Policy family | CAR-T products indexed | Prior-auth program signal | Product criteria fully extracted |
|---|---|---:|---:|---:|
| Harvard Pilgrim / Point32Health | resolved | 7 | yes | no |
| Cigna | resolved | 7 | policy-specific workflow pending | no |
| Aetna | resolved for verified CPBs | 2 verified this pass | yes | partial |
| UnitedHealthcare | current guideline resolved | current CAR-T guideline | plan-specific path pending | partial/pending direct extraction |
| Anthem BCBS NH | administrative framework resolved | CAR-T-specific policy pending | NH precertification framework present | no |

## Next gate-building task

Use the resolved payer architecture to build synthetic authorization event episodes with timestamps and reasons for:

1. straightforward approval;
2. additional-information request and delay;
3. medical-necessity denial;
4. benefit exclusion;
5. network/site-of-care denial;
6. peer-to-peer reconsideration;
7. formal appeal overturn;
8. authorization expiration/re-submission;
9. payer-policy change during an active treatment episode.

Each synthetic episode should preserve the policy ID/version that was operative at the time of the payer decision.