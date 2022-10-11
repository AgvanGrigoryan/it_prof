from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import answers

cancel_button: str


async def test_kb_case():
    # test_kb = ReplyKeyboardMarkup(resize_keyboard=True)

    q_a1_btn = KeyboardButton(answers.q_a1)
    q_a2_btn = KeyboardButton(answers.q_a2)
    q_a3_btn = KeyboardButton(answers.q_a3)
    q_a4_btn = KeyboardButton(answers.q_a4)
    q_a5_btn = KeyboardButton(answers.q_a5)
    cancel = KeyboardButton(cancel_button)
    test_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10, selective=True).row(q_a1_btn, q_a2_btn, q_a3_btn, q_a4_btn, q_a5_btn).add(cancel)

    return test_kb
