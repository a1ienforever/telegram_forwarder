from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.domain.entities.base import BaseEntity

T = TypeVar("T", bound=BaseEntity)  # Сущность, наследуемая от BaseEntity


class BaseRepositories(ABC, Generic[T]):
    @abstractmethod
    async def get_all(self, session) -> list[T]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int, session) -> T | None:
        pass

    @abstractmethod
    async def create(self, session, entity: BaseEntity) -> T:
        pass
