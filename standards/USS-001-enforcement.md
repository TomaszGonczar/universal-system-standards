# USS-001 — Pragmatic Enforcement

**Status:** Normative Standard  
**Cluster:** Cluster 2 (Execution, Security & Orchestration)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Automate safe, deterministic hygiene operations while strictly escalating risky or irreversible actions to appropriate authorization gates.

---

## Normative Rules

1. **001-01** — An agent or execution harness **MUST** classify proposed actions by reversibility, scope, and consequence according to the unified risk matrix ([patterns/risk-matrix.md](../patterns/risk-matrix.md)) before execution.
2. **001-02** — An execution harness **SHOULD** automatically permit and execute low-risk, deterministic, and reversible operations (Level 1 and Level 2) when automated verification is available.
3. **001-03** — Critical operations (Level 4), including normative standard modifications, irreversible file deletions, credential access, and cross-system boundary changes, **MUST** require explicit Operator authorization.
4. **001-04** — An audit trail **MUST** be preserved for all meaningful automated modifications at Level 2 and Level 3.
5. **001-05** — When the risk classification of an operation cannot be determined with certainty, the agent **MUST** halt execution and request authorization.

---

## Prohibitions

- Systems **MUST NOT** impose manual approval gates for trivial, reversible edits classified as Level 1.
- Agents **MUST NOT** bypass higher-risk approval gates by fragmenting a single substantive operation into multiple minor actions.

---

## Verification

A compliant system **MUST** demonstrate deterministic enforcement by executing one safe automated low-risk operation without human intervention and intercepting one protected high-risk operation with a mandatory authorization halt.
