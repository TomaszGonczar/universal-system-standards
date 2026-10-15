# USS-006 — Knowledge Freshness & Reference Integrity

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Keep references and instructions aligned with actual systems.

## Rules
1. **006-01** — Trigger targeted integrity checks after relevant changes.
2. **006-02** — Run periodic review for drift not covered by event checks.
3. **006-03** — Age alone does not prove documentation is stale.
4. **006-04** — Use existing Git and filesystem references before introducing graph infrastructure.
5. **006-05** — Semantic changes to protected documentation require appropriate approval.

## Prohibited
- Do not auto-rewrite architectural meaning based on guesses.
- Do not scan all content on every trivial edit.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Change a referenced file and verify the targeted drift check detects it.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
