from fastapi_users.schemas import BaseUser, BaseUserCreate
from pydantic import BaseModel, PositiveInt

from app.models.user import UserRole


class UserRead(BaseUser[int]):
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserShort(BaseModel):
    id: PositiveInt
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserCreate(BaseUserCreate):
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
