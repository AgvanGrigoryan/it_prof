from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang_button: str
cancel_button: str

async def settings_kb():
    # Lang Select kb
    lang = KeyboardButton(lang_button)
    cancel = KeyboardButton(cancel_button)
    settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    return settings_kb.add(lang).add(cancel)
