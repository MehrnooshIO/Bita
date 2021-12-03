from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from v_0_1_0.core.schemas.user_schema import UserCreationSchema
from v_0_1_0.core.models import crud
from v_0_1_0.core.models.db import sessionLocal


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


@accounts.get("/users")
def get_users(db: Session = Depends(get_db)):
    try:
        users_list = crud.get_users_db(db)
        return users_list
    except:
        pass


@accounts.get("/users/{user_id}")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_id_db(db, user_id)
        return user
    except:
        pass