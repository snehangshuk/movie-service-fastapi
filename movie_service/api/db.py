from sqlalchemy import (Column, Integer, String, Table,
                        create_engine, JSON)
from sqlalchemy.sql.schema import MetaData
from databases import Database

DATABASE_URL = "sqlite:///./movie_db"
database = Database(DATABASE_URL)

metadata = MetaData()
movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', JSON),
    Column('casts', JSON)
)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
