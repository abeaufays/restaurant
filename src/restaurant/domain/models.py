from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    id: int
    name: str
    price: int


@dataclass
class User:
    id: int
    name: str
    email: str


@dataclass
class Event:
    id: int
    owner: User
    available_items: List[Item]
    participants: List[User]
