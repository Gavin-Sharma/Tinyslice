import pytest
import flask
import requests


def test_api_grocery_list():
    response = requests.get("http://localhost:5000/api/grocery_list")
    data = response.json()
    assert response.status_code == 200
    assert data[0]["name"] == "Apple"
