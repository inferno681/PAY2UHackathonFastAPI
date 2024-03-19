from fastapi_users.schemas import BaseUser, BaseUserCreate
from pydantic import BaseModel, PositiveInt


class UserRead(BaseUser[int]):
    id: PositiveInt
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
