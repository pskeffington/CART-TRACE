# CART-TRACE Access Extension — Gate 2B Preparation Validation Record

## Validation scope

**Lane:** Access Gate 2B preparation and readiness tooling

**Branch:** `agent/access-gate-2-validation`

**Validated head:** `b99ac18baab0de6b19dfdd037b982426cb9d11a4`

**Validation date:** 2026-08-21

## Decision

- [x] PASS — Gate 2B preparation/readiness tooling
- [ ] CONDITIONAL PASS
- [ ] FAIL

This PASS applies only to the metadata-only preparation layer. It does **not** authorize or validate use of governed Dartmouth Health records.

## CI evidence

GitHub Actions run `32508802417` completed successfully for the validated head.

- Python 3.11 — PASS
- Python 3.12 — PASS
- Gate 1 schema tests — PASS
- controlled Phase 5 output generation — PASS
- scholarly artifact rendering/presence checks — PASS
- full repository test suite — PASS

## Validated preparation package

The Gate 2B preparation package now includes:

- `docs/access_gating/access_gate_2_source_readiness_matrix.md`
- `docs/access_gating/access_gate_2_discrepancy_review_template.md`
- `docs/access_gating/access_gate_2b_review_packet_template.md`
- `docs/access_gating/access_gate_2b_source_observability_worksheet.md`
- `docs/access_gating/access_gate_2_provenance_audit_checklist.md`
- `cart_trace/access_gate2_readiness.py`
- `examples/synthetic/access_gate_2b_readiness_fixtures.json`
- `tests/test_access_gate2_readiness.py`

## Validated readiness behavior

The executable readiness layer demonstrates that:

1. source readiness is evaluated from governance and observability metadata only;
2. authorization, linkage, provenance, and PHI containment are hard prerequisites;
3. hard prerequisites cannot be overridden by an aggregate score;
4. unsupported inference blocks progression;
5. PHI export risk blocks progression;
6. absent or unknown evidence cannot be mapped as satisfied;
7. derived fields require a mapping-rule version;
8. observable fields require source attribution;
9. incomplete readiness dimensions fail validation rather than being silently defaulted;
10. a source set is ready for governed sample review only when every included source is individually governed-ready.

## What this PASS establishes

Gate 2B preparation is methodologically ready to receive institutionally authorized source metadata and to determine whether a proposed retrospective source set is ready for controlled governed sample review.

It supports only the following development claim:

> CART-TRACE now has a reproducible, fail-closed metadata contract for deciding whether governed source validation may begin.

## What this PASS does not establish

This PASS does not establish:

- authorization to access Dartmouth Health patient records;
- existence or availability of any specific Dartmouth source field;
- clinical eligibility for CAR-T;
- member-specific insurance coverage;
- payer authorization validity;
- financial clearance;
- treatment readiness;
- prospective workflow authority;
- permission to export PHI or sensitive source text.

## Gate 2B entry remains blocked until

A governed retrospective sample review may begin only after the specific source set proposed for validation has:

1. explicit institutional authorization;
2. documented source ownership/stewardship;
3. approved minimum-necessary field/date scope;
4. approved research linkage method;
5. source-to-event provenance support;
6. characterized event-time and actor observability;
7. PHI containment and public-export boundaries;
8. a reviewer/steward assigned to resolve discrepancies;
9. source metadata that pass `access_gate2_readiness.py` or a narrower institutionally documented validation pathway.

## Current gate status

**Access Gate 1:** PASS

**Access Gate 2A synthetic mapping:** PASS

**Access Gate 2B preparation/readiness tooling:** PASS

**Access Gate 2B governed source validation:** NOT STARTED / authorization-dependent

**Overall Access Gate 2:** IN PROGRESS
