from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from restaurant import database, schemas
from restaurant.repositories import users as users_repo

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users(
    user_repository: users_repo.UserRepository = Depends(
        users_repo.get_user_repository
    ),
):
    """List all users."""
    users = user_repository.get_all()
    return {"users": users}


@router.post("/")
def create_user(
    user: schemas.User,
    user_repository: users_repo.UserRepository = Depends(
        users_repo.get_user_repository
    ),
    db: Session = Depends(database.get_db),
):
    """Create a new user."""
    """Create a new user."""
    user = user_repository.create(name=user.name, email=user.email)
    db.commit()
    return user
