from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/foo", params={"item_id": "1"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }

def test_create_item():
    response = client.post(
        "/items/",
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }