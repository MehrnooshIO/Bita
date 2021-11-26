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


def test_create_blog_post():
    response = client.post("/blog/", json={
        "title": "Test Post",
        "author": "Test Author",
        "content": "Test Content",
        "preview": "Test Preview",
        "tags": ["test", "post"],
        "creation_date": "2020-01-01",
        "last_update_date": "2020-01-01" 
    })
    assert response.status_code == 201
    }