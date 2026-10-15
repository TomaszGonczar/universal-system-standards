# USS-004 — Modular Documentation & Context Economy

**Status:** Normative Standard  
**Cluster:** Cluster 1 (Foundation & Governance)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Maintain concise, navigable, and token-efficient documentation across systems while avoiding duplication and arbitrary length constraints.

---

## Normative Rules

1. **004-01** — `INDEX.md` **MUST** serve as the progressive disclosure index and governance entrypoint, rather than duplicating complete normative specification text.
2. **004-02** — Each normative rule **MUST** have exactly one canonical definition; documents **MUST** link to canonical rule definitions rather than copying text.
3. **004-03** — Each standard document **MUST** address one coherent concern and **SHOULD** split into modular files only when modularity improves retrieval or maintenance.
4. **004-04** — Agents **SHOULD** load only task-relevant documents into active working memory, practicing progressive disclosure.
5. **004-05** — Standards and agent instructions **MUST** use concise imperative requirements, explicit scope boundaries, and verifiable acceptance criteria.
6. **004-06** — Machine-readable schemas **SHOULD** be separated from narrative prose only when programmatic validation or automated tooling genuinely requires it.

---

## Prohibitions

- Repositories **MUST NOT** duplicate identical `AGENTS.md` instructions throughout subdirectories; nested files **MUST** specify localized deltas only.
- Systems **MUST NOT** enforce arbitrary numerical token budgets as universal hard caps on critical instructions or domain knowledge.

---

## Verification

A compliant repository **MUST** validate that all internal document links resolve, rule IDs are globally unique, and progressive disclosure links operate correctly.
