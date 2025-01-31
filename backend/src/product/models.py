
from sqlalchemy import TIMESTAMP,Column, ForeignKey,Integer,String,Table
from database import metadata
sizes = Table(
    'sizes',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('size', String )
)
colors = Table(
    'colors',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('col', String )
)
image_urls = Table(
    'image_urls',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('url', String, unique=True) 
)
category = Table(
    'category',
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=True),
)
product = Table(
    "product",
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String),
    Column('image_url', String),
    Column('price', Integer),
    Column('Category', Integer, ForeignKey(category.c.id)),
    Column('Image_urls', String, ForeignKey(image_urls.c.url)),
    Column('Color', String, ForeignKey(colors.c.col)),
    Column('size', String, ForeignKey(sizes.c.size))
)
