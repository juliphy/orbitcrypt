from aiogram import Bot
from aiogram.enums import ParseMode

from config import config

bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
