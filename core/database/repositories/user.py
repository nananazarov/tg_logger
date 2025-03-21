from typing import Optional

from sqlalchemy import select

from core.database.models.user import User
from core.database.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    async def get_by_tg_user_id(self, tg_user_id: int) -> Optional[User]:
        query = select(User).filter(User.tg_user_id == tg_user_id).limit(1)
        result = await self.db.execute(query)
        user = result.scalars().first()
        if user is None:
            user = User(tg_user_id=tg_user_id)
            self.db.add(user)
            await self.db.flush()
        return user
