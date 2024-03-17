from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .states import BotStates

encrypt_router = Router(name="encrypt_router")

@encrypt_router.message(F.text.lower() == "encrypt")
async def encrypt_handler(message: Message, state: FSMContext):
    await state.set_state(BotStates.WAITING_FOR_FILE_ENCRYPTION)

    await message.answer("Send file to encrypt")


