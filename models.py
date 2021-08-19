from typing import List
from pydantic import BaseModel, Field


class Item(BaseModel):
    title: str
    description: str
    parameters: List[dict] = []

    class Config:
        schema_extra = {
            "example": {
                "title": "Iphone 13",
                "description": "cellphone Iphone",
                "parameters": [
                    {"model": "13"},
                    {"batery": "30000"},
                    {"os": "ios"},
                    {"date": "20.09.2021"}
                ]
            }
        }
        
def response_item(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }
