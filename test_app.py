import pytest
import app

@pytest.fixture
def client():
    flask_app = app.app
    return flask_app.test_client()

def test_end_point(client):
    response_get = client.get("/")
    assert response_get.status_code == 200