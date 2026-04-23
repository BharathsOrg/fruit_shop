import uuid
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import engine
from src.models.fruit import Fruit
from sqlalchemy import inspect

client = TestClient(app)

def test_health_endpoint():
    """
    Test the /health endpoint to ensure it returns the correct status.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Fruit Shop API is healthy"}

def test_root_endpoint():
    """
    Test the root endpoint / to ensure the basic app structure is working.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Fruit Shop API" in response.json()["message"]

def test_get_all_fruits():
    """
    E2E Test: Verify that the GET /api/v1/fruits endpoint returns the seeded data.
    """
    response = client.get("/api/v1/fruits")
    assert response.status_code == 200
    data = response.json()
    
    # Verify we have the seeded fruits
    names = [fruit["name"] for fruit in data]
    assert "Apple" in names
    assert "Banana" in names
    assert "Dragonfruit" in names
    assert len(data) >= 3

def test_create_fruit_e2e():
    """
    E2E Test: Verify the POST /api/v1/fruits endpoint creates a new fruit.
    Uses a UUID to ensure name uniqueness and avoid 400 errors.
    """
    unique_name = f"Unique_Fruit_{uuid.uuid4()}"
    new_fruit = {
        "name": unique_name,
        "description": "A tropical juicy fruit",
        "price": 2.5,
        "stock": 50
    }
    # POST
    post_response = client.post("/api/v1/fruits", json=new_fruit)
    assert post_response.status_code == 201
    assert post_response.json()["name"] == unique_name
    
    # GET to verify
    get_response = client.get("/api/v1/fruits")
    assert get_response.status_code == 200
    names = [fruit["name"] for fruit in get_response.json()]
    assert unique_name in names

def teardown_module(module):
    """
    Cleanup after all tests in the module have run.
    Deletes all entries in the fruit table to ensure a clean state.
    """
    with engine.connect() as connection:
        connection.execute(Fruit.__table__.delete())
        connection.commit()

def test_get_single_fruit():
    """
    E2E Test: Verify retrieving a single fruit by ID.
    Uses a UUID to ensure name uniqueness.
    """
    unique_name = f"Cherry_E2E_{uuid.uuid4()}"
    # First, create the fruit
    post_response = client.post("/api/v1/fruits", json={
        "name": unique_name,
        "description": "Small red fruit",
        "price": 3.0,
        "stock": 10
    })
    assert post_response.status_code == 201
    fruit_id = post_response.json()["id"]
    
    # GET single
    get_response = client.get(f"/api/v1/fruits/{fruit_id}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == unique_name
