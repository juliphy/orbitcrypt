from sqlalchemy import Column, Integer, Enum, String
from sqlalchemy.orm import DeclarativeBase

from .settings import StoreTypeSettings
from routers.file import KeyType as KeyTypeSettings

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    chat_id = Column(String, index=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    language_code = Column(String)

    key_type = Column('key_type', Enum(KeyTypeSettings))
    store_type = Column('store_type', Enum(StoreTypeSettings))