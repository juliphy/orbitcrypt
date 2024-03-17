from aiogram.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    MAIN_MENU = State()

    WAITING_FOR_FILE_ENCRYPTION = State()
    # Decryption states.
    WAITING_FOR_FILE_DECRYPTION = State()
    WAITING_FOR_KEY_DECRYPTION = State()



