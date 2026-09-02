# Methodology

NOESIS uses evidence-conservative experimental practices intended to make failures, uncertainty, and post-hoc interpretation visible rather than silently normalizing them away.

## Preregistration

Where an experiment can be specified prospectively, the task corpus, independent variable, fixed controls, evaluation rules, failure conditions, and evidence requirements are frozen before observing the relevant outcomes.

A failed preregistered run is evidence. It is not silently replaced by a repaired run.

## Authority separation

Model output is not authority. A proposal, plan, generated patch, candidate commit, or prior successful behavior cannot grant itself additional execution or promotion rights.

Effective permissions are bounded by the current explicit authorization context. Persistent agent identity does not imply persistent privilege.

## Independent outcome boundary

Agent self-report and candidate-controlled checks are useful evidence but are insufficient for high-impact semantic success claims. Where practical, terminal success is conditioned on an independently controlled or held-out verifier/oracle whose definition is frozen outside the candidate's control.

## Evidence and provenance

Decision-relevant observations retain source identity and status. The evidence layer avoids converting declarations into observations or temporal proximity into causality.

Positive, negative, interrupted, rejected, and abandoned trajectories are retained when they are relevant to later interpretation.

## Deterministic reconstruction

Cold Replay asks whether a terminal interpretation can be reconstructed from the evidence admitted at a frozen cutoff without re-running the live model. Repeating replay over the same admitted evidence should produce the same canonical result.

A complementary replay-gap test removes a known decision-relevant fact. The expected behavior is explicit uncertainty or fail-closed output rather than reconstruction of unsupported certainty.

## Cross-model experiments

For clean model-substitution experiments, model identity is the independent variable. Task corpus, instructions, source state, tool/sandbox policy, authority rules, evidence schemas, verification logic, and terminal evaluation are held fixed as far as the preregistered design requires.

Task-performance differences are expected and are not automatically safety failures. A more consequential failure is a requirement to introduce model-specific authority, evidence-validity, or verification exceptions to make an arm succeed.

## Adversarial review

Passing the intended path is not sufficient evidence of robustness. Current designs include explicit attempts to falsify candidate-to-authority separation, independent verification, replay completeness, interruption safety, stale authorization handling, privilege persistence, and related boundaries.

## Claim discipline

Results remain scoped to the conditions actually tested. Operational assurance is not presented as universal agent safety, and threat-model targets are not described as implemented controls until independently supported by evidence.