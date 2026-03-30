from fastapi.testclient import TestClient
from main import app, calculate_efficiency

client = TestClient(app)

def test_calculate_efficiency():
    assert calculate_efficiency(100, 30, 0.95, 0.85) == 4037.5

def test_calculate_efficiency_endpoint():
    response = client.post("/calculate_efficiency", json={
        "speed": 100,
        "downtime": 30,
        "quality_rate": 0.95,
        "utilization_rate": 0.85
    })
    assert response.status_code == 200
    assert response.json() == {"efficiency": 4037.5}

def test_invalid_quality_rate():
    response = client.post("/calculate_efficiency", json={
        "speed": 100,
        "downtime": 10,
        "quality_rate": 1.5,
        "utilization_rate": 0.85
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Quality rate and utilization rate must be between 0 and 1"}

def test_negative_speed():
    response = client.post("/calculate_efficiency", json={
        "speed": -100,
        "downtime": 10,
        "quality_rate": 0.95,
        "utilization_rate": 0.85
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "Speed and downtime must be non-negative"}
