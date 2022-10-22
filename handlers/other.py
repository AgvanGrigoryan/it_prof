from aiogram import Dispatcher, types

from answers import question_ans_btns
from create_bot import bot
from keyboards.settings_case_kb import settings_kb
from keyboards.test_inline_kb import test_inline_markup, answers_btns
from keyboards.test_reply_kb import test_reply_markup
from result import test, get_test_reply_callback, users, User_test

settings_text: str
message_error: str
test_button: str
settings_button: str
test_started: str


# async def translate_other():
#     global sett_text, msg_err, sett_btn, test_started
#     sett_text = await ans_sett_text()
#     msg_err = await ans_msg_err()
#     sett_btn = await ans_sett_btn()
#     test_started = await ans_test_started()


# @dp.message_handler(Text(equals='✨ Test', ignore_case=True), state='*')
async def test_start(message: types.Message):
    test_reply_kb_case = await test_reply_markup()
    if users.__contains__(message.from_user.id):
        users[message.from_user.id].reset()
    else:
        users[message.from_user.id] = User_test(message.from_user.id)

    await bot.send_message(message.from_user.id, test_started, reply_markup=test_reply_kb_case)
    await test(message, message.from_user.id)



# @dp.message_handler(Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
async def settings_open(message: types.Message):
    # 'Կարգավորումների բաժին՝'
    setting_kb = await settings_kb()
    await bot.send_message(message.from_user.id, settings_text, reply_markup=setting_kb)

# async def test_reply(message: types.Message):
     # await bot.send_message(message.from_user.id, "Test is complete")
#     await count(message)



# @dp.message_handler()
async def all_message(message: types.Message):
    # "⚠ Անհասկանալի հրաման ⚠"
    await message.reply(message_error)
    await message.delete()

# test_answers = ['yes', 'almostYes', 'i don\'t know', 'almost no', 'no']
def register_handlers_other(disp: Dispatcher):
    disp.register_message_handler(test_start, commands=['test'])
    disp.register_message_handler(test_start, lambda message: message.text == test_button)
    disp.register_message_handler(settings_open, lambda message: message.text == settings_button)
    disp.register_message_handler(settings_open, commands=['settings'])
    # disp.register_message_handler(test_reply, lambda message: message.text == answers_btns[0])
    # disp.register_message_handler(test_reply, lambda message: message.text == answers_btns[1])
    # disp.register_message_handler(test_reply, lambda message: message.text == answers_btns[2])
    # disp.register_message_handler(test_reply, lambda message: message.text == answers_btns[3])
    # disp.register_message_handler(test_reply, lambda message: message.text == answers_btns[4])

    # disp.register_message_handler(lang_set, lambda message: message.text == language_button)
    # disp.register_message_handler(load_lang, state=FSMClient.lang)
    # disp.register_message_handler(all_message)
