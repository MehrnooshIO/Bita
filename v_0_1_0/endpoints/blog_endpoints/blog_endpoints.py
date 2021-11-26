from fastapi import APIRouter

blog = APIRouter(
    tags=["blog"],
    prefix="/blog",
)


@blog.get("/")
def get_blog():
    return {"message": "List of Blog Posts"}