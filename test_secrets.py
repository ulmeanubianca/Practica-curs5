import os
from unittest.mock import patch
from fastapi.testclient import TestClient
from main_secrets import app, calculate_efficiency

client = TestClient(app)

@patch.dict(os.environ, {"USERNAME": "user_name"})
def test_calculate_efficiency_endpoint_with_username():
    response = client.post("/calculate_efficiency", json={
        "speed": 100,
        "downtime": 30,
        "quality_rate": 0.95,
        "utilization_rate": 0.85
    }, headers={"x-username": "user_name"})
    assert response.status_code == 200
    assert response.json() == {"efficiency": 4037.5}

@patch.dict(os.environ, {"USERNAME": "invalid_user_name"})
def test_calculate_efficiency_endpoint_with_invalid_username():
    response = client.post("/calculate_efficiency", json={
        "speed": 100,
        "downtime": 30,
        "quality_rate": 0.95,
        "utilization_rate": 0.85
    }, headers={"x-username": "user_name"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


    