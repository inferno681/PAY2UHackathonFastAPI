from pydantic import BaseModel, PositiveInt


class CardRead(BaseModel):
    card_number: PositiveInt


class CardCreate(CardRead):
    pass


class CardUpdate(BaseModel):
    card_number: PositiveInt | None = None
