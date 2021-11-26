from pydantic import BaseModel
from typing import List, Optional


class PostSchema(BaseModel):
    title: str
    author: str
    content: str
    preview: str
    tags: Optional[List[str]] = None
    created_at: str
    last_updated_at: str
