from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
import answers


# HINTS
# Programmer - a
# Tester - b
# Designer - c
# Information security specialist - d
# System administrator - e
# Marketer - f


# QUESTION KB
async def get_answers_kb():
    q_a1_btn = KeyboardButton(answers.q_a1, callback_data='a')
    q_a2_btn = KeyboardButton(answers.q_a2, callback_data='b')
    q_a3_btn = KeyboardButton(answers.q_a3, callback_data='c')
    q_a4_btn = KeyboardButton(answers.q_a4, callback_data='d')
    q_a5_btn = KeyboardButton(answers.q_a5, callback_data='e')
    question_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10).row(q_a1_btn, q_a2_btn, q_a3_btn, q_a4_btn, q_a5_btn)
    return question_kb
