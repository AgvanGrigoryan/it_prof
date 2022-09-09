from aiogram import types
from create_bot import dp, bot
from keyboards.client_kb import main_menu
from questions import *
from keyboards import questions_kb

score = 0


async def test(message: types.Message):
    # await bot.send_message(message.from_user.id, question[0], reply_markup=questions_kb.question_kb[0])
    for i in question:
        await bot.send_message(message.from_user.id, i)
        # poxel darcnel tvov cikl ev avelacnel keyboard


async def count(cb):
    global score
    num = cb.data
    score += int(num)
    await next_question(cb.message, cb)
    await bot.send_message(cb.from_user.id, score, reply_markup=main_menu)
    await cb.answer()


@dp.callback_query_handler(text='5')
async def plus_five(callback: types.CallbackQuery):
    await count(callback)


@dp.callback_query_handler(text='4')
async def plus_four(callback: types.CallbackQuery):
    await count(callback)


@dp.callback_query_handler(text='3')
async def plus_three(callback: types.CallbackQuery):
    await count(callback)
    return callback.inline_message_id


@dp.callback_query_handler(text='2')
async def plus_two(callback: types.CallbackQuery):
    await count(callback)


@dp.callback_query_handler(text='1')
async def plus_one(callback: types.CallbackQuery):
    await count(callback)


async def next_question(msg: types.Message, callback: types.CallbackQuery):
    await bot.edit_message_text(text=question_2, chat_id=msg.chat.id, message_id=msg.message_id, inline_message_id=callback.inline_message_id, reply_markup=questions_kb.question_2_kb)

