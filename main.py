from fastapi import FastAPI
from v_0_1_0.endpoints.blog_endpoints.blog_endpoints import blog

app = FastAPI(
    title="Bita Creative Solutions",
    description="Bring Your Ideas In To Codes",
    version="0.1.0",
)

app.include_router(blog)
