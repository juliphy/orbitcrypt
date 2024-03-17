from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import DeclarativeBase

from settings import KeyTypeSettings, StoreTypeSettings

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chat_id = Column(Integer, index=True, nullable=False, unique=True)

    key_type = Column('value', Enum(KeyTypeSettings))
    store_type = Column('value', Enum(StoreTypeSettings))