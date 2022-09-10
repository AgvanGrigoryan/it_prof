from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


from create_bot import bot
from handlers.client import action_cancel
from keyboards import settings_case_kb, test_case_kb, client_kb
from language import ans_sett_text, ans_msg_err

from select_lang import lang_set, load_lang, FSMClient
from result import *


async def test_cancel(message: types.Message):
    types.ReplyKeyboardRemove()
    await bot.send_message("Գլխավոր մենյու՝", reply_markup=client_kb.main_menu)
    await cancel()


# @dp.message_handler(Text(equals='✨ Test', ignore_case=True), state='*')
async def test_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Թեստը սկսված է՝', reply_markup=test_case_kb.test_kb)
    await test(message)


# @dp.message_handler(Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
async def settings_open(message: types.Message):
    sett_text = await ans_sett_text()
    # 'Կարգավորումների բաժին՝'
    await bot.send_message(message.from_user.id, sett_text, reply_markup=settings_case_kb.settings_kb)


# @dp.message_handler()
async def all_message(message: types.Message):
    msg_err = await ans_msg_err()
    # "⚠ Անհասկանալի հրաման ⚠"
    await message.reply(msg_err)
    await message.delete()


def register_handlers_other(disp: Dispatcher):
    dp.register_message_handler(test_start, commands=['test'])
    disp.register_message_handler(test_start, Text(equals='✨ Թեստ', ignore_case=True), state="*")
    disp.register_message_handler(settings_open, Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
    dp.register_message_handler(settings_open, commands=['settings'])
    disp.register_message_handler(lang_set, Text(equals='Լեզու', ignore_case=True), state='*')
    disp.register_message_handler(load_lang, state=FSMClient.lang)
    dp.register_message_handler(test_cancel, lambda message: message.text == "⬅ չեղարկել")
    disp.register_message_handler(all_message)
