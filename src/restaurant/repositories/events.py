from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.repositories import base


class EventRepository(base.BaseRepository[models.Event]):
    """Repository for Event model."""

    def __init__(self, db: Session):
        super().__init__(models.Event, db)


def get_event_repository(db: Session = Depends(database.get_db)) -> EventRepository:
    """Dependency to inject EventRepository."""
    return EventRepository(db)
