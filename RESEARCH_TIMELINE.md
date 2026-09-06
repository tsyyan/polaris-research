# Research Timeline and Public Provenance

This timeline is a reviewer-facing provenance index for the public NOESIS / Polaris research snapshot. It is intentionally conservative: it records only milestones that are represented by existing public artifacts or repository history and does not convert private work into a public claim.

| Date | Milestone | Public evidence / boundary |
|---|---|---|
| July 2026 | Public research release v1.0.0 established the earlier evidence-conservative incident-reconstruction track. | Retained as historical research material under `docs/historical/`; the v1.1 release notes identify v1.0.0 as the preceding public release. |
| 2026-09-03 | Public research snapshot v1.1 documented the current bounded autonomous-agent research track. | `RESEARCH_STATUS.md`, `RESULTS.md`, `METHODOLOGY.md`, `TECHNICAL_ARCHITECTURE.md`, and release metadata. |
| 2026-09-03 | EXP-083 and EXP-084 were published as completed, internally validated results within their preregistered bounds. | Exact public hypothesis/design/outcome artifacts under `reference/experiments/exp_083/` and `reference/experiments/exp_084/`. |
| 2026-09-03 | Reviewed scientific-core artifacts were transferred into the public reference snapshot with content-integrity provenance. | `reference/SOURCE_PROVENANCE.md` records Git blob identities for the transferred artifacts and explicitly limits what that provenance establishes. |
| 2026-09-03 | A completed negative cross-model Ornith probe was documented and retained rather than repaired post hoc. | `CROSS_MODEL_RESEARCH.md`, `RESULTS.md`, and `RESEARCH_STATUS.md`. |
| 2026-09-03 | P1 Clean Cross-Model Independence was publicly classified as preregistered, while Claude was classified only as a proposed subsequent independent model-family replication. | `RESEARCH_STATUS.md`, `CROSS_MODEL_RESEARCH.md`, and `CLAUDE_REPLICATION_PROPOSAL.md`. |
| 2026-09-06 | The public snapshot received reviewer-facing documentation improvements before an Anthropic External Researcher Access application. | Public repository history records the application-preparation commit. Changes clarified AI-safety positioning, the Claude experimental unit/outcomes, resource rationale, and reproducibility boundary; no completed-result status was upgraded. |
| 2026-09-06 | The public README was returned to grant-neutral research wording and this provenance timeline was added. | Current `README.md` and this document. |

## Interpretation

The 2026-09-06 application preparation is deliberately visible in repository history. It should be interpreted as packaging and clarification of an existing public research snapshot, not as evidence that the underlying completed results were produced for the application.

The strongest public provenance for the completed scientific-core artifacts is the combination of the dated v1.1 snapshot, the experiment hypothesis/design/outcome records, and `reference/SOURCE_PROVENANCE.md`. The latter establishes content identity for the listed transferred artifacts but does not make private dependencies independently inspectable.

## Limits

This timeline does not claim independent third-party replication, institutional affiliation, external endorsement, or a longer public track record than the repository actually provides. Private engineering history is not used here as a substitute for public evidence.
