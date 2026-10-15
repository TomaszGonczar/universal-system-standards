# USS-009 — Risk-Adaptive Recovery & Failure Handling

**Status:** Normative Standard  
**Cluster:** Cluster 4 (Reliability, Quality & Lifecycle)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Ensure system and agent failures are bounded, diagnosable, and safely recoverable without inducing state corruption or duplicate side-effects.

---

## Normative Rules

1. **009-01** — Systems **MUST** configure explicit execution timeouts, bounded retry limits, and exponential backoff for operations subject to transient failure.
2. **009-02** — When an operation yields an indeterminate outcome, systems **MUST** reconcile system state before retrying non-idempotent operations.
3. **009-03** — Long-running tasks, migrations, and multi-step workflows **MUST** record durable checkpoints at verifiable execution boundaries.
4. **009-04** — Systems **MUST** scale recovery and reliability requirements to the unified risk matrix ([patterns/risk-matrix.md](../patterns/risk-matrix.md)), mandating verified rollback capabilities for Level 3 and Operator-supervised recovery for Level 4.
5. **009-05** — Checkpoint resumption and rollback routines **MUST** be validated through automated test coverage; systems **MUST NOT** assume unverified recovery paths function during outages.

---

## Prohibitions

- Systems **MUST NOT** execute unbounded retry loops without explicit backoff and maximum duration limits.
- Automated runners **MUST NOT** replay external side-effect operations when previous execution status remains unknown or indeterminate.

---

## Verification

A compliant system **MUST** simulate an execution interruption during a multi-step task and demonstrate clean state recovery from a durable checkpoint.
