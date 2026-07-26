# Public/Private Repository Separation Proposal

Status: **PROPOSAL — NO REPOSITORY VISIBILITY CHANGE AUTHORIZED**

## Purpose

Separate the private NOESIS development repository from a deliberately
published public research repository without exposing the private repository,
its history, branches, issues, settings, credentials, or operational material.
Polaris is the public-facing research program; NOESIS is the repository and
implementation that hosts and supports that work.

This proposal does not authorize publication. The private repository must
remain private unless a human owner separately approves a specific release.

## Proposed model

Maintain two repositories with independent access controls and histories:

- **Private source repository:** the authoritative development workspace,
  including operational material and work not approved for disclosure.
- **Public research repository:** a curated, reviewable release containing only
  explicitly approved code, documentation, tests, and evidence artifacts.

The public repository is created from a clean export or allowlisted release
tree. It is not made public by changing the visibility of the private
repository, mirroring all refs, or pushing the private Git history.

## Publication boundary

Every public release should be assembled from an explicit allowlist. At
minimum, the release review must:

1. identify the exact source commit and proposed public tree;
2. exclude `.env`, `.noesis/`, credentials, local logs, caches, private
   correspondence, unpublished data, internal-only operations, and unrelated
   Git metadata;
3. scan the full exported content and its intended history for secrets,
   personal data, absolute local paths, private URLs, and restricted material;
4. validate licensing and third-party redistribution rights;
5. run repository tests, knowledge-base validation, package verifiers, and
   Markdown link validation against the export;
6. obtain human approval for the exact reviewed tree and destination;
7. publish only that approved tree to a separately configured public remote;
8. verify the public result from an unauthenticated context before adding its
   canonical URL to outreach documents.

An omission, uncertain disclosure classification, failed check, or difference
between the reviewed and proposed public tree stops publication.

## Synchronization policy

There is no automatic private-to-public synchronization. Each update is a new
reviewed release. Automation may prepare a candidate export and reports, but it
must not create a public repository, change visibility, push to a public
remote, or update the public canonical URL without explicit human approval.

Public contributions should be reviewed and selectively applied to the private
source repository. No workflow should grant public contributors access to the
private repository or import private refs into the public repository.

## Identity and traceability

Each public release should record:

- the private source commit known to the authorized maintainers;
- the digest of the approved public tree or release archive;
- the review checklist and human approval;
- the public commit and release identifiers after publication;
- any intentional omissions that affect reproduction or interpretation.

Private identifiers need not be published when doing so would disclose
restricted information, but the maintainers should retain the mapping.

## B-01 disposition

Until a public repository passes this process, outreach material must not claim
that a public repository URL is available. After publication and
unauthenticated verification, the placeholder statement may be replaced with
the approved canonical URL.
