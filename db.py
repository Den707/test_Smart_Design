from bson import ObjectId
from pymongo import MongoClient
from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel, Field

client = MongoClient('localhost', 27017)
db = client['item_base']
collection = db['item_collection']

def item_help(item) -> dict:
    return {
        'id': str(item['_id']),
        'title': str(item['title']),
        'description': str(item['description']),
        'parameters': item['parameters'],
    }

def create_i(item_data: dict) -> dict:
    item = collection.insert_one(item_data)
    new_item = collection.find_one({'_id': item.inserted_id})
    return item_help(new_item)

def item_id(id: str) -> dict:
    if ObjectId.is_valid(id):
        item = collection.find_one({'_id': ObjectId(id)})
        return item_help(item)
    else:
        return {'error': 'not valid id'}

def items_parameters(params: dict):
    items = []
    query = {}

    for p in params:
        if p in ['title', 'description']:
            query[p] = {'$regex': params[p]}
        else:
            query['parameters.' + p] = params[p]

    for item in collection.find(query, {"title": 1, "_id": 0}):
        items.append(item)
    return items
