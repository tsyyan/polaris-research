# Pilot-006 Public Record

Disclosure state: **PUBLIC_REVIEW_PROJECTION**

This is a bounded projection of private canonical records. It is not the
canonical record and does not expose the underlying evidence.

| Field | Public value |
|---|---|
| Pilot identifier | `PILOT-006` |
| Purpose | Test a preregistered dual-track workflow that preserves live observations separately from sealed reconstruction inputs |
| Decision structure | Live response is preserved and classified as `BYTE_IDENTICAL` or `DRIFT_OBSERVED`; sealed reconstruction continues only on sealed inputs |
| Execution disposition | `COMPLETED / PASS` within the declared trust model |
| Declared sources processed | `7/7` |
| `DRIFT_OBSERVED` | `5` |
| `BYTE_IDENTICAL` | `2` |
| Deterministic replay | Reported matched |
| Sealed substitution | Reported not occurred |

## Canonical identities

- Closure record: `P006-CLOSURE-RECORD`, SHA-256
  `d45f15692af9fca3d3e819b252ce5e5263a1e0ca8b90cd51eeb3758fa44c3bf1`
- Execution report: `P006-EXECUTION-REPORT`, SHA-256
  `5722d1dfab58c9c74fab5e5907546c4237ff89ba7c5e6f90cf59c95d1ef9d74a`
- Sealed manifest: `P006-SEALED-MANIFEST`, SHA-256
  `9c0befe64c4509149e8cc1f6cdd4ead7b11825e5b53bded83de9217f6a57b20a`

See the [Private Artifact Index](PRIVATE_ARTIFACT_INDEX.json) for byte lengths
and additional identities.

## Limitations

The private records, source bytes, corpus, processing implementation, and
execution evidence are not public. The counts and dispositions above are not
independently verifiable from this projection. A digest identifies bytes but
does not reveal, validate, or license their content.
