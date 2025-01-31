import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from favorites.models import favorite
from favorites.schemas import FavoriteCreate
from sqlalchemy.sql import text
router = APIRouter(
    prefix="/favorite",
    tags=["Favorite"]
)


@router.get("/")
@cache(expire=30)
async def get_long_op(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(favorite)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.scalars().all(),
            "details": None
            
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })




