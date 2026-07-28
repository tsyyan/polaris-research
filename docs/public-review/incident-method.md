# AI Incident Method Review

## Exact review question

Does the public methodology conservatively distinguish observations, reported
claims, hypotheses, conflicts, drift, and unknowns without implying incident
truth or access to the private corpus?

## Concise technical model

Sources are qualified before reconstruction. Live bytes are preserved as new
observations and classified against sealed bytes. Reconstruction uses the
sealed track. Causal explanations are not selected when admitted evidence does
not support them.

## Publicly reviewable claims

- The conceptual method separates evidence roles and keeps drift explicit.
- Pilot-006 used a declared seven-source decision structure.
- The public projection reports five `DRIFT_OBSERVED` and two
  `BYTE_IDENTICAL` classifications without publishing source content.

See [Pilot-006 Public Record](PILOT_006_PUBLIC_RECORD.md) and
[Claims Boundary](CLAIMS_BOUNDARY.md).

## Not verifiable here

Corpus qualification, source content, acquisition responses, source-card
accuracy, and the correctness of individual classifications cannot be checked
from this package. The private execution and sealed evidence identifiers are
listed in the [Private Artifact Index](PRIVATE_ARTIFACT_INDEX.json).

## Disclosure limitation

No raw evidence, third-party source text, or corpus is included. Counts are a
public projection of private records, not independently inspectable evidence.

## Focused questions

1. Are the evidence-role distinctions methodologically adequate?
2. Could the drift classification be misread as semantic change?
3. Are unknowns and missing evidence treated conservatively?
4. Which unavailable evidence blocks a meaningful incident-method finding?
