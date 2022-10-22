from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import answers


# HINTS
# Programmer - a
# Tester - b
# Designer - c
# Information security specialist - d
# System administrator - e
# Marketer - f

cancel_button: str

# QUESTION KB
async def test_reply_markup():
    cancel = KeyboardButton(cancel_button)
    reply_test_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(cancel)
    return reply_test_markup
