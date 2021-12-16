from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import (
    UserCreationSchema,
    UserLoginSchema,
)
from v_0_1_0.core.models import crud
from v_0_1_0.core.utilities.utilities import (
    hash_password,
    check_password,
    generate_token,
)

#  Import Dependencies
from v_0_1_0.core.dependencies.depen import oath2_scheme, get_db


accounts = APIRouter(tags=["Accounts"], prefix="/accounts")


@accounts.post("/register", status_code=201)
def create_account(user: UserCreationSchema, db: Session = Depends(get_db)):
    if crud.get_user_by_email_db(db, user.email):
        raise HTTPException(status_code=409, detail={"message": "Email already exists"})
    else:
        user.password = hash_password(user.password)
        id = crud.create_user_db(db, user)
        return {"message": "User created sucsessfully", "id": id}


@accounts.post("/token", status_code=200)
def login_account(user: UserLoginSchema, db: Session = Depends(get_db)):
    user_in_db = crud.get_user_by_email_db(db, user.email)
    if not user_in_db:
        raise HTTPException(status_code=404, detail={"message": "User not found"})
    if not check_password(user.password):
        raise HTTPException(status_code=401, detail={"message": "Incorrect password"})
    return {"access_token": generate_token({"email": user.email})}


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
