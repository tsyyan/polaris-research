# EXP-083 Hypothesis

Within a bounded single-host sealed-history topology, a content-defined task
intent, declared episode context, terminal postcondition frozen before execution
and canonical ordered memberships of independently validated EXP-082 execution
results can form one deterministic episode closure.

A version-bound non-LLM evaluator over independently validated terminal manifest
evidence can derive `SATISFIED`, `UNSATISFIED` or `INDETERMINATE`, mapping only
those values to `COMMITTED_SUCCESS`, `FAILED_POSTCONDITION` or `INDETERMINATE`.
Stored outcomes and model/executor reports are untrusted. Cold Replay must derive
the same membership, evaluation and outcome solely from sealed primitives with
zero live dependencies. No prospective outcome is asserted.
