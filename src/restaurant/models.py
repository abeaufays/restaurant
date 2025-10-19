from pydantic import BaseModel, EmailStr
from typing import List


class Item(BaseModel):
    """Represent a meal, drink or any piece of food available at the restaurant."""

    name: str
    price: int


class User(BaseModel):
    """Represent a person or entity that can participate in restaurant events."""

    name: str
    email: EmailStr


class Event(BaseModel):
    """Represent an event where multiple users participate with available items."""

    available_items: List[Item]
    participants: List[User]
    owner: User
