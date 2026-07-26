# Polaris Research

[![Release](https://img.shields.io/github/v/release/tsyyan/polaris-research?label=release)](https://github.com/tsyyan/polaris-research/releases/tag/v1.0.0)
[![License](https://img.shields.io/github/license/tsyyan/polaris-research)](LICENSE)

Polaris is an evidence-conservative research program for reproducible AI
incident reconstruction and evaluation.

## Overview

Polaris is the public research program within NOESIS. It studies how identified
evidence can be acquired, structured, reconstructed, evaluated, and replayed
without promoting source narratives, plausible interpretations, or
well-formed artifacts into objective truth.

The public repository is a documentation-first research release. It presents
the bounded methodology, architecture, reproducibility materials, and
Pilot-006 result intended for technical review.

## Research Question

How can an AI incident be reconstructed from declared evidence so that
observations, reported claims, analytical conclusions, and unknowns remain
distinct—and another researcher can reproduce the resulting artifacts or
identify a precise disagreement?

## Current Status

| Area | Status |
| --- | --- |
| Milestone 2 | **COMPLETED — ACCEPTED** |
| Pilot-006 | **COMPLETED — PASS** |
| Public release | **v1.0.0** |

Milestone 2 was accepted with bounded scope. Pilot-006 completed the frozen
research workflow and its deterministic replay and drift-observation
validation.

## What Polaris Demonstrates

Within the tested Pilot-006 and local experimental scope, Polaris demonstrates:

- a reproducible reconstruction workflow;
- evidence provenance tracking;
- deterministic replay;
- separation of sealed inputs and live observations; and
- drift observation classification.

## What Polaris Does Not Claim

Polaris:

- does not determine objective truth;
- does not determine root cause automatically;
- does not solve all AI incident investigation; and
- does not provide production guarantees.

These limitations are part of the research boundary, not pending product
claims.

## Pilot-006

Pilot-006 applied the frozen Polaris workflow to an approved public-incident
evidence corpus while keeping newly acquired live observations separate from
the sealed research inputs.

- **Methodology:** content-identified inputs, provenance-preserving processing,
  deterministic reconstruction, evaluation, publication, and cold replay.
- **Sources:** a frozen public-incident evidence corpus and separately preserved
  live observations used for drift comparison.
- **Results:** the declared processing workflow completed; deterministic replay
  and drift-observation validation passed.
- **Artifacts:** this public release includes the research summary,
  architecture boundary, reproducibility materials, and Pilot-006 summary.
  Datasets, raw evidence, and private operational artifacts are excluded.

The result supports a bounded research workflow. It does not establish semantic
truth, automated causality, general incident resolution, or production
readiness.

## Documentation

- [Architecture](docs/architecture/ARCHITECTURE_PRINCIPLES.md)
- [Research Package](docs/outreach/README.md)
- [Reproducibility Guide](docs/README.md#reproducibility)
- [Claims Boundary](docs/architecture/ADR-038-milestone-2-closure.md#bounded-exclusions-and-carry-over)
- [Pilot-006 Case Study](docs/README.md#pilot-006)
- [Complete documentation map](docs/README.md)

## License

Code is licensed under the [Apache License 2.0](LICENSE).

Documentation is licensed under
[Creative Commons Attribution 4.0 International](docs/DOCUMENTATION_LICENSE.md).
The Polaris name and marks are governed by the
[trademark policy](TRADEMARK.md).

## Contact / Review

Technical review is welcome, especially methodological critiques,
reproduction attempts, documentation corrections, and reports of concrete
defects. See [CONTRIBUTING.md](CONTRIBUTING.md) for the supported contribution
paths and [SECURITY.md](SECURITY.md) for security-related reports.
