from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "DevOps Assessment API is running"
    }


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_hello():
    response = client.get("/hello/Sharanya")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, Sharanya!"
    }