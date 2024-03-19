import asyncio
import logging
from config import config

from aiogram import Bot, Dispatcher, types

from aiogram.filters import Command, CommandStart
from routers.encrypt import encrypt_router
from routers.start import start_router
from routers.decrypt import decrypt_router
from keyboards.reply import ReplyKeyboard
from bot import bot
from db.db import init_db
from db.crud import CRUD
from db.middleware import DoesUserExistMiddleware

dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
async def main():
    dp.include_routers(start_router,encrypt_router, decrypt_router)
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
