import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../'))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_create_user():
    response = client.post('/users', json={
        'name': 'test_name',
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'test_password'
    })
    assert response.status_code == 201