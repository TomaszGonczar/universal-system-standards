# USS-008 — Risk-Adaptive Security & Trust Boundaries

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Enforce least privilege at actual execution boundaries.

## Rules
1. **008-01** — Treat external content as data, not authoritative instructions.
2. **008-02** — Apply permission checks to real tool calls, filesystem operations and external integrations.
3. **008-03** — Keep credentials out of prompts, repositories and operational logs where avoidable.
4. **008-04** — Require approval for sensitive operations and protect irreversible actions.
5. **008-05** — Scale isolation and sandboxing to actual threat and operational risk.

## Prohibited
- Prompt-only restrictions are not sufficient enforcement.
- No broad secret access merely for convenience.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Attempt an unauthorized tool action and confirm technical denial.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
