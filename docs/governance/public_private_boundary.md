# CART-TRACE Public/Private Data Boundary

## Purpose

This document defines which CART-TRACE artifacts may remain in the public research repository and which materials must remain inside an approved governed clinical-data environment.

The boundary protects patient privacy, institutional confidentiality, and scientific traceability while allowing the public repository to document the frozen method and reproducible synthetic implementation.

## Public repository may contain

- canonical schemas, state/transition vocabularies, and frozen temporal semantics;
- synthetic fixtures and controlled synthetic outputs;
- generic source-field inventory templates;
- generic local-mapping and adjudication protocols;
- non-identifying validation methods;
- code and tests that operate on synthetic or appropriately de-identified demonstration data;
- public scholarly tables/figures generated from synthetic data;
- aggregate governed findings only when disclosure is approved and sufficiently non-identifying;
- mapping-coverage or validation summaries only when local governance permits release.

## Governed environment only

The following must not be committed to the public repository:

- PHI or direct patient identifiers;
- dates/timestamps linked to identifiable patients unless formally de-identified for release;
- medical record numbers, account numbers, encounter identifiers, or other restricted local identifiers;
- raw clinical free text;
- patient-level source extracts, screenshots, or source-system exports;
- production credentials, connection strings, secrets, tokens, or internal endpoints;
- institution-specific field/table names when restricted by policy;
- local source-label dictionaries if disclosure is restricted;
- patient-level adjudication notes or reviewer evidence;
- restricted counts or small-cell outputs not approved for disclosure;
- governed working datasets or intermediate files containing patient-level clinical records.

## Repository interface rule

Public code may define the expected semantic contract, but governed extraction logic should be configured so that sensitive source names and credentials are provided only inside the approved environment. The public repository should not require a committed institution-specific configuration to function on synthetic tests.

## Local mapping separation

The public repository may retain:

- the canonical target vocabulary;
- the mapping protocol;
- generic mapping-status vocabulary;
- synthetic mapping examples.

The governed environment should retain:

- exact institution-specific source labels;
- mapping reviewer notes;
- local precedence rationale containing restricted system context;
- versioned local mapping files when those files expose restricted metadata.

If a local mapping can be safely published, release requires separate governance review and must not be assumed by default.

## Validation/adjudication separation

Public artifacts may describe discrepancy categories, validation procedures, and approved aggregate results. Patient-level comparisons, screenshots, source excerpts, disagreement notes, and adjudication evidence remain governed.

## Derived outputs

Before any governed output leaves the approved environment, review should confirm:

1. disclosure is permitted by the applicable approval/data-use framework;
2. no patient-level identifiers or restricted metadata are present;
3. small cells or rare trajectories are handled according to institutional disclosure rules;
4. the output is clearly distinguished from synthetic validation evidence;
5. the output preserves enough method/version metadata for scientific reproducibility without exposing protected data.

## Code-change boundary

Institution-specific extraction adapters may be developed privately if necessary. Changes to the frozen public analytic semantics are not permitted merely to accommodate local data quirks. Local adaptation should occur in source mapping, staging, or governed configuration unless a demonstrated method defect triggers formal gate-impact review.

## Incident rule

If protected or restricted material is discovered in a public branch, issue, pull request, workflow artifact, or commit history, stop further publication activity and follow the applicable institutional and GitHub remediation procedures. Do not rely on a subsequent deletion commit as sufficient remediation for exposed sensitive data.

## Gate 6 readiness criterion

Gate 6 readiness requires that investigators can state, before governed extraction begins, where each data class will live, which artifacts may cross the boundary, who approves disclosure, and how local source/mapping configuration remains separated from the public synthetic repository.
