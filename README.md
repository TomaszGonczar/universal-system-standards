# Universal System Standards (USS)

[![Validation](https://img.shields.io/badge/verification-100%25%20offline-success)](tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Standards: BCP 14](https://img.shields.io/badge/Normative-IETF%20BCP%2014-informational)](INDEX.md)
[![Status: RC](https://img.shields.io/badge/Status-v0.1.0--rc1-orange)](CHANGELOG.md)

**Universal System Standards (USS)** establishes a minimal, uniform technical skeleton across independent AI-agent systems (e.g. Hermes, ATLAS, OMEGA, BI Agent). It defines common wire protocols, trust boundaries, state machines, and verification receipts in Git while preserving complete domain sovereignty for individual systems.

---

## Core Architectural Principles

1. **The Minimal Skeleton (Technical Backbone):** USS provides the cross-system invariants required for interoperability, trust, and determinism. It standardizes verification states (`IMPLEMENTED`, `VERIFIED`, `ACCEPTED`), check outcomes (`PASS`, `FAIL`, `CHECK_BLOCKED`, `NOT RUN`), and trust boundaries.
2. **Domain Sovereignty (No Micromanagement):** USS never dictates internal prompts, tools, or domain-specific instructions. Sizing of `AGENTS.md` is governed by local domain complexity—arbitrary numerical file-length brackets are rejected.
3. **Zero Live Operational Data:** The standards repository contains solely normative specifications, reference patterns, generic templates, and verification tooling. No live registries, databases, or observation inboxes exist here.
4. **100% Offline Verifiability:** All standards validation and compliance checks run offline using standard Python 3. No external pip dependencies, central daemons, or mandatory cloud services.
5. **Decentralized Adoption:** Systems pin an approved cryptographic Git release tag and adopt standards on their own schedule without automatic cross-system rollouts.

---

## Repository Structure

```text
.
├── README.md               # Project overview and navigation
├── AGENTS.md               # Clean agent instructions for USS repository
├── INDEX.md                # Progressive disclosure index and cross-system definitions
├── LICENSE                 # MIT License
├── CHANGELOG.md            # Release history (Keep a Changelog 1.1.0)
│
├── governance/             # Normative authority, boundaries, and release mechanics
│   ├── BOUNDARIES.md       # Roles, boundaries, and Single Source of Truth rules
│   ├── RELEASE_PROCESS.md  # Cryptographic release signing and verification gates
│   ├── DECISION_LEDGER.md  # Verbatim 16 ratified workshop decisions (frozen)
│   └── decisions/          # Architectural Decision Records (MADR format)
│       └── 0001-gate-0-ratified-baseline.md
│
├── standards/              # The 14 normative USS standards (IETF BCP 14)
│   ├── USS-001-enforcement.md
│   ├── USS-002-contract.md
│   ├── USS-003-observations.md
│   ├── USS-004-documentation.md
│   ├── USS-005-workspace-hygiene.md
│   ├── USS-006-knowledge-freshness.md
│   ├── USS-007-orchestration.md
│   ├── USS-008-security.md
│   ├── USS-009-reliability.md
│   ├── USS-010-verification.md
│   ├── USS-011-dependencies.md
│   ├── USS-012-observability.md
│   ├── USS-013-controlled-independent-adoption.md
│   └── USS-014-lifecycle.md
│
├── patterns/               # Nonmandatory reference engineering patterns
│   ├── risk-matrix.md      # Unified 4-tier risk classification (L1–L4)
│   ├── observation-flow.md # Recommended observation formatting & routing
│   ├── local-projection.md # Consumer adoption and local projection mechanics
│   └── cost-adaptive-routing.md # Telemetry-driven model cost optimization
│
├── templates/              # Clean consumer projection templates
│   ├── AGENTS.template.md
│   ├── OBSERVATION.template.md
│   ├── SYSTEM_ADOPTION.template.md
│   └── SYSTEM_REGISTRY.template.md
│
└── tools/                  # Zero-dependency offline verification tooling
    ├── uss-validate.py     # Standards and adoption validator (Python 3 stdlib)
    └── test_validator.py   # Comprehensive validator test suite
```

---

## Standards Clusters (Progressive Disclosure)

For efficient agent context management, standards are grouped into four cohesive clusters:
- **Cluster 1: Foundation & Governance:** [USS-002](standards/USS-002-contract.md), [USS-004](standards/USS-004-documentation.md), [USS-013](standards/USS-013-controlled-independent-adoption.md)
- **Cluster 2: Execution, Security & Orchestration:** [USS-001](standards/USS-001-enforcement.md), [USS-007](standards/USS-007-orchestration.md), [USS-008](standards/USS-008-security.md)
- **Cluster 3: Hygiene, Freshness & Dependencies:** [USS-005](standards/USS-005-workspace-hygiene.md), [USS-006](standards/USS-006-knowledge-freshness.md), [USS-011](standards/USS-011-dependencies.md)
- **Cluster 4: Reliability, Quality & Lifecycle:** [USS-009](standards/USS-009-reliability.md), [USS-010](standards/USS-010-verification.md), [USS-012](standards/USS-012-observability.md), [USS-014](standards/USS-014-lifecycle.md)

See [INDEX.md](INDEX.md) for full summaries and cross-standard invariants.

---

## Offline Validation Tooling

USS ships with a zero-dependency Python 3 validation utility:

### 1. Repository Self-Check:
Validates rule-ID uniqueness, BCP 14 syntax, internal markdown link integrity, template sanitization, and release tag signatures:
```bash
python3 tools/uss-validate.py --self
```

### 2. Consumer Repository Adoption Check:
Validates that an adopting system repo correctly pins a version, defines status, provides verifiable local evidence (anti-fabrication check), and scaffolds `AGENTS.md`:
```bash
python3 tools/uss-validate.py --consumer /path/to/consumer/repo
```

### 3. Run Test Suite:
Executes unit tests covering positive and negative validation scenarios:
```bash
python3 tools/test_validator.py
```

---

## Governance & Release Authority

- **Product Owner & Sole Normative Authority:** The Operator.
- **Independent Implementer:** OMP (Orca ADE).
- **Operational Consumers:** Hermes, ATLAS, OMEGA, BI Agent.
- **Release Verification:** Official normative releases require a cryptographically signed Git tag (`git tag -s vX.Y.Z`) created by the Operator. Unsigned tags are non-normative drafts.

See [governance/BOUNDARIES.md](governance/BOUNDARIES.md) and [governance/RELEASE_PROCESS.md](governance/RELEASE_PROCESS.md) for full governance specifications.
