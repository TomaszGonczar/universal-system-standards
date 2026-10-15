# Proposed defaults — token and operational budgets

**STATUS: PROPOSED / NOT RATIFIED.** These are initial editing targets for the Hermes implementation pilot, not universal hard constraints. The Operator must approve before promotion to a normative USS release.

## Document budgets (estimated LLM tokens, not words)

| Document | Recommended target | Soft review threshold | Notes |
|---|---:|---:|---|
| Root `AGENTS.md` | 300–800 | 1,200 | High-signal global instructions and navigation only |
| Nested scoped `AGENTS.md` | 150–500 | 800 | Only rules that differ for that subtree |
| `USS.md` index | 250–600 | 900 | Navigation and governance, not duplicated standards |
| Individual USS standard | 350–900 | 1,200 | Purpose, rules, prohibitions, defaults, verification |
| Agent task contract | 150–400 | 600 | Goal, scope, acceptance, budget, constraints |
| Local USS adoption summary | 200–600 | 900 | Version pin, applicability, exceptions and links |
| Routine observation | 80–250 | 400 | Symptom, evidence, impact, proposal |
| 30-day review summary | 400–900 | 1,300 | Changes, exceptions, risks, actions |
| 90-day review summary | 700–1,500 | 2,000 | Trends, proposed amendments, impact |

## Rules for token limits
1. These are **soft targets**, not truncation requirements. Accuracy and safety outrank token targets.
2. Do not silently truncate normative content to fit a budget.
3. Count with the model tokenizer if available; otherwise mark estimates as approximate and disclose method.
4. Above the soft threshold: first remove repetition, then split by responsibility, then use links/progressive disclosure. Do not create artificial fragmentation.
5. A justified overage is acceptable if it reduces ambiguity or avoids loss of critical instructions.
6. No default loading of every USS standard into every agent context. Load index + relevant rules.
7. Record the measured/estimated token size and any justified overage in review output, not necessarily in each source file.

## Proposed operational defaults (all require pilot validation)

| Parameter | Initial recommendation | Caveat |
|---|---|---|
| Hermes light governance review | Every 30 days | Cadence ratified; schedule not yet configured |
| Hermes deep governance review | Every 90 days | Cadence ratified; schedule not yet configured |
| Observations | Deduplicate by issue + system + evidence | No forced central log collection |
| Automatic retry | Finite, task-specific | No universal count without idempotency analysis |
| Log retention | Locally configured by risk | No invented universal duration |
| Worker concurrency | Explicit per-task/project cap | No universal numeric cap |
| Agent cost budget | Explicit per-task when measurable | No invented universal currency/token ceiling |
| Protected deletion | Requires explicit authorization | Existing ratified risk boundary |

## Example `AGENTS.md` (illustrative, not mandatory)
```md
# Agent Instructions

## Mission
Implement only the requested task. Prefer simple, reversible changes.

## Read first
- Project README and task-relevant local docs.
- USS adoption record; only applicable USS standards.

## Boundaries
- Do not modify unrelated repositories or protected SSOT.
- Do not expose secrets or perform irreversible actions without approval.
- Stop if required evidence is unavailable.

## Completion
- Run relevant checks; report PASS/FAIL/BLOCKED/NOT RUN honestly.
- Return changed files, verification evidence, open risks and next decision.
```
