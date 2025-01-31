import time
import hashlib
from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.models import User
from auth.base_config import current_user
from database import get_async_session
from orders.models import order
from orders.schemas import OrderCreate
from sqlalchemy.sql import text
router = APIRouter(
    prefix="/orders",
    tags=["Order"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    return 1


@router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_user)):
    return {"message": f"Hello {user.email}!"}

def generate_key():
    # Берем текущее время и генерируем hash
    hash_object = hashlib.sha256(str(time.time()).encode())
    return str(hash_object.hexdigest()[:12])  # Обрезаем до 12 символов


@router.post("/")
async def add_specific_orders(new_order: OrderCreate, session: AsyncSession = Depends(get_async_session)):
    new_order = new_order.dict()
    new_order["Code"] = generate_key()
    new_order["price"] = sum(item['price']*item['quantity'] for item in new_order['items'])
    stmt = insert(order).values(**new_order)
    
    await session.execute(stmt)
    await session.commit()
    return new_order


@router.get("/{order_Code}")
async def get_specific_order(
        order_Code: str,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(order).where(order.c.Code == order_Code)
        result = await session.execute(query)
        
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })
# @router.get("/main")
# async def main(session: AsyncSession = Depends(get_async_session)):
#     titles = await session.execute(text('SELECT title  FROM product'))
#     price = await session.execute(text('SELECT price FROM product'))
#     image_urls = await session.execute(text('SELECT image_url  FROM product'))
#     priceList = price.scalars().all()
#     image_urlList = image_urls.scalars().all()
#     listResult = []
#     result = {
#     f'Info{i}':{
#         'id': i, 
#         'price': priceList[i], 
#         'image_url': image_urlList[i]
#     } for i in range(12)
# }
#     for i in range(len(result)):
#         listResult.append(result[f'Info{i}'])
#         print(listResult)

#     return listResult

