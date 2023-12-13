from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_db = []

class Item(BaseModel):
    id: int
    name: str
    price: float

items = []

@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items", response_model=List[Item],status_code=200)
async def read_items():
    return items

@app.put("/items", response_model=Item, status_code=200)
async def update_item(item_id:int, item:Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
async def delete_items(item_id:int, item:Item):
    del items[item_id]
    return ("succesfully! Item delete")