from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.domain import models as domain_models


class EventRepository:
    """Repository for Event model."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, owner_id: int) -> domain_models.Event:
        """Create a new event."""
        instance = models.Event(owner_id=owner_id)
        self.db.add(instance)
        self.db.flush()
        return instance.to_domain()

    def get_by_id(self, id: int) -> Optional[domain_models.Event]:
        """Get instance by ID."""
        instance = self.db.query(models.Event).filter(models.Event.id == id).first()
        if instance:
            return instance.to_domain()
        return None

    def get_all(self) -> List[domain_models.Event]:
        """Get all instances."""
        instances = self.db.query(models.Event).all()
        return [i.to_domain() for i in instances]


def get_event_repository(db: Session = Depends(database.get_db)) -> EventRepository:
    """Dependency to inject EventRepository."""
    return EventRepository(db)
