# Universal System Standards — Release & Verification Process

**Status:** Normative Governance Specification  
**Authority:** The Operator (Product Owner)

---

## 1. Release Philosophy & Versioning

Universal System Standards (USS) adheres strictly to **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`) and **Keep a Changelog 1.1.0**:
- **MAJOR** (`X.0.0`): Breaking changes to normative standards, modified rule IDs, altered state machine enums, or tightened mandatory verification requirements.
- **MINOR** (`0.Y.0`): Backward-compatible additions of new rules, new nonmandatory patterns, or expanded template schemas.
- **PATCH** (`0.0.Z`): Backward-compatible errata, editorial clarifications, documentation typos, or tooling bug fixes.
- **Release Candidates** (`vX.Y.Z-rcN`): Staged candidates prepared by implementers for final Operator review, test validation, and cryptographic signing.

---

## 2. Cryptographic Release Authorization (OD-5)

Prompt-only restrictions and unsigned Git tags do not constitute normative authorization:
1. **Mandatory Signature:** Every official normative release tag (`vX.Y.Z`) **MUST** be cryptographically signed by the Operator using a registered SSH or GPG signing key.
2. **Offline Verification:** The release tag signature **MUST** be verifiable 100% offline using `git tag -v` and `tools/uss-validate.py` against trusted Operator public keys (configured via `--signer`, the `USS_OPERATOR_SIGNER` environment variable, or standard Git `allowed_signers`).
3. **Unsigned Tags Invalid:** Any unsigned tag, or any tag signed by an unauthorized key, is considered unratified draft material and **MUST NOT** be recognized as an approved standard release by consuming systems.

---

## 3. Phased Implementation & Review Gates

Every standard modification progresses through deterministic, verifiable review gates:

```
[Phase 0: Audit & Architecture] ──> Gate 0: PO Plan & Baseline Approval
                                             │
[Phase 1: Repo Bootstrap]        ──> Gate 1: Baseline Layout Verification
                                             │
[Phase 2: Standards Drafting]    ──> Gate 2: Normative Content Review
                                             │
[Phase 3: Tooling & Test Suite]  ──> Gate 3: Offline Tooling PASS Receipt
                                             │
[Phase 4: Release Hardening]     ──> Gate 4: Operator Cryptographic Signature
                                             │
                                             ▼
                                  Published vX.Y.Z Git Tag
```

### Gate Checklist:
- **Gate 0 (Architecture):** Operator ratifies baseline decisions and repository boundaries.
- **Gate 1 (Scaffolding):** Clean directory layout, license, and baseline governance documents verified.
- **Gate 2 (Normative Content):** Standards rewritten in BCP 14 syntax, deduplicated, and mapped to risk levels.
- **Gate 3 (Tooling):** Offline validation suite and test suite execute with deterministic `PASS` receipts.
- **Gate 4 (Release):** Final changelog reviewed; Operator applies cryptographic signature to Git tag.

---

## 4. Consumer Adoption & Migration Lifecycle

Consuming systems (Hermes, ATLAS, OMEGA, BI Agent) adopt USS independently:
1. **Version Pinning:** A consuming repository pins a specific signed Git tag (or exact commit hash) in its local `SYSTEM_ADOPTION.md`.
2. **Local Verification:** The adopting system verifies its compliance with adopted rule IDs using local tests and captures evidence.
3. **No Automatic Push:** The USS repository never pushes updates or forces migrations. Upgrades are initiated solely by the adopting system's maintainers.
