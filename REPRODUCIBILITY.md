# Reproducibility Boundary

This page states exactly what the public NOESIS / Polaris snapshot supports and what it intentionally does not claim to provide.

## Reproducible from the public snapshot

The repository exposes the frozen research descriptions, bounded results ledger, experiment designs and outcomes for EXP-083 and EXP-084, source-provenance metadata, and exact reviewed scientific-core reference artifacts. These materials allow an external reviewer to inspect the hypotheses, preregistered boundaries, admitted evidence model, deterministic derivations, reported dispositions, and the relationship between public reference artifacts and their recorded source identities.

## Inspectable but not standalone-executable

The Python modules under `reference/kernel/` are exact reviewed artifacts copied from the private engineering repository. They intentionally retain imports to private scientific-core dependencies. They are therefore inspectable implementation evidence, not a claim that this curated public snapshot is a standalone installable package.

The public experiment materials should likewise be read as a reproducible research record within their stated evidence boundary, not as a promise that every private operational dependency can be reconstructed from this repository alone.

## Intentionally private

Credentials, host and network configuration, control-plane/mailbox implementation, deployment and recovery entrypoints, privileged procedures, and other operational details remain private where publication would increase attack surface without materially improving scientific review.

## Validation terminology

- **Internally validated within preregistered bounds** means the stated result was executed and checked within the project's frozen experimental boundary; it does not mean independent third-party replication.
- **Completed negative result** means the observed failure/disposition was retained rather than repaired post hoc and rerun as though the original interface had succeeded.
- **Preregistered** and **proposed** work are not presented as completed evidence.

## External replication

No claim of independent third-party reproduction is made unless explicitly stated in the relevant result. The planned cross-model program, including the proposed Claude arm, is designed to strengthen evidence about which control properties survive model substitution while preserving the same claim discipline.
