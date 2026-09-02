# Public Research Release v0.1.0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `tsyyan/polaris-research` into a reviewer-grade, citeable public research snapshot while preserving a strict public/private boundary around the operational `tsyyan/polaris` repository.

**Architecture:** Keep the public repository as a curated research package rather than a source mirror. Add a fast reviewer path, explicit status/results ledgers, a high-level technical architecture, and an allowlisted `reference/` snapshot containing only representative scientific-core code and experiment records. Verify copied material against the reviewed private source and create a frozen GitHub release only after merge.

**Tech Stack:** Markdown, Python reference source, CFF 1.2 citation metadata, Git/GitHub.

**Spec:** `docs/superpowers/specs/2026-09-03-public-research-release-design.md`

## Global Constraints

- Do not publish credentials, tokens, environment values, private URLs/addresses/hostnames, user-home paths, or secret material.
- Do not publish NOVA control-plane implementation, mailbox protocols, node management, recovery entrypoints, deployment profiles, current host configuration, network topology, ACL/service details, or attack-enabling remediation procedures.
- Copied scientific-core artifacts must match the reviewed private source exactly unless a redaction is explicitly documented.
- Planned work must never be presented as established evidence.
- The public package must remain understandable without access to the private repository.
- Release tag: `v0.1.0-research-snapshot`; release title: `NOESIS / Polaris — Public Research Snapshot 2026.09`.

---

### Task 1: Reviewer-facing status and navigation

**Files:**
- Create: `RESEARCH_STATUS.md`
- Create: `RESULTS.md`
- Create: `TECHNICAL_ARCHITECTURE.md`
- Modify: `README.md`
- Create: `docs/historical/README.md`

**Interfaces:**
- Consumes: approved design plus current public research overview and bounded private research outcomes.
- Produces: one 5–10 minute reviewer path and explicit `COMPLETED / ACTIVE / PREREGISTERED / PROPOSED` distinctions.

- [ ] Create `RESEARCH_STATUS.md` with separate status sections and explicit non-claims.
- [ ] Create `RESULTS.md` with EXP-083, EXP-084, the negative Ornith probe, and operational P0 evidence, each with strongest allowed claim.
- [ ] Create `TECHNICAL_ARCHITECTURE.md` describing `TaskIntent -> EpisodeDefinition -> authorization -> execution evidence -> TerminalObservation -> evaluation -> EpisodeOutcome -> ExperienceRecord -> Cold Replay` without deployment details.
- [ ] Create `docs/historical/README.md` marking earlier incident-reconstruction/outreach material as historical.
- [ ] Update `README.md` to present the reviewer path, reference snapshot, status/result links, and historical boundary.
- [ ] Verify every new root-level local Markdown link resolves to a public-tree path.

### Task 2: Curated scientific-core reference snapshot

**Files:**
- Create: `reference/README.md`
- Create: `reference/kernel/episode_closure.py`
- Create: `reference/kernel/experience_extraction.py`
- Create: `reference/experiments/exp_083/hypothesis.md`
- Create: `reference/experiments/exp_083/design.md`
- Create: `reference/experiments/exp_083/outcome.md`
- Create: `reference/experiments/exp_084/hypothesis.md`
- Create: `reference/experiments/exp_084/design.md`
- Create: `reference/experiments/exp_084/outcome.md`

**Interfaces:**
- Consumes: exact reviewed source content from private `tsyyan/polaris` branch `development-agent-linux-node`.
- Produces: inspectable research implementation and hypothesis→design→outcome chains without operational code.

- [ ] Review each source for secret-like values, private paths/hosts, operational references, and misleading standalone assumptions.
- [ ] Copy `kernel/episode_closure.py` exactly to `reference/kernel/episode_closure.py`.
- [ ] Copy `kernel/experience_extraction.py` exactly to `reference/kernel/experience_extraction.py`.
- [ ] Copy selected EXP-083 and EXP-084 hypothesis/design/outcome files exactly.
- [ ] Add `reference/README.md` stating these are exact reference artifacts whose private-only imports/dependencies are intentionally not included and that the snapshot is not a standalone runnable package.
- [ ] Verify copied files match the reviewed source text byte-for-byte at the text-content level.

### Task 3: Citation and release metadata

**Files:**
- Modify: `CITATION.cff`
- Create: `RELEASE_NOTES_v0.1.0.md`

**Interfaces:**
- Consumes: reviewer-facing status/results and public source boundaries.
- Produces: citeable metadata and frozen release notes.

- [ ] Update CFF title to `NOESIS / Polaris Research`, version `0.1.0`, release date `2026-09-03`, author Andrey Tsyganok, repository URL, abstract, and research keywords.
- [ ] Create release notes separating completed results, active/preregistered work, proposed Claude replication, reference-code scope, and explicit limitations.
- [ ] Check CFF content for consistency with README and release notes.

### Task 4: Public-boundary verification and adversarial review

**Files:**
- Review all branch changes; no required new file unless a correction is needed.

**Interfaces:**
- Consumes: complete branch diff.
- Produces: verified release candidate or an explicit blocker.

- [ ] Open a pull request from `public-research-release-v0.1.0` to `main`.
- [ ] Inspect the complete PR diff and changed-file list.
- [ ] Search changed content for secret/token patterns, private host/path strings, current operational node details, and privileged procedures.
- [ ] Verify copied scientific-core content against the private source versions used for review.
- [ ] Verify README/local Markdown links and reviewer navigation.
- [ ] Adversarially check that every statement is classified as completed, active, preregistered, or proposed and does not exceed its evidence.
- [ ] Merge only if all checks pass.

### Task 5: Frozen GitHub release

**Files:**
- GitHub release/tag only; no new source file required after verified merge.

**Interfaces:**
- Consumes: verified merged `main` commit and `RELEASE_NOTES_v0.1.0.md`.
- Produces: immutable public citation target `v0.1.0-research-snapshot`.

- [ ] Re-fetch merged `main` and verify the expected research snapshot files exist.
- [ ] Create tag/release `v0.1.0-research-snapshot` from the verified merged commit.
- [ ] Use title `NOESIS / Polaris — Public Research Snapshot 2026.09` and the verified release notes.
- [ ] Re-fetch the public release and confirm tag, target commit, title, and notes.
