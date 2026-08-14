# CART-TRACE Governed Source-Field Inventory

## Purpose

This document defines the minimum governed source-data inventory needed to evaluate whether institutional records can support CART-TRACE trajectory reconstruction without changing the frozen synthetic method.

The inventory is a readiness and data-quality artifact. It does not authorize extraction, contain PHI, or prescribe institution-specific field names in the public repository.

## Inventory principles

For each local source field, document:

- source domain/table or interface;
- local field name inside the governed environment;
- semantic role in CART-TRACE;
- data type and timestamp precision;
- timezone/offset behavior;
- expected completeness;
- source-system provenance;
- whether the field is required, conditionally required, or optional;
- whether the field participates in source-to-canonical mapping;
- known ambiguity, duplication, or lifecycle behavior;
- approved owner/steward for interpretation.

Local identifiers and examples containing PHI remain outside the public repository.

## Required source domains

| Domain | Minimum semantic fields | Role | Requirement |
|---|---|---|---|
| CAR T infusion | therapy-episode identifier, infusion timestamp | defines episode and treatment-relative time zero | required |
| Encounter | encounter identifier, start/end timestamps, encounter category | establishes care episodes and continuity | required |
| Location/unit history | source record identifier, start/end timestamps, source location label | primary evidence for level-of-care state | required when available locally |
| Admission/discharge/disposition | admission/discharge timestamps, disposition status or event | supports admission/discharge boundaries | required or conditionally required depending on encounter model |
| Transfer/location change | transfer timestamp and source/destination location identifiers | supports state-transition boundaries and concordance review | conditionally required |
| Emergency care | encounter identifier, start/end timestamps, emergency category/location | identifies emergency state and post-discharge acute-care return | required for return measures |
| Provenance | source system/domain, stable source-record identifier | permits source-to-derived audit | required |
| Observation horizon | last known observation timestamp or equivalent governed ascertainment field | determines follow-up sufficiency | required for return-status interpretation |

## Infusion anchor review

The infusion anchor must be reviewed for:

- whether a distinct administered infusion event exists;
- timestamp precision and timezone/offset availability;
- duplicate or corrected infusion records;
- whether repeat infusions can occur for one patient;
- whether the event can be linked deterministically to the relevant therapy episode.

CART-TRACE uses the actual infusion timestamp as the sole treatment-relative anchor. Order, scheduling, eligibility, or intent timestamps are not substitutes.

## Encounter and location review

Assess whether local records permit reconstruction of contiguous care-state evidence across `[0,720)` hours after infusion. Record:

- location-event granularity;
- whether start/end timestamps are explicit or derived;
- whether unit changes overwrite prior values or preserve history;
- duplicate-event behavior;
- missing-end behavior;
- timestamp ties and ordering behavior;
- whether care-location labels encode administrative rather than clinical location concepts;
- whether emergency, observation, routine inpatient, stepdown/intermediate, and intensive-care settings are distinguishable.

## Mapping-readiness fields

For every unique local location/encounter label proposed for mapping, the governed inventory should capture:

- source label;
- source domain/system;
- local description;
- frequency or record count in the governed cohort;
- candidate canonical state;
- mapping rationale;
- mapping reviewer;
- mapping status: `approved`, `needs_review`, `unmapped`, or `excluded_from_mapping`;
- priority/precedence if multiple source domains can overlap;
- effective mapping version.

Counts may be reported publicly only if permitted and sufficiently non-identifying; otherwise only the mapping structure belongs in public documentation.

## Data-quality dimensions

The inventory should support explicit measurement of:

1. infusion-anchor availability;
2. source-record identifier availability;
3. encounter/location temporal completeness;
4. source-label mapping coverage;
5. timestamp precision and timezone coherence;
6. duplicate and overlap burden;
7. open-end/censoring burden;
8. unresolved conflict burden;
9. observation-horizon completeness;
10. source-to-derived provenance coverage.

These are characterization outputs, not reasons to silently modify the frozen reconstruction rules.

## Readiness categories

Each required field/domain should be classified as:

- `available_and_interpretable`;
- `available_needs_validation`;
- `partially_available`;
- `not_available`;
- `not_yet_assessed`.

A domain marked `partially_available` or `not_available` must include a documented impact on reconstructability or metric availability.

## Public/private boundary

The public repository may contain this generic inventory structure, canonical semantic roles, validation criteria, synthetic examples, and non-identifying aggregate findings when approved. Institution-specific table names, credentials, PHI, raw free text, patient identifiers, sensitive source examples, and restricted local mapping details remain in the governed environment.

## Completion criterion

The source-field inventory is complete when every field needed to establish the therapy episode, infusion anchor, care-state evidence, transitions, provenance, and metric-specific follow-up has a documented local source or an explicit absence/limitation statement, with responsible interpretation and mapping status recorded.
