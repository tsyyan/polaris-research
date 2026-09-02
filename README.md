# NOESIS / Polaris — Public Research Snapshot

NOESIS is an independent research program in computational epistemology: how evidence, interpretation, decisions, and belief revision can remain explicit, auditable, and reproducible in computational systems.

Polaris is its reference implementation and experimental testbed. One current research track uses autonomous AI development agents to study a safety-relevant question:

> Can increasingly autonomous agents receive useful operational authority while authorization, evidence, evaluation, recovery, and replay remain externally verifiable and non-self-certifying across model and execution boundaries?

## Current research track

The current work studies bounded autonomous development agents under explicit separation of:

- model proposal and execution authority;
- candidate generation and promotion;
- agent self-report and independently observed outcome;
- persistent agent identity and episode-scoped permissions;
- live execution and deterministic reconstruction from retained evidence.

The methodology is falsification-oriented. Experiments are preregistered where appropriate, negative trajectories are retained, and claims are kept within the evidence actually observed.

A completed cross-model probe produced a negative portability result rather than a successful demonstration: a hidden dependency between a model's response surface and the host normalization contract was exposed. The result was preserved rather than repaired post hoc. This finding motivates a stricter cross-model independence program in which model identity changes while the surrounding task, authority, evidence, verification, and evaluation contracts remain fixed.

## Public snapshot

This repository is a research-facing snapshot. Active engineering, operational control infrastructure, credentials, host configuration, and security-sensitive implementation details remain in a private development repository.

The public snapshot is intended to expose enough information to review the research questions, methodology, threat boundaries, completed bounded findings, and proposed replication design without publishing operational attack surface.

Start here:

- [Research overview](RESEARCH_OVERVIEW.md)
- [Methodology](METHODOLOGY.md)
- [Cross-model research](CROSS_MODEL_RESEARCH.md)
- [Threat-model summary](THREAT_MODEL_SUMMARY.md)
- [Claude replication proposal](CLAUDE_REPLICATION_PROPOSAL.md)
- [Claims boundary](docs/public-review/CLAIMS_BOUNDARY.md)

## Status and claims

This repository does **not** claim that autonomous agents are generally safe, that the current controls solve alignment, or that results generalize beyond their frozen experimental conditions. Completed operational results, preregistered future work, and research proposals are identified separately.

## License

Apache-2.0. See `LICENSE`.