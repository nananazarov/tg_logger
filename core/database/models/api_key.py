from datetime import datetime, timezone

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
import secrets

from core.database.models.base import Base


class ApiKey(Base):
    __tablename__ = "api_keys"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False, index=True, unique=True
    )
    chat_id: Mapped[int] = mapped_column(BigInteger, nullable=False, index=True, unique=True)
    key: Mapped[str] = mapped_column(
        nullable=False, index=True, unique=True, default=secrets.token_urlsafe(32)
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(tz=timezone.utc), index=True
    )
