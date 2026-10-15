# USS-010 — Risk-Adaptive Quality Gates

**Status:** Normative Standard  
**Cluster:** Cluster 4 (Reliability, Quality & Lifecycle)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Enforce rigorous, evidence-based quality gates by maintaining strict separation between implementation, verification, and normative acceptance.

---

## Normative Rules

1. **010-01** — Systems and task coordinators **MUST** track `IMPLEMENTED` (code authored), `VERIFIED` (tests and checks executed with passing receipts), and `ACCEPTED` (normative sign-off by designated authority) as distinct, sequential states.
2. **010-02** — Quality gates **MUST** require deterministic automated tests, observable execution receipts, or cryptographic proofs wherever technically feasible.
3. **010-03** — Verification depth and test stringency **MUST** scale according to the unified risk matrix ([patterns/risk-matrix.md](../patterns/risk-matrix.md)), requiring independent integration proofs for Level 3 and Operator sign-off for Level 4.
4. **010-04** — Automated verification runners **MUST** report check outcomes strictly using the standardized tokens: `PASS`, `FAIL`, `CHECK_BLOCKED` (execution hindered by environment or prerequisite failure), or `NOT RUN`.
5. **010-05** — Any required check reporting `FAIL`, `CHECK_BLOCKED`, or `NOT RUN` **MUST** block advancement to `ACCEPTED`, but **MUST NOT** prevent iterative repair or diagnostic execution.
6. **010-06** — Quality gates **MUST** reject self-confirming test structures where test assertions merely echo implementation logic without testing actual behavioral boundaries.

---

## Prohibitions

- Agents and systems **MUST NOT** fabricate verification results or claim `PASS` without recorded execution receipts.
- Systems **MUST NOT** mark unexecuted checks (`NOT RUN`) as `PASS` or silently dilute acceptance requirements to force a passing gate.

---

## Verification

A compliant workflow **MUST** demonstrate distinct transitions from `IMPLEMENTED` through `VERIFIED` with recorded receipts, proving that a `CHECK_BLOCKED` or `FAIL` outcome halts progression to `ACCEPTED`.
