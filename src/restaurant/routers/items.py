from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from restaurant import database, schemas
from restaurant.repositories import items as items_repo

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/")
def list_items(
    item_repository: items_repo.ItemRepository = Depends(
        items_repo.get_item_repository
    ),
):
    """List all items."""
    items = item_repository.get_all()
    return {"items": items}


@router.post("/")
def create_item(
    item: schemas.Item,
    item_repository: items_repo.ItemRepository = Depends(
        items_repo.get_item_repository
    ),
    db: Session = Depends(database.get_db),
):
    """Create a new item."""
    db_item = item_repository.create(name=item.name, price=item.price)
    db.commit()
    db.refresh(db_item)
    return db_item
