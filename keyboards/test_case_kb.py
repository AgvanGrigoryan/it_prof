from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = KeyboardButton('⬅ չեղարկել')

test_kb = ReplyKeyboardMarkup(resize_keyboard=True)

test_kb.add(cancel)
