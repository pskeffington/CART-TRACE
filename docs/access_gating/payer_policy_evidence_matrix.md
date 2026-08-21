# CAR-T Payer Policy Evidence Matrix — Dartmouth Health Access Extension

## Status

**Public-source evidence map / non-operational / retrieved 2026-08-19**

This document records payer-policy evidence relevant to a future retrospective Dartmouth Health CAR-T access study. It does not determine coverage for any member and must not be used as an authorization rule engine. Member benefit language, plan-specific exclusions, state law, network contracts, and current payer review remain controlling.

## Evidence normalization rule

Each payer profile is decomposed into the same analytic fields:

- policy family and line of business;
- policy/effective/review date;
- prior authorization or precertification signal;
- product and indication specificity;
- prior-therapy requirements;
- age/performance/organ-function criteria;
- infection/GVHD/inflammatory-disease exclusions;
- previous CAR-T/repeat-treatment rule;
- site/facility requirement;
- Medicare precedence rule;
- unresolved plan-specific uncertainty.

A field is marked `not yet resolved` when the current public source does not establish it. Absence from a public source must never be interpreted as absence of a payer requirement.

---

## UnitedHealthcare / Optum — current CAR-T clinical guideline

**Source:** UnitedHealthcare Provider / Optum, *Chimeric Antigen Receptor T-Cell (CAR T) Therapy — Clinical Guidelines*  
**Effective date:** 2026-07-01  
**Public source:** https://www.uhcprovider.com/content/dam/provider/docs/public/policies/clinical-guidelines/chimeric-antigen-receptor-tcell-therapy.pdf

### Applicability

The guideline states that Medicare Advantage medical-necessity review should first use the Medicare Coverage Database for NCDs and LCDs/LCAs and then the Medicare Benefit Policy Coverage Manual. The document therefore should not be treated as overriding Medicare coverage rules.

### Facility signal

Optum states an expectation that facilities offering the named autologous CAR-T products be certified, or be in the process of certification, to Foundation for the Accreditation of Cellular Therapy (FACT) Immune Effector Cell standards.

**Research encoding:**

- `site_standard_type = FACT_IEC_expectation`
- `site_standard_source = UHC_Optum_2026-07-01`
- `site_standard_is_fda_rems = false`

This is analytically important after FDA REMS elimination: a payer/facility accreditation expectation must be represented separately from the former FDA REMS certification requirement.

### Universal patient-level review dimensions

The guideline identifies performance status and comorbidities as critical eligibility considerations and explicitly calls out renal, hepatic, cardiac, pulmonary, hematologic, neurologic, autoimmune/immunosuppression, and active/uncontrolled-infection review.

Universal contraindication language includes pregnancy, immunosuppressive treatment for autoimmune disease, active/uncontrolled infection, uncontrolled HIV, specified active viral infections, active GVHD after allogeneic transplant, solid tumors, and previous CAR-T in relapsed/refractory disease.

**Research encoding:** these should be represented as `payer_clinical_review_criteria`, not as Dartmouth clinical criteria.

### Product/indication specificity

The July 2026 guideline contains product- and disease-specific sections for adult and pediatric/AYA ALL, multiple myeloma, non-Hodgkin lymphoma, CLL/SLL, DLBCL, follicular lymphoma, mantle-cell lymphoma, and marginal-zone lymphoma. It includes current FDA-approved products including Yescarta, Tecartus, Carvykti, Abecma, Breyanzi, Aucatzyl, and Kymriah.

The guideline also records the 2025 FDA removal of the CAR-T REMS and distinguishes that change from ongoing safety monitoring.

### Prior authorization status

**Not established by the clinical-guideline document alone.** The guideline establishes review criteria, but plan/product-specific prior-authorization requirements must be captured from the applicable UnitedHealthcare authorization source.

### Current evidence grade

`policy_criteria_captured / authorization_path_pending`

---

## Aetna — Gene-based, Cellular & Other Innovative Therapies pathway

Aetna publishes product-specific Clinical Policy Bulletins and identifies CAR-T agents as Gene-based, Cellular & Other Innovative Therapies (GCIT) products receiving dedicated review.

### Carvykti — CPB 1007

**Source:** Aetna, *Ciltacabtagene Autoleucel (Carvykti)*  
**Policy number:** 1007  
**Last review shown:** 2026-03-13  
**Public source:** https://www.aetna.com/cpb/medical/data/1000_1099/1007.html

#### Authorization signal

The policy states that precertification is required for Aetna participating providers and members in applicable plan designs, through the National Medical Excellence / GCIT pathway.

#### Initial-approval criteria captured

For adult relapsed/refractory multiple myeloma, the public policy requires a prior treatment history including an immunomodulatory agent and proteasome inhibitor, lenalidomide-refractory disease, no previous requested drug or other CAR-T therapy, ECOG 0–2, adequate/stable major-organ function, and absence of specified CNS involvement, clinically significant active infection, active GVHD, and active inflammatory disorder.

The public policy describes treatment as one dose and classifies other indications as experimental/investigational/unproven.

**Research encoding:**

- `prior_authorization_required = true` for applicable Aetna plan designs;
- `review_program = Aetna_GCIT_NME`;
- `repeat_or_prior_car_t_restriction = present`;
- `performance_status_requirement = ECOG_0_2`;
- `organ_function_requirement = present`;
- `infection_gvhd_inflammatory_exclusions = present`.

### Kymriah — CPB 0920

**Source:** Aetna, *Tisagenlecleucel (Kymriah)*  
**Policy number:** 0920  
**Last review shown:** 2026-02-24  
**Public source:** https://www.aetna.com/cpb/medical/data/900_999/0920.html

#### Authorization signal

Aetna states that precertification is required for participating providers and members in applicable plan designs through the same National Medical Excellence pathway.

#### Exclusions and indication structure

The public policy explicitly addresses previous CD19-directed CAR-T exposure, organ-function adequacy/stability, hepatitis/infection, active GVHD, and active inflammatory disorder. It contains separate criteria for pediatric/young-adult B-cell ALL and adult B-cell lymphomas, including age, disease state, prior-therapy, tumor-expression/disease-burden requirements where applicable, and performance-status requirements.

Repeat Kymriah administration is described as experimental/investigational.

### Current evidence grade

`product_specific_policy_and_authorization_path_captured`

### Remaining Aetna work

Capture the corresponding current CPBs for Yescarta, Tecartus, Breyanzi, Abecma, and any other product in the Dartmouth formulary/treatment pathway, then normalize product-specific criteria without assuming that one CPB applies across all CAR-T agents.

---

## Harvard Pilgrim / Point32Health — evidence captured, direct product MNG retrieval still needed

**Current public evidence family:** Point32Health provider medical-drug program updates and Harvard Pilgrim product/network documentation.

### CAR-T program evidence

Point32Health's September 2025 medical-drug program update identifies Carvykti and Kymriah policy updates for Harvard Pilgrim Health Care Commercial and other Point32Health lines of business, specifically removing obsolete REMS language after FDA's 2025 REMS elimination.

A separate October 2025 update reports removal of authorized-treatment-center requirements for Abecma, Breyanzi, Carvykti, Kymriah, Tecartus, and Yescarta for Tufts Health Together. This must **not** be generalized automatically to Harvard Pilgrim Commercial because the stated affected line of business differs.

**Public source:** https://www.point32health.org/provider/point32health-medical-drug-program-updates-092025

### Harvard Pilgrim network/product complexity

Point32Health describes Harvard Pilgrim national products that use combinations of Harvard Pilgrim and UnitedHealthcare networks. Access America products are built on Harvard Pilgrim systems, while Passport is built on UnitedHealthcare systems with UnitedHealthcare managing member administrative services. This creates a material research requirement to capture the specific product and servicing issuer/administrator before assigning a payer policy.

**Public source:** https://www.point32health.org/provider/network-plans/our-plans/harvard-pilgrim-health-care-products

### Current evidence grade

`program_and_product_structure_captured / direct_car_t_MNG_pending`

### Required next retrieval

Retrieve the current Point32Health Medical Benefit Drug Medical Necessity Guidelines for each CAR-T product applicable to Harvard Pilgrim Commercial and record:

- policy/MNG identifier;
- effective date;
- prior authorization requirement;
- specific disease and prior-treatment criteria;
- organ-function/performance criteria;
- prior-CAR-T/repeat-treatment rules;
- site/facility language;
- submission pathway.

---

## Anthem Blue Cross Blue Shield of New Hampshire — policy architecture captured, CAR-T-specific document pending

Anthem's current administrative medical policy states that medical policies and clinical utilization-management guidelines are evidence-based tools, but federal/state law and the member's contract provisions take precedence in benefit determinations.

**Source:** Anthem, ADMIN.00001 *Medical Policy Formation*, published 2026-01-06.  
**Public source:** https://www.anthem.com/medpolicies/abcbs/active/mp_pw_a044135.html

Anthem's current medical-necessity policy defines medical necessity using accepted medical standards, clinical appropriateness, effectiveness, and comparative resource use.

**Source:** Anthem, ADMIN.00004 *Medical Necessity Criteria*, published 2026-07-01.  
**Public source:** https://www.anthem.com/medpolicies/abc/active/mp_pw_a044145.html

Anthem's current therapeutic-apheresis guideline explicitly points CAR-T/ex-vivo cellular therapy review to other applicable plan documents and therefore should not be used as the CAR-T coverage policy itself.

**Source:** Anthem, CG-MED-68 *Therapeutic Apheresis*, published 2026-04-15.  
**Public source:** https://www.anthem.com/medpolicies/abcbs/active/gl_pw_d056816.html

### Current evidence grade

`policy_architecture_captured / NH_car_t_specific_criteria_pending`

### Required next retrieval

Identify the exact CAR-T/autologous cellular-immunotherapy medical policy or clinical UM guideline used for Anthem BCBS New Hampshire and determine whether the applicable commercial and Medicare Advantage products use the same clinical criteria and authorization channel.

---

## Cigna — current coverage-policy index captured, CAR-T-specific policy pending

Cigna's current provider coverage-policy index separates medical/administrative policies from drug coverage policies and states that coverage policies assist in interpreting standard plan provisions.

**Public source:** https://static.cigna.com/assets/chcp/resourceLibrary/coveragePolicies/index.html

The public policy index is current and searchable, but this pass did not resolve a single CAR-T-specific policy document with sufficient confidence to encode product criteria.

### Current evidence grade

`policy_index_captured / car_t_specific_policy_pending`

---

## Cross-payer findings for the Dartmouth model

### 1. `payer` is not a sufficient analytic key

The minimum policy key should be:

`payer_entity + plan/product + line_of_business + servicing_administrator + state/service_area + policy_version`

Harvard Pilgrim/UnitedHealthcare shared-network products illustrate why this is necessary.

### 2. Facility requirements need typed provenance

At least three different concepts can appear in source material:

- former FDA REMS certification;
- payer/network site-of-care requirement;
- FACT Immune Effector Cell accreditation expectation.

These must never be collapsed into a single boolean `certified_center` field.

Recommended fields:

- `facility_requirement_type`
- `facility_requirement_authority`
- `facility_requirement_policy_version`
- `facility_requirement_effective_date`
- `facility_requirement_status`

### 3. Clinical criteria belong to the actor that asserted them

A payer's organ-function, performance-status, infection, prior-treatment, or repeat-CAR-T criterion should be encoded as a payer review rule. Dartmouth clinical candidacy should remain a separate institutional/clinical status even when the criteria overlap.

### 4. Prior authorization is a workflow state, not a clinical state

Recommended authorization states:

- `not_required`
- `required_not_submitted`
- `submitted_pending`
- `additional_information_requested`
- `approved`
- `partially_approved`
- `denied_medical_necessity`
- `denied_benefit_exclusion`
- `denied_network_or_site`
- `denied_missing_authorization`
- `peer_to_peer_pending`
- `appeal_pending`
- `overturned_on_reconsideration_or_appeal`
- `final_denial`
- `expired`
- `unknown`

### 5. Policy drift must be measurable

The REMS removal demonstrates why every gate event needs both a decision timestamp and policy effective/version dates. A 2024 denial or approval cannot be reinterpreted using a 2026 policy without explicitly modeling the policy change.

---

## Immediate next pass

1. Resolve Anthem BCBS New Hampshire's exact CAR-T clinical policy and authorization path.
2. Retrieve the direct Harvard Pilgrim/Point32Health CAR-T product MNGs.
3. Expand Aetna from Carvykti/Kymriah to the complete CAR-T product set relevant to Dartmouth.
4. Capture UnitedHealthcare's plan-specific prior-authorization pathway separately from the Optum clinical guideline.
5. Resolve Cigna's CAR-T drug/medical policy family.
6. Convert the normalized fields into synthetic authorization episodes for approval, information-request delay, medical-necessity denial, network/site denial, and appeal overturn.
