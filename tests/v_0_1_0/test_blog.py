import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))

from fastapi.testclient import TestClient
from main import site

client = TestClient(site)


def test_get_blog_root():
    response = client.get("/blog/")
    assert response.status_code == 200
    assert response.json() == {"message": "List of Blog Posts"}