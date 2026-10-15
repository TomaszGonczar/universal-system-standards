# USS-014 — Controlled Lifecycle & Knowledge Handover

**Status:** Draft specification derived from ratified workshop decision; Operator approval required before normative release.

**Purpose:** Manage system state, retirement and transfer of SSOT safely.

## Rules
1. **014-01** — Register independent systems with owner, lifecycle state, documentation and adopted USS release.
2. **014-02** — Use EXPERIMENTAL, ACTIVE, MAINTENANCE, MIGRATING, ARCHIVED and RETIRED consistently.
3. **014-03** — Separate pause, archive, decommission, retire and delete.
4. **014-04** — For material migration, classify knowledge ADOPT, ADAPT, REFERENCE or REJECT.
5. **014-05** — Transfer authoritative write ownership only after verified cutover.
6. **014-06** — Review jobs, integrations, credentials, state and recovery before decommission.

## Prohibited
- No autonomous destructive retirement of active systems.
- No implicit dual-write ownership.

## Defaults and limits
- Apply risk-proportionate limits. See `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Proposed numbers are **not ratified**.
- Exceptions require explicit rationale and appropriate authorization.

## Verification
Verify cutover and absence of leftover active jobs before retirement.

## Related
See `governance/BOUNDARIES_AND_SSOT.md` for cross-standard ownership.
