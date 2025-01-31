from datetime import datetime

from pydantic import BaseModel


class FavoriteCreate(BaseModel):
    id: int
    user_id: int
    product_id: int

