from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import UserCreationSchema
from v_0_1_0.core.models import crud
from v_0_1_0.core.models.db import sessionLocal
from hashlib import sha256

#  Import Dependencies
from v_0_1_0.core.dependencies.depen import oath2_scheme, get_db


accounts = APIRouter(tags=["Accounts"], prefix="/accounts")


# TODO: #3 Change try - except block to cover more db failiour cases
@accounts.post("/register", status_code=201)
def create_account(user: UserCreationSchema, db: Session = Depends(get_db)):
    if crud.get_user_by_email_db(db, user.email):
        raise HTTPException(status_code=409, detail={"message": "Email already exists"})
    else:
        hashed_password = sha256(user.password.encode("utf-8")).hexdigest()
        user.password = hashed_password
        id = crud.create_user_db(db, user)
        return {"message": "User created sucsessfully", "id": id}


@accounts.get("/users")
def get_users(db: Session = Depends(get_db)):
    try:
        users_list = crud.get_users_db(db)
        return users_list
    except:
        pass


@accounts.get("/users/{user_id}")
def get_user_by_id(
    user_id: int, token: str = Depends(oath2_scheme), db: Session = Depends(get_db)
):
    try:
        user = crud.get_user_by_id_db(db, user_id)
        return user
    except:
        pass
