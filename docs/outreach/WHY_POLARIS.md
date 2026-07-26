# Why Does Polaris Exist?

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

AI incidents are often investigated through a mixture of operational records,
public statements, postmortems, evaluator outputs, benchmarks, and expert
interpretation. Each can contribute useful information. The research problem is
that a later reader may be unable to determine exactly which evidence produced
which conclusion, which facts were unavailable at the time, or whether replay
quietly substituted a different source or interpretation.

Three distinctions are especially easy to lose.

First, source integrity is not semantic truth. Exact preservation can establish
what a source said and which bytes were analyzed. It cannot establish that the
source was complete, accurate, or causally correct.

Second, an observation is not an explanation. A timestamped event, a reported
symptom, a retrospective causal statement, and an investigator's hypothesis
have different epistemic roles. Flattening them into one timeline can make a
coherent narrative appear better supported than it is.

Third, repeatable tooling is not necessarily reproducible inquiry. A pipeline
may execute twice while drawing on mutable pages, implicit selection rules,
ambient state, or an evaluator with undeclared context. Another investigator
then cannot tell whether disagreement comes from evidence, method, or hidden
inputs.

Benchmarks and aggregate metrics answer important performance questions, but
they usually do not preserve the case-specific path from evidence to
conclusion. Observability systems preserve traces, but traces alone do not
classify the epistemic status of external claims or prevent post-hoc
interpretation from acquiring the appearance of execution fact. Human and
model-based review can add judgment, but judgment remains dependent on visible
context, criteria, and evaluator identity.

Polaris exists to study the missing methodological layer: how to make an
incident account independently inspectable while refusing to infer what the
evidence does not contain. Its central question is not “Can we produce the most
complete explanation?” but:

> Can another investigator recover the same evidence boundary, apply the same
> declared rules, reproduce the same bounded artifacts, and see exactly where
> knowledge ends?

This objective makes negative and inconclusive outcomes meaningful. If public
evidence cannot distinguish competing hypotheses, preserving that result is
more informative than selecting a plausible root cause. If a source changes,
the acquisition occurrence matters. If metadata provenance is unavailable, an
explicit Unknown is a result rather than a defect to be filled.

The completed Polaris work establishes only a bounded local foundation for this
inquiry. It does not prove that a public incident can be substantively resolved,
that human investigators will benefit, or that reproduced artifacts are true.
Those are separate empirical questions. The proposed
[independent methodology pilot](PILOT_PROPOSAL.md) is designed to expose these
limits on one public case.

For the demonstrated scope and exclusions, see the
[one-pager](POLARIS_ONE_PAGER.md), [research summary](RESEARCH_SUMMARY.md), and
[technical FAQ](FAQ.md).
