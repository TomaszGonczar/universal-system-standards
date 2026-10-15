# Pattern: Unified 4-Tier Risk Matrix (L1–L4)

**Status:** Reference Pattern  
**Related Standards:** [USS-001](../standards/USS-001-enforcement.md), [USS-002](../standards/USS-002-contract.md), [USS-008](../standards/USS-008-security.md), [USS-009](../standards/USS-009-reliability.md), [USS-010](../standards/USS-010-verification.md)

---

## 1. Executive Summary

The Unified 4-Tier Risk Matrix synthesizes operational reversibility, verification requirements, and authorization boundaries into a coherent taxonomy for autonomous agent execution. It replaces isolated or undefined legacy tokens (such as `Q1–Q4` and `R1–R3`) with deterministic action classes.

---

## 2. Risk Classification Matrix

| Level | Name | Scope & Reversibility | Examples | Autonomous Agent Permission | Quality Gate Requirement (USS-010) | Recovery Tier (USS-009) |
|---|---|---|---|---|---|---|
| **L1** | **Minimal** | Fully reversible, localized, zero production consequence. Scratchpad operations. | Non-instructional documentation fixes, scratchpad notes, temporary diagnostic reads. *(Note: Instructional files like `AGENTS.md`, prompts, skills, and standards are strictly excluded).* | **Full Autonomy** | Local smoke verification; static syntax check. | Best-effort local restart. |
| **L2** | **Low** | Readily reversible workspace changes with deterministic validation. | Deleting disposable build artifacts, reversible file relocations, mechanical code formatting (P1), structural cleanup (P2). | **Autonomous with Passing Tests** | Automated local unit tests (`PASS`). | Idempotent local replay. |
| **L3** | **Substantive** | Significant code changes, state alterations, or instructional updates. | Modifying application code, database schema migrations, environment dependency updates, updating `AGENTS.md` instructions. | **Requires Coordinator / Review Gate** | Automated test suite + independent coordinator review receipt. | Checkpointed durable state with verified rollback. |
| **L4** | **Critical** | Irreversible impact, normative changes, security boundaries, or cross-system side-effects. | Normative standard modifications, publishing releases, irreversible data/repo deletion, accessing credentials/secrets, semantic pruning (P3) of protected assets. | **Operator Authorization Mandatory** | Passing test receipts + explicit Operator cryptographic sign-off. | Operator-supervised disaster recovery. |

---

## 3. Pruning Autonomy Mapping (USS-002 Rule 002-05)

Controlled context and workspace pruning must map directly to this matrix:

1. **P1 (Mechanical Pruning):** Stripping trailing whitespace, normalising newlines, cleaning blank lines. Classified as **L1/L2**. Fully autonomous when verification is available.
2. **P2 (Reversible Structural Pruning):** Relocating obsolete build files to archive directories, collapsing redundant log sections. Classified as **L2**. Autonomous when automated rollback tests pass.
3. **P3 (Semantic Pruning):** Modifying or truncating descriptive text, removing deprecation notes, rephrasing explanations. Classified as **L3**. Requires substantive review.
4. **Protected Content:** Single Source of Truth records, contract specifications, active recovery checkpoints, and `AGENTS.md` root security invariants **MUST NEVER** be pruned autonomously. Modification requires **L4 Operator authorization**.

---

## 4. Default Decision Rules for Agents

- **Rule of Escalation:** When an agent is uncertain whether an operation is L2 or L3, it **MUST** escalate to L3.
- **No Fragmentation:** An agent **MUST NOT** split an L3 or L4 operation into multiple L1 or L2 steps to circumvent authorization gates.
