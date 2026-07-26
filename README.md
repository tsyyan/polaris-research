# Polaris

**Evidence-Conservative AI Incident Reconstruction and Evaluation**

**Naming:** Polaris is the public-facing research program; **NOESIS** is the
repository and implementation that hosts and supports that work. They are not
separate projects.

Polaris is an open research project focused on building a reproducible methodology for reconstructing, analyzing, and evaluating AI incidents using verifiable evidence.

Rather than attempting to explain what an AI system "thought", Polaris is designed to answer a narrower and more rigorous question:

> **What can be demonstrated from available evidence, what remains unknown, and which conclusions are actually justified?**

The project emphasizes reproducibility, conservative reasoning, and explicit uncertainty over speculative interpretation.

---

# Research Goals

Polaris aims to develop a methodology that enables researchers to:

- reconstruct publicly documented AI incidents from verifiable evidence;
- distinguish observations from interpretations;
- preserve provenance across the entire evidence lifecycle;
- identify unsupported causal claims;
- compare competing hypotheses without selecting unsupported conclusions;
- produce deterministic and independently reproducible evaluation artifacts.

The long-term objective is to support more reliable investigation of AI failures and provide a stronger foundation for evaluating safety, robustness, and operational behavior.

---

# Core Principles

Polaris is built around several architectural principles:

- **Evidence First** — conclusions must originate from verifiable evidence.
- **Conservative by Design** — unknown information remains unknown.
- **Reproducible Research** — identical inputs produce identical outputs.
- **Immutable Provenance** — evidence history is append-only and traceable.
- **Explicit Boundaries** — the system clearly distinguishes observations, claims, evaluations, and hypotheses.
- **Fail-Closed Validation** — unverifiable information is rejected rather than silently accepted.

---

# Current Status

## Milestone 1 — Complete

Milestone 1 established the deterministic research infrastructure, including:

- immutable experiment records;
- deterministic projections;
- provenance tracking;
- reproducible experiment execution;
- architectural governance.

---

## Milestone 2 — Complete

Milestone 2 introduced a formal evidence architecture, including:

- verifiable acquisition boundaries;
- observed claim qualification;
- evidence-conservative evaluation;
- deterministic qualification pipeline;
- independent architectural review and bounded acceptance.

Current verification status:

- 603 passing tests
- deterministic experiment records
- independent architecture reviews completed
- bounded methodological claims
- clean reproducible repository state

---

# Current Research

## Pilot-001

**Reproducible Reconstruction of a Public AI Incident**

Pilot-001 is complete with result **FAIL-CLOSED TERMINATION**. Preregistration,
human review, Freeze, Seal, and Protocol Acquisition completed. Before
Extraction, verification found that the sealed Reproduction Unit did not
uniquely identify the required deterministic extraction procedure.

Extraction and downstream semantic phases were not executed. This is a protocol
completeness deficiency, not a demonstrated software or architecture failure.
Pilot-001 remains sealed and unchanged.

## Pilot-002

Pilot-002 passed independent review, Human Freeze Authorization, Freeze, and
Reproduction Unit v2 sealing. Protocol Acquisition then started under Protocol
v1.0.0: four of seven sources were byte-identical and three were rejected for
identity drift. A sealed acquisition-contract deficiency prevented preserving
the mismatching response bytes, so the Pilot stopped fail-closed before
Extraction as `INVALID/STOPPED`. No semantic or incident result is claimed.

## Pilot-003

Pilot-003 remediates durable acquisition but remains **not started**. Its first
independent preregistration review was rejected because the review package did
not expose the canonical implementation-manifest basis of its identities. A
self-contained corrected package is ready for re-audit. Freeze, sealing,
authorization activation, Acquisition, and downstream processing remain
blocked pending independent preregistration and corpus passing dispositions.

---

# Repository Structure

```text
docs/                 Architecture decisions and research documentation
experiments/          Experiment records and methodology
kernel/               Core evidence model and execution logic
tests/                Deterministic validation suite
research/             Research artifacts and reports
tools/                Development and analysis utilities
```

---

# Research Methodology

Every experiment follows a structured lifecycle:

1. Research question
2. Hypothesis
3. Methodology
4. Deterministic implementation
5. Independent verification
6. Acceptance or falsification
7. Immutable experiment record

Architectural changes are documented through Architecture Decision Records (ADRs), ensuring that design evolution remains transparent and reviewable.

---

# Project Roadmap

## Milestone 3

Current research directions include:

- Pilot-002 processing-identity readiness and preregistration;
- reproducible AI incident reconstruction;
- evidence gap analysis;
- competing hypothesis evaluation;
- counterfactual assessment;
- evidence-backed preventive constraints;
- longitudinal pattern discovery across AI incidents.

---

# Project Philosophy

Polaris does **not** attempt to reconstruct hidden reasoning processes or infer unavailable internal information.

Instead, it seeks to establish a reproducible framework capable of answering:

- What was directly observed?
- Which claims are supported?
- Which information is missing?
- Which conclusions remain unjustified?
- What can another researcher independently reproduce?

---

# Contributing

Contributions are welcome.

All contributions should preserve the project's core principles:

- reproducibility;
- deterministic behavior;
- evidence provenance;
- conservative evaluation;
- explicit architectural documentation.

Significant architectural changes should be accompanied by an Architecture Decision Record (ADR).

Pilot-002's final transition is recorded by EXP-056. Freeze passed and Protocol
Acquisition began, then stopped fail-closed before Extraction. The sealed
Reproduction Unit remains immutable.

---

# License

License information will be added before the first public research release.

---

# Citation

If Polaris contributes to your research, please cite the repository and reference the relevant experiment records and Architecture Decision Records where appropriate.

## Pilot-003 terminal status

Pilot-003 passed both independent review gates, owner authorization, Freeze,
and sealing. EXP-061 stopped execution before the first HTTP request because
the selected acquisition function requires a caller-supplied transport whose
concrete implementation was not sealed. No source was attempted; Extraction
and downstream processing did not start. The terminal disposition is
`INVALID/STOPPED`.

## Execution Readiness

ADR-040 requires every successor pilot after Pilot-003 to pass a pre-review
Execution Readiness gate. EXP-062 demonstrates the mechanism on Pilot-004 with
content-identified transport and external execution policies, a full
non-authoritative end-to-end dry run, and fail-closed late-binding detection.
The candidate is ready for review-package preparation, but is not reviewed,
frozen, sealed, or started.

## Pilot-004 immutable pre-review baseline

EXP-063 binds the Execution Readiness PASS candidate to an immutable baseline
and records a prospective, still-unconfirmed hypothesis about reducing
post-review stop-class architectural defects. Separate independently
verifiable preregistration and corpus packages are ready for external review.
Any drift in baseline members or identities mechanically blocks rebuilding the
packages. Pilot-004 remains unfrozen, unsealed, and unstarted.

## Pilot-004 Freeze result

Both external review gates passed and the owner authorization was recorded, but
EXP-065 blocked Freeze before sealing. The reviewed implementation is
exclusively `NON_RESEARCH_DRY_RUN`; no content-identified authoritative
Protocol Acquisition path exists. Pilot-004 therefore remains unsealed and
unstarted, with zero network requests. Its prospective Execution Readiness
effectiveness hypothesis is falsified for this pilot.

## Pilot-005 review candidate

Pilot-005 uses one content-identified executor for `SIMULATION` and `RESEARCH`.
Its B1 research-mode closure and B2 research-path simulation gates pass, as do
end-to-end readiness and no-late-binding checks. The candidate is immutably
baselined and packaged for independent preregistration and corpus review; it is
not frozen, sealed, or started.

## M2 final status

**Milestone 2: COMPLETED — ACCEPTED**

Final validation: **Pilot-006 COMPLETED — PASS**

The closure evidence includes independent architecture and corpus reviews, a
frozen reproduction unit, deterministic replay validation, and drift
observation validation. These results establish a bounded, research-grade
reconstruction workflow with evidence provenance; they do not establish
semantic truth or general incident resolution.

The project is transitioning to **Phase 3 — External Validation & Research
Packaging**, starting with Research Package v1.
