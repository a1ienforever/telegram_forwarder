from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.interfaces.storage.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    setting_id: Mapped[int] = mapped_column(ForeignKey("settings.id"), unique=True, nullable=True)

    setting: Mapped["Setting"] = relationship(
        "Setting",
        back_populates="user",
        lazy="selectin",
        uselist=False
    )
