# Boundaries, precedence and SSOT

## Sources of truth
- USS approved Git tag: canonical normative requirements and release history.
- System local repository: implementation, local operational state and adopted USS pin.
- System registry: identity, lifecycle, ownership and documentation pointers; do not duplicate all local state.
- Hermes: curated observations, proposals and review coordination; never supersedes live evidence.

## Ownership of overlapping rules
| Overlap | Canonical owner |
|---|---|
| 001 / 008 / 010 approvals | 001 enforcement approach; 008 authorization boundary; 010 acceptance evidence |
| 002C / 005 / 014 pruning | 002C autonomy levels; 005 files; 014 whole-system retirement |
| 003 / 006 / 012 signals | 003 curated observations; 006 freshness; 012 raw operational events |
| 007 / 009 / 010 task control | 007 delegation; 009 recovery; 010 verification |
| 006 / 013 change | 006 knowledge integrity; 013 release/adoption |
| 011 / 014 recovery | 011 environment reproduction; 014 lifecycle and transfer |

## Conflict resolution
1. A locally pinned approved USS release determines applicable normative contract; newer releases are proposals until adopted.
2. Local projection cannot rewrite the meaning of a normative USS rule.
3. Security, protected data, active recovery and required verification evidence are not overridden by cleanup convenience.
4. Mechanical editorial changes may be automatic if they do not change meaning; substantive changes require Operator approval.
5. A change of SSOT write owner requires verified cutover. Do not silently dual-write.
6. When unclear, mark `DECISION REQUIRED` with options, impact and evidence. Do not invent authority.
