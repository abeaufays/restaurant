from fastapi import FastAPI
from restaurant.routers import items, users, events

app = FastAPI()

# Include routers
app.include_router(items.router)
app.include_router(users.router)
app.include_router(events.router)
