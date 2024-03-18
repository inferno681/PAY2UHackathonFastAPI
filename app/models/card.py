from sqlalchemy import Column, ForeignKey, Integer

from app.core.db import Base


class Card(Base):
    """Модель банковских карт"""

    user_id = Column(Integer, ForeignKey("user.id"))
    card_number = Column(Integer, nullable=False)
