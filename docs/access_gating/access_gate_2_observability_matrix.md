# CART-TRACE Access Extension — Gate 2 Observability Matrix

**Status:** planning artifact / non-operational

## Purpose

This matrix defines what must be directly observable, what may be derived, and what must remain unknown when retrospective source evidence is incomplete. It is a precondition for governed Dartmouth mapping work.

Observability labels:

- `direct` — explicit source assertion/event.
- `derived` — deterministic research transformation from direct evidence.
- `partial` — some required dimensions may be present but not sufficient for the gate.
- `not_observable` — source class cannot support the gate.
- `unknown` — not yet assessed in the governed environment.

## A0-A8 observability matrix

| Gate | Required research meaning | Preferred direct source | Minimum direct evidence | Permitted derivation | Explicit non-inference rule | Current governed observability |
|---|---|---|---|---|---|---|
| A0 | referral/case entry | referral intake/order | referral received, case opened, or equivalent intake event | normalize source timestamp/status into A0 event | diagnosis, encounter, or treatment history alone cannot imply referral | unknown |
| A1 | product-indication evidence available for retrospective comparison | program/clinical review source | documented evidence set sufficient for review | derive `evidence_completeness` only | research logic may not declare patient clinically eligible | unknown |
| A2 | Dartmouth program review/acceptance | explicit program disposition | review result or acceptance/non-acceptance event | normalize local disposition vocabulary | payer approval cannot imply program acceptance | unknown |
| A3 | facility/service pathway feasibility | facility/logistics source | explicit pathway feasibility, site/logistics status, or institutional requirement | normalize requirement type and status | prior FDA REMS history alone cannot imply current facility feasibility | unknown |
| A4 | network/benefit applicability | benefit/network record | explicit network/benefit status tied to plan/product | normalize payer/administrator/product dimensions | payer family name alone cannot establish network or benefit applicability | unknown |
| A5 | medical necessity/prior authorization workflow | authorization record | submission, information request, decision, peer-to-peer, appeal, expiration | derive turnaround and delay intervals | clinical candidacy cannot substitute for authorization state | unknown |
| A6 | Medicare-specific administrative coverage context | Medicare/MAC/NCD-linked record | attributable Medicare coverage/authorization state and applicable policy version | attach policy provenance/version | current FDA label or historic REMS status cannot alone define Medicare coverage state | unknown |
| A7 | financial clearance | financial-services record | pending, satisfied, not-satisfied, waived, or documented financial hold | derive financial-clearance interval | payer authorization cannot imply financial clearance | unknown |
| A8 | aggregate administrative access-ready milestone | explicit institutional milestone or governed deterministic derivation | all configured prerequisite administrative gates explicitly satisfied/not applicable with no unresolved hold | derive only from governed rule version | A5 approval alone can never imply A8 satisfied | unknown |

## Field observability requirements

| Schema field | Minimum observability rule |
|---|---|
| `patient_research_id` | governed crosswalk or approved research identifier only |
| `access_episode_id` | derived from versioned episode rule |
| `event_id` | derived deterministically |
| `gate_id` | derived from documented source-to-gate rule |
| `gate_domain` | deterministic lookup |
| `status` | explicit source assertion or documented normalization; never inferred from silence |
| `status_timestamp` | direct event time preferred; record time fallback requires uncertainty |
| `decision_timestamp` | explicit decision time only, otherwise null/unknown |
| `decision_actor_type` | direct actor context or source-class mapping |
| `source_type` | direct source classification |
| `source_record_id` | governed record reference or safe surrogate |
| payer/policy fields | only from attributable payer/benefit/policy/authorization evidence |
| `reason_code` | direct code or documented normalization from governed text |
| `reason_text_original` | governed environment only |
| `facility_requirement_type` | typed by asserting authority |
| `evidence_completeness` | derived from a versioned completeness rule |
| `uncertainty_flag` | derived whenever required evidence, timing, actor, or policy linkage is unresolved |

## Conflict and missingness behavior

1. Missing source evidence produces `unknown`, `partial`, or absence of a mapped event; it does not produce `satisfied`.
2. Conflicting source events are retained as separate events with provenance.
3. A later correction does not erase earlier history unless the source itself documents replacement and the research representation preserves both the prior and corrected states.
4. Payer-policy drift requires event-time policy provenance.
5. Derived A8 must carry the rule version and upstream evidence trace.

## Gate 2 acceptance target

Before Gate 2 can pass, governed review should replace each `unknown` in the current-observability column with one of:

- `direct`;
- `partial`;
- `derived`;
- `not_observable`.

Any gate that is `partial` or `not_observable` must have an explicit analytic limitation and may not be silently reconstructed from unrelated fields.
