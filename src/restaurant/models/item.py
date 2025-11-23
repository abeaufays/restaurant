from sqlalchemy import Column, Integer, String

from restaurant import database


class Item(database.Base):
    """Database table for items (meals, drinks, food)."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    def to_domain(self) -> "domain_models.Item":
        from restaurant.domain import models as domain_models

        return domain_models.Item(id=self.id, name=self.name, price=self.price)
