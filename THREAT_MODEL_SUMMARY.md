# Development-Agent Threat Model — Public Summary

This document summarizes research targets for the autonomous-development-agent track. It is not a claim that every listed control has already been implemented or proven.

## Protected properties

The program aims to preserve:

1. **Authority integrity** — proposals, generated candidates, historical trust, or model confidence do not create execution/promotion authority.
2. **Evidence integrity** — observations retain provenance and cannot be silently elevated beyond what their source supports.
3. **Outcome integrity** — an executor or candidate cannot be the sole basis for a high-impact semantic success claim.
4. **Replay integrity** — missing decision-relevant evidence remains unknown rather than being reconstructed as certainty.
5. **Isolation** — generated or exploratory code cannot obtain production consequences merely by existing in an experimental worker.
6. **Identity/authority separation** — a persistent agent identity does not accumulate implicit privileges across episodes.
7. **Recovery integrity** — interruption, retry, resume, and checkpoint behavior must not silently duplicate effects or widen scope.

## Failure sources considered

The threat model includes capable but mistaken agents, malicious task/repository content, unsafe generated code, compromised experimental workers, stale or drifted execution nodes, incorrect verifiers, operator error, stale/duplicate/reordered messages, external model/service drift, privilege creep, and Goodhart-style optimization against telemetry.

## Adversarial scenarios

Current falsification targets include:

- candidate-to-authority laundering;
- verifier gaming or broken-intent PASS;
- unauthorized target/profile injection;
- sandbox/secret boundary violations;
- persistent privilege creep;
- Cold Replay gaps;
- interrupted or duplicated execution;
- remote environment drift;
- evidence-source corruption;
- telemetry self-optimization;
- model/task/harness drift misclassified as learning;
- unavailable-human and approval-fatigue cases.

## Explicit limits

The public research claims do not include protection against arbitrary kernel/hypervisor compromise, compromised cloud/GitHub roots of trust, physical compromise of trusted machines, perfect reproduction of complete host state, or universal semantic correctness for arbitrary natural-language tasks.

The purpose of the threat model is to define falsifiable boundaries and prevent stronger safety claims from being inferred from narrower operational evidence.