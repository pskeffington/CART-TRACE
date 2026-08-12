# CART-TRACE Governance and Data-Use Boundary

CART-TRACE is a public, synthetic-first research framework. The repository defines methods for reconstructing and characterizing CAR T-cell hospital care trajectories; it is not an operational clinical system.

## Public repository boundary

The public repository may contain:

- synthetic patient/episode identifiers;
- synthetic timestamps and encounters;
- generic care-state mappings;
- schemas, algorithms, tests, and figures generated from synthetic data;
- public methodological documentation.

The public repository must not contain:

- protected health information (PHI);
- direct or quasi-identifying free text copied from clinical records;
- production database credentials or endpoints;
- institution-specific secrets or access-control details;
- raw institutional extracts;
- patient-level governed research data.

## Institutional-data gate

Real hospital data are outside the public development boundary until all required institutional approvals are in place. Depending on the eventual study, these may include research oversight, privacy review, data-use authorization, information-security review, or other local requirements.

CART-TRACE does not presume that any specific approval pathway applies. The approved protocol and institutional determination govern actual data use.

## Minimum-necessary principle

If institutional data are used, extraction should be limited to fields required to answer the thesis question and validate the reconstruction method. The initial minimum footprint is expected to include:

- research episode identifier;
- infusion anchor;
- encounter start/end;
- location or level-of-care information sufficient for mapping;
- discharge and acute-care-return records;
- source identifiers needed for audit/provenance;
- selected timestamps or clinical observations only when necessary for contextual analysis.

CMC/manufacturing data, patient-generated health data, free-text notes, and unrelated clinical domains are not required for the thesis core.

## Separation of environments

Public development and governed analysis should be treated as separate environments.

**Public environment:** synthetic data, public code, test fixtures, documentation.

**Governed environment:** approved institutional inputs, local source-to-canonical mappings, protected validation artifacts, and any restricted outputs.

Only de-identified or aggregate results that are permitted by the governing approval may move from the governed environment into public thesis artifacts.

## Provenance requirements

Every derived interval, transition, and utilization measure should be traceable to:

1. source record identifier(s) within the governed environment;
2. source system/domain;
3. transformation rule or function;
4. transformation version;
5. uncertainty/missingness status where applicable.

Public synthetic examples should exercise the same provenance contract using synthetic source identifiers.

## Missingness and conflict

CART-TRACE must not silently fill missing location or encounter information in ways that create false certainty. Missing or conflicting source information should be represented using explicit uncertainty fields or the canonical `unknown` state.

## Research-use limitation

CART-TRACE outputs are intended for retrospective methods and health-services research. They must not be used to:

- determine patient placement;
- issue clinical alerts;
- diagnose toxicity;
- recommend escalation or de-escalation;
- recommend discharge;
- recommend treatment;
- substitute for institutional clinical workflows.

## Publication and thesis outputs

Before dissemination of governed-data results:

- verify that figures/tables comply with institutional disclosure rules;
- avoid patient-level displays that could enable re-identification unless specifically approved;
- document cohort selection and missingness;
- distinguish methodological validation from clinical utility;
- state that descriptive associations do not establish operational recommendations.

## Governance change control

Changes that broaden the required data footprint, introduce new sensitive domains, or move the project toward prospective/operational use require explicit scope and governance review before implementation.
