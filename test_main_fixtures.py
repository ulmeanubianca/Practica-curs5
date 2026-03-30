import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Fixture to set up the test client
@pytest.fixture
def test_client():
    return TestClient(app)

# Fixture to provide sample data
@pytest.fixture
def sample_data():
    return {
        "speed": 100,
        "downtime": 30,
        "quality_rate": 0.95,
        "utilization_rate": 0.85
    }

# Exercise: Write a Test with Fixtures for FastAPI Endpoint
def test_calculate_efficiency_with_fixtures(test_client, sample_data):
    response = test_client.post("/calculate_efficiency", json=sample_data)
    assert response.status_code == 200
    expected_efficiency = 4037.5
    assert response.json() == {"efficiency": expected_efficiency}

def test_invalid_quality_rate_with_fixtures(test_client, sample_data):
    sample_data["quality_rate"] = 1.5
    response = test_client.post("/calculate_efficiency", json=sample_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Quality rate and utilization rate must be between 0 and 1"}

def test_negative_speed_with_fixtures(test_client, sample_data):
    sample_data["speed"] = -100
    response = test_client.post("/calculate_efficiency", json=sample_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Speed and downtime must be non-negative"}
