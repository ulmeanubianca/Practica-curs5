import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def test_client():
    return TestClient(app)

# Exercise: Write Parameterized Tests for FastAPI Endpoint
@pytest.mark.parametrize("speed, downtime, quality_rate, utilization_rate, expected", [
    (100, 30, 0.80, 0.90, 3600),
    (300, 30, 0.80, 0.80, 9600),
    (150, 15, 0.90, 0.90, 9112.5),
])
def test_calculate_efficiency_endpoint_parametrized(test_client, speed, downtime, quality_rate, utilization_rate, expected):
    response = test_client.post("/calculate_efficiency", json={
        "speed": speed,
        "downtime": downtime,
        "quality_rate": quality_rate,
        "utilization_rate": utilization_rate
    })
    assert response.status_code == 200
    assert response.json() == {"efficiency": expected}
