from typing import Generic, TypeVar, Type, Optional, List
from sqlalchemy.orm import Session

from restaurant import database

ModelType = TypeVar("ModelType", bound=database.Base)


class BaseRepository(Generic[ModelType]):
    """Base repository providing common CRUD operations."""

    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def create(self, **kwargs) -> ModelType:
        """Create a new instance."""
        instance = self.model(**kwargs)
        self.db.add(instance)
        return instance

    def get_by_id(self, id: int) -> Optional[ModelType]:
        """Get instance by ID."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> List[ModelType]:
        """Get all instances."""
        return self.db.query(self.model).all()

    def delete(self, id: int) -> bool:
        """Delete instance by ID. Returns True if deleted, False if not found."""
        instance = self.get_by_id(id)
        if instance:
            self.db.delete(instance)
            return True
        return False
