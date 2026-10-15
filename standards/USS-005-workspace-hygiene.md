# USS-005 — Safe Workspace Hygiene

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Keep workspaces clean without losing important state.

## Rules
1. **005-01** — Classify candidates before cleanup: proven disposable, reversible/archivable, ambiguous, protected.
2. **005-02** — Automate cleanup only where safety and recovery are established.
3. **005-03** — Preserve SSOT, active environments, checkpoints, verification evidence, and unknown dependencies.
4. **005-04** — Prefer reversible moves with bounded retention over permanent deletion when uncertain.
5. **005-05** — Do not infer disposability from file age, size or filename alone.

## Prohibited
- No destructive cleanup of unknown caches or environments.
- No deletion during active incident preservation.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Perform dry-run and restore test on representative cleanup.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
