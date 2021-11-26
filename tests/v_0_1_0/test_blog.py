from fastapi.testclient import TestClient
from main import site


client = TestClient(site)


def test_get_blog_root():
    response = client.get("/blog")
    assert response.status_code == 200
    