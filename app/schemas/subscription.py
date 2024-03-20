from pydantic import BaseModel, PositiveInt


class SubscriptionRead(BaseModel):
    id: PositiveInt
    name: str
    description: str
    monthly_price: float
    semi_annual_price: float
    annual_price: float


class SubscriptionShort(BaseModel):
    id: PositiveInt
    name: str
    description: str
