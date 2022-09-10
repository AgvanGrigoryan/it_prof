from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Lang Select kb
lang = KeyboardButton('Լեզու')
cancel = KeyboardButton('⬅ չեղարկել')
settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
settings_kb.add(lang).add(cancel)
