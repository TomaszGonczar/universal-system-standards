# USS-009 — Risk-Adaptive Recovery & Failure Handling

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Make failures bounded, diagnosable and recoverable.

## Rules
1. **009-01** — Use timeouts, bounded retries and backoff for transient failures.
2. **009-02** — Reconcile unknown outcomes before retrying non-idempotent actions.
3. **009-03** — Use durable checkpoints for long-running or critical workflows.
4. **009-04** — Distinguish R1 basic, R2 recoverable and R3 critical reliability requirements.
5. **009-05** — Test resume and failure handling; do not assume checkpoint code works.

## Prohibited
- No unbounded retry loops.
- No automatic duplicate external side effects after uncertain outcomes.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Interrupt a representative workflow and verify safe recovery.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
