from typing import Union
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}
