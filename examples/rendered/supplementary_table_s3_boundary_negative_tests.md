# Supplementary Table S3. Boundary and negative test inventory

Synthetic specification artifact only. These cases define expected behavior at reconstruction and analytic boundaries; they do not estimate clinical frequencies.

| Test case | Requirement | Controlled expected behavior |
|---|---|---|
| Duplicate same-state records | RECON-003 | Collapse duplicate source evidence into one canonical interval; do not create a false transition |
| Missing/open end | VALID-004 | Preserve explicit open/censored interval; duration is not calculable without a defensible end |
| Study-window end | TIME-004 | An event at exactly +720 h is outside the primary `[0,720)` analytic window |
| Adjacent intervals | VALID-004 | Shared boundary is allowed under `[start,end)` semantics without overlap or double counting |
| Same-day return | METRIC-007 | Preserve emergency as the care state and classify the discharged-to-emergency transition as `acute_care_return` |
| Equal-priority conflict | RECON-004 / PROV-003 / PROV-004 | Resolve irreconcilable equal-priority state disagreement to explicit `unknown` with source provenance |
| Invalid canonical state | structural validation | Reject values outside the canonical state vocabulary |
| Missing infusion anchor | temporal validation | Do not calculate treatment-relative trajectory timing without a valid infusion anchor |
| Malformed timestamp | structural/temporal validation | Reject unparseable timestamp input rather than manufacturing chronology |
| Reversed interval | temporal validation | Reject or flag end-before-start intervals as invalid |

**Controlled sources:** `examples/synthetic/phase2_boundary_cases.json`, `examples/synthetic/invalid_phase2_cases.json`, frozen Phase 2 fixtures, and automated tests.
