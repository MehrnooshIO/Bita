from fastapi.security import OAuth2PasswordBearer
from v_0_1_0.core.models.models import sessionLocal


oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()