from datetime import datetime

from sqlalchemy import (
    Column, Date, Float, ForeignKey, Integer, String, Text
)
from sqlalchemy.orm import relationship

from app.core.constants import LENGTH_LIMITS_NAME_FIELDS
from app.core.db import Base


class Subscription(Base):
    """Модель подписок"""
    name = Column(String(LENGTH_LIMITS_NAME_FIELDS), nullable=False)
    description = Column(Text)
    monthly_price = Column(Float)
    semi_annual_price = Column(Float)
    annual_price = Column(Float)
    users = relationship("UserSubscription", back_populates="subscription")


class UserSubscription(Base):
    """Модель связи M2M"""
    __tablename__ = "user_subscription"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    subscription_id = Column(Integer, ForeignKey(
        "subscription.id"), primary_key=True)
    start_date = Column(Date, default=datetime.now)
    end_date = Column(Date)

    user = relationship("User", back_populates="subscriptions")
    subscription = relationship("Subscription", back_populates="users")
