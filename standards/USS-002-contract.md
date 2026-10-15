# USS-002 — Canonical Contract, Local Projections & Controlled Pruning

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Maintain one canonical USS contract; allow independent local adoption and bounded cleanup.

## Rules
1. **002-01** — The canonical approved USS release lives in versioned Git; a local system pins a tag or commit.
2. **002-02** — Local projections must identify the adopted release and applicable rule IDs.
3. **002-03** — Requirements describe outcomes; reference patterns are nonmandatory when equivalent evidence exists.
4. **002-04** — Do not silently rewrite normative requirements in local projections.
5. **002-05** — Pruning levels: P1 mechanical, P2 reversible structural, P3 validated noncritical semantic; protect SSOT and contracts.
6. **002-06** — Keep local operations possible offline; a central always-on USS service is not required.

## Prohibited
- Never auto-prune protected contracts or active recovery artifacts.
- Never assume latest release equals adopted release.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Verify version pin, projection references and protected pruning gate.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
