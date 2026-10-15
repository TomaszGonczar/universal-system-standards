# Pattern: Local Projection & System Adoption

**Status:** Reference Pattern  
**Related Standards:** [USS-002](../standards/USS-002-contract.md), [USS-004](../standards/USS-004-documentation.md), [USS-013](../standards/USS-013-controlled-independent-adoption.md)

---

## 1. The Projection Concept

Universal System Standards maintains a canonical specification in Git. Consuming systems do not copy the entire specification repository into their trees. Instead, each system projects only the relevant standards into its local environment through a **Local Projection**:

1. **Version Pinning:** The consuming system pins an approved cryptographic release tag (e.g. `v0.1.0`) in its local `SYSTEM_ADOPTION.md`.
2. **Selective Rule Mapping:** The system declares which specific rule IDs apply to its domain scope.
3. **Local Sovereignty:** The consuming repository is the sole authoritative Single Source of Truth (SSOT) for its adoption status. An external system registry serves purely as a discovery index.

---

## 2. Directory Layout in an Adopting System

A compliant adopting repository typically scaffolds the following minimal artifacts:

```text
consumer-repo/
├── AGENTS.md               # Root agent instructions (mission, boundaries, stop conditions)
├── SYSTEM_ADOPTION.md      # Authoritative USS version pin and compliance ledger
├── observations/           # Drop directory for emitted USS observations
│   └── 2026-10-15-example.md
└── tests/
    └── test_uss_compliance.py # Deterministic local evidence receipts
```

---

## 3. Scaffolding `AGENTS.md` & Hierarchy Rules

- **Root `AGENTS.md`:** Governs the entire repository, defining global mission, security trust boundaries, stop conditions, and completion report format.
- **Nested `AGENTS.md` Files:** Subdirectories may include localized `AGENTS.md` files only to define domain-specific deltas (e.g. frontend test rules, backend db migrations). Nested files **MUST NOT** weaken or contradict root security invariants.
- **Token Economy:** Sizing should be driven by domain complexity and progressive disclosure. Hard numerical token limits are rejected.

---

## 4. Evidence-Based Compliance (Anti-Fabrication)

When declaring `COMPLIANT` status in `SYSTEM_ADOPTION.md`:
- Every declared rule ID **MUST** link to verifiable local test scripts, configuration files, or deterministic execution receipts.
- A version pin alone does not constitute compliance.
- Any standard not yet implemented or partially adopted **MUST** be marked as `PARTIAL`, `EXEMPT`, or `UNKNOWN`, accompanied by an exception entry specifying rationale, owner, risk level, and review expiration.
