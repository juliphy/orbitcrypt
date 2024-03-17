

class Utilities:
    @staticmethod
    def encrypt_file():
        pass

    @staticmethod
    def decrypt_file():
        pass

    @staticmethod
    def encode_to_hex(string: str) -> str:
        return string.encode("utf-8").hex()

    @staticmethod
    def decode_from_hex(string: str) -> str:
        return bytes.fromhex(string).decode("utf-8")

    @staticmethod
    def bold_text(string: str, parse_mode: str = "HTML"):
        match parse_mode:
            case "HTML":
                return "<b>" + string + "</b>"
            case "Markdown":
                return "**" + string + "**"

        raise ValueError("Invalid parse_mode")

    @staticmethod
    def italic_text(string: str, parse_mode: str = "HTML"):
        match parse_mode:
            case "HTML":
                return "<i>" + string + "</i>"
            case "Markdown":
                return "*" + string + "*"

        raise ValueError("Invalid parse_mode")
