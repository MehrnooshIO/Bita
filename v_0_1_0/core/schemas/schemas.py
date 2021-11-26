from pydantic import BaseModel
from typing import List, Optional


class PostSchema(BaseModel):
    title: str
    author: str
    content: str
    preview: str
    tags: Optional[List[str]] = None
    creation_date: str
    last_update_date: str
