from sqlalchemy import Column, Integer, String
from restaurant.database import Base


class Item(Base):
    """Database table for items (meals, drinks, food)."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
