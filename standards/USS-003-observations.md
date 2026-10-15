# USS-003 — Observations to Hermes

**Status:** Normative Standard  
**Cluster:** Cluster 1 (Foundation & Governance)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Capture actionable cross-system feedback and failure patterns to drive controlled, evidence-based improvements to Universal System Standards.

---

## Normative Rules

1. **003-01** — Consuming systems **SHOULD** emit actionable observations formatted according to [templates/OBSERVATION.template.md](../templates/OBSERVATION.template.md), documenting source system, symptom, observable evidence, impact, and suggested action. The default local drop location **SHOULD** be `observations/` within the consuming repository.
2. **003-02** — Hermes **SHOULD** deduplicate and group recurring observations; raw operational telemetry, debug traces, and sensitive logs **MUST** remain localized within source systems.
3. **003-03** — Hermes **MAY** draft change recommendations and report synthesis to the Operator, but **MUST NOT** approve normative USS modifications.
4. **003-04** — Observation records **MUST** preserve provenance and explicitly distinguish verified factual evidence from diagnostic hypotheses.
5. **003-05** — Implementations **MUST NOT** introduce a dedicated observation agent daemon or mandatory central database; observations **MUST** be transmitted via standard Git artifacts or lightweight Markdown file drops.

---

## Prohibitions

- Systems **MUST NOT** apply normative standard modifications automatically based solely on an observation report.
- Consuming systems **MUST NOT** ingest credentials, API keys, or bulk unscrubbed prompts into observation files.

---

## Verification

A compliant system **MUST** demonstrate traceability from an emitted observation artifact to a recorded review outcome or an explicit, documented no-action decision.
