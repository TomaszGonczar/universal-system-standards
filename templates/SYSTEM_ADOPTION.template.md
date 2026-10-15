# USS System Adoption Record — Template

**Status:** Reference Projection Template  
**Target Path:** `SYSTEM_ADOPTION.md` in root of consuming repository  
**Authority:** The local repository is the sole authoritative Single Source of Truth (SSOT) for its adopted version and compliance state.

---

## 1. System Identity

- **System ID:** `<system-identifier>` (e.g. `hermes`, `atlas`, `omega`, `bi-agent`)
- **System Owner:** `<designated-human-or-agent-owner>`
- **Repository Path:** `[relative-or-canonical-repo-path]`
- **System Lifecycle State:** `PLANNED` | `EXPERIMENTAL` | `ACTIVE` | `MAINTENANCE` | `MIGRATING` | `ARCHIVED` | `RETIRED` | `UNKNOWN`

---

## 2. Adopted Standards Contract

- **Adopted USS Release:** `<vX.Y.Z-tag-or-commit-sha>` (MUST reference an approved release)
- **Adoption Date:** `YYYY-MM-DD`
- **Applicable Rule Scope:**
  - `USS-001`: `001-01`, `001-02`, `001-03`, `001-04`, `001-05`
  - `USS-002`: `002-01`, `002-02`, `002-03`, `002-04`, `002-05`, `002-06`
  - `USS-008`: `008-01`, `008-02`, `008-03`, `008-04`, `008-05`
  - `USS-010`: `010-01`, `010-02`, `010-03`, `010-04`, `010-05`, `010-06`
  - `USS-013`: `013-01`, `013-02`, `013-03`, `013-04`, `013-05`, `013-06`
  - `[Add additional adopted standards and rule IDs as appropriate]`

---

## 3. Compliance Evidence Ledger (Anti-Fabrication)

> **Invariant (Rule `013-05`):** A version pin alone does not constitute compliance. Claiming `COMPLIANT` requires referencing verifiable local tests, configs, or execution receipts.

| Rule ID | Compliance State (`COMPLIANT` / `PARTIAL` / `EXEMPT`) | Local Evidence Path / Test Receipt |
|---|---|---|
| `001-01` | `COMPLIANT` | `tests/test_risk_classification.py` |
| `008-03` | `COMPLIANT` | `.gitignore` and `tests/test_secret_leakage.py` |
| `010-04` | `COMPLIANT` | `ci/report_formatter.py` |
| `<rule-id>` | `<state>` | `<verifiable-local-evidence-file>` |

---

## 4. Exceptions & Variances

| Rule ID | Exception Rationale | Risk Level | Owner | Review Expiration |
|---|---|---|---|---|
| `<rule-id>` | `<technical justification>` | `L1` \| `L2` \| `L3` | `<owner>` | `YYYY-MM-DD` |

---

## 5. Formal Adoption Status

- **Evaluated Compliance Status:** `UNKNOWN` (must be verified: `COMPLIANT` | `PARTIAL` | `EXEMPT` | `NOT_APPLICABLE` | `UNKNOWN`)
- **Last Verification Receipt:** `YYYY-MM-DD` (`PASS`)
- **Next Review Due:** `YYYY-MM-DD`
