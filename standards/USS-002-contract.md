# USS-002 — Canonical Contract, Local Projections & Controlled Pruning

**Status:** Normative Standard  
**Cluster:** Cluster 1 (Foundation & Governance)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Maintain one canonical versioned USS contract in Git while enabling independent local system projections and bounded, safe cleanup.

---

## Normative Rules

1. **002-01** — The canonical approved USS release **MUST** live in versioned Git; a consuming system **MUST** pin a specific cryptographic tag or immutable commit hash.
2. **002-02** — Local projections **MUST** identify the adopted release version and specify applicable rule IDs in their local adoption record.
3. **002-03** — Normative requirements **MUST** describe testable outcomes; reference patterns in `patterns/` are nonmandatory when equivalent verifiable evidence is provided.
4. **002-04** — Adopting systems **MUST NOT** silently rewrite or weaken normative requirements in local projections.
5. **002-05** — Automated context and workspace pruning **MUST** be strictly limited to level P1 (mechanical formatting) and level P2 (reversible structural refactoring); level P3 (semantic modification) **MUST** require substantive authorization (Level 3/4); protected content (SSOT, contracts, recovery artifacts) **MUST NOT** be pruned autonomously.
6. **002-06** — Local operations, standards checks, and builds **MUST** remain fully functional offline; a centralized always-on USS service **MUST NOT** be required.

---

## Prohibitions

- Automated processes **MUST NOT** auto-prune protected contracts, active recovery artifacts, or Single Source of Truth records without explicit Operator approval.
- Consuming systems **MUST NOT** assume that the latest published release equals their locally adopted release.

---

## Verification

A compliant system **MUST** provide a verifiable version pin in `SYSTEM_ADOPTION.md`, maintain explicit mapping of applicable rule IDs, and demonstrate that autonomous pruning is blocked on protected contract files.
