from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_duplicate_signup_is_rejected():
    response = client.post(
        "/activities/Chess%20Club/signup?email=michael@mergington.edu"
    )

    assert response.status_code == 409
    assert "already signed up" in response.json()["detail"].lower()


def test_valid_signup_succeeds():
    response = client.post(
        "/activities/Chess%20Club/signup?email=newstudent@mergington.edu"
    )

    assert response.status_code == 200
    assert "newstudent@mergington.edu" in response.json()["message"]
