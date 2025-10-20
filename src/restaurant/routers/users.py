from fastapi import APIRouter

from restaurant import schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users():
    """List all users."""
    return {"users": []}


@router.post("/")
def create_user(user: schemas.User):
    """Create a new user."""
    return user
