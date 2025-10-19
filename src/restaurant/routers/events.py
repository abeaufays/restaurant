from fastapi import APIRouter
from restaurant.models import Event

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/")
def list_events():
    """List all events."""
    return {"events": []}


@router.post("/")
def create_event(event: Event):
    """Create a new event."""
    return event
