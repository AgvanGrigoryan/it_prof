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

users = dict()


class User_test():
    def __init__(self, user_id):
        self.id = user_id
        self.prof_count = dict()
        self.prof_count['a'] = 0
        self.prof_count['b'] = 0
        self.prof_count['c'] = 0
        self.prof_count['d'] = 0
        self.prof_count['e'] = 0
        self.prof_count['f'] = 0

        self.user_question = 0

    def increment(self):
        self.user_question += 1


async def cancel(message: types.Message):
    """Обнуляет данные теста текущего пользователя"""
    id = message.from_user.id
    if message.from_user.id in users.keys():
        users[id].user_question = 0


async def test(message: types.Message, user_id=0):
    """Поочередный вывод тестов"""
    # show user prof_count
    if user_id in users.keys():
        user = users[user_id]
        for us_prof in user.prof_count:
            print(user.prof_count[us_prof])
        print('\n')

    global us_id
    if us_id != user_id and user_id not in users.keys():
        us_id = user_id
        users[user_id] = User_test(user_id)
        users[user_id].user_question = 0

    if user_id in users.keys():
        user = users[user_id]
        i = user.user_question
        if i == len(question):
            await message.answer('Թեստը ավարտված է։', reply_markup=main_menu)
            user.user_question = 0
            res = await result(user_id)
            await show_results(res, message)
        else:
            await message.delete()
            await message.answer(text=f"{i + 1}/{len(question)}\n" + question[i],
                                 reply_markup=questions_kb.question_kb[i])
            user.increment()


async def result(user_id):
    """Считает результаты теста"""
    user_res = users[user_id].prof_count
    letter = user_res[max(user_res, key=user_res.get)]
    results = []
    for let in user_res:
        if user_res[let] == letter:
            results.append(profession[let])
    return results


async def show_results(res, message: types.Message):
    """Отображает результаты теста"""
    message_text = "Թեստի արդյունքից որոշվել է որ \nձեզ են համախատասխանում \nհետևյալ ՏՏ-մասնագիտությունները՝\n\n"
    for prof in res:
        message_text += f'*{prof},*\n'
    message_text += '\nՇնորհակալ ենք մեզ վստահելու համար։'
    await message.answer(message_text, parse_mode='Markdown')


async def count(cb):
    """Собирает запросы и распределяет ответы по профессиям"""
    for letter in list(cb.data):
        users[cb.from_user.id].prof_count[letter] += 1
    await test(cb.message, cb.from_user.id)
    await cb.answer()


@dp.callback_query_handler(text=callback_values)
async def get_callback(callback: types.CallbackQuery):
    """Принимает заранее написанные(в callbakc_values) запросы"""
    await count(callback)


@dp.callback_query_handler(text='pass')
async def get_pass_callback(callback: types.CallbackQuery):
    """Принимает запрос для пропуска теста"""
    await test(callback.message, callback.from_user.id)
    await callback.answer()
