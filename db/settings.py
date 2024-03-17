from enum import Enum

from routers.file import KeyType


class KeyTypeSettings(KeyType):
    pass

class StoreTypeSettings(Enum):
    INZIP = "inzip"
    SEPERATE = "seperate"
