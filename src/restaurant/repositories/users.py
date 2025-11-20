from fastapi import Depends
from sqlalchemy.orm import Session

from restaurant import database, models
from restaurant.repositories import base


class UserRepository(base.BaseRepository[models.User]):
    """Repository for User model."""

    def __init__(self, db: Session):
        super().__init__(models.User, db)


def get_user_repository(db: Session = Depends(database.get_db)) -> UserRepository:
    """Dependency to inject UserRepository."""
    return UserRepository(db)
