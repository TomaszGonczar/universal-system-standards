# Changelog

All notable changes to Universal System Standards (USS) are documented in this file.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0-rc1] - 2026-10-15

### Added
- **BCP 14 Standard Language:** Rewrote all 14 standards to strictly use IETF RFC 2119 / RFC 8174 normative keywords (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`).
- **Progressive Disclosure Clusters:** Grouped the 14 standards into 4 cohesive clusters in `INDEX.md` (Foundation & Governance; Execution, Security & Orchestration; Hygiene, Freshness & Dependencies; Reliability, Quality & Lifecycle).
- **Unified 4-Tier Risk Matrix (L1–L4):** Added `patterns/risk-matrix.md` establishing deterministic boundaries for action reversibility, test requirements, and Operator authorization gates.
- **Reference Patterns:**
  - `patterns/observation-flow.md`: Decentralized Markdown observation routing to Hermes without central daemons or databases.
  - `patterns/local-projection.md`: Guidance for consumer repositories adopting USS projections.
  - `patterns/cost-adaptive-routing.md`: Pragmatic model cost routing conditioned on programmatic telemetry.
- **Offline Standards Validator (`tools/uss-validate.py`):** Zero-dependency Python 3 standard library tool supporting repository self-checks (`--self`) and consumer adoption validation (`--consumer <path>`).
- **Validator Test Suite (`tools/test_validator.py`):** Comprehensive unit tests covering rule uniqueness, BCP 14 syntax, link integrity, anti-fabrication evidence checks, and cryptographic signature verification.
- **Formal Governance:**
  - `governance/BOUNDARIES.md`: Defined Operator as sole Product Owner and normative authority; defined Hermes as operational consumer only.
  - `governance/RELEASE_PROCESS.md`: Enforced mandatory cryptographic Git tag signing (SSH/GPG) by the Operator.
  - `governance/decisions/0001-gate-0-ratified-baseline.md`: Ratified all Gate 0 architectural choices (OD-1…OD-15, DR-1…DR-6) in MADR format.
- **Projection Templates:** Renamed and standardized templates to `.template.md` suffix (`AGENTS.template.md`, `OBSERVATION.template.md`, `SYSTEM_ADOPTION.template.md`, `SYSTEM_REGISTRY.template.md`).

### Changed
- **Boilerplate Deduplication:** Eliminated repeated boilerplate (~31% token overhead) across all 14 standards by centralizing universal boundaries in `INDEX.md` and `governance/BOUNDARIES.md`.
- **Vocabulary Disambiguation:** Disambiguated `BLOCKED` into `CHECK_BLOCKED` (verification test prerequisite obstacle in USS-010) and `SYSTEM_BLOCKED` (runtime operational state in USS-012).
- **State Machine Expansion:** Added `UNKNOWN` and `PLANNED` to system lifecycle enum in USS-014; added `UNKNOWN` to adoption compliance enum in USS-013.
- **Model Cost Optimization Conditionality:** Rephrased rule `007-03` as a `SHOULD` recommendation dependent on programmatic access to telemetry.
- **File Renaming:** Aligned slug `standards/USS-013-controlled-independent-adoption.md` with standard title while preserving rule IDs (`013-01` .. `013-06`).
- **Consumer SSOT:** Codified that the local adopting repository is the sole authoritative Single Source of Truth for its adopted USS version pin.

### Removed
- **Governance Role Ambiguity:** Removed all occurrences of "operational co-PO" referring to Hermes.
- **Over-Prescriptive Token Budgets:** Deleted `governance/DEFAULTS_AND_TOKEN_BUDGETS.md`. Reaffirmed that file sizing is governed by domain necessity and progressive disclosure.
- **Draft Scaffolding:** Removed obsolete handoff files (`PROMPT_FOR_HERMES.md`, `USS.md`, `implementation/PLAN_AND_GATES.md`, `MANIFEST.json`).

---

## [0.1.0-draft] - 2026-10-13

### Added
- Initial transcription of 16 ratified workshop decisions into 14 draft technical standards.
- Initial draft templates and governance proposals.
