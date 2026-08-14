# CART-TRACE Governed Local Mapping Protocol

## Purpose

This protocol defines how institution-specific encounter and location concepts may be mapped to the frozen CART-TRACE canonical care-state vocabulary inside an approved governed environment.

The protocol preserves separation between local source semantics and the public synthetic model. It does not place institution-specific labels, identifiers, or PHI in the public repository.

## Frozen canonical target

Local mappings may target only the existing canonical states:

- `outpatient`;
- `emergency`;
- `routine_inpatient`;
- `intermediate_care`;
- `intensive_care`;
- `discharged`;
- `unknown`.

`acute_care_return` remains a transition type and must never be introduced as a mapped care state.

## Mapping workflow

For each distinct local source label or source-domain concept:

1. identify the authoritative source system/domain;
2. preserve the exact local label in the governed environment;
3. document the local operational meaning using approved metadata or steward review;
4. propose one canonical CART-TRACE state or `unmapped`;
5. record the mapping rationale and reviewer;
6. assign a precedence/priority only when overlapping source domains require deterministic resolution;
7. assign a mapping status;
8. include the rule in a versioned local mapping release;
9. validate the rule against representative governed records before analytic use.

## Mapping statuses

Use one of:

- `approved` — mapping meaning is sufficiently clear for governed reconstruction;
- `needs_review` — meaning remains ambiguous or requires steward/adjudicator input;
- `unmapped` — no defensible canonical mapping exists;
- `excluded_from_mapping` — source concept is not relevant to the CART-TRACE care-state representation.

`needs_review` and `unmapped` concepts must not be silently assigned to a care state.

## Conflict and uncertainty behavior

The frozen reconstruction principles remain authoritative:

- higher-priority evidence may supersede lower-priority overlapping evidence only under a documented local precedence rule;
- equal-priority disagreement between incompatible canonical states resolves to `unknown`;
- unresolved or unmapped evidence remains explicit rather than being forced to the closest category;
- mapping uncertainty and source conflict should be distinguishable during governed review even if the current public schema carries a general uncertainty field.

## Priority assignment

Priority is a source-resolution property, not a clinical-severity score. It should reflect which source domain is more authoritative for care-location reconstruction when records overlap.

Every non-default priority assignment must document:

- source domains being ordered;
- reason for authority ordering;
- reviewer/owner;
- evidence used to establish precedence;
- effective mapping version.

Do not infer priority solely from the apparent acuity of a source label.

## Versioning

Each governed mapping release should record:

- mapping version;
- effective date;
- source-system/version context if relevant;
- approved rules;
- changed rules since prior version;
- reviewer(s);
- reason for each material change;
- affected episode count or scope where permitted;
- validation evidence for changed rules.

A mapping change after analysis begins requires an impact assessment and regeneration of affected governed trajectories and metrics.

## Validation sample

Before a mapping version is accepted for analytic use, review a stratified set of governed records that includes, where available:

- common routine inpatient labels;
- intermediate/stepdown labels;
- intensive-care labels;
- emergency labels;
- outpatient labels;
- transfer scenarios;
- labels with multiple possible meanings;
- overlapping source-domain evidence;
- unmapped or disputed concepts.

The goal is semantic/source concordance, not estimation of clinical incidence.

## Mapping coverage reporting

Governed analysis should quantify:

- unique labels assessed;
- records covered by approved mappings;
- records assigned `needs_review`;
- records left `unmapped`;
- episodes affected by mapping uncertainty;
- episodes containing `unknown` attributable to source conflict or mapping limitation.

Mapping coverage should be reported separately from trajectory reconstruction success.

## Public/private boundary

Public artifacts may document the protocol, canonical targets, versioning rules, status vocabulary, and approved aggregate mapping-quality measures when permitted. The local label dictionary, local source names where restricted, patient-level examples, PHI, reviewer notes containing sensitive context, and governed record excerpts remain private.

## Completion criterion

The local mapping protocol is ready for Gate 6 when all local concepts needed for the intended cohort have been inventoried, each has a controlled mapping status, precedence rules are documented, a version identifier exists, and the planned validation/adjudication process can detect and resolve semantic disagreements without changing the frozen canonical model implicitly.
