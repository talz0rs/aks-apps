from conftest import client


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_get_item():
    r = client.post("/items", json={"name": "sword", "description": "sharp"})
    assert r.status_code == 201
    item_id = r.json()["id"]

    r2 = client.get(f"/items/{item_id}")
    assert r2.status_code == 200
    assert r2.json()["name"] == "sword"
