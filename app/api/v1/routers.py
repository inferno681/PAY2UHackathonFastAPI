from fastapi import APIRouter

from app.api.v1.endpoints import (
)

router = APIRouter()

router.include_router(some_router, tags=["some"])
