import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import UserCreationSchema
from v_0_1_0.core.models import crud
from v_0_1_0.core.models.db import Base, sessionLocal, engine


Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


accounts = APIRouter(
    prefix="/accounts"
)


@accounts.get("/register")
def create_user_form():
    pass


# TODO: #3 Change try - except block to cover more db failiour cases
@accounts.post("/register", status_code=201)
def create_account(user: UserCreationSchema, db: Session=Depends(get_db)):
    try:
        id = crud.create_user_db(db, user)
        return {"id": id}
    except Exception as e:
        raise HTTPException(
            status_code=424,
            detail={
                "message": "Could not create account",
                "error": str(e)
            }
        )