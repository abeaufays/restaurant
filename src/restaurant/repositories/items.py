from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.repositories import base


class ItemRepository(base.BaseRepository[models.Item]):
    """Repository for Item model."""

    def __init__(self, db: Session):
        super().__init__(models.Item, db)


def get_item_repository(db: Session = Depends(database.get_db)) -> ItemRepository:
    """Dependency to inject ItemRepository."""
    return ItemRepository(db)
