from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey, Boolean

metadata = MetaData()


status = Table(
    "status",
    metadata,
    Column("status_name", String, primary_key=True)
)


menu = Table(
    "menu",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("actuality", Boolean, default=True, nullable=False),
    Column("price", Integer, nullable=False),
    Column("title", String, nullable=False)
)
