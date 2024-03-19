from db.settings import StoreTypeSettings
from routers.file import KeyType as KeyTypeSettings
from aiogram.types import User


class User:
    chatid: str
    name: str
    username: str
    language_code: str

    key_type: KeyTypeSettings
    store_type: StoreTypeSettings

    def __init__(self, aiogram_user: User):
        self.key_type = KeyTypeSettings.FILEKEY
        self.store_type = StoreTypeSettings.SEPERATE

        self.chatid = str(aiogram_user.id)
        self.name = aiogram_user.first_name if aiogram_user.last_name is None else aiogram_user.first_name + aiogram_user.last_name
        self.username = aiogram_user.username
        self.language_code = aiogram_user.language_code
