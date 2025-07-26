from app.domain.entities.base import BaseEntity
from app.domain.entities.channel import ChannelEntity
from app.domain.entities.user import UserEntity


class UserSettingsEntity(BaseEntity):
    id: int
    user: "UserEntity"
    channels: list[ChannelEntity]  # m2m
    is_sending: bool
