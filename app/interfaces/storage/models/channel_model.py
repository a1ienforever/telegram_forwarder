from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from app.interfaces.storage.models.base_model import BaseModel
from app.interfaces.storage.models.setting_model import setting_channel_association


class Channel(BaseModel):
    __tablename__ = 'channels'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    settings = relationship(
        'Setting',
        secondary=setting_channel_association,
        back_populates='channels',
        lazy='selectin'

    )