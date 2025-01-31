from datetime import datetime
from typing import List
from pydantic import BaseModel
from cart.schemas import Item
class OrderCreate(BaseModel):
    Payment_method: str
    name:  str
    email: str
    description: str
    phoneNumber: str
    address: str
    items: List[Item]
    Order_status: int
