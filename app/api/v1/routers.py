from fastapi import APIRouter

from app.api.v1.endpoints import (
    subscription_router
)

router = APIRouter()

router.include_router(subscription_router, tags=["subscription"])
