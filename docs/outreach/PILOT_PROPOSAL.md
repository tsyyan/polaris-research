# Proposal for an Independent Methodology Pilot

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

## Goal

Test whether an independent researcher can apply the Polaris protocol to one
publicly documented AI incident and reproduce the same bounded analytical
artifacts—or identify a precise, protocol-relevant disagreement.

## Research Question

Given a predeclared public source boundary and fixed analytical contracts, can
two investigators independently distinguish supported observations, attributed
claims, unresolved gaps, and competing hypotheses without introducing
unavailable facts or unsupported causality?

## Scope

- One public AI incident selected before acquisition begins.
- Publicly accessible, citable sources only.
- A fixed acquisition cutoff and documented inclusion/exclusion rules.
- Versioned extraction, epistemic labeling, reconstruction, and evaluation
  rules.
- One primary Polaris run and one independent review or rerun.
- Comparison of source inventories, structured records, trajectory artifacts,
  gaps, hypotheses, and validation outcomes.

## Non-goals

- Product development, deployment, procurement, or adoption.
- Funding or institutional endorsement.
- Attribution of legal, ethical, or organizational responsibility.
- Recovery of private chain-of-thought or hidden system state.
- Proof of semantic truth or the real root cause.
- Evaluation of a company's overall safety or reliability.
- Validation of Milestone 3 mitigations, policies, or improvement mechanisms.
- Generalization from one incident to AI incidents as a class.

## Deliverables

1. Preregistered incident, cutoff, source policy, schemas, and success criteria.
2. Content-identified evidence inventory with acquisition occurrences.
3. Attributed extraction records with explicit Unknown values.
4. A bounded reconstruction containing timeline, evidence gaps, and competing
   hypotheses.
5. Deterministic evaluation and cold-replay artifacts for supported local
   contracts.
6. Independent review or rerun report, including disagreements and failed
   checks.
7. Threats-to-validity and claim-boundary statement.

## Expected Duration

Four to six weeks after incident selection and protocol agreement. This is an
estimate for a bounded pilot, not a delivery commitment.

## Required External Participation

One technically qualified reviewer should spend approximately 8–16 hours to:

- review the preregistered protocol before execution;
- independently inspect or reproduce the source inventory and selected
  artifacts;
- challenge epistemic labels, exclusions, and causal language;
- document deviations, disagreements, and possible falsifications.

No code contribution, product integration, confidential data, endorsement, or
financial support is requested.

## Expected Outcome

The expected output is evidence about the methodology, not agreement with an
incident narrative. Success may produce reproducible bounded artifacts.
Inconclusive or negative results—such as an irreconcilable source boundary,
unstable public evidence, or non-reproducible labeling—are valid and should be
reported without repair by assertion.

## Threats to Validity

- **Selection bias:** the chosen incident may be unusually well documented.
- **Public-evidence bias:** published accounts may omit or frame decisive facts.
- **Archive instability:** sources may change or become inaccessible.
- **Extraction judgment:** structured labels may depend on reviewer
  interpretation.
- **Protocol coupling:** the method may fit the selected incident too closely.
- **Reviewer non-independence:** discussion may align judgments prematurely.
- **Tooling validity:** deterministic mechanics do not establish semantic
  correctness.
- **Single-case limitation:** no population-level conclusion follows.

Mitigations include preregistration, exact source identity, independent labeling
before reconciliation, explicit Unknown values, preserved disagreements, and a
fixed cutoff.

## Boundaries

The pilot inherits the bounded M2 claims in
[ADR-038](../architecture/ADR-038-milestone-2-closure.md). External sources are
attributed evidence, not Polaris Execution Truth. A causal statement in a
source remains a reported causal claim unless separately supported by an
accepted causal contract. Analytical artifacts are read-only and acquire no
execution, policy, or production authority.

## Success Criteria

The pilot succeeds methodologically only if:

1. The incident, cutoff, contracts, and inclusion rules were fixed before the
   primary analysis.
2. Every included record resolves to exact acquired content and an acquisition
   occurrence.
3. Unsupported, missing, ambiguous, or conflicting inputs remain visible and
   fail closed where required.
4. The declared local deterministic artifacts cold-replay byte-identically from
   unchanged persisted inputs.
5. The external reviewer can reproduce the artifacts or provide a
   record-specific account of divergence.
6. No final statement exceeds the evidence boundary or the limitations listed
   above.

See the [research summary](RESEARCH_SUMMARY.md) and [technical FAQ](FAQ.md).
