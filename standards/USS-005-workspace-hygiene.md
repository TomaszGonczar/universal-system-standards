# USS-005 — Safe Workspace Hygiene

**Status:** Normative Standard  
**Cluster:** Cluster 3 (Hygiene, Freshness & Dependencies)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Maintain clean, deterministic workspaces and remove disposable artifacts without risking the loss of state, recovery data, or active configurations.

---

## Normative Rules

1. **005-01** — Cleanup processes **MUST** classify candidate files into four explicit categories before execution: proven disposable, reversible/archivable, ambiguous, or protected.
2. **005-02** — Systems **SHOULD** automate cleanup only where deterministic safety checks and rollback mechanisms are established.
3. **005-03** — Cleanup processes **MUST** preserve Single Source of Truth records, active environment configurations, durable checkpoints, verification evidence, and files with unknown dependencies.
4. **005-04** — When uncertainty exists regarding a file's utility, agents **MUST** prefer reversible relocations (such as archiving or staging with bounded retention) over permanent deletion.
5. **005-05** — Automated tools **MUST NOT** infer disposability from file age, file size, or filename patterns alone.

---

## Prohibitions

- Automated tools **MUST NOT** perform destructive deletion on unrecognized caches, environments, or scratch directories.
- Automated cleanup **MUST NOT** execute during active incident triage or state recovery operations.

---

## Verification

A compliant system **MUST** provide a dry-run mode for cleanup operations and demonstrate successful file restoration from a simulated automated cleanup.
