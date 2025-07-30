from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.database.models.base_model import BaseModel
from app.adapters.database.models.setting_model import setting_channel_association


class Channel(BaseModel):
    __tablename__ = "channels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    settings = relationship(
        "Setting", secondary=setting_channel_association, back_populates="channels", lazy="selectin"
    )
