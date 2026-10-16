# Universal System Standards (USS)

**Current Release:** `v1.0.1`  
**Status:** **FROZEN — OPERATOR APPROVED** (2026-10-16)  
**Normative Authority:** One authenticated human Operator per deployment  
**Canonical Specification:** [`USS_v1.0.1_FROZEN_2026-10-16.md`](USS_v1.0.1_FROZEN_2026-10-16.md)  
**SHA-256:** `9cb3e0f74d98afff24c572581f0e1ab8b235349ceb4f2b097c15f2b6494ec64e`

---

## What is USS?

**Universal System Standards (USS) is a lightweight, Operator-owned engineering constitution for independently operating AI systems.**

Its purpose is to make single-Operator AI systems easier to build, verify, govern, understand, and maintain without making them dependent on a new platform or compliance framework.

USS prevents:
- Repeated reinvention of engineering conventions
- False `IMPLEMENTED`, `VERIFIED`, and `ACCEPTED` claims
- Drift in instructions and sources of truth
- Lost task context
- Unnecessary manual approvals for safe work
- Accumulation of unmanaged temporary files

### Core Principle: Zero Mandatory Runtime Dependencies
USS standardizes **required outcomes and behavioral contracts**, not a specific implementation or orchestration framework:
- **No** new runtime framework, agent CLI, or compliance proxy
- **No** persistent memory database, central telemetry daemon, or run registry
- **No** janitor daemons, lease managers, or universal TTL garbage collectors
- **No** mandatory folder hierarchies, compulsory templates, or rigid token targets

A participating system must continue running with its native runtime, OS and Git permissions, tests, code, and project facts if all optional USS artifacts disappear.

---

## Architecture & Document Structure

The full text is contained in [`USS_v1.0.1_FROZEN_2026-10-16.md`](USS_v1.0.1_FROZEN_2026-10-16.md):

### Part I: Six Constitutional Principles (Normative)
- **USS-U1 — Operator authority and non-self-amendment:** Only the human Operator establishes or revises policy, standing permissions, and acceptance criteria. Agents cannot grant themselves authority. Discloses `SHARED_TRUST` where true isolation does not exist.
- **USS-U2 — Real boundaries, downstream effects and injection risk:** Authorization is the intersection of the Operator grant and effective runtime/OS capabilities. Prompting modes (`yolo`, `always-ask`) are not OS containment or egress control. Injection is a capability problem.
- **USS-U3 — Truthful and minimal guidance; untrusted context stays data:** Provide concise, discoverable repository facts. External inputs, skills, scratch, and observations remain untrusted data. Zero secrets in documentation or logs.
- **USS-U4 — Evidence-bound claims and Operator acceptance:** Strict distinction between `IMPLEMENTED` (code exists), `VERIFIED` (executed checks passed on identified state), and `ACCEPTED` (Operator decision). Passing weakened checks does not satisfy original requirements.
- **USS-U5 — Static AUDIT and minimal BOOTSTRAP:** By default, AUDIT is static and read-only without side effects. BOOTSTRAP inspects first and applies only the smallest authorized change. Zero compliance theater.
- **USS-U6 — Intentional file lifecycle and minimalism:** Automatic deletion is strictly self-cleanup of a run's privately owned temporary directory. Never delete other runs' outputs, registered worktrees, or unknown files. Zero mandatory runtime dependencies.

### Part II: Seven Conditional Operational Standards (Normative When Applicable)
- **SLOT-01 — Repository Orientation / `AGENTS.md`:** Brief, current factual instructions with entrypoints and local SSOT. No mandatory template or length limit.
- **SLOT-02 — Agent Skills and Tool Contracts:** Prefer public Agent Skills format. `allowed-tools` is pre-approval, not portable denial.
- **SLOT-03 — Verification and Evidence:** Separate applicability, check outcome (`PASS`, `FAIL`, `CHECK_BLOCKED`, `NOT_RUN`), and work claim. Routine closeout is a short handoff, not automatic receipt files.
- **SLOT-04 — Bounded Autonomy / T0–T3:**
  - `T0 (Observe)`: read and bounded inspection — AUTO under grant.
  - `T1 (Workspace)`: normal edit, format, test, local commit — AUTO under grant.
  - `T2 (Granted External)`: scoped external action with named resource and credential — AUTO if preauthorized.
  - `T3 (Reserved)`: authority modification, secret/host privilege change, execution-surface promotion — DENY until scoped Operator authorization.
- **SLOT-05 — Scratch, Observations and Continuity:** Scratch is transient; observations are rare and attributed. Never store credentials in scratch or evidence.
- **SLOT-06 — Unified AUDIT / BOOTSTRAP Lite:** Distinguish static conformance, runtime enforcement, and operational evidence.
- **SLOT-07 — Repository Hygiene and Safe Cleanup:** Purpose-revealing paths; unique per-run temporary directories; preserve evidence before cleanup.

### Non-Normative Appendices
- **Appendix A — Reading Guide:** Definitions of evaluation axes (Applicability, Outcome, Work claim, Integration, Boundary disclosure).
- **Appendix B — OMEGA / ATLAS Pilot Lessons:** Real-world audit insights that informed v1.0.1 clarifications.

---

## Evaluation Vocabulary

| Axis | Values | Meaning |
|---|---|---|
| **Applicability** | `APPLICABLE`, `NOT_APPLICABLE [reason]` | An absent trigger is not a PASS |
| **Check Outcome** | `PASS`, `FAIL`, `CHECK_BLOCKED`, `NOT_RUN` | Blocked or unrun is not success |
| **Work Claim** | `IMPLEMENTED`, `VERIFIED`, `ACCEPTED` | Code authored vs. tests run vs. human sign-off |
| **Integration** | `INTEGRATED UNDER GRANT [id]` | Preauthorized integration is not Operator acceptance |
| **Boundary** | `ENFORCED [tested scope]`, `UNVERIFIED`, `SHARED_TRUST` | Configuration is not proof of security |

---

## License

MIT License — see [LICENSE](LICENSE) for details.
