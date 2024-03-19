from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.exceptions import Error403Schema, ErrorSchema
from app.crud import subscription_crud
from app.schemas import SubscriptionRead

router = APIRouter()


@router.get(
    '/subscriptions',
    tags=['subscription'],
    responses={
        200: {'model': list[SubscriptionRead]},
        401: {'model': ErrorSchema},
        403: {'model': Error403Schema},
    },
)
async def get_subscriptions(
    session: AsyncSession = Depends(get_async_session),
):
    data = await subscription_crud.get_multi(session=session)
    return data
