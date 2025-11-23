from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.domain import models as domain_models


class UserRepository:
    """Repository for User model."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, email: str) -> domain_models.User:
        """Create a new user."""
        instance = models.User(name=name, email=email)
        self.db.add(instance)
        self.db.flush()
        return instance.to_domain()

    def get_by_id(self, id: int) -> Optional[domain_models.User]:
        """Get instance by ID."""
        instance = self.db.query(models.User).filter(models.User.id == id).first()
        if instance:
            return instance.to_domain()
        return None

    def get_all(self) -> List[domain_models.User]:
        """Get all instances."""
        instances = self.db.query(models.User).all()
        return [i.to_domain() for i in instances]


def get_user_repository(db: Session = Depends(database.get_db)) -> UserRepository:
    """Dependency to inject UserRepository."""
    return UserRepository(db)
