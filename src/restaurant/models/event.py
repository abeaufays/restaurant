from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from restaurant import database
from restaurant.models import associations


class Event(database.Base):
    """Database table for events with available items and participants."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    owner = relationship("User", foreign_keys=[owner_id])
    available_items = relationship("Item", secondary=associations.event_items)
    participants = relationship("User", secondary=associations.event_participants)
