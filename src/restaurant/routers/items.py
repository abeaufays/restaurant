from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from restaurant import database, models, schemas

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items(db: Session = Depends(database.get_db)):
    """List all items."""
    items = db.query(models.Item).all()
    return {"items": items}


@router.post("/")
def create_item(item: schemas.Item, db: Session = Depends(database.get_db)):
    """Create a new item."""
    db_item = models.Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
