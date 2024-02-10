from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_read_drivers():
    response = client.get("/?start_date=2021-01-01&end_date=2024-01-01")
    assert response.status_code == 200  # Expected status code for success
    assert response.json()["code"] == 0
    assert len(response.json()["records"]) > 0  # Ensure there are records returned
    response = client.get("/?start_date=2023-01-01&end_date=01-01-2024")
    assert response.status_code == 402  # Expected status code for incorrect date format
