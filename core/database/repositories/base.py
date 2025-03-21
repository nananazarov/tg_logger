from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    model_cls: Type[ModelType]

    def __init__(self, db: AsyncSession):
        self.db = db
