# EXP-083 Preregistered Design

## Question, boundary and historical reuse

Can NOESIS deterministically assemble a bounded task episode and evaluate a
pre-execution terminal postcondition without trusting an LLM, executor success
or stored outcome? EXP-083 reuses EXP-079 `SandboxManifest` as terminal state
evidence, EXP-080 operations/attempts/sealed runs, EXP-081 complete authority
validation and EXP-082 `DerivedAuthorizedExecution` validation. It adds only
task intent, declared episode context, frozen episode definition, ordered
execution membership, terminal-observation reference, evaluation and outcome.

The conceptual boundaries remain distinct: TaskIntent != Episode != Execution
!= TerminalObservation != PostconditionEvaluation != EpisodeOutcome. Derived
evaluation/outcome and stored or self-reported classifications are not primitive
truth.

## Prospective minimum model

- `TaskIntent`: content-bound bounded task label and schema version.
- `EpisodeContext`: nonempty declared domain separator; no global uniqueness.
- `TerminalPostcondition`: task/context-bound predicate, canonical resource and
  evaluator version `sandbox.manifest.resource/v1`.
- `EpisodeDefinition`: pre-execution identity over task, context and frozen
  postcondition. Every member operation must carry this identity as its existing
  `proposal_id`, proving the goal was selected before its attempt existed.
- `EpisodeExecutionMembership`: exact episode identity, validated EXP-082
  `result_id`, binding/attempt identity and positive canonical ordinal.
- `TerminalObservation`: content-bound reference to the terminal membership,
  exact EXP-080 attempt evidence and its existing post-execution manifest.
- `SealedEpisode`: final closure over the definition, ordered membership IDs and
  terminal observation. Evaluation and outcome are re-derived, not trusted.

## Bounded predicate grammar

The complete grammar is `RESOURCE_EXISTS(resource)` and
`RESOURCE_ABSENT(resource)` under evaluator
`sandbox.manifest.resource/v1`. Resource is a nonempty canonical relative POSIX
path: no absolute path, empty/dot segment, `..`, backslash or duplicate slash.
Only a content-valid, conclusive `CompleteSandboxObserver` manifest can prove
truth or falsity. Missing/unresolvable/invalid/inconclusive evidence yields
`INDETERMINATE`; it never becomes `UNSATISFIED` merely from absence of evidence.

## Frozen invariants

I1 TaskIntent != Episode. I2 Episode != individual Execution. I3 membership is
content-bound to one exact episode. I4 ordering is canonical and deterministic.
I5 postcondition is frozen before the first member attempt. I6 stored outcomes
are not primitive truth. I7 model/executor self-report cannot establish outcome.
I8 terminal observation independently validates. I9 evaluation is deterministic
and evaluator-version-bound. I10 SATISFIED requires sufficient valid evidence.
I11 UNSATISFIED requires sufficient valid evidence proving false. I12 missing,
invalid or insufficient evidence derives INDETERMINATE. I13 another episode's
execution cannot establish this outcome. I14 Cold Replay uses sealed primitives
and zero live dependencies. I15 EpisodeContext is bounded declared separation,
not global uniqueness. I16 frozen postcondition identity participates in the
pre-execution episode definition and cannot be substituted afterward.

I17 the terminal observation references the highest-ordinal membership and its
exact attempt post-manifest. I18 membership ordinals are contiguous from one;
duplicates, gaps and noncanonical tuple order reject.

## Cases A--N

| Case | Construction | Frozen outcome |
|---|---|---|
| A | valid member and satisfying conclusive terminal manifest | `COMMITTED_SUCCESS` |
| B | sufficient manifest proves predicate false | `FAILED_POSTCONDITION` |
| C | missing/insufficient terminal evidence | `INDETERMINATE` |
| D | reported/stored SUCCESS while predicate false | `FAILED_POSTCONDITION` |
| E | reported/stored FAILED while predicate true | `COMMITTED_SUCCESS` |
| F | substitute P2 after execution under P1 | reject / cannot establish success |
| G | insert sibling-episode execution | reject |
| H | reorder otherwise valid executions | distinct closure or reject noncanonical order |
| I | substitute another terminal observation | reject |
| J | invalid EXP-082/081 ancestry | no valid/successful episode |
| K | identical task/postcondition with distinct contexts | distinct episode identities |
| L | omit execution and forge COMPLETE/SUCCESS | cannot repair omission |
| M | stored SUCCESS/FAILED/INDETERMINATE contradictions | primitives determine result |
| N | normal/manipulated Cold Replay | same derivation; zero live calls |

## Semantic substitutions S1--S16

S1 task; S2 episode context; S3 frozen postcondition; S4 postcondition after
cutoff; S5 sibling execution; S6 execution order; S7 duplicate membership; S8
omitted execution plus forged COMPLETE/SUCCESS; S9 terminal observation; S10
terminal resource; S11 predicate/evaluator version; S12 stored SUCCESS; S13
stored FAILED; S14 stored INDETERMINATE; S15 valid observation over invalid
execution ancestry; S16 independently initiated identical-episode identity
collision. Enclosing identities are recomputed for semantic attacks; stale hash
rejection is not the intended mechanism.

## Identity question, falsifiers and governance

Two otherwise identical independently initiated episodes must remain distinct
when their declared nonempty context IDs differ. Collision is an append-only
finding and stop-the-line event. The hypothesis is also falsified if post-hoc
goal substitution, unrelated execution/observation, malformed ancestry, forged
stored/self-reported outcomes, insufficient-evidence failure, noncanonical
membership or live replay dependence establishes success.

G1 and mandatory fresh G2 follow preliminary execution. BLOCKER, HIGH or a
core-inconclusive result triggers append-only remediation and fresh execution,
G1 and G2. G3 and EXP-084 are out of scope. EXP-083 is only the Episode Closure
stage of M3 and does not close the milestone; the intended later path remains
EXP-084 dataset extraction followed by the M3 final integration trial.
