# EXP-084 Preregistered Design and Field Admissibility Audit

## Bounded meaning and historical reuse

A trustworthy experience record is canonical and versioned; every admitted
factual value is grounded in validated sealed evidence or a declared
deterministic derivation, with prediction-cutoff classification and precise
provenance. Trustworthy does not mean complete, unbiased, representative,
causally or statistically sufficient, suitable for arbitrary ML, or evidence
that learning will improve the system.

EXP-084 reuses the complete EXP-083 `SealedEpisodeHistory` and live
`derive_episode` path, which transitively revalidates EXP-079 `SandboxManifest`,
EXP-080 operation/attempt/run, EXP-081 authority and EXP-082 authorized
execution evidence. It creates no execution, authority, observation or episode
semantics.

## Frozen Field Admissibility Audit

| Field | Meaning / exact source | Kind | Phase | Canonical / missingness | Provenance | Decision |
|---|---|---|---|---|---|---|
| source_episode_id | frozen episode definition ID | direct | PRE_DECISION | string / VALUE | EpisodeDefinition | ADMIT |
| task_id | bounded intent identity | direct | PRE_DECISION | string / VALUE | TaskIntent | ADMIT |
| episode_context_id | declared domain identity | direct | PRE_DECISION | string / VALUE | EpisodeContext | ADMIT |
| postcondition_id | frozen predicate identity | direct | PRE_DECISION | string / VALUE | TerminalPostcondition | ADMIT |
| predicate | frozen RESOURCE_EXISTS/ABSENT | direct | PRE_DECISION | enum string / VALUE | TerminalPostcondition | ADMIT |
| terminal_resource | frozen relative resource | direct | PRE_DECISION | string / VALUE | TerminalPostcondition | ADMIT |
| evaluator_version | frozen evaluator semantics | direct | PRE_DECISION | string / VALUE | TerminalPostcondition | ADMIT |
| membership_ids | canonical episode execution order | direct | POST_DECISION | ordered strings / VALUE | EpisodeExecutionMembership IDs | ADMIT |
| execution_count | count of validated memberships | derived `len(membership_ids)` | POST_DECISION | integer / VALUE | membership IDs + extractor | ADMIT |
| terminal_observation_id | exact final observation reference | direct/absence | POST_DECISION | VALUE or NOT_OBSERVED; never null/empty | TerminalObservation or EpisodeDefinition | ADMIT |
| terminal_evaluation | EXP-083 derived evaluation | derived | LABEL | enum string / VALUE | derived episode closure + evaluator | ADMIT |
| episode_outcome | EXP-083 derived outcome | derived | LABEL | enum string / VALUE | derived episode closure + evaluator | ADMIT |
| task label text | opaque human label, not required for factual identity view | direct but unnecessary | PRE | — | TaskIntent | REJECT minimality |
| task difficulty / complexity / semantic class | unsupported semantics | inferred | unknown | no valid representation | none | REJECT |
| strategy quality / failure reason | unsupported semantics | inferred | POST | no valid representation | none | REJECT |
| success-only eligibility flag | survivorship policy, not episode fact | invented | POST | — | none | REJECT |

No admitted field is optional except terminal observation presence. Its valid
absence is `NOT_OBSERVED`; `UNKNOWN` and `NOT_APPLICABLE` remain reserved
explicit states and are not silently substituted. Invalid or contradictory
source evidence rejects extraction rather than becoming missingness. Missing is
never coerced to zero, false, empty string or empty sequence.

## Frozen schema, cutoff and provenance

`ExperienceRecordV1` contains identity/version bindings, typed
`PreDecisionV1`, `PostDecisionV1`, `LabelV1`, and one canonical
`FieldProvenance` entry for every admitted field path. Schema is
`noesis.experience-record/v1`; extractor is
`noesis.exp084.sealed-episode/v1`. Record identity hashes schema, extractor,
source derived episode closure and complete canonical content/provenance. It is
content identity, not global uniqueness.

PRE_DECISION contains only EpisodeDefinition inputs already bound into the
operation `proposal_id` before its first attempt. Memberships, counts and
terminal observation are POST_DECISION. Evaluation and outcome are LABEL.
Phase is fixed by schema field path, not mutable metadata; arbitrary fields are
not accepted.

Provenance entries bind field path, fixed phase, source content IDs and a named
derivation (`direct/v1`, `membership-count/v1`, `missing-not-observed/v1`, or
the EXP-083 terminal derivation). A generic episode root alone is insufficient.

`DatasetManifestV1` binds schema/extractor versions and the lexicographically
sorted, duplicate-free exact record-ID set. Input order cannot create a second
ordering; omission/insertion changes dataset identity. It performs no filtering,
analytics, sampling or learning and cannot mutate record identity.

## Frozen invariants I1--I25

I1 Record != Episode. I2 no new factual authority. I3 every fact has validated
provenance/declared derivation. I4 unsupported inferred facts forbidden. I5 PRE
is pre-cutoff only. I6 POST cannot enter PRE. I7 LABEL cannot enter PRE. I8
evaluation/outcome are LABEL. I9 missingness explicit. I10 no missing coercion.
I11 deterministic extraction. I12 extractor version bound. I13 schema version
bound. I14 same inputs give canonical-byte-identical record. I15 stored records
untrusted in Cold Extraction. I16 field provenance independently verifiable. I17
dataset exact canonical membership/order. I18 Cold Extraction zero live calls.
I19 invalid episode cannot yield record. I20 source substitution cannot preserve
original validity. I21 phase metadata cannot launder post-cutoff data into PRE.
I22 dataset membership cannot alter record identity. I23 failed episodes
admissible. I24 indeterminate episodes admissible. I25 no success-only filter.

## Cases A--P and S1--S20

A success record; B failure retained; C indeterminate retained; D repeated
canonical-byte identity; E Cold Extraction/zero live; F stored tampering ignored;
G sibling source cannot preserve record; H POST/PRE leakage reject; I LABEL/PRE
reject; J unsupported semantic field reject/not admitted; K observation absence
is NOT_OBSERVED; L provenance substitution reject; M extractor substitution
reject/distinct identity; N schema substitution reject/distinct identity; O
deterministic multi-record manifest; P mixed outcomes retained.

S1 episode ID; S2 task; S3 context; S4 postcondition; S5 execution count; S6
outcome; S7 evaluation; S8 POST/PRE; S9 LABEL/PRE; S10 provenance source; S11
provenance omission; S12 missingness category; S13 missing to zero; S14
NOT_OBSERVED to false/empty; S15 extractor version; S16 schema version; S17
sibling record; S18 dataset omission; S19 insertion; S20 reorder. Content-valid
substitutions recompute enclosing identities where possible; stale hashes are
not the intended mechanism.

## Falsifiers and boundary

Nondeterminism, replay difference/live dependency, unproven facts, semantic
invention, leakage, missingness coercion, success filtering, invalid-source
extraction, version laundering, manifest ambiguity, stored override or any open
BLOCKER/HIGH/core-INCONCLUSIVE falsifies or stops terminalization. G2 explicitly
attacks scientific validity beyond hashes. G3, EXP-085 and M3 Final Integration
Trial are out of scope.

EXP-084 is the last planned new architectural layer before that trial, but does
not close M3. Passive Meta Observer, taxonomy, statistical analysis, prediction,
counterfactual datasets and Shadow Policy Learning are optional downstream
consumers and never prerequisites for record validity.
