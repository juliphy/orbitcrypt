import asyncio
import logging
from config import config

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram import F

bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

async def main():
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
