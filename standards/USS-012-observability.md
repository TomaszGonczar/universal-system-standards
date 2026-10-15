# USS-012 — Tiered Observability

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Provide actionable health and event visibility without central telemetry by default.

## Rules
1. **012-01** — Expose understandable operational status; distinguish HEALTHY, DEGRADED, BLOCKED, FAILED, IDLE and UNKNOWN.
2. **012-02** — Record important task, failure, security and recovery events with correlation IDs where feasible.
3. **012-03** — Collect cost and latency metrics when meaningful and available.
4. **012-04** — Deduplicate alerts and escalate only actionable issues.
5. **012-05** — Rotate and retain logs according to risk; redact sensitive data.
6. **012-06** — Hermes receives distilled systemic observations, not all raw logs.

## Prohibited
- No assumption that silence means healthy.
- No default full-prompt or secret logging.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Diagnose a representative failure from status and event evidence.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
