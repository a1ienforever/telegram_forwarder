from abc import abstractmethod
from typing import List, Optional

from app.domain.entities.user import UserEntity
from app.domain.repositories_interfaces.base_repo import BaseRepositories


class UserRepository(BaseRepositories):

    @abstractmethod
    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserEntity]:
        """Возвращает пользователя по Telegram ID."""
        ...

    @abstractmethod
    async def get_by_channel_id(self, channel_id: int) -> List[UserEntity]:
        """Возвращает пользователей канала по Channel ID."""
        ...
