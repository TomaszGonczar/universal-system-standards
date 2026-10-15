# External System Registry — Template

**Status:** Reference Projection Template  
**Isolation Notice (OD-6 & OD-15):** This file is a generic schema template. Live system registries, private infrastructure inventories, and operational logs **MUST NOT** be committed to the Universal System Standards repository.

---

## Ecosystem System Catalog

| System ID | Role & Primary Function | Lifecycle State | Owner | Documentation Path | Adopted USS Pin | Evidence Receipt |
|---|---|---|---|---|---|---|
| `<system-a>` | `<primary role / domain responsibility>` | `ACTIVE` | `<designated-owner>` | `docs/architecture.md` | `v0.1.0` | `[Receipt Link]` |
| `<system-b>` | `<primary role / domain responsibility>` | `PLANNED` | `<designated-owner>` | `README.md` | `NONE` | `[Pending]` |
| `<system-id>` | `<description>` | `UNKNOWN` | `<owner>` | `<path>` | `<pin>` | `<link>` |

---

## Allowed Lifecycle Values (USS-014 Rule `014-02`)

- **`PLANNED`**: Conceptualized system prior to repository creation or initial deployment.
- **`EXPERIMENTAL`**: Active prototype under rapid development; non-normative.
- **`ACTIVE`**: Full operational system processing tasks.
- **`MAINTENANCE`**: Operational system with frozen feature development receiving security/bug patches.
- **`MIGRATING`**: System undergoing knowledge handover or workload cutover to a successor system.
- **`ARCHIVED`**: Decommissioned system preserved in read-only state for historical recovery.
- **`RETIRED`**: Formally decommissioned system with terminated background jobs and revoked credentials.
- **`UNKNOWN`**: Unverified or unclassified state requiring immediate assessment.
