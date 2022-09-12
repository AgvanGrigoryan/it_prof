from aiogram import types
from create_bot import dp, bot
from keyboards.client_kb import main_menu
from questions import *
from keyboards import questions_kb

callback_values = ['a', 'b', 'c', 'd', 'e', 'f', 'abde', 'abcdef']

profession = dict()
profession['a'] = 'Programmist'
profession['b'] = 'Testirovshik'
profession['c'] = 'Designer'
profession['d'] = 'Info Bezaposnost'
profession['e'] = 'Sis. admin'
profession['f'] = 'marketing'

prof_letter = dict()
prof_letter['a'] = 0
prof_letter['b'] = 0
prof_letter['c'] = 0
prof_letter['d'] = 0
prof_letter['e'] = 0
prof_letter['f'] = 0

i = 0


# not working
async def cancel():
    global i
    i = 0


async def test(message: types.Message):
    # message = callback.data
    global i
    if i == len(question):
        i = 0
        await message.answer('Թեստը ավարտված է։', reply_markup=main_menu)
        res = await result()
        await show_results(res, message)
    else:
        await message.answer(text=f"{i + 1}/{len(question)}\n" + question[i], reply_markup=questions_kb.question_kb[i])
        i += 1
    await message.delete()


async def result():
    letter = prof_letter[max(prof_letter, key=prof_letter.get)]
    results = []
    for let in prof_letter:
        if prof_letter[let] == letter:
            results.append(profession[let])
    return results


async def show_results(res, message: types.Message):
    for prof in res:
        await message.answer(prof)


async def count(cb):
    for letter in list(cb.data):
        prof_letter[letter] += 1
    await test(cb.message)
    await cb.answer()


@dp.callback_query_handler(text=callback_values)
async def get_callback(callback: types.CallbackQuery):
    await count(callback)


@dp.callback_query_handler(text='pass')
async def get_pass_callback(callback: types.CallbackQuery):
    await test(callback.message)
    await callback.answer()


# @dp.callback_query_handler(text='4')
# async def plus_four(callback: types.CallbackQuery):
#     await count(callback)
#
#
# @dp.callback_query_handler(text='3')
# async def plus_three(callback: types.CallbackQuery):
#     await count(callback)
#     return callback.inline_message_id
#
#
# @dp.callback_query_handler(text='2')
# async def plus_two(callback: types.CallbackQuery):
#     await count(callback)
#
#
# @dp.callback_query_handler(text='1')
# async def plus_one(callback: types.CallbackQuery):
#     await count(callback)
#
#
# @dp.callback_query_handler(text='0')
# async def plus_one(callback: types.CallbackQuery):
#     await count(callback)
