from app.domain.entities.channel import ChannelEntity
from app.adapters.database.mappers.base_mapper import BaseMapper
from app.adapters.database.models import Channel


class ChannelMapper(BaseMapper):
    @classmethod
    def from_entity(cls, entity: ChannelEntity) -> Channel:
        return Channel(
            id=entity.id,
            name=entity.name,
        )
