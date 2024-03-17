from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import DeclarativeBase
from models import Base
from settings import KeyTypeSettings

# строка подключения
sqlite_database = "sqlite:///metanit.db"
engine = create_engine(sqlite_database)
def init_db():

    Base.metadata.create_all(engine)
