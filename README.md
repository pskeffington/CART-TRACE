# CART-TRACE

**Research question:** How can heterogeneous longitudinal clinical and patient-generated data be transformed into reproducible patient-level trajectories for studying CAR T-cell treatment, toxicity, recovery, and response?

CART-TRACE is a public research scaffold for representing the CAR-T care pathway as a sequence of **auditable decision gates** linked to explicit evidence and provenance. The project is designed for clinical informatics, outcomes research, reproducibility, and evidence mapping. It is **not** an autonomous clinical decision-support system and does not replace product labeling, institutional review, or clinician judgment.

## Current scaffold

- `gates/gate-registry.yaml` — twelve major decision points from patient identification through post-CAR-T treatment selection.
- `schemas/evidence-record.schema.json` — structured evidence provenance, authority class, population, threshold, uncertainty, and action semantics.
- `evidence/evidence-map.md` — seeded source-grounded map of the strongest evidence classes, regulatory updates, validated tools, and explicit evidence gaps.

## Design principles

1. **Evidence precedes logic.** A computable threshold should not exist unless a source supports it for the relevant product, indication, and population.
2. **Authority is explicit.** Regulatory requirements, society recommendations, trial enrollment criteria, institutional practices, observational associations, and investigational approaches are represented separately.
3. **No silent universalization.** Pivotal-trial inclusion criteria and local practice patterns are not automatically promoted into universal eligibility gates.
4. **Uncertainty is data.** Missing thresholds, conflicting sources, population mismatch, and stale evidence should route to human review rather than produce a false binary decision.
5. **Longitudinal provenance matters.** Source version/date, patient timepoint, product, indication, measurement context, and decision rationale should remain traceable.

## Near-term build path

The next research pass should populate structured evidence records for each gate, beginning with current FDA product labels and safety communications, then major professional-society guidance, pivotal trials, comparative/real-world studies, and externally validated prediction tools. Product- and disease-specific modules should be layered onto the common gate registry rather than forcing one universal CAR-T pathway.

## Scope and safety

This repository is intended for scholarly and public-interest research. Any future software using these structures should require local clinical governance, source-version verification, validation in the intended population, and appropriate human review before patient-care use.
