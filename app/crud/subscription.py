from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Subscription

from .base import CRUDBase


class CRUDSubscription(CRUDBase):
    async def get_subscriptions_by_id(self, session: AsyncSession):
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()


subscription_crud = CRUDSubscription(Subscription)
