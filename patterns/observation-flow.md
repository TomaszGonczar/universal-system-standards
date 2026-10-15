# Pattern: Decentralized Observation Flow

**Status:** Reference Pattern  
**Related Standards:** [USS-003](../standards/USS-003-observations.md), [USS-012](../standards/USS-012-observability.md)

---

## 1. Overview & Mechanics

Universal System Standards uses a decentralized, asynchronous observation flow to collect operational learnings, failure cases, and refinement opportunities from consuming systems (e.g. ATLAS, OMEGA, BI Agent, Hermes).

To maintain the core mandate of zero central runtimes and zero mandatory databases:
- Observations are formatted as plain Markdown files adhering to [`templates/OBSERVATION.template.md`](../templates/OBSERVATION.template.md).
- The default drop path within any consuming repository is `observations/`.
- No central background daemon, event bus, or database is required.

---

## 2. Emission Lifecycle

```
[System Anomaly / Learning]
            │
            ▼
[Generate observations/YYYY-MM-DD-slug.md]
  (Clean signal: symptom, evidence, impact)
  (Strictly scrubbed: zero secrets, zero bulk prompts)
            │
            ▼
[Committed to Consumer Repository or Submitted via PR / Issue]
            │
            ▼
[Periodic Review by Hermes (30d/90d Authorized Cadence)]
  (Hermes groups, deduplicates, and drafts proposals)
            │
            ▼
[Operator Review & Gate 2 / MADR Recording]
```

---

## 3. Observation Hygiene & Security

1. **Facts vs. Hypotheses:** Emitters must clearly separate observed execution facts (error codes, unexpected behavior, environment receipts) from speculative diagnoses.
2. **Credential Redaction:** API keys, access tokens, customer identifiers, and unscrubbed model prompts **MUST NOT** be embedded into observation files.
3. **Actionability:** Observations should link to specific USS rule IDs (e.g. `007-03`, `010-04`) to facilitate direct triage.

---

## 4. Hermes Operational Role

Hermes acts as an operational consumer and observation synthesizer:
- Ingests committed observation files during scheduled review jobs.
- Deduplicates identical failure patterns across independent systems.
- Formulates draft architectural recommendations as MADR records in `governance/decisions/` or GitHub issues.
- **Hermes never approves normative standard changes.** All normative revisions require Operator ratification.
