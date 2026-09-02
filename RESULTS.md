# Results Ledger

This ledger contains externally useful bounded findings. It intentionally mixes positive and negative results because failure to reproduce or transfer an assumption is part of the evidence.

| Workstream | Status | Observed result | Strongest allowed claim | Public evidence |
|---|---|---|---|---|
| EXP-083 deterministic episode closure | Completed / internally validated within preregistered bounds | Frozen cases and semantic substitutions produced their expected dispositions; an adversarial review first found an observer-policy weakness, which was remediated and re-tested | In the tested single-host sealed-history topology, terminal evaluation can be re-derived from validated evidence without trusting model/executor success reports or stored outcomes | [`reference/experiments/exp_083/`](reference/experiments/exp_083/) |
| EXP-084 deterministic experience extraction | Completed / internally validated within preregistered bounds | Canonical `ExperienceRecordV1` extraction preserved cutoff separation, explicit missingness, exact provenance and deterministic cold extraction across success/failure/indeterminate episodes | In the tested topology, a validated episode can produce a canonical factual experience record whose admitted values are source-bound or declared deterministic derivations | [`reference/experiments/exp_084/`](reference/experiments/exp_084/) |
| Ornith cross-model proposal probe | Completed negative result | Zero exact canonical proposal bindings under the frozen 15-case interface; preserved raw responses exposed a model-response-surface/normalization mismatch | The then-frozen model-facing interface was not portable to this model/runtime combination as-is; the result does not prove general model incapability | [`CROSS_MODEL_RESEARCH.md`](CROSS_MODEL_RESEARCH.md) |
| Earlier P0 operational assurance | Completed bounded operational result | Bounded remote work could be admitted/rejected fail-closed, executed in disposable workspaces, recovered after interruption, and returned to autonomous operation under tested conditions | A practical multi-host control substrate existed under the tested operational boundary; this does not prove general security or infrastructure reliability | [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) |

## Why the negative result matters

The Ornith probe is deliberately prominent. The easy response would have been to modify the parser or promote intermediate reasoning into executable candidate content and rerun until the benchmark passed. That would have changed the experimental interface after seeing the outcome.

Instead, the original disposition was retained. The failure exposed a hidden assumption about which model response surface constitutes declared action intent. That finding became input to the later clean cross-model program.

## Representative implementation

The public reference snapshot contains two scientific-core implementation files:

- [`reference/kernel/episode_closure.py`](reference/kernel/episode_closure.py) — content-bound episode definition, terminal observation validation, deterministic evaluation/outcome derivation, and Cold Replay entry point;
- [`reference/kernel/experience_extraction.py`](reference/kernel/experience_extraction.py) — canonical `ExperienceRecordV1`, phase separation, field provenance, explicit missingness, validation, and dataset-manifest derivation.

These are exact reviewed reference artifacts from the private engineering repository, but their private-only dependencies are intentionally not mirrored here. See [`reference/README.md`](reference/README.md).

## Claim boundary

The results above do not establish general agent alignment, general security, dataset representativeness, learning effectiveness, universal model portability, or correctness for arbitrary natural-language tasks. See [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) and [`THREAT_MODEL_SUMMARY.md`](THREAT_MODEL_SUMMARY.md).
