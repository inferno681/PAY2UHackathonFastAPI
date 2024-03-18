from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Column, Date, DateTime, Float, ForeignKey, Integer, String, Text
)
from sqlalchemy.orm import relationship

from app.core.constants import (
    LENGTH_LIMITS_NAME_FIELDS,
    LENGTH_LIMITS_USER_FIELDS,
)
from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    """Модель пользователя"""

    created = Column(DateTime, default=datetime.now)
    first_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    last_name = Column(String(LENGTH_LIMITS_USER_FIELDS), nullable=False)
    middle_name = Column(String(LENGTH_LIMITS_USER_FIELDS))
    phone_number = Column(Integer, nullable=False)
    card_number = relationship("card_number", back_populates="user")
    subscriptions = relationship("user_subscription", back_populates="user")


class CardNumber(Base):
    """Модель банковских карт"""

    user_id = Column(Integer, ForeignKey("user.id"))
    card_number = Column(Integer, nullable=False)


class Subscription(Base):
    """Модель подписок"""
    name = Column(String(LENGTH_LIMITS_NAME_FIELDS), nullable=False)
    description = Column(Text)
    monthly_price = Column(Float)
    semi_annual_price = Column(Float)
    annual_price = Column(Float)
    users = relationship("user_subscription", back_populates="subscription")


class UserSubscription(Base):
    """Модель связи M2M"""
    __tablename__ = "user_subscription"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    subscription_id = Column(Integer, ForeignKey(
        "subscription.id"), primary_key=True)
    start_date = Column(Date, default=datetime.now)
    end_date = Column(Date)

    user = relationship("user", back_populates="subscriptions")
    subscription = relationship("subscription", back_populates="users")
