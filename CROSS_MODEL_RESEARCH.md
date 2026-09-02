# Cross-Model Research

## Motivation

A safety or evidence property that holds only for one model-facing interface may be a property of that interface rather than of the surrounding control architecture. NOESIS therefore treats cross-model substitution as an explicit experimental variable rather than assuming portability.

## Completed negative probe

A frozen 15-case proposal probe was executed against an Ornith 9B model through Ollama using an unchanged existing model adapter/normalization path.

The preregistered disposition was:

`MODEL_SPECIFIC_INTERFACE_DEPENDENCE`

The arm produced zero exact canonical proposal bindings under the frozen interface. Offline inspection of preserved raw responses showed that most task-relevant reasoning appeared in a `thinking` surface while the host-declared candidate `content` surface was empty. Two cases emitted non-empty content but did not satisfy the frozen canonical proposal contract.

This does **not** establish that the model was generally incapable of representing the requested proposal. It establishes that the existing model-facing response/normalization contract did not transfer cleanly to this model/runtime combination.

The experiment was not rerun with a repaired parser or prompt. In particular, private/intermediate reasoning was not retrospectively promoted into executable proposal content, because reasoning evidence and declared action intent are distinct surfaces.

The negative result exposed a hidden coupling cheaply and motivated a prospective cross-model design.

## Clean cross-model independence study

The subsequent preregistered program asks whether authorization, execution, evidence, normalization, evaluation, and terminal-outcome semantics survive model substitution when the surrounding experimental contract is fixed.

The intended controls include fixed:

- task corpus and instructions;
- source identities;
- harness and adapter policy defined for the experiment;
- authority path;
- sandbox/tool/network policy;
- verification and evaluation logic;
- evidence schemas and terminal interpretation rules.

Model self-report is not terminal success. A model-specific requirement to weaken authority, evidence, or verification rules is a safety-relevant failure condition rather than an acceptable compatibility patch.

## Replication

The primary preregistered comparison is preserved. Additional model families are treated as later replication arms rather than silently replacing or rewriting the original experiment after outcomes are known.

An independently developed Claude model family is a useful replication candidate because it can help distinguish properties of the surrounding control/evidence architecture from dependencies on the local model families used in the primary study.

Exact model identity and invocation conditions should be frozen prospectively before the replication begins.