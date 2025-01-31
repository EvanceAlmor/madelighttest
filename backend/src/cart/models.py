from sqlalchemy import TIMESTAMP, Column, Integer, Table
from datetime import datetime
from database import metadata
from sqlalchemy.dialects.postgresql import JSONB
cart = Table(
    "cart",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, primary_key=True),
    Column("items", JSONB),
)