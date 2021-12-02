import os
import sys
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))


from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import UserCreationSchema
from v_0_1_0.core.models.user_model import User


# Create new user
def create_user_db(db: Session, user: UserCreationSchema):
    """
    Create new user in database and return the id of that new record
    """
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.id


def get_users_db(db:Session):
    """
    Retrive list of registered useres from database
    """
    return db.query(User).all()
