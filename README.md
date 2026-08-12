# CART-TRACE

**CART-TRACE** is a research framework for reconstructing longitudinal hospital care trajectories around CAR T-cell therapy.

The current MS HSE thesis question is:

> **How can longitudinal clinical data be used to characterize hospital resource utilization and transitions in level of care following CAR T-cell therapy?**

## Current research scope

The thesis focuses on the hospital episode surrounding CAR T-cell infusion, with particular attention to:

- treatment-relative time (`day 0 = infusion`);
- inpatient and outpatient encounters;
- care location and level-of-care transitions;
- high-acuity escalation and de-escalation;
- length of stay;
- discharge timing;
- 7-day and 30-day acute-care reuse;
- provenance, missingness, and reproducible transformation rules.

The primary unit of analysis is the **CAR T-cell therapy episode**, not the individual encounter.

Initial development uses a synthetic-first window of approximately `day -7` through `day +30`, subject to refinement with advisor input and governed data availability.

## Thesis aims

1. **Reconstruct the hospital episode** on a common treatment-relative timeline.
2. **Characterize utilization trajectories** across care settings and acuity levels.
3. **Identify recurrent descriptive care phenotypes** without turning those phenotypes into clinical labels or recommendations.

See [THESIS.md](THESIS.md) for the full thesis scaffold.

## Research guardrails

CART-TRACE is a **research project**, not a clinical decision-support system.

The public repository will not:

- contain PHI, production credentials, or identifying free text;
- issue clinical alerts;
- diagnose CRS, ICANS, or other toxicities from raw signals;
- recommend transfer, escalation, discharge, or treatment;
- represent research associations as validated bedside guidance.

Public development is synthetic-first. Any future use of institutional data must occur under appropriate governance and approvals.

## Repository direction

Near-term implementation is intentionally narrow:

`episode schema -> care-state vocabulary -> treatment-relative time -> synthetic episodes -> transition reconstruction -> utilization metrics -> validation`

Broader CART-TRACE ideas such as patient-generated signals, rural follow-up, prospective monitoring, or other translational extensions are treated as **post-thesis opportunities**, not requirements for the current MS project.

See [ROADMAP.md](ROADMAP.md) for the phased build plan.

## Guiding principle

**Signals into evidence. Evidence into care.**

For the thesis, that means making the hospital care sequence transparent, reproducible, and measurable before attempting prediction or clinical implementation.
