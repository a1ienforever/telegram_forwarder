from app.domain.entities.channel import ChannelEntity
from app.interfaces.storage.mappers.base_mapper import BaseMapper
from app.interfaces.storage.models import Channel


class ChannelMapper(BaseMapper):
    @classmethod
    def from_entity(cls, entity: ChannelEntity) -> Channel:
        return Channel(
            id=entity.id,
            name=entity.name,
        )