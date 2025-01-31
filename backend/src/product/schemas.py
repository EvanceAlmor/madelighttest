

from pydantic import BaseModel


class ProductCreate(BaseModel):
    id: int
    title: str
    image_url: str
    price: int
    Category: str
    