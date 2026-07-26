# Polaris Technical FAQ

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

## Why not use LLM-as-a-Judge?

An LLM judge can be a useful evaluator, but its output is another
producer-attributed claim. It may depend on model version, hidden service
changes, prompt context, or undeclared inputs. Polaris therefore does not treat
LLM agreement as truth. M2 proved input independence only for one built-in
closed declarative evaluator, not for LLM evaluators.

## Why not rely on benchmarks alone?

Benchmarks measure performance under a defined task and information boundary.
They do not by themselves preserve incident evidence, establish provenance,
expose missing inputs, or make a particular conclusion reproducible. Polaris
uses benchmark results as bounded experimental evidence, not as substitutes for
case reconstruction.

## How is Polaris different from LangSmith?

LangSmith is commonly used for application tracing, debugging, and evaluation.
Polaris is a research methodology for evidence-conservative incident
reconstruction: it emphasizes content identity, attributed public sources,
explicit epistemic states, fail-closed replay, and non-authoritative analytical
artifacts. This is a difference in research question, not a claim of product
superiority or a feature-by-feature comparison.

## How is causality handled?

Canonical records do not infer semantic causality. They record observable
ordering, declared operational relationships, and source-attributed causal
claims. A source saying “X caused Y” proves that the source made that claim, not
that Polaris verified it.

## Why are Unknown values preserved?

Replacing missing information with a plausible value creates false evidence and
can alter downstream conclusions. Polaris distinguishes Unknown from absent,
withheld, and not applicable, and prevents later records or caller defaults from
silently filling an earlier gap.

## Does Polaris reconstruct hidden model reasoning?

No. It reconstructs declared visible context and observable, attributed
records. Rationales and explanations are statements made by identified
producers, not proof of private chain-of-thought or internal causal process.

## Can Polaris determine the real root cause?

Not from methodology alone. Polaris can organize evidence, surface conflicts,
and bound competing hypotheses. A real root-cause claim requires sufficient
case-specific evidence and an independently justified causal method; M2 makes no
such general claim.

## Why is deterministic reproducibility important?

It separates disagreement about method or evidence from variation introduced by
mutable inputs, ambiguous selection, ambient state, or nondeterministic tooling.
Byte-identical replay does not prove truth, but failure to replay weakens the
auditability of a conclusion.

## What has actually been experimentally validated?

Within a local experimental trust model: content-bound canonical trajectory
construction and cold replay; declared boundary-completion checks; preservation
of acquisition occurrences, Unknown values, gaps, and typed lineage;
fail-closed rejection of specified invalid evidence states; and input
independence for one closed declarative evaluator. Synthetic studies also
validated benchmark, ablation, and conflict-resolution mechanisms under their
stated conditions.

## What remains outside the project's claims?

Semantic truth, hidden reasoning, universal or real root causality, human
benefit, general benchmark superiority, trusted production corpora,
arbitrary-evaluator independence, transport and host security, distributed
consensus, production readiness, and all Milestone 3 mitigation or improvement
authority.

See [ADR-038](../architecture/ADR-038-milestone-2-closure.md), the
[research summary](RESEARCH_SUMMARY.md), and the
[pilot proposal](PILOT_PROPOSAL.md).
