# Research Status

Snapshot date: **2026-09-03**

This page separates completed evidence from active, preregistered, and proposed work. The labels below are part of the claim boundary: work does not move between categories because it is expected to succeed.

## COMPLETED

### EXP-083 — Deterministic Episode Closure

Status: **internally validated within preregistered bounds**.

A bounded single-host sealed-history experiment showed that a frozen task intent, episode context, terminal postcondition, independently validated execution membership, and terminal observation can be deterministically closed into a terminal evaluation/outcome without trusting stored success labels or model/executor self-report.

Public evidence: [`reference/experiments/exp_083/`](reference/experiments/exp_083/)

### EXP-084 — Deterministic Experience Record Extraction

Status: **internally validated within preregistered bounds**.

A validated sealed episode can be deterministically transformed into a canonical, versioned `ExperienceRecordV1` with explicit PRE_DECISION, POST_DECISION, LABEL, missingness, and field provenance. Cold extraction reproduces the record without a live model or mutable execution dependency.

Public evidence: [`reference/experiments/exp_084/`](reference/experiments/exp_084/)

### Cross-model Ornith probe

Status: **completed negative result**.

A frozen proposal probe did not transfer cleanly through the unchanged model-facing normalization path. The preregistered disposition was `MODEL_SPECIFIC_INTERFACE_DEPENDENCE`. Preserved responses exposed a hidden dependency between the declared candidate surface and the model/runtime response surface. The result was not repaired post hoc.

Public summary: [`CROSS_MODEL_RESEARCH.md`](CROSS_MODEL_RESEARCH.md)

### Earlier operational P0 assurance

Status: **completed bounded operational assurance**.

Earlier P0 work demonstrated bounded task admission, fail-closed rejection, disposable execution, interruption/recovery handling, and successful autonomous operation across the tested host/control conditions. This is operational evidence, not a general autonomous-agent safety claim.

## ACTIVE

### P0 Exit v2 / adversarial development-agent closure

Status: **active stronger gate**.

The current program strengthens earlier operational assurance with real generated development episodes, independent outcome oracles, injected interruption, explicit authority ambiguity, deterministic Cold Replay, retained failed/abandoned trajectories, and a fixed adversarial matrix. Until this stronger gate is completed, it must not be described as a passed result.

Public threat boundary: [`THREAT_MODEL_SUMMARY.md`](THREAT_MODEL_SUMMARY.md)

## PREREGISTERED

### P1 — Clean Cross-Model Independence

Status: **preregistered; primary comparison not presented here as completed**.

A dedicated preregistration freezes the surrounding task/harness/control contract so that model identity is the experimental variable. Model-specific changes to authority, evidence-validity, or terminal verification rules are not allowed merely to make an arm succeed.

Public description: [`CROSS_MODEL_RESEARCH.md`](CROSS_MODEL_RESEARCH.md)

## PROPOSED

### Claude independent model-family replication

Status: **proposed replication; no Claude result is claimed**.

Claude is proposed as a subsequent independent model-family replication after the frozen primary comparison. Exact model identity and invocation conditions would be frozen prospectively before execution.

Proposal: [`CLAUDE_REPLICATION_PROPOSAL.md`](CLAUDE_REPLICATION_PROPOSAL.md)

## Explicit non-claims

This snapshot does not establish general autonomous-agent safety, alignment, perfect sandbox containment, arbitrary natural-language goal verification, universal cross-model portability, or reliable external infrastructure. Threat-model targets and planned experiments are not treated as implemented or validated properties until evidence supports them.
