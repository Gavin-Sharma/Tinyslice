import pytest
import flask
import requests

#make sure app.py is running before running the test

@pytest.fixture
def app():
    from app import app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

def test_request_index(client):
    response = client.get("/")
    assert b"<h2>Click on the plus button below to create a new grocery list!!</h2>" in response.data

def test_request_contact(client):
    response = client.get("/contact")
    assert b"<h1 class=\"contact-hone\">Contact us</h1>" in response.data

def test_api_grocery_list(client):
    response = client.get("/api/grocery_list")
    assert response.json[0]["name"] == "Apple"
