import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate
from sqlalchemy.sql import text
router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get("")
async def get_specific_operations(
        operation_type: str,
        session: AsyncSession = Depends(get_async_session),
):
    try:
        query = select(operation).where(operation.c.type == operation_type)
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


@router.post("")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/main")
async def main(session: AsyncSession = Depends(get_async_session)):
    titles = await session.execute(text('SELECT title  FROM product'))
    price = await session.execute(text('SELECT price FROM product'))
    image_urls = await session.execute(text('SELECT image_url  FROM product'))
    priceList = price.scalars().all()
    image_urlList = image_urls.scalars().all()
    listResult = []
    result = {
    f'Info{i}':{
        'id': i, 
        'price': priceList[i], 
        'image_url': image_urlList[i]
    } for i in range(12)
}
    for i in range(len(result)):
        listResult.append(result[f'Info{i}'])
        print(listResult)

    return listResult

