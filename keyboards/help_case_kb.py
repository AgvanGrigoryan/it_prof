from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_button: str


async def help_kb_case():
    cancel = KeyboardButton(cancel_button)
    help_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10, selective=True).add(cancel)

    return help_kb
