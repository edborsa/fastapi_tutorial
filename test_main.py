from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_route():
    response = client.get("/")
    assert response.status_code == 200

    message = response.json()["message"]

    assert message == "Hello World"
