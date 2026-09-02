"""EXP-084 canonical factual experience extraction from validated episodes."""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import StrEnum
from typing import Any

from kernel.canonical import canonical_json_bytes
from kernel.episode_closure import SealedEpisodeHistory, derive_episode
from kernel.sandbox_observation import _identity


SCHEMA_VERSION = "noesis.experience-record/v1"
EXTRACTOR_VERSION = "noesis.exp084.sealed-episode/v1"
DATASET_SCHEMA_VERSION = "noesis.dataset-manifest/v1"


class Phase(StrEnum):
    PRE_DECISION = "PRE_DECISION"
    POST_DECISION = "POST_DECISION"
    LABEL = "LABEL"


class Missingness(StrEnum):
    VALUE = "VALUE"
    NOT_OBSERVED = "NOT_OBSERVED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class FactualValue:
    status: Missingness
    value: str | None

    def body(self) -> dict[str, str | None]:
        return {"status": self.status.value, "value": self.value}


@dataclass(frozen=True)
class PreDecisionV1:
    source_episode_id: str
    task_id: str
    episode_context_id: str
    postcondition_id: str
    predicate: str
    terminal_resource: str
    evaluator_version: str

    def body(self) -> dict[str, str]:
        return dict(self.__dict__)


@dataclass(frozen=True)
class PostDecisionV1:
    membership_ids: tuple[str, ...]
    execution_count: int
    terminal_observation: FactualValue

    def body(self) -> dict[str, Any]:
        return {"membership_ids": list(self.membership_ids),
                "execution_count": self.execution_count,
                "terminal_observation": self.terminal_observation.body()}


@dataclass(frozen=True)
class LabelV1:
    terminal_evaluation: str
    episode_outcome: str

    def body(self) -> dict[str, str]:
        return dict(self.__dict__)


@dataclass(frozen=True)
class FieldProvenance:
    field_path: str
    phase: Phase
    source_ids: tuple[str, ...]
    derivation: str

    def body(self) -> dict[str, Any]:
        return {"field_path": self.field_path, "phase": self.phase.value,
                "source_ids": list(self.source_ids), "derivation": self.derivation}


@dataclass(frozen=True)
class ExperienceRecordV1:
    record_id: str
    schema_version: str
    extractor_version: str
    source_episode_closure_id: str
    pre_decision: PreDecisionV1
    post_decision: PostDecisionV1
    label: LabelV1
    provenance: tuple[FieldProvenance, ...]

    def body(self) -> dict[str, Any]:
        return {"schema_version": self.schema_version,
                "extractor_version": self.extractor_version,
                "source_episode_closure_id": self.source_episode_closure_id,
                "pre_decision": self.pre_decision.body(),
                "post_decision": self.post_decision.body(),
                "label": self.label.body(),
                "provenance": [item.body() for item in self.provenance]}


def _provenance(history: SealedEpisodeHistory, closure_id: str,
                membership_ids: tuple[str, ...], observation_id: str | None
                ) -> tuple[FieldProvenance, ...]:
    postcondition_id = history.postcondition.postcondition_id
    direct = "direct/v1"
    return (
        FieldProvenance("pre_decision.source_episode_id", Phase.PRE_DECISION,
                        (history.definition.episode_id,), direct),
        FieldProvenance("pre_decision.task_id", Phase.PRE_DECISION,
                        (history.task.task_id,), direct),
        FieldProvenance("pre_decision.episode_context_id", Phase.PRE_DECISION,
                        (history.context.context_id,), direct),
        FieldProvenance("pre_decision.postcondition_id", Phase.PRE_DECISION,
                        (postcondition_id,), direct),
        FieldProvenance("pre_decision.predicate", Phase.PRE_DECISION,
                        (postcondition_id,), direct),
        FieldProvenance("pre_decision.terminal_resource", Phase.PRE_DECISION,
                        (postcondition_id,), direct),
        FieldProvenance("pre_decision.evaluator_version", Phase.PRE_DECISION,
                        (postcondition_id,), direct),
        FieldProvenance("post_decision.membership_ids", Phase.POST_DECISION,
                        membership_ids, direct),
        FieldProvenance("post_decision.execution_count", Phase.POST_DECISION,
                        membership_ids, "membership-count/v1"),
        FieldProvenance("post_decision.terminal_observation", Phase.POST_DECISION,
                        ((observation_id,) if observation_id else
                         (history.definition.episode_id,)),
                        direct if observation_id else "missing-not-observed/v1"),
        FieldProvenance("label.terminal_evaluation", Phase.LABEL,
                        (closure_id, postcondition_id),
                        "exp083-terminal-evaluation/v1"),
        FieldProvenance("label.episode_outcome", Phase.LABEL,
                        (closure_id,), "exp083-outcome-map/v1"),
    )


def extract_experience(history: SealedEpisodeHistory, *, now: str,
                       schema_version: str = SCHEMA_VERSION,
                       extractor_version: str = EXTRACTOR_VERSION
                       ) -> ExperienceRecordV1:
    if schema_version != SCHEMA_VERSION or extractor_version != EXTRACTOR_VERSION:
        raise ValueError("unsupported experience schema or extractor version")
    episode = derive_episode(history, now=now)
    membership_ids = episode.membership_ids
    observation = (FactualValue(Missingness.VALUE, episode.observation_id)
                   if episode.observation_id else
                   FactualValue(Missingness.NOT_OBSERVED, None))
    pre = PreDecisionV1(history.definition.episode_id, history.task.task_id,
        history.context.context_id, history.postcondition.postcondition_id,
        history.postcondition.predicate.value, history.postcondition.resource,
        history.postcondition.evaluator_version)
    post = PostDecisionV1(membership_ids, len(membership_ids), observation)
    label = LabelV1(episode.evaluation.value, episode.outcome.value)
    value = ExperienceRecordV1("", schema_version, extractor_version,
        episode.closure_id, pre, post, label,
        _provenance(history, episode.closure_id, membership_ids,
                    episode.observation_id))
    return replace(value, record_id=_identity(value.body()))


def validate_experience_record(record: ExperienceRecordV1,
                               history: SealedEpisodeHistory, *, now: str) -> None:
    if record.record_id != _identity(record.body()):
        raise PermissionError("experience record integrity mismatch")
    expected = extract_experience(history, now=now)
    if canonical_json_bytes(record.body()) != canonical_json_bytes(expected.body()):
        raise PermissionError("experience record differs from sealed episode extraction")


class ColdExperienceExtractor:
    def __init__(self) -> None:
        self.live_call_count = 0

    def extract(self, history: SealedEpisodeHistory, *, now: str,
                stored_record: ExperienceRecordV1 | None = None) -> ExperienceRecordV1:
        del stored_record
        return extract_experience(history, now=now)


@dataclass(frozen=True)
class DatasetManifestV1:
    dataset_id: str
    dataset_schema_version: str
    experience_schema_version: str
    extractor_version: str
    ordered_record_ids: tuple[str, ...]

    def body(self) -> dict[str, Any]:
        return {"dataset_schema_version": self.dataset_schema_version,
                "experience_schema_version": self.experience_schema_version,
                "extractor_version": self.extractor_version,
                "ordered_record_ids": list(self.ordered_record_ids)}


def make_dataset_manifest(records: tuple[ExperienceRecordV1, ...], *,
                          sources: tuple[SealedEpisodeHistory, ...],
                          now: str) -> DatasetManifestV1:
    if not records or len(records) != len(sources):
        raise ValueError("dataset requires at least one experience record")
    source_by_episode = {item.definition.episode_id: item for item in sources}
    if len(source_by_episode) != len(sources):
        raise ValueError("duplicate dataset episode source")
    for record in records:
        if (record.schema_version != SCHEMA_VERSION
                or record.extractor_version != EXTRACTOR_VERSION
                or record.record_id != _identity(record.body())):
            raise ValueError("invalid experience record for dataset")
        source = source_by_episode.get(record.pre_decision.source_episode_id)
        if source is None:
            raise ValueError("experience record lacks exact episode source")
        validate_experience_record(record, source, now=now)
    identifiers = tuple(sorted(record.record_id for record in records))
    if len(identifiers) != len(set(identifiers)):
        raise ValueError("duplicate dataset record")
    value = DatasetManifestV1("", DATASET_SCHEMA_VERSION, SCHEMA_VERSION,
                              EXTRACTOR_VERSION, identifiers)
    return replace(value, dataset_id=_identity(value.body()))


def validate_dataset_manifest(manifest: DatasetManifestV1,
                              records: tuple[ExperienceRecordV1, ...], *,
                              sources: tuple[SealedEpisodeHistory, ...],
                              now: str) -> None:
    expected = make_dataset_manifest(records, sources=sources, now=now)
    if (manifest.dataset_id != _identity(manifest.body())
            or canonical_json_bytes(manifest.body())
            != canonical_json_bytes(expected.body())):
        raise PermissionError("dataset manifest differs from canonical membership")
