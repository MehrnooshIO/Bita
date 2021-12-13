from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import UserCreationSchema
from v_0_1_0.core.models.models import User
from typing import List


def create_user_db(db: Session, user: UserCreationSchema) -> int:
    """
    Create new user in database and return the id of that new record
    """
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.id


def get_users_db(db:Session) -> List[User]:
    """
    Retrive list of registered useres from database
    """
    return db.query(User).all()


def get_user_by_id_db(db:Session, user_id: int) -> User:
    """
    Retrive user from database by id
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email_db(db:Session, email: str) -> User:
    """
    Retrive user from database by email
    """
    return db.query(User).filter(User.email == email).first()