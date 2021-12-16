from hashlib import sha256
from jose import jwt
import os
from datetime import datetime, timedelta

secret_key = os.environ.get("SECRET_KEY")


def hash_password(password: str):
    return sha256(password.encode("utf-8")).hexdigest()


def check_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password


def generate_token(payload: dict) -> str:
    payload.update({"exp": datetime.utcnow() + timedelta(minutes=15)})
    return jwt.encode(payload, secret_key, algorithm="HS256")


def decode_token(token: str) -> dict:
    return jwt.decode(token, secret_key, algorithms=["HS256"])    
