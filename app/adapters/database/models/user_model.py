from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.database.models import BaseModel


class User(BaseModel):
    from app.adapters.database.models import Setting

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    setting_id: Mapped[int] = mapped_column(ForeignKey("settings.id"), unique=True, nullable=True)

    setting: Mapped[Setting] = relationship("Setting", back_populates="user", lazy="selectin", uselist=False)
