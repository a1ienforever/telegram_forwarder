from abc import abstractmethod

from app.domain.entities.channel import ChannelEntity
from app.domain.interfaces.repositories.base_repo import BaseRepositories


class ChannelRepository(BaseRepositories):
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> list[ChannelEntity]: ...
