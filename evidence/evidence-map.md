# CAR-T decision-gating evidence map

Status: **research scaffold, not a clinical decision support system**. This map separates regulatory requirements, consensus recommendations, trial eligibility, observational associations, and investigational thresholds. A blank or unresolved threshold must not be converted into a clinical rule without source-level review.

Evidence was initially verified 2026-08-12 against current FDA materials and indexed primary/consensus literature.

## Evidence hierarchy used in CART-TRACE

1. **A — Regulatory or multiple high-quality sources:** current FDA prescribing information, approval/safety communications, binding regulatory requirements, or concordant high-quality evidence.
2. **B — High-quality consensus or pivotal evidence:** major society consensus/guideline or pivotal/practice-changing trial evidence.
3. **C — Observational/external validation:** high-quality real-world cohorts, comparative observational evidence, externally validated prediction tools.
4. **D — Expert/institutional practice:** expert recommendations or common operational practice without a defensible universal threshold.
5. **E — Investigational/insufficient:** exploratory associations or unresolved evidence gaps.

## Gate-level map

| Gate | Decision | Measurable criterion / evidence target | Current strongest support | Authority | Strength | Auditable implication | Important gap / disagreement |
|---|---|---|---|---|---|---|---|
| G01 Patient identification | Is CAR-T evaluation appropriate for the disease state and prior-treatment history? | Histology/diagnosis, refractory/relapsed status, prior lines and required prior drug classes, age where label-specific | Current FDA product labels and indication pages; product-specific approval letters | Regulatory | A | **Proceed to evaluation only when an on-label indication or explicitly documented investigational pathway exists.** | Indications evolve rapidly and differ substantially by product. Never infer eligibility from a disease label alone; current product-specific USPI must be rechecked. |
| G02 Eligibility / baseline fitness | Is the patient sufficiently eligible/fit to continue? | Performance status, infection, organ function, marrow reserve, CNS disease, comorbidity burden | FDA labels + pivotal-trial populations + EBMT/JACIE/EHA best-practice recommendations | Regulatory + consensus + pivotal | A/B | **Evaluate/mitigate abnormalities; distinguish label contraindications/warnings from trial enrollment cutoffs.** | Trial thresholds are often narrower than real-world practice and should not automatically become absolute exclusion gates. No single universal organ-function or blood-count threshold is defensible across all products/indications. |
| G03 Product / therapy selection | Which product or alternative therapy is best supported? | Exact indication, prior exposure, disease kinetics, efficacy endpoints, toxicity profile, logistics | Current FDA indication/label; pivotal and comparative trials by disease | Regulatory + trial | A/B | **Select within the set of currently indicated options, then document comparative evidence and patient-specific tradeoffs.** | Head-to-head evidence is limited for many products/indications; cross-trial comparisons are confounded. |
| G04 Leukapheresis readiness | Can cell collection proceed? | Clinical stability, infection, lymphocyte/cell-collection feasibility, recent therapy and washout, access | Product/manufacturer collection requirements; EBMT/EHA preparation guidance; trial protocols | Regulatory/technical + consensus | B/D | **Pause or mitigate when collection/manufacturing feasibility is threatened.** | Universal minimum lymphocyte thresholds are not established across products. Manufacturing specifications and washout practices may be product/institution specific. |
| G05 Bridging strategy | Is bridging needed and what strategy is appropriate? | Disease tempo/burden, symptoms, prior sensitivity, planned collection/infusion interval, washout and toxicity | EBMT/EHA CAR-T handbook; disease-specific trials/real-world evidence | Consensus + observational | B/C | **Use bridging as an individualized disease-control strategy rather than an automatic gate.** | No universal regimen or tumor-burden threshold defines when bridging is mandatory; selection bias strongly affects observational comparisons. |
| G06 Lymphodepletion readiness | Can lymphodepleting chemotherapy begin? | Product-specific regimen, interval to infusion, renal/organ function, counts, infection, clinical stability | Current USPI plus EBMT/EHA lymphodepletion guidance | Regulatory + consensus | A/B | **Use the product-specific regimen/timing as the regulatory anchor; pause for unresolved acute instability.** | Dose modification and postponement thresholds can be institution/product specific; avoid importing pivotal-trial laboratory cutoffs as universal rules. |
| G07 Infusion readiness | Should the manufactured product be infused now? | Product release/identity, completion of lymphodepletion, active infection, acute instability, interval requirements | Current product USPI and institutional cellular-therapy release processes | Regulatory + institutional | A/D | **Proceed only after product-specific release and label requirements are met and acute contraindicating conditions have been reviewed.** | Definitions of clinically significant infection/instability are context dependent; not all are reducible to a single numeric threshold. |
| G08 Toxicity risk | What pre-infusion risk state should alter surveillance/mitigation? | Baseline inflammation, counts, tumor burden, performance/organ reserve; CAR-HEMATOTOX inputs (ANC, hemoglobin, platelets, CRP, ferritin) in validated populations | CAR-HEMATOTOX development/validation literature; external population validation; product/pivotal toxicity data | Validated prediction + observational | C | **Use validated scores for risk stratification in populations where validated; do not use them as sole treatment-denial gates.** | Generalizability across diseases, products, lines of therapy, and newer practice remains incomplete. Predictive cutpoints do not automatically establish benefit from a specific intervention. |
| G09 Early post-infusion monitoring | What monitoring intensity and toxicity escalation are required? | CRS/ICANS signs, vitals, neurologic assessment, cytopenias/infection, product-specific delayed toxicities | Current FDA labels; ASTCT CRS/ICANS grading; EBMT/JACIE/EHA best practices | Regulatory + consensus | A/B | **Use current label monitoring requirements and ASTCT grading as the auditable classification backbone.** | Management can remain product- and institution-specific despite standardized grading. FDA eliminated the class REMS in 2025; obsolete REMS certification/tocilizumab-access requirements must not be encoded as current regulatory gates. |
| G10 Response assessment | Has a meaningful response occurred at the appropriate time? | Disease-specific response criteria, imaging, marrow/MRD where validated, timing | Pivotal trials + disease-specific accepted response criteria + follow-up guidance | Trial + consensus | B | **Assess using disease-appropriate criteria and prespecified timing; preserve raw measurement and classification provenance.** | A universal CAR-T response timepoint does not exist across lymphoma, ALL, and myeloma. MRD value and actionability differ by disease/context. |
| G11 Relapse / nonresponse | Is there confirmed primary failure or relapse requiring pathway change? | Confirmed disease recurrence/progression, timing, antigen status where informative, prior response duration | Disease-specific post-CAR-T literature and consensus | Trial/observational + consensus | B/C | **Confirm failure phenotype before redirecting treatment; document target status when it materially informs options.** | Evidence for routine antigen retesting and optimal timing varies by disease; mechanisms are heterogeneous. |
| G12 Subsequent treatment | What therapy is supported after CAR-T failure? | Disease, relapse timing, target expression, fitness, available approved agents/trials | Current disease-specific approvals, prospective studies, high-quality real-world cohorts | Regulatory + trial + observational | A-C | **Re-enter disease-specific treatment selection rather than applying a single post-CAR-T algorithm.** | Sequencing evidence remains rapidly evolving; many comparisons are nonrandomized and subject to referral/immortal-time bias. |

## Seed authoritative sources

### Regulatory

- **FDA, 2025-06-26 — Elimination of REMS for autologous CD19- and BCMA-directed CAR-T products.** The FDA removed requirements for specially certified hospitals/clinics and on-site immediate tocilizumab access under the REMS. Labeling was updated to retain product safety monitoring, including at-least-two-week monitoring language, daily monitoring for at least one week, proximity to a healthcare facility for at least two weeks, and avoidance of driving for two weeks. The class remains subject to routine safety monitoring and 15-year postmarketing long-term safety follow-up. Authority: regulatory; supports G09 and long-term surveillance provenance.
- **FDA, 2024-04-18 — Boxed-warning class labeling change for T-cell malignancies.** FDA required class labeling updates for serious T-cell malignancy risk after BCMA- or CD19-directed autologous CAR-T therapies and recommended lifelong monitoring for secondary malignancies. Authority: regulatory; supports longitudinal surveillance beyond the acute gating sequence.
- **Current FDA product pages/USPI — ABECMA, BREYANZI, CARVYKTI, KYMRIAH, TECARTUS, YESCARTA.** Use these as the primary source for current indication, preparation, dosing, contraindication/warning, and product-specific monitoring fields. Product pages and labels must be date-versioned because indications and warnings change.
- **FDA CARVYKTI safety update, 2025-10-10.** Current FDA product materials identify a boxed warning for immune effector cell-associated enterocolitis after ciltacabtagene autoleucel. This is an example of a product-specific delayed toxicity that should not be generalized to all products without evidence.

### Consensus / professional guidance

- **Lee DW et al. ASTCT Consensus Grading for Cytokine Release Syndrome and Neurologic Toxicity Associated with Immune Effector Cells. 2019. PMID 30592986; DOI 10.1016/j.bbmt.2018.12.758.** Provides harmonized CRS and neurotoxicity/ICANS definitions and grading. Authority: society consensus; supports G09 classification, not automatic treatment thresholds.
- **Hayden PJ et al. EBMT/JACIE/EHA best-practice recommendations for adults and children receiving CAR-T therapy. 2022. PMID 34923107; DOI 10.1016/j.annonc.2021.12.003.** Broad pathway guidance spanning preparation, administration, and follow-up. Authority: professional-society best practice; supports G02-G12 while remaining subordinate to current US regulatory labeling where applicable.
- **Kröger N et al., eds. The EBMT/EHA CAR-T Cell Handbook. 2022. PMID 36121969.** Includes disease-specific bridging, lymphodepletion, CRS/HLH, ICANS, cytopenia/infection, response, and relapse chapters. Authority: expert consensus/handbook; useful for structuring evidence questions rather than establishing universal hard stops.

### Validated / observational risk evidence

- **Rejeski K et al. CAR-HEMATOTOX risk stratification in R/R LBCL. 2022. PMID 35580927; DOI 10.1136/jitc-2021-004475.** Supports risk stratification using baseline hematopoietic reserve and inflammatory markers for severe infection and disease outcomes in CD19 CAR-T-treated R/R LBCL.
- **Population-based external validation of CAR-HEMATOTOX in R/R LBCL. 2025. PMID 40668622.** In a 245-patient real-world cohort, the score was associated with clinically significant prolonged neutropenia and showed moderate discrimination. Authority: external validation; supports G08 as a risk-stratification input, not a standalone eligibility exclusion.

## Explicit non-rules / gaps to preserve

The following should remain `threshold: null` until a source review demonstrates a defensible product- and population-specific threshold:

- universal age cutoff for CAR-T eligibility;
- universal ECOG cutoff outside a specific label/trial/guideline context;
- universal creatinine clearance, LVEF, bilirubin, ANC, platelet, or absolute lymphocyte cutoff for all CAR-T products;
- a single tumor-burden value mandating bridging therapy;
- a universal inflammatory-marker cutoff that should prevent infusion;
- CAR-HEMATOTOX or another risk score as a sole deny/proceed criterion;
- one universal post-infusion monitoring schedule independent of current product labeling;
- one universal response-assessment timepoint across lymphoma, leukemia, and myeloma;
- one universal post-CAR-T relapse sequence.

## Provenance rule

Every future executable or computable gate should point to one or more structured `evidence-record` objects. The implementation should fail closed to **human review / insufficient evidence** when a required source is stale, a threshold is absent, authority classes conflict, or the patient/product population falls outside the source population.
