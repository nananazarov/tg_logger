from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.database.models.base import Base


class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False, index=True, unique=True
    )
    api_key_id: Mapped[int] = mapped_column(ForeignKey("api_keys.id"), nullable=False, index=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.now(tz=timezone.utc), index=True
    )
