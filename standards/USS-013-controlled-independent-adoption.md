# USS-013 — Controlled Independent Adoption

**Status:** Normative Standard  
**Cluster:** Cluster 1 (Foundation & Governance)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Decouple the centralized publication of Universal System Standards from independent local system adoption schedules and migration paths.

---

## Normative Rules

1. **013-01** — Normative releases of USS **MUST** be published as versioned Git releases adhering to SemVer 2.0.0, accompanied by a changelog and impact assessment.
2. **013-02** — Each independent system **MUST** record its adopted release version in a local [templates/SYSTEM_ADOPTION.template.md](../templates/SYSTEM_ADOPTION.template.md) record and **MAY** adopt or upgrade releases on an independent schedule.
3. **013-03** — Verified mechanical, formatting, or editorial corrections that preserve normative meaning **MAY** be merged without requiring a MAJOR version bump.
4. **013-04** — Normative changes to standard rules, new standard introductions, and release publications **MUST** require explicit Operator authorization and cryptographic tag signatures.
5. **013-05** — Systems **MUST** report adoption compliance strictly using the standardized status tokens: `COMPLIANT`, `PARTIAL`, `EXEMPT`, `NOT_APPLICABLE`, or `UNKNOWN`. Any claim of `COMPLIANT` **MUST** reference verifiable local evidence files.
6. **013-06** — Any standard or rule marked as `EXEMPT` or `PARTIAL` **MUST** record a formal exception specifying technical rationale, risk evaluation, owner, and a review expiration date.

---

## Prohibitions

- The USS repository **MUST NOT** trigger or enforce automatic rollouts or unsolicited modifications to consuming system repositories.
- Consuming systems **MUST NOT** assert `COMPLIANT` status based solely on updating a version pin without passing local verification tests.

---

## Verification

A compliant governance process **MUST** demonstrate that draft standard proposals cannot achieve normative status or trigger release publication without Operator cryptographic signature verification.
