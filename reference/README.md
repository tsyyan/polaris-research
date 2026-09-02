# Curated Technical Reference Snapshot

This directory exposes a small set of **real scientific-core artifacts** from the private NOESIS/Polaris engineering repository for external technical review.

## What is included

- [`kernel/episode_closure.py`](kernel/episode_closure.py) — deterministic episode closure, terminal observation validation, terminal evaluation/outcome derivation, and Cold Replay entry point;
- [`kernel/experience_extraction.py`](kernel/experience_extraction.py) — canonical `ExperienceRecordV1`, cutoff phases, field provenance, explicit missingness, validation, and dataset-manifest derivation;
- [`experiments/exp_083/`](experiments/exp_083/) — hypothesis, preregistered design, and bounded outcome for deterministic episode closure;
- [`experiments/exp_084/`](experiments/exp_084/) — hypothesis, preregistered design/field admissibility audit, and bounded outcome for deterministic experience extraction.

## Exact-source policy

The Python and experiment files in this snapshot are copied from the reviewed private source without research-semantic rewriting. Their provenance is intentionally visible through original experiment identifiers and module names.

## Not a standalone package

The two Python modules import additional scientific-core modules that are not included in this public snapshot. They are therefore **reference implementation artifacts, not a standalone runnable distribution**. Their purpose is to make the concrete data structures, integrity checks, deterministic derivations, and separation of evidence/outcome semantics inspectable without mirroring the full private repository.

Missing private dependencies must not be interpreted as hidden evidence for the public claims. The corresponding experiment hypothesis/design/outcome records are included so a reviewer can inspect what was actually tested and the limitations attached to the results.

## Deliberately excluded

This snapshot does not include NOVA control-plane code, mailbox protocols, host/node configuration, credentials, deployment/recovery entrypoints, privileged procedures, or current operational security details.

See [`../TECHNICAL_ARCHITECTURE.md`](../TECHNICAL_ARCHITECTURE.md) for the high-level research architecture and [`../THREAT_MODEL_SUMMARY.md`](../THREAT_MODEL_SUMMARY.md) for the public threat boundary.
