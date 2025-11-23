from sqlalchemy import Column, Integer, String

from restaurant import database


class User(database.Base):
    """Database table for users (people or entities participating in events)."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)

    def to_domain(self) -> "domain_models.User":
        from restaurant.domain import models as domain_models

        return domain_models.User(id=self.id, name=self.name, email=self.email)
