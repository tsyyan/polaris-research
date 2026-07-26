# ADR-038: Milestone 2 Closure

## Status

Accepted by explicit project-owner decision on 2026-07-22.

## Context

Milestone 2 asked whether Polaris can transform immutable execution and external
evidence into structured, reproducible knowledge about observable decisions,
actions, outcomes, and evaluations without reconstructing hidden reasoning.

The initial architecture audit rejected closure because local contracts did not
compose. EXP-035–EXP-049 then addressed mandatory boundary invocation,
derived-authority publication, evaluator independence, qualification provenance,
global persisted reference resolution, canonical trajectory selection/order,
repeated acquisition occurrence history, and unknown/lineage preservation.

The second closure audit after terminal EXP-049 returned **Accepted with bounded
scope — formal closure on governance hold**. The project owner subsequently made
the required ADR-028–ADR-037 dispositions and directed full M2 closure.

## Decision

Milestone 2, **Verifiable Decision Intelligence**, is closed with bounded scope.

The accepted claim is:

> Polaris can deterministically construct and cold-replay a content-bound local
> analytical trajectory from validated persisted stores, prove required declared
> boundary completion under its experimental trust model, evaluate through the
> built-in closed declarative evaluator, preserve acquisition occurrences,
> explicit unknowns and typed lineage, and fail closed on unresolved, ambiguous,
> substituted, noncanonical, or caller-promoted evidence.

Execution Truth remains the M1 Runtime Ledger. M2 analytical artifacts are
read-only and grant no execution or production authority.

## Accepted architecture dispositions

- ADR-028: accepted with bounded experimental HMAC trust-root scope.
- ADR-029: rejected and superseded by ADR-030.
- ADR-030: accepted for local derived-authority publication/loading.
- ADR-033: rejected as written and superseded by ADR-034.
- ADR-034: accepted as the fail-closed qualification provenance gate.
- ADR-035: accepted for the built-in closed declarative evaluator only.
- ADR-036: accepted for the local persisted resolver; unsupported namespaces
  remain rejected.
- ADR-037: accepted for local single-policy canonical composition.

ADR-031 and ADR-032 retain their earlier accepted status subject to their stated
limits and later corrections.

## Bounded exclusions and carry-over

M2 closure does not claim or authorize:

- Corpus Freeze or a trusted production incident corpus;
- a result for the planned EXP-042B human-effect study;
- semantic truth of publications, metadata, reconstructions, or evaluations;
- a positive qualification-metadata provenance path where ADR-034 returns Unknown;
- human, LLM, plugin, remote, or arbitrary-code evaluator independence;
- support for the unresolved `source_prefix` namespace;
- TLS/DNS/proxy or archive-operator trust;
- parser sandboxing, host/process compromise resistance, HMAC key custody,
  distributed ordering/consensus, or production authorization;
- Milestone 3 pattern, improvement, mitigation, or policy authority.

These are explicit future work or non-goals, not hidden M2 success claims.

## Evidence

- terminal EXP-027–EXP-049 records and integrity registry;
- `docs/research/milestone_2_second_closure_audit_after_exp_049.md`;
- full repository verification: `603 passed, 1 skipped` before closure;
- current experiment manifest and valid knowledge base.

## Consequences

M2 architecture recovery is complete. New work may begin under Milestone 3 only
through separately accepted hypotheses and authority boundaries. Historical
failed, inconclusive, rejected, legacy, and bounded records remain unchanged.

