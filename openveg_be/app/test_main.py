from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_welcome():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the OpenVeg API!"}
