from aiogram import Dispatcher, types

from create_bot import bot
from keyboards.settings_case_kb import settings_kb
from keyboards.test_case_kb import test_kb_case
from result import test




settings_text: str
message_error: str
test_button: str
settings_button: str
language_button: str
test_started: str


# async def translate_other():
#     global sett_text, msg_err, sett_btn, test_started
#     sett_text = await ans_sett_text()
#     msg_err = await ans_msg_err()
#     sett_btn = await ans_sett_btn()
#     test_started = await ans_test_started()


# @dp.message_handler(Text(equals='✨ Test', ignore_case=True), state='*')
async def test_start(message: types.Message):
    test_kb = await test_kb_case()
    await bot.send_message(message.from_user.id, test_started, reply_markup=test_kb)
    await test(message, message.from_user.id)


# @dp.message_handler(Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
async def settings_open(message: types.Message):
    # 'Կարգավորումների բաժին՝'
    setting_kb = await settings_kb()
    await bot.send_message(message.from_user.id, settings_text, reply_markup=setting_kb)


# @dp.message_handler()
async def all_message(message: types.Message):
    # "⚠ Անհասկանալի հրաման ⚠"
    await message.reply(message_error)
    await message.delete()


def register_handlers_other(disp: Dispatcher):
    disp.register_message_handler(test_start, commands=['test'])
    disp.register_message_handler(test_start, lambda message: message.text == test_button)
    disp.register_message_handler(settings_open, lambda message: message.text == settings_button)
    disp.register_message_handler(settings_open, commands=['settings'])
    # todolizun poxel@ nastroykaneren chi ashxadi
    # disp.register_message_handler(lang_set, lambda message: message.text == language_button)
    # disp.register_message_handler(load_lang, state=FSMClient.lang)
    disp.register_message_handler(all_message)
