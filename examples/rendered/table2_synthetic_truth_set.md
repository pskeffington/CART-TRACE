# Table 2. Prespecified synthetic trajectory truth set

Six synthetic therapy episodes define the controlled Phase 2 oracle used to exercise deterministic reconstruction, transition derivation, post-infusion metrics, uncertainty handling, and acute-care-return logic. These fixtures are methodological test cases rather than estimates of clinical frequency.

| Fixture class | Intended trajectory pattern | Key edge condition | Expected transitions / pattern | Principal requirements tested |
|---|---|---|---|---|
| Routine recovery (`SYN-FIX-001`) | Routine inpatient care followed by discharge | Baseline uncomplicated trajectory | `routine_inpatient -> discharged` | `VALID-001`, `VALID-002`, `RECON-001`, `METRIC-001`, `METRIC-006` |
| Prolonged routine inpatient (`SYN-FIX-002`) | Extended routine inpatient care followed by discharge | Long duration | `routine_inpatient -> discharged` | `VALID-001`, `VALID-002`, `METRIC-001`, `METRIC-006` |
| Transient intermediate-care escalation (`SYN-FIX-003`) | Routine inpatient -> intermediate care -> routine inpatient -> discharge | Nested higher-priority interval | escalation, de-escalation, discharge | `VALID-001`, `VALID-002`, `RECON-004`, `METRIC-003`, `METRIC-004`, `METRIC-005` |
| Intensive-care escalation (`SYN-FIX-004`) | Routine inpatient -> intensive care -> routine inpatient -> discharge -> emergency return | Higher-acuity nesting plus post-discharge return | escalation, de-escalation, discharge, acute-care return | `VALID-001`, `VALID-002`, `RECON-004`, `METRIC-003`, `METRIC-004`, `METRIC-005`, `METRIC-007` |
| Early acute-care return (`SYN-FIX-005`) | Routine inpatient -> discharge -> emergency return | Post-discharge return | discharge, acute-care return | `VALID-001`, `VALID-002`, `RECON-006`, `METRIC-007` |
| Conflicting location evidence (`SYN-FIX-006`) | Routine inpatient -> unknown -> routine inpatient -> discharge | Equal-priority conflict, explicit unknown, missingness | conflict represented as `unknown`; no arbitrary state assignment | `VALID-001`, `VALID-002`, `PROV-003`, `PROV-004`, `RECON-004`, `METRIC-008` |

**Controlled source:** `examples/synthetic/fixture_manifest.json` and the six frozen `phase2_*.json` fixture artifacts.
