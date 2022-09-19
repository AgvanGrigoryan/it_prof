from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel_button: str


async def test_kb_case():
    cancel = KeyboardButton(cancel_button)
    test_kb = ReplyKeyboardMarkup(resize_keyboard=True)

    return test_kb.add(cancel)
