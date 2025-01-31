import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from auth.base_config import current_user
from database import get_async_session
from product.models import product
from product.schemas import ProductCreate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("/")
async def sort( session: AsyncSession = Depends(get_async_session)):
    listResult = await session.execute(text('SELECT * FROM product'))


    return listResult.all() 

@router.get("/main/{product_id}")
async def get_specific_products(
        product_id: int,
        session: AsyncSession = Depends(get_async_session),
):
        titles = await session.execute(text('SELECT title  FROM product'))
        price = await session.execute(text('SELECT price FROM product'))
        image_urls = await session.execute(text('SELECT image_url  FROM product'))
        priceList = price.scalars().all()
        image_urlList = image_urls.scalars().all()
        title_List = titles.scalars().all()
        listResult = []
        data = {
            f'Info{i}':{
                'id': i+1, 
                'price': priceList[i], 
                'imageUrl': image_urlList[i],
                'title': title_List[i] ,
                } for i in range(12)
            }
        for i in range(len(data)):
            listResult.append(data[f'Info{i}'])

        return listResult[int(product_id)-1],
     


# @router.post("")
# # async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
# #     stmt = insert(operation).values(**new_operation.dict())
# #     await session.execute(stmt)
# #     await session.commit()
# #     return {"status": "success"}


# @router.get("/main")
# async def main(session: AsyncSession = Depends(get_async_session)):
#     titles = await session.execute(text('SELECT title  FROM product'))
#     price = await session.execute(text('SELECT price FROM product'))
#     image_urls = await session.execute(text('SELECT image_url  FROM product'))
#     titleList = titles.scalars().all()
#     priceList = price.scalars().all()
#     image_urlList = image_urls.scalars().all()
#     listResult = []
#     result = {
#     f'Info{i}':{
#         'id': i+1, 
#         'title': titleList[i],
#         'price': priceList[i], 
#         'imageUrl': image_urlList[i]
#     } for i in range(12)
# }
#     for i in range(len(result)):
#         listResult.append(result[f'Info{i}'])
      

#     return listResult

@router.get("/main")
async def sort(session: AsyncSession = Depends(get_async_session)):
    # print(sortBy)
    # titles = await session.execute(text('SELECT title  FROM product'))
    # price = await session.execute(text('SELECT price FROM product'))
    # image_urls = await session.execute(text('SELECT image_url  FROM product'))
    # titleList = titles.scalars().all()
    # priceList = price.scalars().all()
    # image_urlList = image_urls.scalars().all()
    # listResult = []
    # data = {
    # f'Info{i}':{
    #     'id': i+1, 
    #     'title': titleList[i],
    #     'price': priceList[i], 
    #     'imageUrl': image_urlList[i]
    # } for i in range(12)
    # }

    # for i in range(len(data)):
    #     listResult.append(data[f'Info{i}'])
  return await session.execute(text('SELECT * FROM product'))
       
