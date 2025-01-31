from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from database import metadata
status = Table(
    "status",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("description", String, nullable=False),
)
order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True ),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("name", String),
    Column("email", String),
    Column("Payment_method", String),
    Column("description", String),
    Column("phoneNumber", String),
    Column('address', String),
    Column("items", JSONB),
    Column("Order_status", Integer, ForeignKey(status.c.id)),
    Column("Code", String),
    Column("price", Integer)
)