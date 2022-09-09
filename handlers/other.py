from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

import result
from create_bot import bot, dp
from keyboards import questions_kb, settings_case_kb, client_kb

from questions import *
from select_lang import lang_set, load_lang, FSMClient, FSMContext
from result import *

from language import ans_sett_text


# @dp.message_handler(Text(equals='✨ Test', ignore_case=True), state='*')
async def test_start(message: types.Message):
    await result.test(message)
    # await bot.send_message(message.from_user.id, question_1, reply_markup=questions_kb.question_1_kb)


# @dp.message_handler(Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
async def settings_open(message: types.Message):
    # sett_text = await ans_sett_text()
    await bot.send_message(message.from_user.id, 'Կարգավորումների բաժին՝', reply_markup=settings_case_kb.settings_kb)


# @dp.message_handler()
async def all_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(test_start, Text(equals='✨ Թեստ', ignore_case=True), state="*")
    dp.register_message_handler(settings_open, Text(equals='⚙ Կարգավորումներ', ignore_case=True), state='*')
    dp.register_message_handler(lang_set, Text(equals='Լեզու', ignore_case=True), state='*')
    dp.register_message_handler(load_lang, state=FSMClient.lang)
    # dp.register_message_handler(all_message)

