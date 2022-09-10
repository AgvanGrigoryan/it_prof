from aiogram import types
from create_bot import dp
from keyboards.client_kb import main_menu
from questions import *
from keyboards import questions_kb

prof = dict()
prof['a'] = 'Programmist'
prof['b'] = 'Testirovshik'
prof['c'] = 'Designer'
prof['d'] = 'Info Bezaposnost'
prof['e'] = 'Sis. admin'
prof['f'] = 'marketing'

prof_letter = dict()
prof['a'] = 0
prof['b'] = 0
prof['c'] = 0
prof['d'] = 0
prof['e'] = 0
prof['f'] = 0

i = 0

# not working
async def cancel():
    global i
    i = 0


async def test(message: types.Message):
    global i
    if i == len(question):
        res = await result()
        await message.reply(res, reply_markup=main_menu)
    else:
        await message.reply(text=f"{i + 1}/{len(question)}\n" + question[i], reply_markup=questions_kb.question_kb[i],)

    await message.delete()
    i += 1


async def result():
    return prof[max(prof_letter, key=prof_letter.get)]



async def count(cb):
    prof_letter[cb.data] +=1
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

