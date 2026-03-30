from unittest.mock import patch
from fastapi.testclient import TestClient
from main_mock import app, calculate_efficiency

client = TestClient(app)

@patch('main_mock.get_downtime', return_value=5)
def test_calculate_efficiency_with_mock(mock_get_downtime):
    # Test case 1
    mock_get_downtime.return_value = 5
    speed = 100
    quality_rate = 0.95
    utilization_rate = 0.85
    expected_efficiency = (speed * (1 - (mock_get_downtime.return_value / 60.0)) * quality_rate * utilization_rate) * 100
    assert calculate_efficiency(speed, quality_rate, utilization_rate) == expected_efficiency
    mock_get_downtime.assert_called_once()

    # Test case 2
    mock_get_downtime.return_value = 30
    speed = 100
    quality_rate = 0.90
    utilization_rate = 0.80
    expected_efficiency = 3600
    assert calculate_efficiency(speed, quality_rate, utilization_rate) == expected_efficiency
    assert mock_get_downtime.call_count == 2
