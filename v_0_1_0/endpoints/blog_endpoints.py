import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))

from fastapi import APIRouter, HTTPException
from v_0_1_0.core.schemas.post_schema import PostSchema
from typing import List


blog = APIRouter(
    tags=["Blog"],
    prefix="/blog",
)


@blog.get("/", response_model=List[PostSchema])
def get_blog():
    return {"message": "List of Blog Posts"}


@blog.post("/", response_model=PostSchema, status_code=201)
def create_post(post: PostSchema):
    try:
        return post
    except Exception as e:
        raise HTTPException(
            status_code=424,
            detail={"message": "Unable to create the post",
                    "error": str(e)})
