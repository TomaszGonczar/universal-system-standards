# USS-006 — Knowledge Freshness & Reference Integrity

**Status:** Normative Standard  
**Cluster:** Cluster 3 (Hygiene, Freshness & Dependencies)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Maintain accurate alignment between documentation, architectural decisions, and actual system implementations while avoiding spurious invalidation.

---

## Normative Rules

1. **006-01** — Systems **MUST** trigger targeted reference integrity checks whenever dependent files, schemas, or API definitions are modified.
2. **006-02** — Systems **SHOULD** schedule periodic reviews to identify architectural drift not captured by event-driven checks.
3. **006-03** — Verification tools **MUST NOT** treat documentation as stale or obsolete based solely on file age, commit date, or calendar intervals.
4. **006-04** — Systems **MUST** utilize native Git history and filesystem references before introducing external knowledge graph or database infrastructure.
5. **006-05** — Semantic modifications to protected architectural specifications **MUST** require authorization under Level 3 or Level 4 gates.

---

## Prohibitions

- Automated agents **MUST NOT** rewrite architectural intent or modify normative rules based on speculative inferences.
- Tooling **MUST NOT** trigger global repository validation scans on every trivial edit when targeted dependency checks suffice.

---

## Verification

A compliant system **MUST** modify a referenced file and demonstrate that targeted reference integrity checks detect and report the resulting drift.
