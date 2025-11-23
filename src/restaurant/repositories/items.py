from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.domain import models as domain_models


class ItemRepository:
    """Repository for Item model."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, price: int) -> domain_models.Item:
        """Create a new item."""
        instance = models.Item(name=name, price=price)
        self.db.add(instance)
        self.db.flush()
        return instance.to_domain()

    def get_by_id(self, id: int) -> Optional[domain_models.Item]:
        """Get instance by ID."""
        instance = self.db.query(models.Item).filter(models.Item.id == id).first()
        if instance:
            return instance.to_domain()
        return None

    def get_all(self) -> List[domain_models.Item]:
        """Get all instances."""
        instances = self.db.query(models.Item).all()
        return [i.to_domain() for i in instances]


def get_item_repository(db: Session = Depends(database.get_db)) -> ItemRepository:
    """Dependency to inject ItemRepository."""
    return ItemRepository(db)
