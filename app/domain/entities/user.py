from app.domain.entities.base import BaseEntity
from app.domain.entities.user_settings import UserSettingsEntity


class UserEntity(BaseEntity):
    id: int
    username: str
    telegram_id: int
    settings: "UserSettingsEntity"
