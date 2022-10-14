from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from answers import question_ans_btns

cancel_button: str
answers_btns = []

async def test_kb_case(question_number):
    test_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    answers_btns.clear()
    for question_answers in question_ans_btns[question_number]:
        if question_answers is not None:
            answers_btns.append(question_answers)
            test_kb.add(KeyboardButton(question_answers))
    cancel = KeyboardButton(cancel_button)
    return test_kb.add(cancel)
