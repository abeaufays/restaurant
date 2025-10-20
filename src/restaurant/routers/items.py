from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from restaurant.schemas import Item
from restaurant.database import get_db
from restaurant import models

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items():
    """List all items."""
    return {"items": []}


@router.post("/")
def create_item(item: Item, db: Session = Depends(get_db)):
    """Create a new item."""
    db_item = models.Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
