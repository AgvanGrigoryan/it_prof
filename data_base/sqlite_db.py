import sqlite3 as sq

from aiogram import types

from answers import set_questions_ans_btns
from language import answer
from questions import set_questions

global base, cur


def sql_start():
    global base, cur
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    if base:
        print('Database connected.')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, lang TEXT, username TEXT, fullname TEXT, is_bot TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS language(lang PRIMARY KEY, choose_lang, choosed_lang, hello_info, '
                 'hello_error, cancel_btn, main_menu, test_btn, tst_started, tst_finished, sett_btn, sett_text, '
                 'sett_lang_btn, help_btn, '
                 'help_info, msg_err)')
    base.commit()
    base.execute(
        'CREATE TABLE IF NOT EXISTS questions(lang PRIMARY KEY, question_1,question_2,question_3,question_4,'
        'question_5,question_6,question_7,question_8,question_9,question_10,question_11,question_12,question_13,'
        'question_14,question_15,question_16,question_17,question_18)')
    base.commit()


async def sql_add_command(state, message):
    async with state.proxy() as data:
        res = await check_user_lang(data['user_id'])
        if res is None:
            await add_user_lang(data, message)
            res = await check_user_lang(data['user_id'])
        elif data['lang'] != res[1]:
            await update_user_lang(data, message)
            res = await check_user_lang(data['user_id'])

        await initial_setup(res[1])
        # await client.translate_client()


async def initial_setup(language):
    await count_prof_max_point()
    await answer(language)
    await set_questions(language)
    await set_questions_ans_btns(language)
async def check_user_lang(id):
    res = cur.execute('SELECT * FROM users WHERE user_id=?', (id,)).fetchone()
    base.commit()
    return res


async def add_user_lang(data, message: types.Message):
    cur.execute("INSERT INTO `users` VALUES (?, ?, ?, ?, ?)", (data['user_id'], data['lang'], message.from_user.username, message.from_user.full_name, message.from_user.is_bot))
    base.commit()


async def update_user_lang(data, message: types.Message):
    cur.execute('UPDATE `users` SET `lang`=?,`username`=?,`fullname`=?,`is_bot`=? WHERE `user_id`=?', (data['lang'], message.from_user.username, message.from_user.full_name, message.from_user.is_bot, data['user_id']))
    base.commit()

async def count_prof_max_point():
    res = cur.execute('SELECT `answer_1`,`answer_2`,`answer_3`,`answer_4`, `answer_5`  FROM `answers`').fetchone()
    base.commit()
    for row in res:
        # todo profesion maximum point count
        print(row)