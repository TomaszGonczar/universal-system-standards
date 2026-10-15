# USS-007 — Risk-Adaptive Agent Orchestration

**Status:** Normative Standard  
**Cluster:** Cluster 2 (Execution, Security & Orchestration)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Delegate tasks only when complexity or parallelism justifies it, maintaining bounded authority, resource limits, and deterministic coordinator integration.

---

## Normative Rules

1. **007-01** — Each delegated worker task **MUST** specify an explicit objective, bounded scope, expected output schema, measurable acceptance criteria, resource limits, and permitted tools.
2. **007-02** — Orchestrators **SHOULD** prefer a single focused agent or deterministic script over a multi-agent swarm for simple, sequential, or localized work.
3. **007-03** — When model selection and cost telemetry are programmatically accessible, systems **SHOULD** select the most cost-efficient sufficiently reliable model based on total accepted-result cost, referencing [patterns/cost-adaptive-routing.md](../patterns/cost-adaptive-routing.md).
4. **007-04** — Orchestrators **MUST** prevent uncontrolled concurrent writes to shared mutable files or state through serialized waves, explicit locks, or isolated workspaces.
5. **007-05** — Orchestrators **MUST** enforce bounded retries, execution timeouts, and cost limits scaled to risk; the coordinator agent **MUST** retain sole ownership of integration and acceptance.
6. **007-06** — Substantive operations (Level 3) with significant uncertainty or cross-system consequences **SHOULD** undergo independent verification or review prior to acceptance.

---

## Prohibitions

- Systems **MUST NOT** permit infinite, recursive, or unbounded delegation loops.
- Delegated worker agents **MUST NOT** escalate execution privileges beyond the coordinator's authorized boundary.

---

## Verification

A compliant orchestrator **MUST** demonstrate a documented worker task contract with bounded resources and provide traceable evidence of coordinator review and acceptance.
