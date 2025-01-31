from sqlalchemy import TIMESTAMP, Column, Integer, Table
from datetime import datetime
from database import metadata

favorite = Table(
    "favorite",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("product_id", Integer),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)