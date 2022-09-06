from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# QUESTION KB
q1_a1 = InlineKeyboardButton("Red", callback_data='1')
q1_a2 = InlineKeyboardButton("Blue", callback_data='0')
question_1_kb = InlineKeyboardMarkup().add(q1_a1).add(q1_a2)
