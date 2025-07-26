from app.domain.entities.user import UserEntity
from app.interfaces.storage.mappers.base_mapper import BaseMapper
from app.interfaces.storage.mappers.setting_mapper import SettingMapper
from app.interfaces.storage.models import User


class UserMapper(BaseMapper):
    @classmethod
    def to_entity(cls, model: User):
        return UserEntity(
            id=model.id,
            username=model.username,
            telegram_id=model.telegram_id,
            setting=SettingMapper.to_entity(model.setting),
        )

    @classmethod
    def from_entity(cls, entity: UserEntity):
        return User(
            id=entity.id, username=entity.username, telegram_id=entity.telegram_id, setting_id=entity.setting.id
        )
