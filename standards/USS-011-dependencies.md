# USS-011 — Managed Reproducibility

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Keep runtime, tooling and recovery reproducible without mandating containers.

## Rules
1. **011-01** — Declare runtimes, packages, CLI/MCP tools and relevant external service dependencies.
2. **011-02** — Prefer lockfiles and isolated project dependencies where supported.
3. **011-03** — Distinguish bootstrap, rebuild and recovery procedures.
4. **011-04** — Check tool capabilities and behavior, not only version strings.
5. **011-05** — Validate risky updates and maintain rollback or recovery path.
6. **011-06** — Protect caches and environments needed for offline operation.

## Prohibited
- No mandatory Docker or Nix.
- No blind cache purge or destructive dependency upgrade.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Bootstrap a clean representative environment and run smoke checks.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
