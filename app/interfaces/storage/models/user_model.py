from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.interfaces.storage.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)

    setting = relationship(
        'Setting',
        back_populates='user',
        uselist=False,
        lazy='selectin'
    )