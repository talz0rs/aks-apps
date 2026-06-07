from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory item store
items: dict[int, dict] = {}
next_id = 1


# Request/response schemas
class ItemCreate(BaseModel):
    name: str
    description: str | None = None


class ItemResponse(ItemCreate):
    id: int


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, "name": item.name, "description": item.description}
    items[next_id] = new_item
    next_id += 1
    return new_item


@app.get("/items", response_model=list[ItemResponse])
def list_items():
    return list(items.values())


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = {"id": item_id, "name": item.name, "description": item.description}
    items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
