from fastapi.testclient import TestClient
from main import app
from typing import List
from v_0_1_0.core.models.user_model import User

client = TestClient(app)

def test_create_user():
    response = client.post('/accounts/register', json={
        'name': 'test_name',
        'username': 'test_user',
        'email': 'test@example.com',
        'password': 'test_password'
    })
    assert response.status_code == 201
    assert response.json().get('id') is not None


def test_get_users():
    response = client.get('/accounts/users')
    assert isinstance(response.json(), List)
