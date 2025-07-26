from typing import TypeVar

from app.interfaces.storage.models import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseMapper:
    @classmethod
    def to_entity(cls, model):
        raise NotImplementedError

    @classmethod
    def from_entity(cls, entity):
        raise NotImplementedError

    @classmethod
    def to_entity_list(cls, models: list[T]) -> list[T]:
        return [cls.to_entity(model) for model in models]

    @classmethod
    def from_entity_list(cls, entities: list[T]) -> list[T]:
        return [cls.from_entity(entity) for entity in entities]
