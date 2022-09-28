from aiogram import types
from create_bot import dp
from keyboards.client_kb import main_menu_kb
from questions import question
from keyboards import questions_kb
import sqlite3 as sq


callback_values = ['a', 'b', 'c', 'd', 'e', 'f', 'abde', 'abcdef']

profession = dict()
profession['a'] = 'Programming'
profession['b'] = 'Software testing'
profession['c'] = 'Design'
profession['d'] = 'Information Security'
profession['e'] = 'System Administration'
profession['f'] = 'Marketing'

test_users = dict()
us_id = 0

users = dict()


class User_test:
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

    def reset(self):
        self.prof_count = dict()
        self.prof_count['a'] = 0
        self.prof_count['b'] = 0
        self.prof_count['c'] = 0
        self.prof_count['d'] = 0
        self.prof_count['e'] = 0
        self.prof_count['f'] = 0

        self.user_question = 0

async def cancel(message: types.Message):
    """Обнуляет данные теста текущего пользователя"""
    id = message.from_user.id
    if message.from_user.id in users.keys():
        users[id].reset()


async def test(message: types.Message, user_id=0):
    """Поочередный вывод тестов"""

    global us_id
    if us_id != user_id and user_id not in users.keys():
        us_id = user_id
        users[user_id] = User_test(user_id)
        users[user_id].user_question = 0

    if user_id in users.keys():
        user = users[user_id]
        i = user.user_question
        if i == len(question):
            main_menu = await main_menu_kb()
            await message.answer('Թեստը ավարտված է։', reply_markup=main_menu)
            res = await result(user_id)
            await show_results(res, message)
            user.reset()
        else:
            await message.delete()
            await message.answer(text=f"{i + 1}/{len(question)}\n" + question[i],
                                 reply_markup=questions_kb.question_kb[i])
            user.increment()


async def result(user_id):
    """Считает результаты теста"""
    true_var = 7
    user_res = users[user_id].prof_count
    letter = max(user_res, key=user_res.get)
    max_num = user_res[letter]
    results = dict()
    courses = []
    for let in user_res:
        base = sq.connect("choose_it_prof.db")
        cur = base.cursor()
        if user_res[let] == max_num:
            query_result = cur.execute("SELECT `link` FROM  `courses` WHERE `prof_letter` = ? LIMIT 2",
                                       (let,)).fetchmany(2)
            for row in query_result:
                courses.append(row[0])

            results[profession[let]] = round((max_num/true_var)*100, 2)
    # users[user_id].reset()
    return [results, courses]


async def show_results(res, message: types.Message):
    prof = res[0]
    courses = res[1]
    """Отображает результаты теста"""
    message_text = "Թեստի արդյունքից որոշվել է որ \nձեզ են համախատասխանում \nհետևյալ ՏՏ-մասնագիտությունները՝\n\n"
    for key in prof.keys():
        message_text += f'*{key} {prof[key]}%,*\n'
    message_text += '\nՇնորհակալ ենք մեզ վստահելու համար։'
    await message.answer(message_text, parse_mode='Markdown')
    await message.answer("Ձեզ ենք առաչարկում հետևյալ կուրսերը՝")
    for link in courses:
        await message.answer(link)

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
