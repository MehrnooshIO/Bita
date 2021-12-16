from pydantic import BaseModel
from typing import List, Optional


class UserCreationSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str


class UserLoginSchema(BaseModel):
    email: str
    password: str    
