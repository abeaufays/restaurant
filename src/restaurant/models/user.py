from sqlalchemy import Column, Integer, String

from restaurant import database


class User(database.Base):
    """Database table for users (people or entities participating in events)."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
