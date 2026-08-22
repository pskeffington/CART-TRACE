# CART-TRACE Access Extension Literature Review — 2026-08-22

## Review purpose

This focused literature review supports the CART-TRACE retrospective CAR-T access extension. It does not modify the frozen capstone question concerning post-infusion hospital level-of-care trajectories.

The review asks what current literature establishes about CAR-T access barriers and what remains methodologically unresolved for an event-level, provenance-aware reconstruction of the access process.

## Scope and search frame

Priority literature from 2023–2026 was reviewed across PubMed/PMC, emphasizing:

- CAR-T access and implementation barriers;
- insurance, reimbursement, and financial clearance;
- referral and center-level constraints;
- geographic and socioeconomic access;
- disparities and social determinants;
- longitudinal or process-oriented descriptions that can inform an event-level access model.

This is a focused narrative review, not a PRISMA systematic review. It should therefore support construct definition and roadmap prioritization rather than prevalence estimation or causal claims.

## Current evidence synthesis

### 1. CAR-T access is a multi-level health-system problem

Recent reviews consistently describe access barriers at several levels rather than as a single eligibility or insurance decision. Medina-Olivares et al. describe patient, disease, health-system, insurance, referral, manufacturing, regulatory, cost, and treatment-center capacity barriers. A 2025 scoping review of 37 publications similarly organizes barriers across patient, provider, institutional, and policy levels and reports very limited published intervention evidence addressing inequitable access.

This supports CART-TRACE representing access as a sequence of authority-specific events rather than one binary `eligible/not eligible` field.

**Key sources**

- Medina-Olivares M, Gómez-De León A, Ghosh N. *Obstacles to global implementation of CAR T cell therapy in myeloma and lymphoma.* 2024. PMID: 39099684.
- *CAR-T for all? Barriers, facilitators, and interventions to commercial CAR T-cell therapy access.* 2025. PMID: 41448976. DOI: 10.1016/j.blre.2025.101358.
- *Access to CAR T-cell therapy: Focus on diversity, equity and inclusion.* 2023. PMID: 37863793. DOI: 10.1016/j.blre.2023.101136.

### 2. Referral, center capacity, logistics, and reimbursement interact

The implementation literature emphasizes that referral timing, specialized-center capacity, manufacturing/logistical complexity, reimbursement mechanisms, insurance network status, and financial arrangements can interact before therapy is delivered. Recent commentary on standardized pathways highlights differences between centers with pre-negotiated CAR-T contracts and institutions requiring case-by-case financial agreements.

For CART-TRACE, this argues against collapsing referral, institutional acceptance, payer review, and financial clearance into one state. A0–A8 should preserve actor and authority separation.

**Key source**

- *Bridging the Gap: Identifying and Overcoming Barriers to CAR-T Access Through Streamlined and Standardized Pathways.* 2025/2026. PMCID: PMC12809680; PMID: 41551634.

### 3. Insurance is important, but payer status is not equivalent to an observed authorization decision

Multiple reviews identify insurance coverage and reimbursement as major access determinants. Real-world analyses also associate payer type with differences in CAR-T receipt or outcomes. However, insurance category alone does not reveal whether prior authorization was submitted, what policy version applied, which party made a decision, or whether a delay arose from network, benefit, medical-necessity, financial-agreement, or documentation issues.

This distinction is central to the CART-TRACE access model: payer identity and plan metadata are context; authorization submission, review, approval, denial, appeal, or administrative closure must be represented as separately observable events when source evidence exists.

**Key sources**

- *Race and insurance: real-world insights on CAR-T outcomes.* 2024. PMCID: PMC11220370.
- Medina-Olivares et al. 2024. PMID: 39099684.
- *CAR-T for all?* 2025. PMID: 41448976.

### 4. Financial toxicity and logistical burden extend beyond the therapy acquisition cost

Longitudinal qualitative evidence published in 2026 shows that patient concerns evolve over time: early concerns center on treatment access and insurance approval, while later concerns include out-of-pocket costs, work disruption, travel, caregiving, and longer-term financial recovery. Other access reviews identify transportation, temporary lodging, caregiver requirements, and time away from work as substantial barriers.

These findings support a distinction between institutional/payer clearance events and broader patient-level financial or logistical burden. The latter should not be inferred from administrative approval data alone.

**Key sources**

- *Financial toxicity in a phase I/II trial of LV20.19 CAR-T cell for B-cell malignancies: a longitudinal, qualitative study.* 2026. PMCID: PMC12952239.
- *Eliminating REMS for CAR T-Cell Therapies: An Opportunity to Improve Access.* 2025. PMCID: PMC12523345.

### 5. Geographic and socioeconomic disparities remain documented, but local effects vary

National and review literature consistently identifies geography, travel, socioeconomic status, race/ethnicity, insurance, and specialized-center concentration as access concerns. Yet institution-specific findings are not always identical. A Midwest multiple-myeloma referral study found similar apheresis rates by race and did not find distance, income, or insurance to significantly affect access within that cohort, while still identifying a small number of patients unable to proceed because of caregiver or insurance barriers.

This heterogeneity reinforces the need for local descriptive validation rather than assuming national disparity patterns apply unchanged to Dartmouth Health or any specific center.

**Key sources**

- Ghilardi G et al. *Association of age, race, and ethnicity with access, response, and toxicities from CAR-T therapy in children and adults with B-cell malignancies: a review.* 2025. PMCID: PMC11883890.
- *CAR-T Access Disparities for Multiple Myeloma in the Midwest: A Social Determinants of Health Perspective.* 2025. PMCID: PMC12468812.
- *Receiving CAR T-cells gets faster, but not for all in need.* 2025. PMCID: PMC11846599.

### 6. Regulatory context is time-dependent

Access and facility requirements can change materially over time. The FDA eliminated REMS requirements for currently approved autologous CAR-T products in June 2025. Literature published afterward describes the change as a potential reduction in monitoring, travel, and center-related burden.

Therefore, CART-TRACE should never encode facility certification, proximity requirements, or payer/facility rules as timeless attributes. Event-time policy versioning is required whenever historical administrative trajectories are reconstructed.

**Key source**

- *Eliminating REMS for CAR T-Cell Therapies: An Opportunity to Improve Access.* 2025. PMCID: PMC12523345.

## Implications for the A0–A8 construct model

| Gate | Construct | Literature support | Local evidence still required |
|---|---|---|---|
| A0 | referral | strong: referral timing/provider knowledge repeatedly identified | exact referral source, timestamp, status semantics |
| A1 | product-indication evidence | strong clinical/regulatory context, but not equivalent to candidacy | what evidence is actually recorded and by whom |
| A2 | program review/acceptance | strong center-capacity/institutional-process rationale | Dartmouth-specific review events and authority |
| A3 | facility/service feasibility | strong logistics/capacity/regulatory rationale | actual local facility/service constraints and historical version |
| A4 | payer network/benefit context | strong insurance/reimbursement evidence | member-plan and network observability; no inferred coverage |
| A5 | prior authorization/medical-necessity process | strong payer barrier rationale | submission/decision/appeal events and policy versions |
| A6 | Medicare context | relevant for older populations and national coverage context | event-time coverage implementation and local billing workflow |
| A7 | financial clearance | strong financial/reimbursement evidence | distinction among payer decision, contract, patient liability, institutional clearance |
| A8 | aggregate administrative access-ready milestone | methodologically plausible synthesis | must remain nonclinical and only derive from explicitly observed prerequisite states |

## Literature-supported design rules

1. Preserve separate actors: referring provider, CAR-T program, facility, payer, financial office, and research abstraction must not be collapsed into one authority.
2. Treat access as longitudinal rather than binary.
3. Version payer, regulatory, and facility rules by event time.
4. Distinguish contextual variables such as insurance type from actual authorization events.
5. Preserve missing and unobservable states rather than inferring completion.
6. Separate administrative access from clinical candidacy and treatment readiness.
7. Do not assume national disparity findings reproduce locally without governed local validation.
8. Keep patient-level financial/logistical burden conceptually separate from institutional financial-clearance events unless source evidence directly links them.

## Main research gap

The literature is increasingly rich in descriptions of who receives CAR-T, aggregate barriers, disparities, financial toxicity, center capacity, and policy constraints. It is much thinner on reproducible reconstruction of the administrative path itself as an ordered sequence of timestamped, authority-specific, policy-versioned events with explicit provenance and missingness.

That gap is the strongest scholarly position for the CART-TRACE access extension.

A defensible methods contribution would therefore focus on **representation validity**:

> Can heterogeneous retrospective administrative records be transformed into a reproducible CAR-T access trajectory while preserving source provenance, actor authority, policy version, uncertainty, and non-observability?

This is narrower and more supportable than trying to predict access, judge clinical appropriateness, or automate payer decisions.

## Priority literature gaps for the next review pass

1. Studies measuring referral-to-infusion or authorization-related time intervals.
2. Published center-level CAR-T workflow/process maps.
3. Claims/EHR studies distinguishing referral, authorization, leukapheresis, infusion, and abandonment.
4. Prior-authorization turnaround or denial/appeal evidence specific to cellular therapy.
5. FACT/IEC and site-of-care requirements as historical access constraints.
6. Health-services methods for event-log/process-mining reconstruction from EHR and administrative data.
7. Formal data-provenance methods suitable for retrospective clinical process reconstruction.

## Working scholarly conclusion

Current evidence strongly supports studying CAR-T access as a multi-actor, longitudinal health-system process. It also shows why a provenance-aware reconstruction method is needed: the same observed delay may arise from referral, institutional capacity, manufacturing/logistics, payer review, network status, financial agreements, geography, caregiving, or other barriers. Existing literature generally characterizes these factors at cohort or system level; it does not eliminate the need to establish which events are actually observable in a specific institution.

CART-TRACE should therefore continue with a synthetic-first access trajectory model, public literature/construct mapping, and governance preparation while keeping any Dartmouth-specific source validation blocked until appropriate institutional authorization is documented.
