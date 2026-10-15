# Universal System Standards (USS) — Draft v0.1

**Status: DRAFT / NOT NORMATIVE / NOT DEPLOYED.** This package is a handoff, not an approved USS Git release. No changes to OMEGA, ATLAS, Hermes or TPG-SYSTEM are implied.

## Purpose
A small, offline-capable, Git-versioned technical contract for independent agent systems. Avoid new central services, agent frameworks and duplicate local sources of truth.

## Authority
- Operator: sole authority to approve normative USS changes and releases.
- Hermes: operational co-PO; observes, deduplicates, drafts, reviews and coordinates; cannot unilaterally approve normative changes or deploy cross-system changes.
- Each system: owns its implementation, local state, local adoption pin and operational controls.

## Reading order
1. `governance/DECISION_LEDGER.md` — ratified decisions.
2. `governance/DEFAULTS_AND_TOKEN_BUDGETS.md` — proposed defaults, not ratified.
3. `governance/BOUNDARIES_AND_SSOT.md` — ownership and conflict resolution.
4. Relevant `standards/USS-*.md` — only those needed for task.
5. `implementation/PLAN_AND_GATES.md` — controlled execution.

## Contract style
Use purpose, numbered imperative rules, prohibited actions, defaults, verification. Every rule has one canonical home. Reference instead of duplication. Keep documents concise, but do not sacrifice safety, accuracy or required nuance.

## Change control
Draft → inspect → validate → Operator approval → Git tag → independent local adoption. A Git tag is not approval unless the Operator has explicitly authorized publication.
