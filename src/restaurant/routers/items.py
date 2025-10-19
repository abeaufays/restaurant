from fastapi import APIRouter
from restaurant.models import Item

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    """List all items."""
    return {"items": []}


@router.post("/")
def create_item(item: Item):
    """Create a new item."""
    return item
