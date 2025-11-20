from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from restaurant import database, schemas
from restaurant.repositories import events as events_repo

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
def list_events(
    event_repository: events_repo.EventRepository = Depends(
        events_repo.get_event_repository
    ),
):
    """List all events."""
    events = event_repository.get_all()
    return {"events": events}


@router.post("/")
def create_event(
    event: schemas.Event,
    event_repository: events_repo.EventRepository = Depends(
        events_repo.get_event_repository
    ),
    db: Session = Depends(database.get_db),
):
    """Create a new event."""
    # Note: This is a placeholder - Event schema needs owner_id instead of owner object
    db_event = event_repository.create(owner_id=1)  # Temporary hardcoded owner_id
    db.commit()
    db.refresh(db_event)
    return db_event
