from fastapi import FastAPI
from v_0_1_0.endpoints.blog_endpoints import blog
from v_0_1_0.endpoints.accounts_endpoints import accounts

app = FastAPI(
    title="Bita Creative Solutions",
    description="Bring Your Ideas In To Codes",
    version="0.1.0",
)

app.include_router(blog)
app.include_router(accounts)


# @app.on_event("startup")
# async def startup():
#     import os
#     import sys

#     PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))