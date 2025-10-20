from fastapi import APIRouter

from restaurant import schemas

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
def list_events():
    """List all events."""
    return {"events": []}


@router.post("/")
def create_event(event: schemas.Event):
    """Create a new event."""
    return event
