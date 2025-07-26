from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.interfaces.storage.models import BaseModel

setting_channel_association = Table(
    "setting_channel_association",
    BaseModel.metadata,
    Column("setting_id", ForeignKey("settings.id")),
    Column("channel_id", ForeignKey("channels.id")),
)


class Setting(BaseModel):
    from app.interfaces.storage.models import User
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(primary_key=True)
    is_sending: Mapped[bool] = mapped_column(default=True)

    user: Mapped[User] = relationship("User", back_populates="settings", uselist=False, lazy="selectin")

    channels = relationship(
        "Channel", secondary=setting_channel_association, back_populates="settings", lazy="selectin"
    )
