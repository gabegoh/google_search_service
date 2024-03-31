from sqlalchemy import MetaData, Table, Column, String, Integer, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
main_metadata: MetaData = MetaData()

google_searches_table: Table = Table(
    "google_searches",
    main_metadata,
    Column("search_id", String, primary_key=True, nullable=False),
    Column("search_term", String, nullable=False),
    Column("response", String, nullable=True),
    Column("status_code", Integer, nullable=False),
    Column("is_deleted", Boolean, nullable=False),
    Column("created_at", DateTime, nullable=False)
)