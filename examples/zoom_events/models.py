import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import JSON

metadata = sqlalchemy.MetaData()

zoom_event_table = sqlalchemy.Table(
    "zoom_event",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("event", sqlalchemy.String(120), index=True),
    sqlalchemy.Column("payload", JSON),
    sqlalchemy.Column("event_ts", sqlalchemy.BigInteger),
)