# Access Gate 1 CI Addendum

**Branch:** `agent/dartmouth-access-eligibility-gates`  
**Gate status:** CONDITIONAL PASS remains in force  
**Date:** 2026-08-20

## Second CI finding

GitHub Actions run `32322755567` failed in the Python 3.12 full test suite after the first deterministic same-hour ordering fix.

The failing cases were:

- `AG-006-peer-to-peer-overturn`
- `AG-007-formal-appeal-overturn`

Both cases contain two `A5` events at the same hour:

1. `overturned_on_reconsideration_or_appeal`
2. `approved`

The prior tie-break rule used lexical status ordering. That made `approved` sort before `overturned_on_reconsideration_or_appeal`, causing the latter to become the final A5 event and incorrectly changing `terminal_authorization_status` from `approved` to `overturned_on_reconsideration_or_appeal`.

## Corrective action

Commit `cda80634fde3d05e33f2fdf344bedd16881ff957` replaces lexical same-time status ordering with an explicit semantic `STATUS_PRECEDENCE` table.

For same-time payer states, the ordering now preserves process semantics so that an overturn event precedes the resulting approval, leaving `approved` as the terminal authorization status.

The sort remains input-order independent and continues to use deterministic secondary keys.

## Gate implication

Access Gate 1 remains **CONDITIONAL PASS** until a full GitHub Actions matrix passes on or after commit `cda80634fde3d05e33f2fdf344bedd16881ff957`.

No Access Gate 2 governed workflow work should be treated as authorized by the synthetic gate until that condition closes.

## Regression rule

Same-time administrative events must be ordered by explicit process semantics rather than incidental lexical ordering whenever terminal state depends on sequence.

Any future addition to the access-status vocabulary that can share a timestamp with another state must define its same-time precedence and receive a regression test.
