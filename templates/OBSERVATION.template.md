# USS Observation — Template

**Status:** Reference Projection Template  
**Target Drop Path:** `observations/YYYY-MM-DD-<slug>.md` within consuming system repository  
**Security Warning:** Do NOT include credentials, API tokens, or bulk unscrubbed prompts.

---

## Metadata

- **Source System:** `<system-identifier>` (e.g. `hermes`, `atlas`, `omega`, `bi-agent`)
- **Date / Timestamp:** `YYYY-MM-DD HH:MM UTC`
- **Reporter / Agent:** `<agent-id-or-human-operator>`
- **Adopted USS Pin:** `<vX.Y.Z or commit-hash>`

---

## Diagnostic Content

### 1. Observable Symptom
[Concise, factual description of unexpected failure, contract friction, or tool breakdown.]

### 2. Concrete Evidence & References
- Execution commands, error outputs, or log extracts demonstrating the symptom:
  ```text
  [Paste sanitized command output or error receipt here]
  ```
- Related file paths or test scripts: `[tests/... or src/...]`

### 3. Impact & Frequency
- **Severity / Risk Level:** `L1` | `L2` | `L3` | `L4`
- **Occurrence:** `ISOLATED` | `RECURRING` | `SYSTEMIC`
- **Operational Consequence:** [Description of blocked workflow or degraded health state]

### 4. Working Hypothesis (Optional)
[Tentative engineering explanation of why the failure occurred. Distinct from observed facts.]

### 5. Suggested Action & Target Rules
- **Related USS Standards:** [e.g. `USS-007` (Rule `007-03`), `USS-010` (Rule `010-04`)]
- **Proposed Enhancement:** [Suggested standard adjustment, rule refinement, or tooling update]

---

## Operational Disposition (Hermes / Operator Triage)

- **Triage State:** `NEW` | `DUPLICATE` | `UNDER_REVIEW` | `PROPOSAL_DRAFTED` | `NO_ACTION`
- **Assigned MADR / Issue:** `[Link to governance/decisions/ or issue]`
- **Disposition Notes:** [Summary of decision or deduplication rationale]
