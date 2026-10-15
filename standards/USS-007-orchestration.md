# USS-007 — Risk-Adaptive Agent Orchestration

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Delegate only when justified and with bounded authority.

## Rules
1. **007-01** — Each worker task specifies objective, scope, output, acceptance criteria, budget and permitted resources.
2. **007-02** — Prefer one agent or deterministic script over a swarm for simple work.
3. **007-03** — Select the cheapest sufficiently reliable model based on total accepted-result cost.
4. **007-04** — Prevent uncontrolled concurrent writes to shared mutable resources.
5. **007-05** — Limit retries, duration and cost according to risk; coordinator owns integration.
6. **007-06** — Use independent review when consequence or uncertainty warrants it.

## Prohibited
- No infinite delegation loops.
- No permission escalation through delegation.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Inspect a worker task contract and evidence of integrated acceptance.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
