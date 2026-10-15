# USS-003 — Observations to Hermes

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Turn actionable system feedback into controlled USS improvement proposals.

## Rules
1. **003-01** — Systems emit concise observations with source, symptom, evidence, impact and suggested action when known.
2. **003-02** — Hermes deduplicates and groups recurring observations; raw telemetry stays with source systems.
3. **003-03** — Hermes may draft changes and report findings, but cannot approve normative USS modifications.
4. **003-04** — Keep observation provenance and distinguish facts from hypotheses.
5. **003-05** — Do not introduce a dedicated observation agent or database by default.

## Prohibited
- No automatic normative changes based solely on one observation.
- No bulk prompt or secret ingestion into observation inbox.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Trace an observation to a review outcome or explicit no-action decision.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
