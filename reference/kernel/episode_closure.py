"""EXP-083 deterministic episode closure over sealed EXP-079--082 evidence."""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum

from kernel.execution_binding import (
    DerivedAuthorizedExecution, SealedAuthorizedExecutionHistory,
    derive_authorized_executions,
)
from kernel.retry_semantics import AttemptEvidence
from kernel.sandbox_observation import (
    CompleteSandboxObserver, ObjectKind, SandboxManifest, _identity,
)


EVALUATOR_VERSION = "sandbox.manifest.resource/v1"


class PredicateKind(StrEnum):
    RESOURCE_EXISTS = "RESOURCE_EXISTS"
    RESOURCE_ABSENT = "RESOURCE_ABSENT"


class EpisodeEvaluation(StrEnum):
    SATISFIED = "SATISFIED"
    UNSATISFIED = "UNSATISFIED"
    INDETERMINATE = "INDETERMINATE"


class EpisodeOutcome(StrEnum):
    COMMITTED_SUCCESS = "COMMITTED_SUCCESS"
    FAILED_POSTCONDITION = "FAILED_POSTCONDITION"
    INDETERMINATE = "INDETERMINATE"


@dataclass(frozen=True)
class TaskIntent:
    task_id: str
    schema_version: str
    label: str

    def body(self) -> dict[str, str]:
        return {"schema_version": self.schema_version, "label": self.label}


def make_task_intent(*, schema_version: str, label: str) -> TaskIntent:
    if not schema_version or not label:
        raise ValueError("task schema version and label required")
    value = TaskIntent("", schema_version, label)
    return replace(value, task_id=_identity(value.body()))


@dataclass(frozen=True)
class EpisodeContext:
    context_id: str
    declared_context_id: str

    def body(self) -> dict[str, str]:
        return {"declared_context_id": self.declared_context_id}


def make_episode_context(declared_context_id: str) -> EpisodeContext:
    if not declared_context_id:
        raise ValueError("episode context required")
    value = EpisodeContext("", declared_context_id)
    return replace(value, context_id=_identity(value.body()))


@dataclass(frozen=True)
class TerminalPostcondition:
    postcondition_id: str
    task_id: str
    episode_context_id: str
    predicate: PredicateKind
    resource: str
    evaluator_version: str

    def body(self) -> dict[str, str]:
        return {"task_id": self.task_id,
                "episode_context_id": self.episode_context_id,
                "predicate": self.predicate.value,
                "resource": self.resource,
                "evaluator_version": self.evaluator_version}


def _valid_resource(resource: str) -> bool:
    parts = resource.split("/")
    return bool(resource and "\\" not in resource and not resource.startswith("/")
                and "//" not in resource
                and all(part not in {"", ".", ".."} for part in parts))


def make_terminal_postcondition(*, task: TaskIntent, context: EpisodeContext,
                                predicate: PredicateKind, resource: str,
                                evaluator_version: str) -> TerminalPostcondition:
    if evaluator_version != EVALUATOR_VERSION:
        raise ValueError("unsupported terminal evaluator version")
    if not _valid_resource(resource):
        raise ValueError("canonical relative terminal resource required")
    if not isinstance(predicate, PredicateKind):
        raise ValueError("unsupported terminal predicate")
    value = TerminalPostcondition("", task.task_id, context.context_id, predicate,
                                  resource, evaluator_version)
    return replace(value, postcondition_id=_identity(value.body()))


@dataclass(frozen=True)
class EpisodeDefinition:
    episode_id: str
    task_id: str
    episode_context_id: str
    postcondition_id: str

    def body(self) -> dict[str, str]:
        return {"task_id": self.task_id,
                "episode_context_id": self.episode_context_id,
                "postcondition_id": self.postcondition_id}


def make_episode_definition(*, task: TaskIntent, context: EpisodeContext,
                            postcondition: TerminalPostcondition) -> EpisodeDefinition:
    if (postcondition.task_id != task.task_id
            or postcondition.episode_context_id != context.context_id):
        raise ValueError("postcondition does not belong to task episode context")
    value = EpisodeDefinition("", task.task_id, context.context_id,
                              postcondition.postcondition_id)
    return replace(value, episode_id=_identity(value.body()))


@dataclass(frozen=True)
class EpisodeExecutionMembership:
    membership_id: str
    episode_id: str
    execution_result_id: str
    binding_id: str
    attempt_id: str
    ordinal: int

    def body(self) -> dict[str, object]:
        return {"episode_id": self.episode_id,
                "execution_result_id": self.execution_result_id,
                "binding_id": self.binding_id, "attempt_id": self.attempt_id,
                "ordinal": self.ordinal}


def make_episode_membership(*, definition: EpisodeDefinition,
                            execution: DerivedAuthorizedExecution,
                            ordinal: int) -> EpisodeExecutionMembership:
    if ordinal < 1:
        raise ValueError("positive episode membership ordinal required")
    value = EpisodeExecutionMembership("", definition.episode_id,
        execution.result_id, execution.binding_id, execution.attempt_id, ordinal)
    return replace(value, membership_id=_identity(value.body()))


@dataclass(frozen=True)
class TerminalObservation:
    observation_id: str
    episode_id: str
    membership_id: str
    attempt_evidence_id: str
    manifest_id: str
    resource: str

    def body(self) -> dict[str, str]:
        return {key: value for key, value in self.__dict__.items()
                if key != "observation_id"}


def make_terminal_observation(*, definition: EpisodeDefinition,
                              membership: EpisodeExecutionMembership,
                              attempt_evidence: AttemptEvidence,
                              resource: str) -> TerminalObservation:
    if membership.episode_id != definition.episode_id:
        raise ValueError("terminal membership belongs to another episode")
    if attempt_evidence.attempt.attempt_id != membership.attempt_id:
        raise ValueError("terminal evidence does not belong to membership attempt")
    if not _valid_resource(resource):
        raise ValueError("canonical relative terminal resource required")
    value = TerminalObservation("", definition.episode_id,
        membership.membership_id, attempt_evidence.evidence_id,
        attempt_evidence.post_manifest.manifest_id, resource)
    return replace(value, observation_id=_identity(value.body()))


@dataclass(frozen=True)
class SealedEpisodeHistory:
    task: TaskIntent
    context: EpisodeContext
    postcondition: TerminalPostcondition
    definition: EpisodeDefinition
    authorized_history: SealedAuthorizedExecutionHistory
    memberships: tuple[EpisodeExecutionMembership, ...]
    terminal_observation: TerminalObservation | None
    stored_outcomes: tuple[str, ...]
    self_reports: tuple[str, ...]


@dataclass(frozen=True)
class DerivedEpisode:
    closure_id: str
    episode_id: str
    membership_ids: tuple[str, ...]
    observation_id: str | None
    evaluation: EpisodeEvaluation
    outcome: EpisodeOutcome

    def body(self) -> dict[str, object]:
        return {"episode_id": self.episode_id,
                "membership_ids": list(self.membership_ids),
                "observation_id": self.observation_id,
                "evaluation": self.evaluation.value,
                "outcome": self.outcome.value}


def _validate_primitives(history: SealedEpisodeHistory) -> None:
    task, context = history.task, history.context
    postcondition, definition = history.postcondition, history.definition
    if task.task_id != _identity(task.body()) or not task.schema_version or not task.label:
        raise PermissionError("task intent integrity mismatch")
    if (context.context_id != _identity(context.body())
            or not context.declared_context_id):
        raise PermissionError("episode context integrity mismatch")
    if not isinstance(postcondition.predicate, PredicateKind):
        raise PermissionError("terminal postcondition integrity mismatch")
    if (postcondition.postcondition_id != _identity(postcondition.body())
            or postcondition.task_id != task.task_id
            or postcondition.episode_context_id != context.context_id
            or postcondition.evaluator_version != EVALUATOR_VERSION
            or not _valid_resource(postcondition.resource)):
        raise PermissionError("terminal postcondition integrity mismatch")
    if (definition.episode_id != _identity(definition.body())
            or definition.task_id != task.task_id
            or definition.episode_context_id != context.context_id
            or definition.postcondition_id != postcondition.postcondition_id):
        raise PermissionError("episode definition integrity mismatch")


def _attempt_evidence(history: SealedEpisodeHistory, attempt_id: str) -> AttemptEvidence | None:
    for run in history.authorized_history.operation_runs:
        for evidence in run.attempts:
            if evidence.attempt.attempt_id == attempt_id:
                return evidence
    return None


def _evaluate(predicate: TerminalPostcondition,
              manifest: SandboxManifest | None) -> EpisodeEvaluation:
    if manifest is None or not manifest.conclusive:
        return EpisodeEvaluation.INDETERMINATE
    present = any(entry.path == predicate.resource for entry in manifest.entries)
    satisfied = (present if predicate.predicate is PredicateKind.RESOURCE_EXISTS
                 else not present)
    return (EpisodeEvaluation.SATISFIED if satisfied
            else EpisodeEvaluation.UNSATISFIED)


def _validate_terminal_manifest(manifest: SandboxManifest) -> None:
    if manifest.observer_policy != CompleteSandboxObserver.policy_id:
        raise PermissionError("unsupported terminal observer policy")
    paths = tuple(entry.path for entry in manifest.entries)
    if paths != tuple(sorted(paths)) or len(paths) != len(set(paths)):
        raise PermissionError("noncanonical terminal manifest entries")
    for entry in manifest.entries:
        if (not _valid_resource(entry.path) or entry.byte_length < 0
                or len(entry.sha256) != 64
                or any(character not in "0123456789abcdef" for character in entry.sha256)
                or (entry.kind is ObjectKind.DIRECTORY and entry.byte_length != 0)):
            raise PermissionError("invalid terminal manifest entry")
    if manifest.conclusive:
        if manifest.failure is not None:
            raise PermissionError("conclusive terminal manifest has failure")
    elif manifest.entries or not manifest.failure:
        raise PermissionError("invalid inconclusive terminal manifest")


def derive_episode(history: SealedEpisodeHistory, *, now: str) -> DerivedEpisode:
    _validate_primitives(history)
    executions = {item.result_id: item for item in
                  derive_authorized_executions(history.authorized_history, now=now)}
    if not history.memberships:
        raise PermissionError("episode requires execution membership")
    expected_ordinals = tuple(range(1, len(history.memberships) + 1))
    if tuple(item.ordinal for item in history.memberships) != expected_ordinals:
        raise PermissionError("noncanonical episode membership ordering")
    if len({item.membership_id for item in history.memberships}) != len(history.memberships):
        raise PermissionError("duplicate episode membership")
    if (len({item.execution_result_id for item in history.memberships})
            != len(history.memberships)):
        raise PermissionError("duplicate execution membership")

    for member in history.memberships:
        if (member.membership_id != _identity(member.body())
                or member.episode_id != history.definition.episode_id):
            raise PermissionError("episode membership integrity mismatch")
        execution = executions.get(member.execution_result_id)
        if (execution is None or execution.binding_id != member.binding_id
                or execution.attempt_id != member.attempt_id):
            raise PermissionError("episode membership lacks exact validated execution")
        matching_operations = [run.operation for run in
            history.authorized_history.operation_runs
            if any(item.attempt.attempt_id == member.attempt_id for item in run.attempts)]
        if (len(matching_operations) != 1
                or matching_operations[0].proposal_id != history.definition.episode_id):
            raise PermissionError("execution was not initiated under frozen episode")

    manifest: SandboxManifest | None = None
    observation = history.terminal_observation
    if observation is not None:
        terminal = history.memberships[-1]
        evidence = _attempt_evidence(history, terminal.attempt_id)
        if (observation.observation_id != _identity(observation.body())
                or observation.episode_id != history.definition.episode_id
                or observation.membership_id != terminal.membership_id
                or observation.resource != history.postcondition.resource
                or evidence is None
                or observation.attempt_evidence_id != evidence.evidence_id
                or observation.manifest_id != evidence.post_manifest.manifest_id):
            raise PermissionError("terminal observation integrity mismatch")
        manifest = evidence.post_manifest
        _validate_terminal_manifest(manifest)

    evaluation = _evaluate(history.postcondition, manifest)
    outcomes = {
        EpisodeEvaluation.SATISFIED: EpisodeOutcome.COMMITTED_SUCCESS,
        EpisodeEvaluation.UNSATISFIED: EpisodeOutcome.FAILED_POSTCONDITION,
        EpisodeEvaluation.INDETERMINATE: EpisodeOutcome.INDETERMINATE,
    }
    proto = DerivedEpisode("", history.definition.episode_id,
        tuple(item.membership_id for item in history.memberships),
        observation.observation_id if observation else None,
        evaluation, outcomes[evaluation])
    return replace(proto, closure_id=_identity(proto.body()))


class EpisodeColdReplay:
    def __init__(self) -> None:
        self.live_call_count = 0

    def replay(self, history: SealedEpisodeHistory, *, now: str) -> DerivedEpisode:
        return derive_episode(history, now=now)
