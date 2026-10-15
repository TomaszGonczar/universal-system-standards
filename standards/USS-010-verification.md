# USS-010 — Risk-Adaptive Quality Gates

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Separate implementation, verification and acceptance.

## Rules
1. **010-01** — Track IMPLEMENTED, VERIFIED and ACCEPTED as distinct states.
2. **010-02** — Use deterministic tests and observable evidence whenever practical.
3. **010-03** — Use risk classes Q1–Q4 to select verification depth.
4. **010-04** — Report PASS, FAIL, BLOCKED and NOT RUN accurately.
5. **010-05** — Required failed or unrun tests block ACCEPTED, not necessarily repair work.
6. **010-06** — Avoid self-confirming tests; use independent evidence when warranted.

## Prohibited
- No fabricated test results.
- No marking NOT RUN as PASS or reducing requirements to pass.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Inspect a completed task and verify traceable acceptance evidence.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
