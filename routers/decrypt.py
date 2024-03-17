from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from .states import BotStates
from .utils import Utilities

decrypt_router = Router(name="decrypt_router")


@decrypt_router.message(F.text.lower() == "Decrypt")
async def handle_decrypt(message: Message, state: FSMContext) -> None:
    await state.set_state(BotStates.WAITING_FOR_FILE_DECRYPTION)
    await message.answer("Send .encrypted file. Ensure, that the file was encrypted by Orbitcrypt.")


@decrypt_router.message(BotStates.WAITING_FOR_FILE_DECRYPTION, F.document)
async def handle_decrypt_key(message: Message, state: FSMContext) -> None:
    await state.set_state(BotStates.WAITING_FOR_KEY_DECRYPTION)
    await message.answer(f"Send {Utilities.bold_text(".key")} file")
