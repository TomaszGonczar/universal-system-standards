# 0001 - Gate 0 Ratified Baseline Architecture & Scope

* Status: accepted
* Deciders: Operator (Product Owner), Independent Implementer (OMP in Orca ADE)
* Date: 2026-10-15
* Technical Story: Universal System Standards (USS) Initial Architecture & Pre-Implementation Audit

---

## Context and Problem Statement

Independent agent runtimes (Hermes, ATLAS, OMEGA, BI Agent) operating within the Operator's ecosystem lacked a common technical wire and state contract. Terminology regarding status, verification, error reporting, and lifecycle was fragmented. Previous draft v0.1 proposals contained over-prescriptive token limits, 31% repeated boilerplate across standard files, vocabulary collisions (`BLOCKED`), undefined risk classes (`Q1–Q4`, `R1–R3`), and governance contradictions (erroneously labeling Hermes as "co-PO").

A clean architectural baseline is required before creating normative files or implementing verification tooling.

---

## Decision Drivers

1. Maintain the Operator's core architectural mandate: a minimal, uniform technical skeleton across all systems, paired with complete local domain sovereignty (no micromanagement).
2. Guarantee 100% offline cryptographic verifiability with zero external dependencies, zero central runtimes, and zero mandatory daemons.
3. Establish unambiguous, deterministic state machines for verification, runtime health, adoption compliance, and system lifecycles.
4. Eliminate unverified or unenforceably broad prompt-only rules.

---

## Considered Options & Ratified Determinations

### Block 1: Governance & Boundaries
* **OD-1 (Repository Identity):** Adopt name `universal-system-standards`, MIT License, main branch, initially private under Operator personal account (`tomaszgonczar`).
* **OD-10 / F-14 (Removal of "co-PO"):** Strike all references to "co-PO". Operator is the sole Product Owner and normative authority. Hermes is an operational consumer and observation source only.
* **OD-6 & OD-15 (Operational Data Isolation):** The standards repository contains only specifications, nonmandatory patterns, and generic templates. Live system registries, inventories, and operational logs are strictly excluded.
* **OD-7 (Hermes Integration Channel):** Hermes interacts with the USS repository in read-only mode, submitting feedback through Markdown observation files or pull requests triaged by Operator/OMP.
* **OD-9 (Decision Recording Procedure):** Historical 16 workshop decisions are frozen in `governance/DECISION_LEDGER.md`. All subsequent architectural choices, amendments, and exceptions are recorded as numbered MADR records in `governance/decisions/`.

### Block 2: Architecture & Skeleton Scope
* **OD-2 & DR-4 (Status of Token Budgets):** Reject arbitrary numerical token brackets (e.g. 300–800 tokens for `AGENTS.md`). Sizing is governed by domain complexity and progressive disclosure. Numeric thresholds (>1,200 tokens) are soft advisory hints only.
* **DR-2 & OD-13 (Unified 4-Tier Risk Matrix):** Replace undefined risk tokens (`Q1–Q4`, `R1–R3`) with a universal L1–L4 matrix:
  - `L1 Minimal`: read-only, scratchpad, non-instructional edits. Full autonomy.
  - `L2 Low`: disposable build artifacts, reversible file moves. Automated with local tests.
  - `L3 Substantive`: application code, schema changes, environment rebuilds, instructional Markdown. Verified tests + review.
  - `L4 Critical`: normative standard changes, irreversible file deletion, credentials/secrets, cross-system boundaries. Operator authorization mandatory.
* **DR-1 (Controlled Pruning Autonomy):** Pruning levels P1 (mechanical) and P2 (reversible structural) may be executed autonomously when tests pass. P3 (semantic modification) requires L3/L4 authorization. Protected content (SSOT, contracts, recovery artifacts) is never pruned autonomously.
* **DR-3 (Lifecycle Vocabulary):** Expand system lifecycle enums to explicitly include `UNKNOWN` and `PLANNED`.
* **DR-5 (Adoption Version SSOT):** The local repository of an adopting system is the sole authoritative Single Source of Truth for its adopted USS version pin. External registries serve purely as discovery indices.
* **DR-6 (Observation Flow):** Observations are standalone Markdown files adhering to `templates/OBSERVATION.template.md`, dropped in designated local channels (e.g. `observations/`). No central daemon or database.
* **OD-14 (AGENTS.md Scoping & Hierarchy):** Root `AGENTS.md` defines global repository invariants (mission, boundaries, stop conditions, report format). Nested `AGENTS.md` files specify localized deltas only and must not weaken root security invariants.

### Block 3: Standards Refinement
* **OD-3 (Language & Deduplication):** Strip 31% repeated boilerplate. Express all normative rules using IETF BCP 14 (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`). Align filenames with titles (`USS-013-controlled-independent-adoption.md`). Preserve existing rule IDs.
* **OD-11 (Vocabulary Disambiguation):** Separate verification test obstacles (`CHECK_BLOCKED`) from runtime system health states (`SYSTEM_BLOCKED`).
* **OD-12 (Model Cost Routing Conditionality):** Rephrase rule `007-03` as a `SHOULD` recommendation conditioned on the programmatic availability of model selection and cost telemetry.

### Block 4: Release Architecture & Tooling
* **OD-5 (Cryptographic Release Signing):** Release tags `vX.Y.Z` must be cryptographically signed (SSH/GPG) by the Operator. Verified offline by tooling.
* **Tooling Scope:** `tools/uss-validate.py` built exclusively with Python 3 standard library, supporting both repository self-validation (`--self`) and consumer adoption validation (`--consumer <path>`).
* **OD-4 & OD-8 (Pilot System & Hermes Review Jobs):** Pilot consumer selection and Hermes review job scheduling are deferred until after release `v0.1.0` is published and verified offline.

---

## Decision Outcome

Chosen option: Ratify all above items as the baseline specification for Phase 1 through Phase 4 implementation of Universal System Standards `v0.1.0-rc1`.

### Positive Consequences
- Guarantees technical consistency across multi-agent environments without imposing artificial limits.
- Eliminates governance ambiguities between Operator, implementer, and operational consumers.
- Prevents drift through clean SSOT boundaries and offline cryptographic enforcement.
- Provides testable, deterministic verification states.

### Negative Consequences / Trade-Offs
- Requires manual Operator key management and cryptographic signing for official releases.
- Eliminates central auto-sync; requires consuming systems to initiate their own version upgrades.
