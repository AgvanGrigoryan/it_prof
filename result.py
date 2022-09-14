from aiogram import types
from create_bot import dp
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

test_users = dict()
us_id = 0


async def cancel(message: types.Message):
    global test_users
    if message.from_user.id in test_users.keys():
        test_users[message.from_user.id] = 0


async def test(message: types.Message, user_id=0):
    global test_users, us_id
    if us_id != user_id and user_id not in test_users.keys():
        us_id = user_id
        test_users[us_id] = 0

    if user_id in test_users.keys():
        i = test_users[user_id]
        if i == len(question):
            await message.answer('Թեստը ավարտված է։', reply_markup=main_menu)
            test_users[user_id] = 0
            res = await result()
            await show_results(res, message)
        else:
            await message.answer(text=f"{i + 1}/{len(question)}\n" + question[i], reply_markup=questions_kb.question_kb[i])
            test_users[user_id] += 1
        await message.delete()


async def result():
    letter = prof_letter[max(prof_letter, key=prof_letter.get)]
    results = []
    for let in prof_letter:
        if prof_letter[let] == letter:
            results.append(profession[let])
    return results


async def show_results(res, message: types.Message):
    message_text = "Թեստի արդյունքից որոշվել է որ \nձեզ են համախատասխանում \nհետևյալ ՏՏ-մասնագիտությունները՝\n\n"
    for prof in res:
        message_text += f'{prof},\n'
    message_text += '\nՇնորհակալ ենք մեզ վստահելու համար։'
    await message.answer(message_text)


async def count(cb):
    for letter in list(cb.data):
        prof_letter[letter] += 1
    await test(cb.message, cb.from_user.id)
    await cb.answer()


@dp.callback_query_handler(text=callback_values)
async def get_callback(callback: types.CallbackQuery):
    await count(callback)


@dp.callback_query_handler(text='pass')
async def get_pass_callback(callback: types.CallbackQuery):
    await test(callback.message, callback.from_user.id)
    await callback.answer()
