from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import bot, dp
from keyboards.questions_kb import *

from questions import *


# @dp.message_handler(Text(equals='✨ Test', ignore_case=True), state='*')
async def test_start(message: types.Message):
    await bot.send_message(message.from_user.id, question_1, reply_markup=question_1_kb)


# @dp.message_handler()
async def all_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(test_start, Text(equals='✨ Test', ignore_case=True), state="*")
    # dp.register_message_handler(all_message)

