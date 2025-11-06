from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    """Test the main root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to the GenTales00 API!"
    assert data["version"] == "1.0.0"
    assert data["docs"] == "/docs"

def test_read_api_root():
    """Test the API router root endpoint"""
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the GenTales API"}

def test_read_item():
    """Test getting an item with ID"""
    response = client.get("/api/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query": None}

def test_read_item_with_query():
    """Test getting an item with ID and query parameter"""
    response = client.get("/api/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query": "test"}

def test_read_item_string_id():
    """Test that string IDs return validation error"""
    response = client.get("/api/items/invalid")
    assert response.status_code == 422  # Validation error