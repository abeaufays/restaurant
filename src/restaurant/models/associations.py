from sqlalchemy import Column, Integer, ForeignKey, Table

from restaurant import database


# Association table for Event and Item (many-to-many)
event_items = Table(
    "event_items",
    database.Base.metadata,
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
    Column("item_id", Integer, ForeignKey("items.id"), primary_key=True),
)


# Association table for Event and User participants (many-to-many)
event_participants = Table(
    "event_participants",
    database.Base.metadata,
    Column("event_id", Integer, ForeignKey("events.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)
