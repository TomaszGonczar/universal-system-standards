# USS-014 — Controlled Lifecycle & Knowledge Handover

**Status:** Normative Standard  
**Cluster:** Cluster 4 (Reliability, Quality & Lifecycle)  
**Authority:** The Operator (Product Owner)

---

## Purpose

Manage system states throughout their operational lifecycle, ensuring safe transitions, clear ownership of Single Source of Truth, and secure decommissioning.

---

## Normative Rules

1. **014-01** — Independent systems **MUST** maintain a registration record documenting designated system owner, current lifecycle state, canonical documentation path, and pinned USS release version.
2. **014-02** — System lifecycle states **MUST** report strictly using the standardized enum tokens: `PLANNED` (conceptualized prior to repository initialization), `EXPERIMENTAL`, `ACTIVE`, `MAINTENANCE`, `MIGRATING`, `ARCHIVED`, `RETIRED`, or `UNKNOWN`.
3. **014-03** — Operational runbooks **MUST** maintain distinct procedures for pausing, archiving, decommissioning, retiring, and permanently purging system resources.
4. **014-04** — During cross-system migrations or handovers, knowledge artifacts and codebases **MUST** be classified as `ADOPT`, `ADAPT`, `REFERENCE`, or `REJECT`.
5. **014-05** — Authoritative write ownership of Single Source of Truth assets **MUST NOT** transition to a successor system until cutover verification is proven.
6. **014-06** — Prior to formal decommissioning of any system, maintainers **MUST** audit and terminate all scheduled background jobs, revoke associated credentials, and verify archive integrity.

---

## Prohibitions

- Autonomous agents **MUST NOT** initiate destructive retirement or resource purging on systems in `ACTIVE` or `MAINTENANCE` states without explicit Operator authorization.
- Migrating systems **MUST NOT** permit concurrent, uncoordinated dual-write access to shared mutable operational datasets.

---

## Verification

A compliant decommission process **MUST** demonstrate complete cutover verification, revoke operational credentials, and confirm the absence of lingering background scheduled tasks.
