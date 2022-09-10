from aiogram import types
from create_bot import dp
from keyboards.client_kb import main_menu
from questions import *
from keyboards import questions_kb

score = 0
i = 0


async def cancel():
    global i, score
    print(i, score)
    i = 0
    score = 0
    print(i, score)


async def test(message: types.Message):
    global i, score

    if i == len(question):
        await message.reply(str(score), reply_markup=main_menu)
        i = 0
        score = 0
    else:
        await message.reply(text=f"{i + 1}/{len(question)}\n" + question[i], reply_markup=questions_kb.question_kb[i],)

    await message.delete()
    i += 1


async def count(cb):
    global score
    num = cb.data
    score += int(num)
    await test(cb.message)
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


@dp.callback_query_handler(text='0')
async def plus_one(callback: types.CallbackQuery):
    await count(callback)

