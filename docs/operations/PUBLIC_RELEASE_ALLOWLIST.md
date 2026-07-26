# Polaris Public Release Allowlist

Status: **RELEASE CANDIDATE ONLY — PUBLICATION NOT AUTHORIZED**

This file is the machine-readable and human-readable disclosure boundary for
the first Polaris public repository candidate. The exporter reads the JSON
block below and copies no source path that is not matched by `include`.

```json public-release-allowlist
{
  "schema_version": 1,
  "include": [
    ".gitattributes",
    ".gitignore",
    "LICENSE",
    "README.md",
    "TRADEMARK.md",
    "docs/architecture/ADR-038-milestone-2-closure.md",
    "docs/architecture/ARCHITECTURE_PRINCIPLES.md",
    "docs/architecture/GLOSSARY.md",
    "docs/DOCUMENTATION_LICENSE.md",
    "docs/operations/PUBLIC_PRIVATE_REPOSITORY_SEPARATION_PROPOSAL.md",
    "docs/operations/PUBLIC_RELEASE_ALLOWLIST.md",
    "docs/outreach/COVER_LETTER.md",
    "docs/outreach/FAQ.md",
    "docs/outreach/PILOT_PROPOSAL.md",
    "docs/outreach/POLARIS_ONE_PAGER.md",
    "docs/outreach/README.md",
    "docs/outreach/RESEARCH_SUMMARY.md",
    "docs/outreach/WHY_POLARIS.md",
    "scripts/build_public_release_candidate.py"
  ],
  "exclude": [
    ".git/**",
    ".github/**",
    ".noesis/**",
    ".env",
    ".env.*",
    "AGENTS.md",
    "PUBLIC_RELEASE_CANDIDATE_MANIFEST.json",
    "artifacts/**",
    "datasets/**",
    "experiments/**",
    "logs/**",
    "memory/**",
    "research/**",
    "tests/**",
    "venv/**",
    "venv_broken_*/**",
    "work/**"
  ]
}
```

## What is included

- The public project overview and the bounded Milestone 2 claim.
- The Apache 2.0 code license, CC BY 4.0 documentation policy, and reserved
  Polaris name policy.
- Architecture principles and glossary needed to interpret that claim.
- The external outreach package and its local cross-references.
- The public/private separation proposal and this disclosure boundary.
- The deterministic exporter used to reproduce and scan the candidate.
- Repository-neutral text settings used by a future clean public history.

This is intentionally a documentation-first candidate. It is sufficient for a
human disclosure review, but it is not presented as a complete source,
evidence, or reproduction release.

## What is excluded and why

- Git metadata, remotes, branches, issues, and private history: the public
  repository must start from a clean, separately approved history.
- Environment files, local operational state, caches, logs, virtual
  environments, and work directories: these can contain credentials, machine
  details, or transient private data.
- Project memory, agent instructions, and internal governance material: these
  are private development controls, not public research artifacts.
- Experiment records, research corpora, raw acquired material, datasets,
  artifacts, and evidence packages: redistribution rights and disclosure scope
  require a separate review.
- Implementation packages and tests: this first candidate does not yet make a
  supported software-release claim. A later allowlist may add code and its
  complete test dependencies after licensing and disclosure review.
- CI and repository automation: these are destination-specific and must be
  approved for the separately configured public repository.
- The generated release manifest: it stays beside the candidate as private
  release-control evidence and is not part of the proposed public tree.

## Publication gate

Building a candidate does not authorize publication. A human owner must review
the exact manifest and candidate tree, confirm licensing and redistribution
rights, approve the destination and release identity, and explicitly authorize
repository creation and push. Only after the pushed result is verified without
authentication may an approved canonical URL be added to outreach documents.
