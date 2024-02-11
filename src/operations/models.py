from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey

from src.auth.models import user
from src.menu.models import status

metadata = MetaData()

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("owner_id", Integer), #ForeignKey(user.c.id)
    Column("status", String ), #ForeignKey(status.c.status_name)
    Column("price", Integer),
    Column("composition", String),
    Column("created_at", TIMESTAMP),
)

