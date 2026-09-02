# NOESIS / Polaris — Public Research Snapshot

NOESIS is an independent research program in computational epistemology: how evidence, interpretation, decisions, authority, and belief revision can remain explicit, auditable, and reproducible in computational systems.

Polaris is the reference implementation and experimental testbed. The current safety-relevant track studies bounded autonomous AI development agents.

> **Research question:** Can increasingly autonomous agents receive useful operational authority while authorization, evidence, evaluation, recovery, and replay remain externally verifiable and non-self-certifying across model and execution boundaries?

## Reviewer path — 5–10 minutes

1. **[Research Overview](RESEARCH_OVERVIEW.md)** — the program and current question.
2. **[Research Status](RESEARCH_STATUS.md)** — what is completed, active, preregistered, or proposed.
3. **[Results Ledger](RESULTS.md)** — bounded positive and negative findings with maximum claims.
4. **[Technical Architecture](TECHNICAL_ARCHITECTURE.md)** — the evidence/control flow and representative implementation links.
5. **[Methodology](METHODOLOGY.md)** — preregistration, falsification, independent evaluation, provenance, and Cold Replay.
6. **[Cross-Model Research](CROSS_MODEL_RESEARCH.md)** — preserved negative portability result and clean model-substitution program.
7. **[Claude Replication Proposal](CLAUDE_REPLICATION_PROPOSAL.md)** — proposed independent model-family replication; not a completed result.

For safety scope and limitations, see **[Threat Model Summary](THREAT_MODEL_SUMMARY.md)** and the earlier **[Claims Boundary](docs/public-review/CLAIMS_BOUNDARY.md)**.

## What is technically inspectable here

This is not only a prose proposal. The curated [`reference/`](reference/) snapshot exposes real scientific-core artifacts from the private engineering repository:

- [`reference/kernel/episode_closure.py`](reference/kernel/episode_closure.py) — `TaskIntent`, frozen `EpisodeDefinition`, terminal observation validation, deterministic outcome derivation, and `EpisodeColdReplay`;
- [`reference/kernel/experience_extraction.py`](reference/kernel/experience_extraction.py) — canonical `ExperienceRecordV1`, PRE_DECISION / POST_DECISION / LABEL separation, field provenance, explicit missingness, and cold extraction;
- [`reference/experiments/exp_083/`](reference/experiments/exp_083/) — hypothesis → preregistered design → bounded outcome for deterministic episode closure;
- [`reference/experiments/exp_084/`](reference/experiments/exp_084/) — hypothesis → field-admissibility design → bounded outcome for deterministic experience extraction.

The Python files intentionally retain imports to additional private scientific-core modules. They are exact reviewed reference artifacts rather than a misleading standalone package. See [`reference/README.md`](reference/README.md).

## Why the negative result is first-class evidence

A completed cross-model probe did **not** produce the desired portability result. Under the frozen interface, an Ornith model/runtime combination produced zero exact canonical proposal bindings and exposed a hidden dependency between the declared candidate surface and the response/normalization path.

The experiment was not repaired after observing the failure. Intermediate reasoning was not retrospectively promoted into executable intent. The negative disposition was preserved and used to motivate the later clean cross-model independence program.

See [`CROSS_MODEL_RESEARCH.md`](CROSS_MODEL_RESEARCH.md).

## Current control/evidence separation

The research architecture deliberately distinguishes:

```text
proposal ≠ authorization
candidate ≠ promotion authority
execution ≠ terminal success
self-report ≠ outcome evidence
persistent identity ≠ persistent privilege
missing evidence ≠ confident failure
live model ≠ replay authority
```

A compact architecture walkthrough is in [`TECHNICAL_ARCHITECTURE.md`](TECHNICAL_ARCHITECTURE.md).

## Public/private boundary

Active engineering and operational infrastructure remain in a private repository. This public snapshot deliberately excludes credentials, host/network configuration, control-plane/mailbox implementation, deployment/recovery entrypoints, privileged procedures, and other details that would add attack surface without materially improving scientific review.

Earlier public work focused on evidence-conservative AI incident reconstruction. It is retained for provenance and is explicitly historical relative to the current primary track; see [`docs/historical/README.md`](docs/historical/README.md).

## Claim discipline

This repository does **not** claim that autonomous agents are generally safe, that the current controls solve alignment, that sandboxing is perfect, or that results generalize beyond frozen experimental conditions. Completed evidence, active strengthening work, preregistered experiments, and proposals are separated in [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md).

## Citation and license

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). Source code is licensed under Apache-2.0; documentation licensing terms are in [`docs/DOCUMENTATION_LICENSE.md`](docs/DOCUMENTATION_LICENSE.md).
