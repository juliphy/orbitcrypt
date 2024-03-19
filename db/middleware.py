from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from .crud import CRUD
from typing import Callable, Dict, Any, Awaitable
from .schemas import User

class DoesUserExistMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        user = User(event.from_user)
        if not await CRUD.does_exist(str(user.chatid)):
            await CRUD.add_user(user)
        result = await handler(event, data)
        return result
