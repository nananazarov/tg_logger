from datetime import datetime, timezone

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.models.api_key import ApiKey
from core.database.models.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False, index=True, unique=True
    )
    tg_user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, unique=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(tz=timezone.utc), index=True
    )
    api_keys: Mapped[list["ApiKey"]] = relationship(back_populates="user")
