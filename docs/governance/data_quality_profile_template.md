# CART-TRACE Governed Data-Quality Profile Template

## Purpose

Use this template inside the governed environment to characterize whether approved institutional source data can support the frozen CART-TRACE reconstruction and metric contracts. This is a descriptive readiness artifact, not a mechanism for changing analytic rules.

## Cohort accounting

Record:

- candidate therapy episodes identified from the approved cohort definition;
- episodes with valid infusion anchors;
- episodes with required encounter/location source coverage;
- episodes classifiable as `reconstructable`, `reconstructable_with_uncertainty`, or `not_reconstructable`;
- metric-specific denominators after follow-up sufficiency review.

Every denominator change requires a machine-readable or tabular reason code.

## Source-domain profile

For each required source domain, record:

| Dimension | Required characterization |
|---|---|
| Availability | present / partial / absent |
| Record count | governed aggregate count where permitted |
| Identifier coverage | proportion with stable source-record IDs |
| Timestamp precision | seconds / minutes / date-only / mixed |
| Timezone handling | explicit offset / local assumed / mixed / unknown |
| Missing start | count and proportion |
| Missing end | count and proportion |
| Duplicate burden | exact and near-duplicate count/proportion |
| Overlap burden | overlapping source intervals or events |
| Conflict burden | incompatible same-time or same-priority evidence |
| Mapping coverage | approved / needs-review / unmapped label coverage |
| Observation completeness | available horizon relative to metric requirements |

## Infusion-anchor profile

Characterize:

- anchor availability;
- duplicate/corrected anchor records;
- timestamp precision;
- timezone/offset validity;
- linkage to episode identifier;
- repeat-infusion frequency and episode disambiguation.

Do not substitute order, scheduling, eligibility, or intent timestamps for the administered infusion event.

## Temporal-quality profile

Report:

1. reversed or invalid intervals;
2. open-ended records;
3. timestamp ties requiring deterministic ordering;
4. overlaps by source domain;
5. cross-domain disagreements;
6. events outside the `[0,720)` primary analytic window;
7. records retained only for limited pre-infusion continuity context;
8. manufactured or unavailable timestamp precision.

## Mapping-quality profile

For each local source label, capture:

- frequency/count;
- mapping status;
- approved canonical state if mapped;
- mapping version;
- reviewer;
- unresolved ambiguity;
- source-domain priority if overlapping evidence is possible.

Primary mapping outputs should include coverage by record and, where useful, by episode. Unmapped labels remain explicit; they must not be silently assigned to a canonical state.

## Reconstruction-quality profile

Summarize:

- interval count per episode;
- transition count per episode;
- unknown-state burden;
- uncertain interval burden;
- episodes affected by open ends;
- episodes affected by unresolved conflict;
- source-record provenance coverage;
- reconstructability category and reason.

Care location is not a direct toxicity or physiologic-severity measure.

## Follow-up profile

For each return-care measure, characterize whether observation is sufficient to establish:

- positive documented return;
- defensible negative 7-day return;
- defensible negative 30-day return;
- incomplete follow-up.

Negative outcomes require the complete requested observation horizon. A documented qualifying return remains observed even if later follow-up is incomplete.

## Publication boundary

Only approved, non-identifying aggregate summaries may leave the governed environment. Patient-level profiles, local identifiers, restricted source labels, PHI, and adjudication evidence remain governed.

## Completion criterion

The profile is complete when all required domains have an explicit availability assessment, temporal and mapping limitations are quantified, reconstructability and follow-up consequences are visible, and no limitation has been handled by silently altering frozen CART-TRACE rules.
