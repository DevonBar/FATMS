from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

sample_data = {
    1: {"name": "Item One", "description": "This is item one."},
    2: {"name": "Item Two", "description": "This is item two."},
    3: {"name": "Item Three", "description": "This is item three."},
}

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI server!"}

@app.get("/items")
def read_all_items():
    return sample_data

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., description="The ID of the item to retrieve", gt=0, lt=100)):
    item = sample_data.get(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item