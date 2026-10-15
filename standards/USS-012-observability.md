# USS-012 — Tiered Observability

**Status:** Normative Standard  
**Cluster:** Cluster 4 (Reliability, Quality & Lifecycle)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Provide actionable health, event, and diagnostic visibility across agent systems without imposing a centralized telemetry daemon or cloud database.

---

## Normative Rules

1. **012-01** — Systems **MUST** expose operational status strictly using the standardized health tokens: `HEALTHY`, `DEGRADED`, `SYSTEM_BLOCKED` (runtime stalled awaiting external resource or manual unblock), `FAILED`, `IDLE`, or `UNKNOWN`.
2. **012-02** — Systems **SHOULD** record structured audit events for task boundaries, security decisions, and recovery events, attaching correlation IDs across distributed operations where feasible.
3. **012-03** — Systems **SHOULD** collect token consumption, monetary cost, and execution duration metrics when telemetry is programmatically accessible.
4. **012-04** — Alert handlers **MUST** deduplicate recurring notifications and escalate only actionable operational failures.
5. **012-05** — Systems **MUST** sanitize operational logs, redacting credentials, private keys, and sensitive prompts before persistence.
6. **012-06** — Hermes **SHOULD** receive distilled, systemic observation summaries rather than exhaustive raw telemetry feeds.

---

## Prohibitions

- Monitoring systems **MUST NOT** infer that silence or absence of telemetry indicates a `HEALTHY` state.
- Systems **MUST NOT** persist raw API secrets, private keys, or unscrubbed model prompts in permanent log files.

---

## Verification

A compliant system **MUST** simulate a stalled operational condition, verify that the health status correctly transitions to `SYSTEM_BLOCKED`, and confirm that diagnostic logs contain no exposed credentials.
