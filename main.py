from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId

from fastapi.encoders import jsonable_encoder
from models import Item, response_item
from db import create_i, item_id, items_parameters

app = FastAPI(title='Item application')


@app.get('/item/{item_id}')
async def get_item(item_id: str):
    return item_id(item_id)

@app.get('/items/')
async def get_items(request: Request):
    return items_parameters(dict(request.query_params))

# создать новую
@app.post('/item')
async def add_item(item: Item):
    new_item = create_i(jsonable_encoder(item))
    return response_item(new_item, 'New item inserted into DB')

