# Technical Architecture — Research View

This document describes the scientific control/evidence architecture, not the private deployment topology.

## Core flow

```text
Real task
   │
   ▼
TaskIntent ───────────────┐
   │                      │ frozen before execution
   ▼                      │
EpisodeDefinition ◄──── TerminalPostcondition
   │
   ▼
Bounded authorization
   │
   ▼
Model proposal / candidate
   │
   ▼
Execution evidence
   │
   ▼
TerminalObservation
   │
   ▼
Independent deterministic evaluation
   │
   ▼
EpisodeOutcome
   │
   ▼
ExperienceRecordV1
   │
   ├── PRE_DECISION
   ├── POST_DECISION
   ├── LABEL
   └── FieldProvenance
   │
   ▼
Cold Replay / Cold Extraction
```

The architecture is intentionally not a chain of trust in which each downstream component accepts the previous component's declaration. At several points, identity, authority, evidence, and evaluation are revalidated independently.

## Separation of concerns

### 1. Task intent is not execution authority

`TaskIntent` identifies the bounded task. `EpisodeDefinition` binds the task, declared context, and a terminal postcondition frozen before execution. A model can propose an action, but proposal content does not authorize the consequence.

### 2. Episode is not execution

An episode may contain one or more independently validated execution memberships. The episode definition and the execution evidence retain distinct identities. A successful execution process is not automatically a successful episode.

### 3. Self-report is not terminal evidence

The reference implementation stores model/executor reports but does not use them to determine terminal outcome. `TerminalObservation` instead binds the final relevant execution evidence to an independently observed post-execution manifest.

### 4. Missing evidence is not failure evidence

The bounded evaluator can derive `SATISFIED`, `UNSATISFIED`, or `INDETERMINATE`. Missing or inconclusive evidence remains indeterminate rather than being converted into a confident negative result.

### 5. Outcome is re-derived

The terminal outcome is a deterministic mapping from the validated postcondition evaluation. Stored success/failure labels do not override the derivation.

### 6. Experience is a projection, not new factual authority

`ExperienceRecordV1` is extracted only from a revalidated sealed episode. It separates:

- **PRE_DECISION** — evidence bound before the episode's first execution;
- **POST_DECISION** — observed execution membership and terminal-observation facts;
- **LABEL** — re-derived terminal evaluation/outcome.

Every admitted field has explicit source IDs and a named derivation. Unsupported semantic interpretations are excluded from the closed factual schema.

### 7. Replay is an evidence test

Cold Replay and Cold Extraction reconstruct derived state from retained evidence without re-invoking the live model. A replay result is therefore a test of whether the decision-relevant evidence boundary was sufficient, not a second opportunity for the model to reinterpret the run.

## Representative code

- [`reference/kernel/episode_closure.py`](reference/kernel/episode_closure.py)
- [`reference/kernel/experience_extraction.py`](reference/kernel/experience_extraction.py)

The original source modules depend on additional private scientific-core modules. They are published here as exact reviewed reference artifacts, not as a standalone installable package. See [`reference/README.md`](reference/README.md).

## Safety-relevant invariants under study

The current autonomous-agent track studies whether the following properties survive increasing autonomy, model substitution, interruption, and remote execution boundaries:

- proposal does not become authorization;
- candidate existence/test success does not become promotion authority;
- persistent identity does not become persistent privilege;
- executor-controlled checks are not the sole semantic outcome oracle;
- interrupted/retried execution does not silently duplicate or widen effects;
- missing decision-relevant evidence remains unknown/fail-closed;
- model substitution does not require model-specific weakening of authority, evidence, or evaluation rules.

These are research targets. The existence of an invariant in this document is not itself evidence that the invariant holds generally.

## Deliberately private boundary

The public snapshot omits operational node topology, credentials, mailbox/control implementation, recovery entrypoints, privileged deployment procedures, host configuration, and other details that would add attack surface without materially improving scientific review of the research abstractions.
