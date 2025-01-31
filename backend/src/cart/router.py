import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.models import User
from auth.base_config import current_user
from database import get_async_session
from cart.models import cart
from cart.schemas import CartCreate
from sqlalchemy.sql import text
router = APIRouter(
    prefix="/cart",
    tags=["Carts"]
)


@router.get("/")
async def get_long_op(session: AsyncSession = Depends(get_async_session)):
    try:
        result = await session.execute(text('SELECT * FROM cart'))
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
@router.get('/me')
async def get_cart(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    user_cart = await session.execute(select(cart).where(cart.c.user_id == user.id))
    print(user_cart.all())
    if user_cart.all():
        return user_cart.all()
    else:
        await session.execute(insert(cart).values(user_id=user.id,items={"mud": "black"}))
        return {"status": "succes"}
        
@router.post('/create')
async def create_cart(new_cart: CartCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(cart).values(**new_cart.dict())
    print(new_cart)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}





