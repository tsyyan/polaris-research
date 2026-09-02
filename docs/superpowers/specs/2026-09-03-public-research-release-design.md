# Public Research Release v0.1.0 — Design

Date: 2026-09-03
Status: design for reviewer approval

## Goal

Prepare `tsyyan/polaris-research` as a reviewer-grade public research snapshot for external scientific review, including Anthropic's External Researcher Access Program, while preserving a strict boundary around the private `tsyyan/polaris` engineering and operational repository.

The release should let an external researcher understand the research question, inspect representative scientific-core code, follow completed bounded experiments from hypothesis through implementation to outcome, distinguish completed work from active/preregistered/proposed work, and cite a frozen public release.

## Public/private boundary

The public repository is not a mirror of the private repository.

Public material may include:

- research framing and methodology;
- bounded scientific claims and negative results;
- representative scientific-core data structures and deterministic derivation code;
- selected experiment records whose publication does not expose operational attack surface;
- high-level threat-model summaries and explicit limitations;
- public release metadata and citation information.

Do not publish:

- credentials, tokens, environment values, private URLs, addresses, hostnames, user-home paths, or secret material;
- NOVA control-plane implementation, mailbox protocols, node management, recovery entrypoints, deployment profiles, or privileged operational procedures;
- current host configuration, network topology, ACL/service details, or attack-enabling security remediation instructions;
- private-only evidence artifacts or data whose provenance or privacy status is unclear;
- files that depend on unpublished internal paths in a way that would make the public snapshot misleading or non-runnable.

## Reviewer experience

The root README will expose a 5–10 minute reviewer path:

1. Research Overview
2. Research Status
3. Results
4. Technical Architecture
5. Methodology
6. Cross-Model Research
7. Claude Replication Proposal

Historical incident-reconstruction material remains available but is explicitly labeled as an earlier research track rather than the current primary focus.

## New presentation artifacts

### RESEARCH_STATUS.md

A compact ledger separating:

- COMPLETED;
- ACTIVE;
- PREREGISTERED;
- PROPOSED.

No planned work may be described as established evidence.

### RESULTS.md

For each externally useful result, record:

- experiment / workstream;
- status;
- observed result;
- strongest allowed claim;
- public evidence link.

The negative cross-model Ornith result must be prominent because it demonstrates falsification-first practice.

### TECHNICAL_ARCHITECTURE.md

Describe the scientific control/evidence flow without operational deployment details:

`TaskIntent -> EpisodeDefinition -> bounded authorization -> execution evidence -> TerminalObservation -> independent evaluation -> EpisodeOutcome -> ExperienceRecord -> Cold Replay`

Clarify where model proposal, authority, observation, evaluation, and replay remain distinct.

### docs/historical/README.md

Explain that older incident-reconstruction and outreach documents are retained as historical research artifacts and are not the current primary agent-control track.

## Curated technical reference snapshot

Publish selected non-sensitive scientific-core artifacts under `reference/` rather than preserving private repository paths as if this were a full source mirror.

Initial allowlist:

- `kernel/episode_closure.py` -> `reference/kernel/episode_closure.py`
- `kernel/experience_extraction.py` -> `reference/kernel/experience_extraction.py`
- selected EXP-083 hypothesis/design/outcome -> `reference/experiments/exp_083/`
- selected EXP-084 hypothesis/design/outcome -> `reference/experiments/exp_084/`

Every transferred file must be reviewed for secrets, private paths/URLs, operational infrastructure references, misleading imports, and publication-sensitive details.

If a source file is technically useful but imports private-only modules, preserve the source as a clearly labeled reference artifact rather than claiming it is a standalone runnable package. Add `reference/README.md` describing this boundary.

## Citation and release

Update `CITATION.cff` to identify the current public research snapshot:

- title: `NOESIS / Polaris Research`;
- version: `0.1.0`;
- release date: `2026-09-03`;
- author: Andrey Tsyganok;
- repository URL;
- abstract/keywords describing computational epistemology, AI agent control, provenance, reproducibility, and cross-model evaluation.

After merge and fresh verification, create GitHub release/tag:

`v0.1.0-research-snapshot`

Release title:

`NOESIS / Polaris — Public Research Snapshot 2026.09`

The release notes must distinguish completed results, current active work, and the proposed Claude replication.

## Verification

Before merge:

1. inspect the complete PR diff;
2. scan all new/transferred text for secret-like values, private host/path references, and operationally sensitive details;
3. verify all README/local Markdown links resolve within the public tree;
4. verify `RESEARCH_STATUS.md` and `RESULTS.md` agree with the authoritative private research state;
5. verify copied scientific-core artifacts exactly match the reviewed private source version unless a public redaction is explicitly documented;
6. verify the repository remains understandable without access to the private repo;
7. perform an adversarial reviewer pass: identify any claim that could be read more strongly than the underlying evidence supports.

Merge only after these checks pass. Create the release only from the verified merged commit.

## Success criteria

A reviewer should be able to answer, without private access:

- What is NOESIS researching now?
- Which results are completed versus planned?
- What concrete technical architecture implements the research abstractions?
- Can I inspect representative real code and experiment records?
- What negative result has already falsified an assumption?
- Why is Claude scientifically useful as an independent replication family?
- What claims are explicitly out of scope?
- What frozen public version can I cite?

The public package should increase scientific legibility and credibility without materially increasing the operational attack surface of the private development system.