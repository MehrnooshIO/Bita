from pydantic import BaseModel
from typing import List


class BlogPost(BaseModel):
    title: str
    author: str
    content: str
    preview: str
    tags: List[str]
    creation_date: str
    last_update_date: str
