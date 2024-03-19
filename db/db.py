from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import DeclarativeBase
from .models import Base, KeyTypeSettings

# строка подключения
sqlite_database = "sqlite:///my.db"
engine = create_engine(sqlite_database)
async def init_db():

    Base.metadata.create_all(engine)
