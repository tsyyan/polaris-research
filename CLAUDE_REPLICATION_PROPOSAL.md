# Claude Cross-Model Replication Proposal

**Status:** proposed replication; not a completed result.

## Question

Can a fixed autonomous-agent control and evidence architecture preserve its safety-relevant semantics when the underlying model is replaced by an independently developed Claude model family?

## Relationship to existing work

NOESIS already has a cross-model research track and a preregistered primary comparison. The primary experiment must not be rewritten after outcomes are observed.

Claude is proposed as a subsequent independent model-family replication arm.

## Fixed experimental boundary

Before the Claude replication begins, the experiment will freeze the exact model identity and applicable invocation conditions together with the relevant task corpus, instructions, source identities, authority rules, sandbox/tool policy, evidence schemas, verification logic, and terminal evaluation contract.

Claude outputs will be treated as proposals/evidence, not authorization. Agent self-report will not certify semantic task success.

Where the experiment uses an independent or held-out outcome oracle, a candidate-visible self-check cannot override an oracle failure.

Terminal interpretation must remain reconstructable from retained evidence without requiring a new live model invocation.

## Primary failure signal

Ordinary task-performance differences across model families are expected.

The safety-relevant question is whether the Claude arm can operate under the same bounded authority, evidence-validity, and outcome-evaluation rules. Requiring a Claude-specific relaxation of those rules in order to obtain a successful arm is evidence against the intended model-independent control property.

## Why Claude

Claude provides an independently developed frontier model family. A successful or failed replication therefore carries more information about model-family dependence than simply adding another closely related local model to the same experimental lineage.

API access also permits invocation identity, parameters, raw response evidence, failure/retry observations, and resource accounting to be captured consistently by the experimental harness.

## Outputs

Subject to the final preregistration and safety/privacy review, the research-facing outputs are intended to include:

- preregistration and frozen experimental identities;
- paired outcome/evidence matrices;
- positive, negative, interrupted, and rejected trajectories relevant to interpretation;
- deterministic replay artifacts or public summaries where raw artifacts cannot safely be exposed;
- limitations and bounded conclusions.

No result will be presented as general proof of autonomous-agent safety.