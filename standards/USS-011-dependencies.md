# USS-011 — Managed Reproducibility

**Status:** Normative Standard  
**Cluster:** Cluster 3 (Hygiene, Freshness & Dependencies)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Maintain deterministic, reproducible execution environments and tooling without forcing universal containerization or cloud dependencies.

---

## Normative Rules

1. **011-01** — Systems **MUST** explicitly declare required language runtimes, package dependencies, CLI/MCP tools, and external service integrations in standard declarative manifests.
2. **011-02** — Systems **SHOULD** utilize cryptographic lockfiles and isolated project environments (e.g. virtual environments) wherever supported by the ecosystem.
3. **011-03** — Documentation **MUST** distinguish between initial environment bootstrap, rebuild workflows, and disaster recovery steps.
4. **011-04** — Verification checks **MUST** evaluate functional tool capabilities and runtime execution behavior rather than relying solely on version string matching.
5. **011-05** — Risky dependency upgrades (Level 3) **MUST** undergo verification in an isolated workspace with a validated rollback procedure prior to adoption.
6. **011-06** — Systems **MUST** protect pre-fetched caches and local tooling binaries required for complete offline operation.

---

## Prohibitions

- Standards and systems **MUST NOT** mandate Docker, Nix, or any proprietary virtualization technology as a mandatory condition of USS compliance.
- Automated tools **MUST NOT** execute unpinned package upgrades or blind dependency cache purges in active environments.

---

## Verification

A compliant repository **MUST** demonstrate clean environment bootstrap from its declared manifests and verify successful execution of core smoke tests without external network downloads.
