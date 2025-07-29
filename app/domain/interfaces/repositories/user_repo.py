from abc import abstractmethod

from app.domain.entities.user import UserEntity
from app.domain.interfaces.repositories.base_repo import BaseRepositories


class UserRepository(BaseRepositories):
    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: int) -> UserEntity | None:
        """Возвращает пользователя по Telegram ID."""
        ...

    @abstractmethod
    async def get_by_channel_id(self, channel_id: int) -> list[UserEntity]:
        """Возвращает пользователей канала по Channel ID."""
        ...
