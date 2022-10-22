from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from answers import question_ans_btns

answers_btns = []

async def test_inline_markup(question_number):
    test_kb = InlineKeyboardMarkup(resize_keyboard=True)
    answers_btns.clear()
    for question_answers in question_ans_btns[question_number]:
        if question_answers is not None:
            answers_btns.append(question_answers)
            test_kb.add(InlineKeyboardButton(question_answers, callback_data=question_answers))
    return test_kb
