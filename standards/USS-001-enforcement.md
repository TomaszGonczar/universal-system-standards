# USS-001 — Pragmatic Enforcement

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Automate safe, deterministic hygiene; escalate risky actions.

## Rules
1. **001-01** — Classify actions by reversibility, scope and consequence before execution.
2. **001-02** — Automatically perform low-risk, deterministic and reversible changes when verification is available.
3. **001-03** — Require authorization for normative changes, irreversible deletion, sensitive permissions and cross-system effects.
4. **001-04** — Preserve an audit trail for meaningful automated changes.
5. **001-05** — When risk cannot be determined, stop and request review.

## Prohibited
- No universal approval gate for trivial reversible edits.
- Never bypass a higher-risk approval by splitting work into small operations.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Demonstrate one safe automated edit and one blocked protected edit.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
