from aiogram.types import Document
from cryptography.fernet import Fernet
import os

class Utilities:

    @staticmethod
    def generate_fernet_key() -> bytes:
        return Fernet.generate_key()
    @staticmethod
    async def encrypt_file(document: Document):
        key = Utilities.generate_fernet_key()
        fernet = Fernet(key)
        key_path = await Utilities.write_key(key, document)

        with open(f'{document.file_name}', "rb") as file:
            original = file.read()

        file.close()
        os.remove(f'{document.file_name}')
        encrypted = fernet.encrypt(original)
        with open(f'{document.file_name}.orbit', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        encrypted_file.close()

        return [document.file_name + '.orbit', document.file_name + ".key"]

    @staticmethod
    async def write_key(key: bytes, document: Document):
        key_path = f'{document.file_name}.key'
        with open(key_path, "wb") as file:
            file.write(key)

        file.close()

        return key_path


    @staticmethod
    async def decrypt_file():
        pass

    @staticmethod
    async def encode_to_hex(string: str) -> str:
        return string.encode("utf-8").hex()

    @staticmethod
    async def decode_from_hex(string: str) -> str:
        return bytes.fromhex(string).decode("utf-8")

    @staticmethod
    async def bold_text(string: str, parse_mode: str = "HTML") -> str:
        match parse_mode:
            case "HTML":
                return "<b>" + string + "</b>"
            case "Markdown":
                return "**" + string + "**"

        raise ValueError("Invalid parse_mode")

    @staticmethod
    async def italic_text(string: str, parse_mode: str = "HTML") -> str:
        match parse_mode:
            case "HTML":
                return "<i>" + string + "</i>"
            case "Markdown":
                return "*" + string + "*"

        raise ValueError("Invalid parse_mode")
