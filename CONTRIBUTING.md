# Contributing to Polaris Research

Polaris is a documentation-first research repository. It is published for
external technical review; this document describes supported ways to provide
feedback and does not imply an active community-development program.

## Useful Contributions

External researchers can contribute through:

- **bug reports** describing a concrete defect in the published materials or
  reproducibility tooling;
- **documentation corrections** for inaccurate, ambiguous, or broken content;
- **methodological critiques** that identify an unsupported inference,
  unexamined assumption, or reproducibility limitation; and
- **reproduction attempts** reporting the exact release, environment, steps,
  observed result, and any divergence.

## Reporting an Issue

Before opening an issue, check whether the observation is already covered by
the [claims boundary](docs/architecture/ADR-038-milestone-2-closure.md#bounded-exclusions-and-carry-over).

Include:

1. the release tag or commit reviewed;
2. the relevant file or procedure;
3. the expected and observed result;
4. enough detail to reproduce the observation; and
5. whether the report concerns wording, methodology, reproducibility, or
   implementation.

Do not include secrets, private datasets, personal data, or raw incident
evidence in a public issue.

## Proposed Changes

Keep changes narrow and evidence-backed. Corrections must preserve historical
records and must not broaden research claims. Methodology changes require
separate review and are not treated as routine documentation fixes.

Security-related reports should follow [SECURITY.md](SECURITY.md).
