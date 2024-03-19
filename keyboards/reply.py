from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
class ReplyKeyboard:

    @staticmethod
    def main_menu():
        kb = [
            [KeyboardButton(text="Encrypt")],
            [KeyboardButton(text="Decrypt")]
        ]

        keyboard = ReplyKeyboardMarkup(
            keyboard=kb,
            resize_keyboard=True,
            input_field_placeholder="Выберите способ подачи"
        )

        return keyboard
