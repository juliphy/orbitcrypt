from aiogram import Router, types
from aiogram.filters import Command

from db.crud import CRUD
from db.middleware import DoesUserExistMiddleware
from keyboards.reply import ReplyKeyboard

start_router = Router()
start_router.message.outer_middleware(DoesUserExistMiddleware())

@start_router.message(Command("start"))
async def start(message: types.Message):
    if await CRUD.does_exist(str(message.from_user.id)) is False:
        await CRUD.add_user(message.from_user)

    await message.answer("Hello! Here you can encrypt and decrypt your files.", reply_markup=ReplyKeyboard.main_menu())
