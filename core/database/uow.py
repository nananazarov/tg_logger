from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database.repositories.user import UserRepository


class UnitOfWork:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.user = UserRepository(self.db)

    async def commit(self) -> None:
        await self.db.commit()

    async def rollback(self) -> None:
        await self.db.rollback()


@asynccontextmanager
async def get_uow(db: AsyncSession) -> AsyncIterator[UnitOfWork]:
    uow = UnitOfWork(db)
    try:
        yield uow
        await uow.commit()
    except Exception:
        await uow.rollback()
        raise
