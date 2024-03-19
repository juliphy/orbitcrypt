from sqlalchemy.orm import sessionmaker

from .db import engine
from db.schemas import User as UserSchema
from db.models import User as UserModel

session = sessionmaker(autoflush=False, bind=engine)

class CRUD:

    @staticmethod
    async def does_exist(chatid: str) -> bool:
        with session(autoflush=False, bind=engine) as db:
            user = db.query(UserModel).filter(UserModel.chat_id == chatid).first()

        return user is not None


    @staticmethod
    async def add_user(user: UserSchema) -> None:
        print(f"Adding user: {user}")
        user = UserModel(chat_id = user.chatid,
                         name = user.name,
                         username = user.username,
                         language_code = user.language_code,
                         key_type = user.key_type,
                         store_type = user.store_type)

        with session(autoflush=False, bind=engine) as db:
            db.add(user)
            db.commit()