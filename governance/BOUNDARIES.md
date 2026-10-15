# Universal System Standards — Governance & System Boundaries

**Status:** Normative Governance Specification  
**Authority:** The Operator (Product Owner)

---

## 1. System Roles & Normative Boundaries

| Actor | Role | Authority & Boundaries |
|---|---|---|
| **Operator** | **Product Owner (Sole Normative Authority)** | The only entity that ratifies decisions, approves normative standard changes, and cryptographically signs releases. |
| **Independent Implementer (OMP in Orca ADE)** | **Technical Implementer & Architect** | Executes engineering, refactoring, and tooling; proposes minimal structures; cannot approve own proposals. |
| **Hermes** | **Operational Consumer & Observation Source** | Operates existing tools; emits observations; runs scheduled review jobs when authorized. **Not a co-PO, not a normative authority, not the implementer.** |
| **Consuming Systems (ATLAS, OMEGA, BI Agent, etc.)** | **Independent Domain Systems** | Pin a USS release version; project requirements locally; maintain complete domain sovereignty within local boundaries. |

Under no circumstances shall any agent, tooling script, or operational consumer assume or claim product ownership or normative approval authority. All normative changes require explicit Operator authorization.

---

## 2. Core Architectural Principles: Skeleton vs. Over-Specialization

1. **The Minimal Skeleton (Technical Backbone):**
   - USS establishes uniform baseline invariants across all independent systems: common trust boundaries, deterministic verification states (`IMPLEMENTED`, `VERIFIED`, `ACCEPTED`), standardized check outcomes (`PASS`, `FAIL`, `CHECK_BLOCKED`, `NOT RUN`), and 100% offline verifiability.
   - USS provides wire, interface, and state contracts in Git.
2. **Domain Sovereignty (No Micromanagement):**
   - Each independent system owns its internal tools, prompts, models, pipelines, and domain instructions inside its own `AGENTS.md`.
   - USS does not impose rigid numerical file-length or token budgets. Sizing is governed by domain complexity and progressive disclosure.
   - USS does not mandate runtime containerization (Docker, Nix) or specific agent orchestration frameworks.
3. **Zero Live Operational Data:**
   - The standards repository contains solely normative specifications, reference patterns, generic templates, and verification tooling.
   - Live system registries, private infrastructure inventories, active operational logs, and live telemetry data are strictly isolated outside this repository.
4. **Single Source of Truth (SSOT):**
   - The consuming repository is the sole authoritative SSOT for its adopted USS version pin and local projection compliance status.
   - Any external system registry is strictly a discovery index and pointer, preventing synchronization drift and split-brain states.
5. **Zero Central Runtime & Offline Integrity:**
   - USS requires no central daemon, no mandatory database, no background observer process, and no automated cross-system push.
   - All validation and verification checks run fully offline using standard-library tooling.
