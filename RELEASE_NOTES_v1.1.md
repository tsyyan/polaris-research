# NOESIS / Polaris Research v1.1 — Autonomous-Agent Research Snapshot

Tag: `v1.1`

This release succeeds the July 2026 `v1.0.0` public research release. The earlier release focused on evidence-conservative AI incident reconstruction; those materials remain available as historical research artifacts. Version 1.1 presents the current NOESIS/Polaris research track on bounded autonomous AI development agents while preserving that research history rather than rewriting it.

## Completed bounded results included

- **EXP-083 — Deterministic Episode Closure:** a preregistered single-host sealed-history experiment in which terminal evaluation/outcome is re-derived from validated evidence rather than model/executor self-report or stored success labels.
- **EXP-084 — Deterministic Experience Record Extraction:** canonical `ExperienceRecordV1` extraction with PRE_DECISION / POST_DECISION / LABEL separation, explicit missingness, field provenance, and Cold Extraction.
- **Cross-model Ornith probe — negative result:** the frozen model-facing interface failed to transfer cleanly to an Ornith model/runtime combination and exposed a response-surface/normalization dependency. The negative disposition was preserved rather than repaired post hoc.
- **Earlier operational P0 assurance:** bounded fail-closed admission, disposable execution, interruption/recovery, and autonomous operation under tested host/control conditions.

## Active and preregistered work

- **P0 Exit v2** is an active stronger development-agent gate involving real generated development episodes, independent outcome oracles, injected interruption, authority ambiguity, deterministic Cold Replay, retained failed trajectories, and adversarial falsification cases. It is not claimed as complete in this release.
- **P1 Clean Cross-Model Independence** is preregistered in the private research repository. The primary comparison freezes the surrounding task/harness/control contract while varying model identity. No primary P1 result is claimed here.

## Proposed Claude replication

Claude is proposed as a later independent model-family replication arm after the frozen primary comparison. The public proposal explains why independently developed model-family substitution is scientifically useful and why Claude output would remain proposal/evidence rather than authorization or self-certification.

No Claude experiment result is included or implied by this release.

## Inspectable technical reference

The `reference/` directory contains reviewed scientific-core artifacts copied exactly from the private engineering repository and accompanied by a Git-blob provenance manifest:

- deterministic episode closure implementation;
- deterministic experience-record extraction implementation;
- EXP-083 hypothesis, preregistered design, and outcome;
- EXP-084 hypothesis, preregistered design/field admissibility audit, and outcome.

The Python modules retain imports to private-only scientific-core dependencies and are intentionally published as reference artifacts rather than a standalone runnable package.

## Public/private boundary

This release deliberately omits credentials, operational node/network configuration, control-plane/mailbox implementation, recovery/deployment entrypoints, privileged procedures, and other details whose publication would increase attack surface without materially improving scientific review.

## Claim boundary

This release does not establish general autonomous-agent safety, alignment, perfect sandbox isolation, universal model portability, arbitrary natural-language task correctness, dataset representativeness, learning effectiveness, or external infrastructure reliability.

For the current status classification, see `RESEARCH_STATUS.md`; for maximum bounded claims, see `RESULTS.md`; for the research architecture, see `TECHNICAL_ARCHITECTURE.md`; for exact-source transfer integrity, see `reference/SOURCE_PROVENANCE.md`.
