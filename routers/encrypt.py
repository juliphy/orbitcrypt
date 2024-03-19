import os

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, FSInputFile
from .states import BotStates
from bot import bot
from .utils import Utilities

encrypt_router = Router(name="encrypt_router")


@encrypt_router.message(F.text.lower() == "encrypt")
async def encrypt_handler(message: Message, state: FSMContext):
    await state.set_state(BotStates.WAITING_FOR_FILE_ENCRYPTION)

    await message.answer(f"Send file to encrypt. The file must be not more than {await Utilities.bold_text("20MB")}.\n\nFiles encrypted in Orbitcrypt can be decrypted only here.", reply_markup=ReplyKeyboardRemove()    )


@encrypt_router.message(BotStates.WAITING_FOR_FILE_ENCRYPTION, F.document)
async def encrypting_handler(message: Message, state: FSMContext):

    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await bot.download_file(file_path, message.document.file_name)
    encrypt_info = await Utilities.encrypt_file(message.document)

    file = FSInputFile(encrypt_info[0])
    key = FSInputFile(encrypt_info[1])
    await message.answer_document(file, caption=f"This is the encrypted file.\n\nEncrypted in @orbitcryptbot")
    await message.answer_document(key, caption=f"This is the key.\n\nUse to decrypt it in @orbitcryptbot")

    os.remove(encrypt_info[0])
    os.remove(encrypt_info[1])
