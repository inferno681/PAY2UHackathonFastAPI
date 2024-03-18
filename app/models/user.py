from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_USER_FIELDS
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя"""

    created = Column(DateTime, default=datetime.now)
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    middle_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    phone_number = Column(Integer, nullable=False)
    card_number = relationship("card", back_populates="user")
    subscriptions = relationship("user_subscription", back_populates="user")
