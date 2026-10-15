# Pattern: Cost-Adaptive Model Routing

**Status:** Reference Pattern  
**Related Standards:** [USS-007](../standards/USS-007-orchestration.md) (Rule `007-03`), [patterns/risk-matrix.md](risk-matrix.md)

---

## 1. Overview & Principle

Rule `007-03` recommends that systems select the most cost-efficient sufficiently reliable model based on **total accepted-result cost**, provided that model selection and cost telemetry are programmatically accessible in the execution environment.

### Total Accepted-Result Cost
Raw token price per million tokens is an incomplete metric. True cost accounts for task success probability, retry overhead, and integration latency:

$$\text{Total Cost} = \text{Execution Cost} + (\text{Failure Rate} \times \text{Retry Cost}) + \text{Coordinator Integration Overhead}$$

Using a cheaper model that fails 40% of the time often results in higher financial and token cost than routing directly to a capable model that passes on the first turn.

---

## 2. Recommended Risk-Based Routing Tiers

When programmatic routing is supported, agents should map tasks according to the unified risk matrix:

| Task Class | Risk Level | Target Model Tier | Selection Rationale |
|---|---|---|---|
| **Scratchpad / Formatting** | **L1** | Fast / Lightweight (e.g. Flash / Mini tiers) | High throughput, minimal latency, lowest base token expense. |
| **Reversible Edits / Tests** | **L2** | Standard Developer Tier | Reliable code editing and test maintenance with deterministic validation. |
| **Substantive Architecture** | **L3** | High-Capability Coding Models | Multi-file reasoning, refactoring, and integration correctness. |
| **Normative & Security** | **L4** | Frontier / Extended Reasoning Models | Maximum analytical precision, policy adherence, and cryptographic security checks. |

---

## 3. Telemetry Availability & Graceful Fallback

- **Conditional Enforcement:** If an execution environment lacks programmatic API access to dynamically switch models or measure token expenditure, Rule `007-03` is considered satisfied by default using the environment's configured baseline model.
- **No Compliance Penalties:** An adopting system without dynamic model selection **MUST NOT** be marked non-compliant; it simply records that dynamic routing telemetry is currently not available.
