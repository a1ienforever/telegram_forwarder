from app.domain.entities.base import BaseEntity


class ChannelEntity(BaseEntity):
    channel_id: int
    channel_name: str
