# Governance workflow

## Actors
- Operator: Product Owner, normative decision and release authority.
- Hermes: operational co-PO, observer, editor of drafts, reviewer and scheduler coordinator.
- Local systems: independent adoption and implementation authority within their own boundaries.

## Proposal flow
Observation → deduplicate → draft proposal → impact analysis → lint + consistency review → Operator approval → publish release → local adoption separately.

## 30-day review
Review observation trends, exception expirations, broken links, orphaned ownership and unresolved proposals. Produce concise report. No forced changes.

## 90-day review
Evaluate effectiveness, duplicate rules, drift, risks, lifecycle status and candidate amendments. Submit a release proposal only if justified.

## Emergency issues
Prepare urgent proposal promptly; do not bypass normative approval. Existing emergency operational security controls remain governed by local system permissions.

## Release gate
No first normative USS tag without explicit Operator approval. Version scheme may use semantic versioning; proposed version is `v0.1.0`, pending approval. Record source commit, approved decision, change summary and validation evidence.
