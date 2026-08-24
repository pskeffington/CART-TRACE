# Dartmouth Health CAR-T Access Gating Framework

## Status

**Research extension / non-operational / evidence-mapping only**

This workstream is deliberately separate from the frozen CART-TRACE MS Health Data Science capstone core. The capstone reconstructs post-infusion hospital care trajectories and explicitly excludes candidate identification, CAR-T eligibility adjudication, treatment-readiness gating, therapy selection, and prospective decision support.

This extension asks a different health-services question:

> **How can the hospital, payer, and financial-access conditions that determine whether a referred patient can progress toward CAR-T therapy at Dartmouth Health be represented as an auditable, source-grounded sequence of access gates without converting the framework into clinical decision support?**

The framework is descriptive and retrospective. It is not intended to determine whether an individual patient should receive CAR-T therapy, replace Dartmouth clinical review, interpret an insurance contract on behalf of a patient, or automate prior-authorization decisions.

## Dartmouth Health anchor

Dartmouth Cancer Center publicly describes CAR T-cell therapy within its Blood and Marrow Transplantation / Transplant and Cellular Therapy program and directs potential patients and referring clinicians to the program for discussion of whether CAR-T may be a treatment option.

Public Dartmouth sources also establish that:

- specialty care may require referral depending on the patient's health plan;
- referrals should be for a covered service and an in-network provider;
- precertification or prior authorization requirements depend on the health plan and contract;
- Dartmouth Health participates in multiple commercial, Medicaid, Medicare, and Medicare Advantage plans, but network participation varies by plan and geography;
- financial assistance may be available for medically necessary care for eligible uninsured or underinsured patients.

These facts justify separating **clinical candidacy**, **hospital/program acceptance**, **payer coverage**, **authorization**, and **financial clearance** as distinct analytic concepts.

## Canonical access-state model

A patient may occupy more than one access state simultaneously. Unlike the care-trajectory model, this is not a mutually exclusive level-of-care vocabulary.

Recommended status dimensions:

- `referral_status`
- `clinical_candidacy_status`
- `program_acceptance_status`
- `network_status`
- `benefit_coverage_status`
- `prior_authorization_status`
- `financial_clearance_status`
- `treatment_access_status`

Each status should permit at least:

- `not_started`
- `pending`
- `satisfied`
- `not_satisfied`
- `not_applicable`
- `unknown`

No single status should silently substitute for another. In particular, **clinically eligible does not mean covered**, and **covered does not mean clinically eligible**.

## Proposed gate sequence

### Access Gate A0 — Referral / case entry

**Decision represented:** Has a case entered the Dartmouth Transplant and Cellular Therapy evaluation pathway with sufficient referral information to begin review?

Potential evidence fields:

- referral date/time;
- referring clinician/system;
- diagnosis and disease summary received;
- pathology and treatment-history records received;
- insurance information present;
- requested specialty/program;
- referral completeness status.

This gate is administrative. It does not establish CAR-T clinical eligibility.

### Access Gate A1 — Product-indication evidence available

**Decision represented:** Is there sufficient clinical documentation to compare the patient's disease state and prior therapy history with the current FDA-approved indication(s) or other medically accepted indication relevant to the proposed CAR-T product?

Potential evidence fields:

- diagnosis and subtype;
- age;
- disease status;
- prior lines/regimens and response;
- relevant biomarker/antigen information where applicable;
- proposed product;
- source and version of prescribing information;
- unresolved clinical-data gaps.

**Boundary:** This gate records whether evidence is available for review. It does not itself adjudicate treatment.

### Access Gate A2 — Dartmouth program review / acceptance

**Decision represented:** Has the Dartmouth Transplant and Cellular Therapy program accepted the patient for continued CAR-T evaluation or treatment planning?

Potential evidence fields:

- specialist consultation completed;
- multidisciplinary review status if used;
- program disposition;
- reason for hold, deferral, or non-progression;
- alternate treatment or additional workup requested;
- date of decision;
- decision provenance.

Actual Dartmouth internal clinical criteria are governed institutional information and must not be inferred from public web material.

### Access Gate A3 — Facility and service pathway feasibility

**Decision represented:** Can the required CAR-T evaluation and treatment services be delivered through the intended Dartmouth Health facility/program pathway?

Potential evidence fields:

- treatment site;
- product availability/site capability;
- required specialty services available;
- anticipated inpatient/outpatient pathway;
- proximity/monitoring requirements from current product labeling;
- scheduling or capacity constraints;
- required caregiver/logistical planning where institutionally documented.

**Important policy update:** FDA eliminated the REMS for the six then-approved BCMA- and CD19-directed autologous CAR-T products on June 26, 2025. Historical REMS certification therefore must not be modeled as a current universal requirement. Current product labeling and current institutional policy must be versioned separately.

### Access Gate A4 — Payer network / benefit applicability

**Decision represented:** Is Dartmouth Health and the intended treatment pathway within the patient's applicable network and benefit structure, or is an exception/single-case agreement required?

Potential evidence fields:

- payer;
- plan/product;
- employer/group if relevant;
- plan type;
- network status for facility and professional services;
- referral requirement;
- out-of-network benefit status;
- single-case agreement status;
- source policy URL/document and effective date.

Dartmouth's public insurance-participation list is a starting point only. It does not establish that a specific CAR-T episode is covered for a specific member.

### Access Gate A5 — Medical-necessity / prior-authorization determination

**Decision represented:** Has the payer approved the requested CAR-T service under the member's plan and the payer's current medical policy?

Potential evidence fields:

- authorization required yes/no/unknown;
- authorization request date;
- requested product;
- diagnosis and indication submitted;
- payer medical-policy identifier/version;
- decision date;
- approved/denied/pending;
- denial rationale category;
- peer-to-peer/reconsideration/appeal status;
- authorization expiration;
- approved facility/site of care;
- approved units/services if specified.

This is a payer decision, not a clinical eligibility decision.

### Access Gate A6 — Medicare/CMS coverage logic when applicable

**Decision represented:** Does the episode meet the applicable Medicare national coverage framework and any other current Medicare requirements?

CMS NCD 110.24 covers autologous CAR-T for cancer when used for a medically accepted indication, historically stating administration at healthcare facilities enrolled in FDA REMS. FDA eliminated the REMS for the six currently approved BCMA/CD19 autologous products in June 2025. The discrepancy means the research model must preserve policy dates and should not translate the older NCD wording into a current operational facility-certification rule without authoritative Medicare implementation guidance.

Recommended fields:

- Medicare coverage type;
- NCD version/effective date;
- medically accepted indication source;
- product label version;
- any current claims-processing or MAC instruction;
- unresolved policy-version discrepancy flag.

### Access Gate A7 — Financial clearance / patient affordability pathway

**Decision represented:** Are expected patient financial obligations and available assistance pathways sufficiently resolved to permit treatment planning to proceed under institutional policy?

Potential evidence fields:

- estimated patient responsibility;
- deductible/coinsurance status if available;
- manufacturer assistance referral/status;
- foundation support referral/status;
- Dartmouth financial-assistance screening/status;
- travel/lodging support status when documented;
- financial-clearance disposition;
- unresolved affordability barrier.

Financial status must not be represented as medical eligibility.

### Access Gate A8 — Access-ready for treatment scheduling

**Decision represented:** Have the required upstream clinical/program, coverage/authorization, and financial/logistical conditions been satisfied or explicitly waived so the patient can enter the treatment-production/scheduling pathway?

This is an aggregate access milestone, not a clinical-readiness or infusion-readiness determination.

Suggested rule:

`access_ready = program_acceptance satisfied AND required payer authorization satisfied/not_applicable AND required financial clearance satisfied/waived AND no unresolved administrative hold`

The rule must remain configurable because institutional workflows and payer requirements change.

## Analytic distinctions

### Clinical eligibility

A clinician/program determination based on disease, prior therapy, patient condition, product labeling, guidelines, and individualized judgment.

### Hospital/program acceptance

An institutional disposition indicating whether the program will continue evaluation or treatment planning.

### Insurance coverage

Whether the benefit design and applicable coverage policy include the requested service.

### Prior authorization

A payer's prospective approval process for a specific requested service. Authorization is not a guarantee of payment and should not be conflated with coverage.

### Financial clearance

Institutional confirmation that expected financial obligations and assistance pathways have been addressed sufficiently for the workflow to proceed.

### Access-ready

A research-derived administrative milestone indicating that documented non-clinical access barriers are resolved. It must not be labeled `eligible`, `approved for CAR-T`, or `ready for infusion`.

## Minimum event schema

Each gate event should preserve:

- `patient_research_id`
- `episode_id`
- `gate_id`
- `gate_domain` (`referral`, `clinical_review`, `hospital`, `payer`, `financial`, `access`)
- `status`
- `status_timestamp`
- `decision_timestamp` when distinct
- `decision_actor_type`
- `source_system`
- `source_record_id`
- `source_policy_id`
- `source_policy_version`
- `source_policy_effective_date`
- `requested_product`
- `payer_name`
- `plan_name`
- `reason_code`
- `reason_text_original`
- `evidence_completeness`
- `provenance`
- `uncertainty_flag`

Protected health information and payer correspondence must remain in governed environments.

## Delay and attrition measures

The frozen synthetic Gate 3 metric contract is defined in `docs/access_gating/access_gate_3_metric_contract.md`. It formalizes referral-to-access-ready time, authorization turnaround, information-request delay, appeal/reconsideration delay, financial-clearance delay, referral-to-terminal disposition, barrier classification, access-ready proportion, stage reach/attrition, policy-version drift, metric missingness, denominator semantics, and provenance requirements.

These remain health-services/access measures, not treatment-effect, clinical-outcome, or prospective eligibility measures.

## Evidence hierarchy

For each gate, prefer sources in this order:

1. current FDA prescribing information and FDA safety communications;
2. current CMS NCD/claims-processing guidance for Medicare;
3. current payer medical policy and member benefit documents;
4. Dartmouth Health institutional policy/workflow documents inside the governed environment;
5. professional-society guidelines when a clinical criterion is being described;
6. peer-reviewed comparative or health-services research;
7. public-facing webpages only for program and administrative context.

Every policy-derived rule must carry an effective date and version where available.

## Current public evidence anchors — 2026-08-19

- Dartmouth Cancer Center, **CAR T-Cell Therapy**, Transplant and Cellular Therapy / Blood and Marrow Transplantation program: https://cancer.dartmouth.edu/blood-marrow/car-t-cell-therapy
- Dartmouth Hitchcock Medical Center, **Referrals and Precertifications**: https://www.dartmouth-hitchcock.org/patients-visitors/referrals-precertifications
- Dartmouth Hitchcock Medical Center, **Insurances Accepted**: https://www.dartmouth-hitchcock.org/patients-visitors/insurance
- Dartmouth Hitchcock Medical Center, **Financial Assistance**: https://www.dartmouth-hitchcock.org/patients-visitors/financial-assistance
- CMS, **NCD 110.24 — Chimeric Antigen Receptor (CAR) T-cell Therapy**: https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?ncdid=374
- FDA, **FDA Eliminates REMS for Autologous CAR T cell Immunotherapies**, June 26, 2025: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/fda-eliminates-risk-evaluation-and-mitigation-strategies-rems-autologous-chimeric-antigen-receptor

## Current extension gate status

- **Access Gate 1:** PASS — canonical access event model and synthetic baseline.
- **Access Gate 2A:** PASS — synthetic source-to-event mapping.
- **Access Gate 2B preparation/tooling:** PASS — readiness metadata, reporting, provenance, CLI, and governed-review templates.
- **Access Gate 2B governed source validation:** NOT STARTED / authorization-dependent.
- **Access Gate 3A synthetic metric validity:** IN PROGRESS — metric contract frozen; implementation and validation next.
- **Access Gate 3B governed representation validity:** NOT STARTED / authorization-dependent and downstream of Gate 2B governed validation.

## Immediate implementation backlog

1. Implement the frozen Gate 3 episode-level metric representation.
2. Add explicit metric ascertainment/missingness states.
3. Add cohort summaries for access-ready proportion, gate reach, barrier classes, and metric availability.
4. Link each metric to contributing event IDs and mapping/policy versions.
5. Add synthetic cases for unresolved follow-up, repeated information requests, multiple appeal events, and invalid temporal order.
6. Generate deterministic Gate 3 synthetic summary artifacts and CI validation evidence.
7. Build a payer-policy registry for Dartmouth-relevant payers.
8. Record current FDA indication/label versions by CAR-T product.
9. Resolve the post-2025 relationship between CMS NCD 110.24 wording and FDA REMS elimination using current Medicare implementation sources.
10. Define and validate governed Dartmouth source fields only after appropriate authorization.
11. Keep all patient-specific and institutional workflow validation outside the public repository unless explicitly approved for release.
