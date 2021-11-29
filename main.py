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
