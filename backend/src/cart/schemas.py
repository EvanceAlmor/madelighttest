from datetime import datetime
from typing import List
from pydantic import BaseModel, Json
from product.schemas import ProductCreate
class Item(BaseModel):
    id: int
    title: str
    image_url: str
    price: int
    quantity: int
    
class CartCreate(BaseModel):
    id: int
    user_id: int
    items: List[Item]  # Позволяем передавать произвольный JSON-объект

