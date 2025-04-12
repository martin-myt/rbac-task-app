from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.main import app
from app.models.user import User
from app.schemas.user import UserCreate


client = TestClient(app)


def test_create_user(db: Session):
    user_data = {
        "email": "test@example.com",
        "auth0_id": "auth0|test",
        "role": "user"
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["role"] == user_data["role"]


def test_get_users(db: Session):
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_user(db: Session):
    # First create a user
    user_data = {
        "email": "test2@example.com",
        "auth0_id": "auth0|test2",
        "role": "user"
    }
    create_response = client.post("/api/v1/users/", json=user_data)
    assert create_response.status_code == 200
    user_id = create_response.json()["id"]

    # Then get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["role"] == user_data["role"] 