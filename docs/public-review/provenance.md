# Provenance Review

## Exact review question

Does the publicly described identity and lineage model preserve the
distinctions required by Polaris's bounded methodological claims without
implying access to undisclosed evidence?

## Concise technical model

Polaris separates source bytes, acquisition occurrences, attributed claims,
analytical artifacts, evaluations, and publications. Content identities bind
declared bytes; lineage records declared derivations; unknown or conflicting
information is not promoted into fact.

## Publicly reviewable claims

- The published model distinguishes observations from attributed claims.
- The declared boundary separates sealed reconstruction inputs from later live
  observations.
- The public package identifies selected private canonical records by content
  metadata without publishing their content.

See [Claims Boundary](CLAIMS_BOUNDARY.md), [Pilot-006 Public Record](PILOT_006_PUBLIC_RECORD.md),
and the public [Milestone 2 closure boundary](../architecture/ADR-038-milestone-2-closure.md).

## Not verifiable here

The completeness or correctness of private lineage, occurrence histories,
sealed manifests, execution records, and artifact bytes cannot be verified
from this package. Relevant identifiers are `P006-CLOSURE-RECORD`,
`P006-SEALED-MANIFEST`, and `P006-EXECUTION-EVIDENCE` in the
[Private Artifact Index](PRIVATE_ARTIFACT_INDEX.json).

## Disclosure limitation

Hashes support later identity comparison only. They do not expose provenance
content, establish semantic correctness, or prove that a private execution
followed the described model.

## Focused questions

1. Are the public distinctions sufficient for conceptual review?
2. Does any wording promote content identity into semantic provenance?
3. Which unavailable record would be essential for a stronger conclusion?
4. Is the boundary between public projection and private authority explicit?
