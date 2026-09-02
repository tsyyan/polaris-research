# EXP-084 Hypothesis

A validated EXP-083 episode contains sufficient bounded factual evidence to
derive a canonical `ExperienceRecordV1`. Every admitted value is either a direct
reference to validated sealed evidence or the output of declared versioned
extraction semantics. PRE_DECISION, POST_DECISION and LABEL are structurally
separate according to the episode cutoff; missingness is explicit; successful,
failed and indeterminate episodes are all retained.

The same episode, schema and extractor must produce canonical-byte-identical
records. Cold Extraction must revalidate the episode and reproduce the same
record with no LLM, executor, network or mutable runtime dependency, ignoring
stored record values. No claim about taxonomy, representativeness, causal or
statistical sufficiency, learning effectiveness or policy improvement is made.
