import pytest
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

from app.database import Base, engine
import models
import crud
import schemas

# Initialize FastAPI app and test client
app = FastAPI()
client = TestClient(app)

# Set up and tear down functions for tests
@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # Connect to in-memory SQLite database
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    # Create test data
    user = models.User(username="testuser", email="test@example.com", hashed_password="password123")
    db.add(user)
    db.commit()
    db.refresh(user)

    post = models.Post(title="Test Post", content="This is a test post.", owner_id=user.id)
    db.add(post)
    db.commit()
    db.refresh(post)

    yield db

    db.close()

# Define tests for each endpoint
def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_create_user():
    new_user = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "newpassword"
    }
    response = client.post("/users/", json=new_user)
    assert response.status_code == 200
    assert response.json()["username"] == "newuser"

def test_read_post():
    response = client.get("/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"
    assert response.json()["content"] == "This is a test post."

def test_create_post():
    new_post = {
        "title": "New Post",
        "content": "This is a new post."
    }
    response = client.post("/posts/", json=new_post)
    assert response.status_code == 200
    assert response.json()["title"] == "New Post"

def test_update_post():
    updated_post = {
        "title": "Updated Post",
        "content": "This post has been updated."
    }
    response = client.put("/posts/1", json=updated_post)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Post"

def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Post"  # Assuming the delete endpoint returns the deleted post

def test_read_comments():
    response = client.get("/comments/")
    assert response.status_code == 200
    assert len(response.json()) == 0  # Assuming no comments in test setup

# Run tests with pytest
if __name__ == "__main__":
    pytest.main()
