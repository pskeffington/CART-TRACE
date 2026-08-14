# CART-TRACE Governed Discrepancy Log Specification

## Purpose

This specification defines the controlled log used during governed mapping, source-concordance review, and adjudication. It separates local data issues from frozen CART-TRACE method defects.

## Required fields

Each discrepancy record should include:

- discrepancy identifier;
- governed episode identifier, when episode-specific;
- source domain(s);
- discrepancy category;
- source-record identifiers or governed references;
- observed issue;
- affected canonical interval, transition, or metric, if any;
- initial interpretation;
- adjudication status;
- adjudicated resolution;
- reviewer(s);
- mapping version and software version;
- whether the issue changes episode reconstructability;
- whether the issue changes metric eligibility;
- whether gate-impact review is required;
- opened and resolved timestamps.

## Discrepancy categories

Use controlled categories such as:

- `infusion_anchor`;
- `timestamp_precision_or_timezone`;
- `missing_or_open_end`;
- `duplicate_source_record`;
- `source_overlap`;
- `source_conflict`;
- `unmapped_label`;
- `mapping_disagreement`;
- `transition_disagreement`;
- `discharge_boundary`;
- `return_event`;
- `followup_sufficiency`;
- `provenance_gap`;
- `implementation_defect_candidate`;
- `other_documented_issue`.

## Resolution classes

A discrepancy must close with one of:

- `source_interpretation_resolved`;
- `mapping_updated_new_version`;
- `uncertainty_retained`;
- `episode_not_reconstructable`;
- `metric_not_calculable`;
- `incomplete_followup`;
- `no_method_change_required`;
- `gate_impact_review_required`.

## Gate-impact rule

Local source interpretation may not silently change frozen public semantics. If resolving a discrepancy would require a new canonical state, new precedence rule, changed interval boundary convention, changed metric definition, changed follow-up rule, or changed synthetic oracle expectation, classify it as `gate_impact_review_required` and stop local reinterpretation until reviewed.

## Public/private boundary

Patient identifiers, raw source evidence, institution-specific confidential labels, and adjudication notes remain governed. The public repository may contain only this specification and approved aggregate discrepancy summaries that cannot identify patients or restricted systems.

## Completion criterion

A discrepancy log is operational when every disagreement that can affect reconstruction, mapping, provenance, or metric interpretation has a unique record, controlled status, accountable resolution, and explicit gate-impact determination.
