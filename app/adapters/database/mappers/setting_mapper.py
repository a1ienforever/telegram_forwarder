from app.domain.entities.user_settings import UserSettingsEntity
from app.adapters.database.mappers.base_mapper import BaseMapper
from app.adapters.database.mappers.channel_mapper import ChannelMapper
from app.adapters.database.models import Setting


class SettingMapper(BaseMapper):
    @classmethod
    def to_entity(cls, model: Setting) -> UserSettingsEntity:
        return UserSettingsEntity(
            id=model.id,
            user=model.user,
            channels=ChannelMapper.to_entity(model.channels),
            is_sending=model.is_sending,
        )
