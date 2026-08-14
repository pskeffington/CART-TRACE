# CART-TRACE Governed Cohort and Infusion-Anchor Specification

## Purpose

This document defines the minimum cohort and index-event specification required before CART-TRACE is applied to governed retrospective hospital data. It is a pre-analysis design artifact and contains no patient data, institution-specific identifiers, or local source mappings.

The objective is to preserve the frozen CART-TRACE analytic semantics while making cohort construction auditable in a governed environment.

## Unit of analysis

The primary unit is the **CAR T-cell therapy episode**, not the patient, admission, encounter, or product order.

A patient may contribute more than one therapy episode only if the governed protocol explicitly permits repeated CAR T-cell infusions and each episode has an independently identifiable infusion anchor and observation window. Repeated episodes must never be collapsed implicitly.

## Index event

The index event is the documented CAR T-cell infusion timestamp.

Required properties:

- one defensible timestamp per therapy episode;
- sufficient temporal precision to support continuous hour-relative calculations;
- timezone or offset interpretation sufficient for deterministic normalization;
- source provenance identifying the governed record or records supporting the anchor;
- no substitution of admission date, order date, product-release date, leukapheresis date, lymphodepletion date, or another treatment milestone for the infusion timestamp.

The frozen treatment-relative definition remains:

`relative_hours = (event_timestamp - infusion_timestamp).total_seconds() / 3600`

Infusion is `0` hours. Negative values are retained when source records precede infusion; they are not floored to zero.

## Primary analytic window

The primary post-infusion utilization window remains:

`[0, 720)` hours relative to infusion.

An event beginning exactly at `+720` hours is outside the primary analytic window. Limited negative-time encounter or location evidence may be retained only to establish continuity into the post-infusion period.

## Target cohort definition

The governed cohort should include therapy episodes meeting all of the following minimum criteria:

1. a documented CAR T-cell infusion event within the approved study period;
2. an episode identifier that can be linked, within the governed environment, to relevant hospital encounter and location records;
3. a usable infusion timestamp meeting the anchor requirements above;
4. at least one source domain capable of representing post-infusion hospital care or disposition during the study window;
5. data use permitted by the governing protocol, approval, and institutional access controls.

This definition identifies episodes eligible for **reconstruction attempt**. It does not guarantee that every episode is reconstructable or that every utilization metric is calculable.

## Exclusions from the core cohort question

The core capstone cohort should not be defined using prospective decision-support criteria or model-derived risk predictions.

The following are outside the required cohort definition unless an approved protocol explicitly requires them for descriptive stratification:

- treatment eligibility or readiness adjudication;
- toxicity grade or predicted toxicity risk;
- leukapheresis or manufacturing outcomes;
- bridging-therapy choice;
- product-selection recommendations;
- physiologic deterioration prediction;
- patient-generated device or wearable data;
- prospective alert eligibility.

## Reconstructability is an outcome of data review

Episodes that meet the target cohort definition should subsequently be classified as:

- `reconstructable`;
- `reconstructable_with_uncertainty`;
- `not_reconstructable`.

Reconstructability must not be used as an undocumented pre-extraction exclusion criterion. The frequency and reasons for non-reconstructability are themselves data-quality findings.

## Repeat infusion handling

If repeat CAR T-cell therapy is present:

- assign a distinct `episode_id` to each infusion;
- preserve the exact infusion timestamp for each episode;
- prevent source records from being attributed to more than one episode unless the overlap is explicitly reviewed;
- prespecify how overlapping `[0,720)` windows will be handled;
- report repeat-treatment episodes separately if their interpretation materially differs from first treatment episodes.

If repeat treatment is outside the approved study design, exclude it through an explicit protocol rule rather than through downstream reconstruction logic.

## Observation horizon and follow-up

The `[0,720)` infusion-relative window governs the primary hospital-utilization measures. Some post-discharge return measures may require observation extending beyond `+720` hours when discharge occurs late in the primary window.

Therefore, the governed extract should retain an episode-specific `observation_end_relative_hours` sufficient to determine metric follow-up status.

A negative return result may be called observed only when the required follow-up horizon is available. Otherwise the metric must retain the frozen `incomplete_followup` status.

## Minimum cohort accounting

Before primary analysis, report at minimum:

- number of therapy episodes identified from the approved infusion source;
- number with a usable infusion anchor;
- number entering reconstruction review;
- number `reconstructable`;
- number `reconstructable_with_uncertainty`;
- number `not_reconstructable`;
- reasons for non-reconstructability;
- number with sufficient follow-up for each return-care metric.

These counts should be generated in the governed environment and should not contain patient identifiers in public outputs.

## Provenance requirements

For each included episode, governed processing should retain enough provenance to identify:

- the source record supporting the infusion anchor;
- source systems/domains contributing encounter and location evidence;
- the local mapping version applied;
- records contributing to each canonical interval and transition;
- records contributing to each metric result.

Public repository artifacts should contain only synthetic examples, field specifications, aggregate non-identifying methodological summaries, or other material explicitly approved for release.

## Pre-analysis cohort review checklist

Before governed reconstruction begins, confirm:

- [ ] governing approval and data access are active;
- [ ] study period is defined;
- [ ] infusion source and timestamp field are identified;
- [ ] timezone/offset interpretation is documented;
- [ ] therapy-episode identifier strategy is documented;
- [ ] repeat-infusion policy is documented;
- [ ] primary `[0,720)` window is preserved;
- [ ] required post-discharge follow-up horizon is understood;
- [ ] reconstructability is treated as a review result, not a hidden exclusion;
- [ ] public/private artifact boundaries are established;
- [ ] no local preprocessing rule silently changes frozen CART-TRACE semantics.

## Gate relationship

This specification supports Gate 6 governance/data readiness. It does not by itself authorize a governed application. Gate 6 additionally requires the source-field inventory, local mapping/versioning protocol, validation/adjudication plan, public/private boundary, and confirmation of approvals and access.
