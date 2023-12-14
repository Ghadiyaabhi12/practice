from fastapi import FastAPI 
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_db = []

class Item(BaseModel):
    id: int
    name: str
    price: float

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    fake_db.append(item)
    return item

@app.get("/items", response_model=List[Item],status_code=200)
def read_items():
    return fake_db

@app.put("/items", response_model=Item, status_code=200)
def update_item(item_id:int, item:Item):
    fake_db[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_items(item_id:int, item:Item):
    del fake_db[item_id]
    return ("succesfully! Item delete")