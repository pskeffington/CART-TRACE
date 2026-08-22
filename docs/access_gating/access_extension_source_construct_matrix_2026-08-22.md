# CART-TRACE Access Extension — Source-to-Construct Evidence Matrix

**Date:** 2026-08-22  
**Scope:** retrospective, descriptive, non-operational CAR-T access-process representation

## Purpose

This matrix links the A0-A8 access constructs to published evidence and identifies where local institutional confirmation remains necessary. Published literature can support the existence and relevance of an access construct, but it cannot establish that a Dartmouth Health source directly observes that construct or that an individual patient satisfied it.

## Evidence classes

- **Strong external construct support** — multiple recent studies or reviews describe the barrier/process stage directly.
- **Moderate external construct support** — literature supports the general process, but operational definitions vary materially across centers or payers.
- **Local-governance dependent** — the construct may be valid, but its observability and authority must be established from local governed sources.
- **Derived-only / prohibited as inference** — the state must not be inferred unless a controlled rule and supporting authoritative evidence exist.

## A0-A8 matrix

| Gate | Construct | External evidence strength | What literature supports | What literature does **not** establish | Local evidence required before governed use |
|---|---|---|---|---|---|
| A0 | Referral / access initiation | Strong | Referral timing, referral-network participation, external vs internal referral, and referral barriers are recurring determinants of CAR-T access. | That every candidate referral is observable in a single source or that referral implies candidacy. | Authoritative referral event source, timestamp semantics, referring actor, receiving program, duplicate/referral-cancellation handling. |
| A1 | Product-indication evidence context | Moderate | Product indication, disease state, manufacturing/product constraints, and treatment availability affect access pathways. | Clinical eligibility, indication satisfaction, or treatment appropriateness for a person. | Versioned product/policy reference and, if used, a governed source showing only the administrative evidence context without adjudicating clinical candidacy. |
| A2 | Program review / acceptance | Strong-to-moderate | Treatment-center assessment, referral acceptance, center capacity, and qualified-center coordination are repeatedly described as pathway steps and barriers. | A universal definition of "accepted" across centers or a clinical readiness determination. | Local program-review status vocabulary, actor authority, timestamps, supersession/cancellation semantics, and steward confirmation. |
| A3 | Facility / service feasibility | Moderate / local-dependent | Center capacity, slot availability, manufacturing/logistics, caregiver requirements, and treatment-center infrastructure can constrain access. | A universal facility-feasibility state or that a capacity barrier equals a patient-specific denial. | Local scheduling/capacity source, service-line authority, slot-status semantics, product-specific restrictions, and historical context. |
| A4 | Payer network / benefit context | Strong-to-moderate | Insurance type, coverage gaps, network/access constraints, and payer complexity are repeatedly associated with CAR-T access. | Member-specific benefit entitlement or that a public payer policy applies to a particular member without plan-level evidence. | Payer entity, plan/product, line of business, network status, service area, effective policy version, and governed member-level evidence if authorized. |
| A5 | Prior authorization / medical-necessity administrative decision | Strong | Slow/complex approval processes, insurance denial, and payer authorization are documented barriers. | Clinical medical necessity, member entitlement, or the correctness of a payer decision. | Submission event, decision event, decision authority, policy/version in force, appeal/resubmission events, and distinction between initial and final resolution. |
| A6 | Medicare / public-payer context | Moderate | Medicare and public-insurance populations show distinct access patterns; public insurance can be associated with lower CAR-T receipt. | That Medicare status alone determines authorization, facility requirements, or payment outcome. | Current program/payer rules, historical versioning, plan type, MAC/admin context as applicable, and event-time policy evidence. |
| A7 | Financial clearance | Strong-to-moderate | Financial toxicity, treatment costs, insurance complexity, travel/relocation expense, caregiver burden, and financial-navigation needs are well documented. | That financial counseling, insurance approval, or patient affordability is equivalent to institutional financial clearance. | Local financial-clearance event/status, responsible authority, timestamp, hold/release semantics, and separation from payer authorization. |
| A8 | Aggregate administrative access-ready milestone | Local-governance dependent | Literature supports that access depends on multiple interacting administrative/logistical barriers. | A universal or clinically meaningful "ready" state, treatment readiness, or eligibility. | Explicit local rule that combines only observable nonclinical prerequisites; versioned rule; authority separation; proof that no clinical or payer inference is introduced. |

## Key literature anchors

1. Luminari S, et al. *Overcoming barriers to referral for CAR T-cell therapy in patients with non-Hodgkin aggressive B-cell lymphomas: A Delphi consensus.* Cytotherapy. 2025. PMID: 40928447.
   - Supports A0-A2 referral pathway structure and center-to-center coordination.

2. *Logistical challenges of CAR T-cell therapy in non-Hodgkin lymphoma: a survey of healthcare professionals.* 2024. PMCID: PMC11572306.
   - Supports referral delay, center capacity, travel, caregiver, and insurance-approval barriers relevant to A0, A2, A3, A5, and A7.

3. *Inequalities in CAR T-cell therapy access for US patients with relapsed/refractory DLBCL: a SEER-Medicare data analysis.* 2025. PMID: 40378343; PMCID: PMC12466227.
   - Supports geographic, socioeconomic, and Medicare-population access differences relevant to A4, A6, and contextual access analysis.

4. *Access barriers to hematopoietic stem cell transplantation and CAR T-cells in US.* 2025. PMID: 40618383.
   - Supports multilevel infrastructure, socioeconomic, and access-system barriers.

5. *Breaking Access Barriers to Autologous Stem Cell Transplantation and Chimeric Antigen Receptor T Cell Therapy in Hematologic Malignancies—an ASTCT-NMDP ACCESS Initiative.* 2026. PMID: 41663013.
   - Supports physician/referral, public-insurance, product, logistics, and ecosystem-level barriers.

6. *Racial and Socioeconomic Healthcare Disparities in Access to Chimeric Antigen Receptor T (CAR-T) Cell Therapy for Blood Cancers.* 2026. PMID: 41651454.
   - Supports financial, insurance, awareness, racial, and socioeconomic access barriers while emphasizing heterogeneity across studies.

7. *Financial Toxicity in a Phase I/II Trial of LV20.19 CAR-T Cell for B-cell Malignancies: A Longitudinal, Qualitative Study.* 2026. PMID: 41485560.
   - Supports the temporal evolution of insurance, caregiver, travel, out-of-pocket, and financial-navigation burdens relevant to A7 and contextual interpretation of A5.

8. *What population-based databases reveal about equity in access to hematopoietic cell transplant and cellular therapy.* 2026. PMID: 42414149.
   - Supports the methodological caution that no single database adequately captures access and that database strengths must be aligned to the research question.

9. *CAR-T Access Disparities for Multiple Myeloma in the Midwest: A Social Determinants of Health Perspective.* 2025. PMCID: PMC12468812.
   - Demonstrates that local findings can differ from national assumptions; in that cohort, distance was not a significant access barrier while caregiver unavailability, slot availability, and insurance denial were observed.

10. *Obstacles to global implementation of CAR T cell therapy in myeloma and lymphoma.* 2024. PMID: 39099684; PMCID: PMC11294242.
    - Supports patient, referral, insurance, regulation, cost, manufacturing, geography, and center-capacity barriers.

## Interpretation rules

1. External literature validates a **construct**, not a local field.
2. A published association must not be converted into an individual-level administrative state.
3. A local source must be reviewed for actor authority, timestamp semantics, status vocabulary, missingness, historical versioning, and provenance before it can support a gate.
4. Where literature shows heterogeneous effects, CART-TRACE must preserve `unknown`, `partial`, or local-dependent status rather than impose a national pattern.
5. A8 is an analytic/admin milestone only and must never be labeled clinical readiness.
6. Payer and financial constructs remain separate even when operationally correlated.
7. Referral, program acceptance, authorization, financial clearance, and treatment receipt are distinct events and must not be collapsed into one access outcome.

## Research gap sharpened by the matrix

The recent literature documents that CAR-T access is multi-stage and influenced by referral pathways, treatment-center capacity, geography, insurance, payer approval, finances, caregiver/logistical burden, and structural inequity. What is less standardized is a reproducible event-level representation that preserves who asserted each state, when it was true, which policy/version applied, what evidence is missing, and which states are not directly observable.

CART-TRACE should therefore prioritize **provenance-aware administrative trajectory reconstruction** rather than eligibility prediction or generic disparity modeling.

## Next implementation implications

1. Tighten `access_source_mapping.py` so a caller cannot assign an arbitrary `target_gate` unsupported by the source class/evidence rule.
2. Add synthetic conflict fixtures for actor authority, superseded decisions, delayed entry, missing timestamps, and policy-version mismatch.
3. Keep A8 derived only from explicit, versioned nonclinical prerequisites.
4. Build a metadata-only local source inventory linking each proposed field to its gate, authority, provenance, and observability class.
5. Treat any future Dartmouth-specific empirical claim as governed evidence requiring institutional authorization and local validation.
