import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))

from fastapi import APIRouter, HTTPException
from v_0_1_0.core.schemas.user_schema import UserCreationSchema

accounts = APIRouter(
    prefix="/accounts"
)


@accounts.get("/register")
def create_user_form():
    pass


@accounts.post("/register", status_code=201)
def create_account(user: UserCreationSchema):
    try:
        return user
    except Exception as e:
        raise HTTPException(
            status_code=424,
            detail={
                "message": "Could not create account",
                "error": str(e)
            }
        )