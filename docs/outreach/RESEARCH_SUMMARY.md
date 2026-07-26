# Polaris Research Summary

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

## Introduction

Polaris is an open research project on evidence-conservative reconstruction and
evaluation of AI incidents. It does not attempt to reveal what a model
"really thought." It studies a narrower problem: how to turn available,
identified evidence into a reproducible analytical account without promoting
source narratives, plausible interpretations, or well-formed artifacts into
truth.

The project separates execution facts from analytical products. External
postmortems and public records are treated as attributed sources, not as
Polaris execution history. Reconstructions remain read-only analytical
artifacts. This distinction is central to the project's epistemic boundary.

## Research Motivation

AI incident investigation commonly draws on logs, public statements,
postmortems, benchmarks, evaluator judgments, and expert interpretation. These
materials differ in origin, visibility, stability, and evidentiary strength.
They may omit critical context, report causal claims without the underlying
operational evidence, or change after publication.

A persuasive account is not necessarily a reproducible one. Reproduction
requires more than retaining a report: an investigator must be able to identify
the exact inputs, distinguish acquisition from interpretation, preserve missing
information, apply versioned rules, and verify that replay did not silently use
different evidence. Polaris investigates the infrastructure and methodology
needed for that narrower form of assurance.

## Research Questions

1. Can an incident evidence set be acquired, identified, and replayed without
   conflating source integrity with semantic truth?
2. Can observations, reported claims, hypotheses, evaluations, and unknowns
   remain distinct through a composed analytical pipeline?
3. Can reconstruction and evaluation artifacts be reproduced from declared,
   persisted inputs and fail closed when those inputs are missing, ambiguous,
   substituted, or noncanonical?
4. Which conclusions are supported by public evidence, and which require
   unavailable internal records or causal assumptions?
5. Can an independent investigator apply the same protocol and obtain the same
   artifacts—or produce a precise, documented disagreement?

## Methodology

Polaris uses an experiment-first, falsification-oriented workflow. Research
claims are recorded atomically; completed records are immutable; corrections
use new records. Architecture decisions define authority and epistemic
boundaries, while derived analytical artifacts remain replaceable and
non-authoritative.

The evidence workflow distinguishes:

- **acquisition**: recording exact source bytes and acquisition occurrence;
- **extraction**: producing attributed structured claims from identified
  source material;
- **reconstruction**: selecting and ordering validated persisted records under
  a versioned policy;
- **evaluation**: issuing a versioned analytical claim under a declared
  visibility boundary;
- **publication and cold replay**: recomputing from persisted inputs before a
  content-bound analytical result is accepted.

Missing facts are represented explicitly rather than inferred. Source-reported
causal statements remain reported claims; they are not converted into
independently verified causality. Lineage is derived only from typed contract
fields. Schema-valid content does not gain analytical authority merely because
a caller supplies it.

## Completed Milestones

### Milestone 1: Verifiable Execution

Milestone 1 established the underlying local research infrastructure for
append-only execution records, content-addressed artifacts, provenance,
authorization boundaries, and deterministic projections. Milestone 2 did not
replace this execution authority.

### Milestone 2: Verifiable Decision Intelligence

Milestone 2 is accepted with the bounded claim in
[ADR-038](../architecture/ADR-038-milestone-2-closure.md). Its terminal
experiments demonstrated, within the tested local experimental trust model:

- deterministic construction and byte-identical cold replay of one canonical,
  content-bound analytical trajectory from validated persisted stores;
- verification of declared acquisition, extraction, and evaluation boundary
  completion on the covered paths;
- append-only preservation of repeated acquisition occurrences;
- explicit preservation of unknowns, evidence gaps, and typed lineage;
- fail-closed handling of unresolved references, ambiguity, identity
  substitution, noncanonical bytes, and caller-promoted analytical content;
- input independence for one fixed, built-in closed declarative evaluator.

Earlier controlled experiments validated a synthetic incident-investigation
benchmark mechanism, an equal-information ablation, and local cold-verified
conflict handling. These are narrow mechanism results. They do not show general
superiority over conventional investigation, effectiveness for human
investigators, or successful resolution of production incidents.

The milestone also retained negative and inconclusive results. The human-effect
study collected no human responses and authorizes no human-benefit claim.
Corpus qualification did not authorize a trusted production incident corpus.

## Current Research

Milestone 3 begins with Pilot-001, a planned reconstruction of one publicly
documented AI incident. The pilot is intended to test the methodology against
real-world public evidence, not to validate an improvement mechanism or assign
responsibility.

The proposed protocol will predeclare the incident boundary, source inclusion
rules, acquisition cutoff, extraction schema, epistemic labels, reconstruction
policy, and success criteria. Outputs should include an evidence inventory,
attributed claims, a bounded timeline, explicit gaps, competing hypotheses,
replay instructions, and a review log.

Pilot-001 has not yet demonstrated that public evidence is sufficient for a
substantive incident conclusion. A valid outcome may be an inconclusive
reconstruction that precisely identifies what cannot be established.

## Known Limitations

The completed work does not establish:

- semantic truth, completeness, or causal validity of sources,
  reconstructions, or evaluations;
- access to hidden model reasoning, private operational records, or proprietary
  system state;
- a positive provenance result when qualification metadata remains Unknown;
- independence of human, LLM, plugin, remote, or arbitrary-code evaluators;
- transport, archive-operator, parser, host/process, or cryptographic
  key-custody security;
- distributed ordering, consensus, production authorization, or production
  readiness;
- human benefit, general benchmark superiority, or cross-incident
  generalization;
- any Milestone 3 pattern, mitigation, policy, or improvement authority.

The current canonical composition is local and single-policy. An unsupported
`source_prefix` namespace remains rejected. A supplied observation timestamp is
preserved but does not prove external clock truth.

## Future Research

Near-term work is limited to Pilot-001 and independent methodology review. The
priority is to test source selection, epistemic labeling, replay, and
disagreement handling on public evidence.

Later research may study human investigator effects, broader evaluator
isolation, corpus qualification, multi-incident comparison, and evidence-backed
preventive hypotheses. Each requires a separate experiment and cannot inherit
authority from Milestone 2. See the
[pilot proposal](PILOT_PROPOSAL.md), [FAQ](FAQ.md), and
[research rationale](WHY_POLARIS.md).
