from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from restaurant import database, models, schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users(db: Session = Depends(database.get_db)):
    """List all users."""
    users = db.query(models.User).all()
    return {"users": users}


@router.post("/")
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    """Create a new user."""
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
