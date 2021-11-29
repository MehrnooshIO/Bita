from pydantic import BaseModel
from typing import List, Optional


class UserCreationSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str
