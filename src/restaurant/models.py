from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from restaurant import database


# Association table for Event and Item (many-to-many)
event_items = Table(
    "event_items",
    database.Base.metadata,
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True),
)


# Association table for Event and User participants (many-to-many)
event_participants = Table(
    "event_participants",
    database.Base.metadata,
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)


class Item(database.Base):
    """Database table for items (meals, drinks, food)."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class User(database.Base):
    """Database table for users (people or entities participating in events)."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)


class Event(database.Base):
    """Database table for events with available items and participants."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    owner = relationship("User", foreign_keys=[owner_id])
    available_items = relationship("Item", secondary=event_items)
    participants = relationship("User", secondary=event_participants)
