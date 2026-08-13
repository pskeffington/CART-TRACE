# Gate 3 -> 4 Evidence Record

**Transition:** Phase 3 — Deterministic reconstruction -> Phase 4 — Post-infusion utilization measures

**Decision:** PASS

Gate 3 passes on the frozen Phase 2 oracle. The reconstruction implementation now converts source-like encounter/location records into deterministic canonical intervals, typed transitions, and provenance audit records using the Gate 1 semantics. GitHub Actions run `31657957588` completed successfully for commit `536724c4cf996b3192f917d11c909a2ea0eb16fd` using the repository validation workflow.

## Evidence checklist

| Gate requirement | Status | Evidence |
|---|---|---|
| Offset-aware timestamp parsing | Complete | `cart_trace/reconstruction.py`, `tests/test_phase3_primitives.py` |
| Continuous infusion-relative hours | Complete | `relative_hours()` + primitive tests |
| Versioned source-to-canonical mapping | Complete | `config/synthetic_care_state_mapping.json`, reconstruction tests |
| Deterministic source ordering | Complete | `stable_record_sort_key()` + tests |
| Overlap/priority resolution | Complete | reconstruction implementation + frozen escalation fixtures |
| Equal-priority conflict handling | Complete | conflict fixture reconstructs `unknown` with uncertainty |
| Duplicate same-state suppression | Complete | Phase 2 boundary oracle + Phase 3 regression test |
| `[start, end)` interval reconstruction | Complete | boundary sweep + exact oracle comparisons |
| Explicit open-end behavior | Complete | missing-end boundary case + regression test |
| Canonical transition derivation | Complete | exact transition-oracle comparisons |
| Escalation/de-escalation typing | Complete | intermediate/intensive escalation fixtures |
| Discharge typing | Complete | frozen truth sets |
| Acute-care-return typing | Complete | `discharged -> emergency` regression/oracle tests |
| Source-record traceability | Complete | `source_record_ids` propagated on intervals/transitions |
| Reconstruction audit trail | Complete | `build_reconstruction_audit()` |
| Stable canonical serialization | Complete | `stable_serialize()` + repeated-run test |
| Exact interval agreement | PASS | all six frozen Phase 2 fixtures |
| Exact transition agreement | PASS | all six frozen Phase 2 fixtures |
| CI execution | PASS | GitHub Actions run `31657957588` |

## Quantitative acceptance result

The Gate 3 acceptance target requires exact agreement with the prespecified synthetic oracle rather than an approximate performance threshold.

The passing test suite demonstrates:

- 100% expected interval-signature agreement for the six frozen core trajectory fixtures;
- 100% expected transition-signature agreement for the six frozen core trajectory fixtures;
- prespecified `unknown` behavior for equal-priority conflicting location evidence;
- no false transition for duplicate same-state source records;
- explicit null-end/open-end behavior when source end time is missing;
- deterministic output under source-input reordering;
- byte-equivalent stable serialization across repeated reconstruction runs.

## Provenance and auditability

Every reconstructed interval and transition retains one or more contributing `source_record_ids`. The audit layer additionally records:

- a derived artifact-specific provenance identifier;
- source system/domain context;
- transformation name and version;
- mapping-version trace;
- uncertainty flag;
- missingness/open-end reason where applicable.

The public synthetic implementation intentionally leaves execution timestamps out of stable output so reproducibility checks are not contaminated by intentionally variable metadata.

## Interpretation boundary

Passing Gate 3 establishes that CART-TRACE can reproducibly reconstruct the prespecified synthetic hospital care trajectories. It does not establish clinical validity, treatment appropriateness, toxicity severity, or prospective bedside utility.

The implementation remains descriptive and non-operational.

## Frozen Phase 3 artifacts

The following are controlled after Gate 3 passage:

- timestamp parsing and treatment-relative-hour calculation;
- source-label mapping interface and mapping-version behavior;
- deterministic source ordering;
- overlap and equal-priority conflict behavior;
- duplicate same-state suppression;
- interval reconstruction semantics;
- transition classification logic;
- open-end behavior;
- provenance propagation and reconstruction audit contract;
- stable serialization used for reproducibility testing.

Changes to these artifacts require regression against the complete frozen Phase 2 oracle and explicit Gate 3 impact review.

## Authorized next phase

Phase 4 — Post-infusion hospital utilization measures is authorized.

Phase 4 should begin by freezing metric definitions before treating computed values as capstone results. Required initial definitions include:

1. analytic-window clipping and the distinction between pre-infusion continuity context and post-infusion utilization;
2. total inpatient duration;
3. routine, intermediate, and intensive-care duration;
4. high-acuity duration if retained as a combined measure;
5. transition count and time to first escalation;
6. time to discharge;
7. 7-day and 30-day acute-care return;
8. unknown-state burden;
9. zero-versus-missing and incomplete-follow-up behavior;
10. metric provenance and versioning.
