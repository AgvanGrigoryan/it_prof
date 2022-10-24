
from aiogram import types

from create_bot import dp
from keyboards.client_kb import main_menu_kb
from keyboards.test_inline_kb import test_inline_markup, answers_btns
from questions import question
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
        self.reset()

    def increment(self):
        self.user_question += 1

    def reset(self):
        self.prof_count = dict()
        self.prof_count['a'] = 0.0
        self.prof_count['b'] = 0.0
        self.prof_count['c'] = 0.0
        self.prof_count['d'] = 0.0
        self.prof_count['e'] = 0.0
        self.prof_count['f'] = 0.0

        self.user_question = 0

    def show_result(self):
        print("USER ID: " + str(self.id))
        print("programming=" + str(self.prof_count['a']))
        print("Software testing=" + str(self.prof_count['b']))
        print("Design=" + str(self.prof_count['c']))
        print("Information Security=" + str(self.prof_count['d']))
        print("System Administration=" + str(self.prof_count['e']))
        print("Marketing=" + str(self.prof_count['f']))


async def cancel(message: types.Message):
    """Обнуляет данные теста текущего пользователя"""
    id = message.from_user.id
    if message.from_user.id in users.keys():
        users[id].reset()


async def test(message: types.Message, user_id=0):
    """Поочередный вывод вопросов"""
    global us_id, question_msg_box
    if user_id == 0:
        await message.delete()
    elif us_id != user_id and user_id not in users.keys():
        us_id = user_id
        users[user_id] = User_test(user_id)
        users[user_id].user_question = 0

    if user_id in users.keys():
        user = users[user_id]
        i = user.user_question
        if i == len(question):
            res = await result(user_id)
            await show_results(res, message)
            user.reset()
        elif i < len(question):
            test_kb = await test_inline_markup(i)
            question_msg_text = f"{i + 1}/{len(question)}\n" + question[i]
            if i == 0:
                question_msg_box = await message.answer(text=question_msg_text, reply_markup=test_kb)
                user.increment()
            else:
                question_msg_box = await message.answer(text=question_msg_text, reply_markup=test_kb)
                user.increment()


async def result(user_id):
    """Считает результаты теста"""
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    profs_max_point = cur.execute("SELECT `prof_letter`, `max_point` FROM `profession`").fetchall()
    base.commit()
    print(profs_max_point)

    user_res = users[user_id].prof_count
    letter = max(user_res, key=user_res.get)
    max_num = user_res[letter]
    results = dict()
    courses = []
    for let in user_res:
        if user_res[let] == max_num:
            query_result = cur.execute("SELECT `link` FROM  `courses` WHERE `prof_letter` = ? LIMIT 2",
                                       (let,)).fetchmany(2)
            base.commit()
            for row in query_result:
                courses.append(row[0])

            results[profession[let]] = round((max_num/profs_max_point[let])*100, 2)
    # users[user_id].reset()
    return [results, courses]


async def show_results(res, message: types.Message):
    """Отображает результаты теста"""
    prof = res[0]
    courses = res[1]
    main_menu = await main_menu_kb()
    result_text = "Թեստի արդյունքից որոշվել է որ \nձեզ են համախատասխանում \nհետևյալ ՏՏ-մասնագիտությունները՝\n\n"
    for key in prof.keys():
        result_text += f'*{key} {prof[key]}%,*\n'
    result_text += '\nՇնորհակալ ենք մեզ վստահելու համար։'
    await message.answer(result_text, parse_mode='Markdown', reply_markup=main_menu)
    await message.answer("Ձեզ ենք առաչարկում հետևյալ կուրսերը՝")
    for link in courses:
        await message.answer(link)


@dp.callback_query_handler(text=answers_btns)
async def get_test_reply_callback(callback: types.CallbackQuery):
    """Собирает запросы и распределяет ответы по профессиям"""
    global base, cur, res
    message = callback.message
    user_id = callback.from_user.id
    user = users[user_id]
    question_number = user.user_question
    base = sq.connect('choose_it_prof.db')
    cur = base.cursor()
    # get question answer value from db
    answer_clmn = "answer_" + str(answers_btns.index(callback.data)+1)
    query = f"SELECT {answer_clmn} FROM `answers` WHERE `question_num`={question_number}"
    res = cur.execute(query).fetchone()
    base.commit()

    await message.delete()
    for answer in list(res):
        for prof in list(answer.split(",")):
            prof_group = prof.split("=")
            prof_letter = prof_group[0]
            prof_value = float(prof_group[1])
            users[user_id].prof_count[prof_letter] += prof_value
        await test(message, callback.from_user.id)
    await callback.answer("Loading...")




    # await test(cb.message, cb.from_user.id)
    # await cb.answer()


@dp.callback_query_handler(text="kkkk")
async def get_callback(callback: types.CallbackQuery):
    """Принимает заранее написанные(в callbakc_values) запросы"""
    await get_test_reply_callback(callback)


@dp.callback_query_handler(text='pass')
async def get_pass_callback(callback: types.CallbackQuery):
    """Принимает запрос для пропуска теста"""
    await test(callback.message, callback.from_user.id)
    await callback.answer()
