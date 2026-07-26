# Polaris: Evidence-Conservative AI Incident Reconstruction

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

## Mission

Polaris studies how investigators can produce reproducible, reviewable accounts
of AI incidents while keeping observations, source claims, analytical
inferences, evaluations, and unknowns distinct.

## Research Problem

Public incident evidence is incomplete, heterogeneous, retrospective, and often
mutable. Conventional logs, postmortems, dashboards, benchmarks, and narrative
explanations can each be useful, but none alone guarantees that another
investigator can recover the same source set, apply the same rules, and obtain
the same bounded conclusions. Polaris asks:

> What can be demonstrated from the available evidence, what remains unknown,
> and which conclusions survive independent reconstruction?

## Current Status

Milestone 2 is complete with bounded scope under
[ADR-038](../architecture/ADR-038-milestone-2-closure.md). Milestone 3 has
begun as a research phase. Its first planned activity, Pilot-001, is a
reproducible reconstruction of one public AI incident; no Pilot-001 result is
claimed yet.

## What Has Been Demonstrated

Within the tested local experimental trust model, Polaris can:

- construct and cold-replay a content-bound analytical trajectory from
  validated persisted stores;
- verify completion of declared acquisition, extraction, and evaluation
  boundaries on the covered publication and load paths;
- preserve repeated acquisition occurrences, explicit unknowns, evidence gaps,
  and typed lineage;
- fail closed on unresolved, ambiguous, substituted, noncanonical, or
  caller-promoted evidence;
- run one built-in closed declarative evaluator without filesystem, network,
  environment, clock, randomness, cache, or prior-conversation inputs.

Synthetic experiments also validated the benchmark and artifact mechanisms and
showed a narrow benefit from explicit verification metadata in a controlled
conflict condition. They did not establish general superiority or human
benefit.

## Current Research

Pilot-001 will test whether the methodology can be applied to public,
real-world evidence with a predeclared source boundary, explicit epistemic
labels, competing hypotheses, visible evidence gaps, and a reproducible output
package.

## Why Independent Review Matters

The current evidence is primarily local and contract-level. Independent review
can expose hidden assumptions in corpus selection, extraction, labeling,
evaluation, and replay—and can distinguish reproducible mechanics from valid
incident conclusions. See the
[pilot proposal](PILOT_PROPOSAL.md) and [limitations](FAQ.md).

## Repository

The NOESIS repository contains the code, tests, immutable experiment records,
research audits, and architecture decisions. Its public canonical URL will be
added only after the publication review described in the
[repository separation proposal](../operations/PUBLIC_PRIVATE_REPOSITORY_SEPARATION_PROPOSAL.md);
the private repository is not exposed automatically. Start with this
[outreach package](README.md) and the [research summary](RESEARCH_SUMMARY.md).
