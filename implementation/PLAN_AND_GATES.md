# Hermes implementation plan — draft-first

## Phase 0 — Discovery (read-only)
Inspect existing Hermes environment and repositories *only where already authorized*. Find relevant paths, local conventions, current scheduler and git status. Never assume target paths or that migrations are complete. Report facts and unknowns. Do not modify external systems.

## Phase 1 — Create draft USS repository
Create minimal files from handoff; preserve decision ledger and proposed defaults separately. Do not create extra services, databases or agents.

## Phase 2 — Normalize standards
Refine 14 standards for concise imperative language. Enforce unique IDs, single canonical ownership and traceability to ratified decisions. Flag any substantive interpretation as `DECISION REQUIRED`.

## Phase 3 — Build local validator
Use the simplest existing runtime. Validate: 14 documents, 16 ledger decisions, unique IDs, index links, no missing sections, draft/proposal labeling, no broken local references. Optional approximate token-budget report; never auto-truncate.

## Phase 4 — Registry and one-system pilot
Prepare minimal registry from *verified* facts only. Select pilot with Operator; perform read-only gap assessment first. Draft adoption record; do not auto-deploy changes to pilot repo.

## Phase 5 — Hermes workflow
Use existing scheduler if present and authorized. Prepare 30/90-day review instructions; do not silently enable jobs, outbound notifications or autonomous repo writes.

## Phase 6 — Independent review and release candidate
Run validators, cross-standard consistency checks and one negative test for normative-approval protection. Produce review report, diff, unresolved questions and release candidate. STOP before first normative publication.

## Exit criteria
- All 16 ratified decisions represented faithfully.
- 14 standards, unique normative IDs and no duplicated canonical rules.
- Proposed numeric defaults clearly distinguished from approved decisions.
- Validator runs offline and emits reproducible PASS/FAIL/BLOCKED/NOT RUN.
- No changes to unrelated systems; no autonomous normative publication.
- Pilot evidence and explicit Operator approval before release.

## STOP conditions
Unclear ownership; conflict with ratified decision; missing access; unverified facts; irreversible action; security boundary change; semantic ambiguity; risk of changing existing production systems. Report `DECISION REQUIRED` and stop affected action, continue only independent safe tasks.
