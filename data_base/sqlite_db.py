import sqlite3 as sq

from handlers import client
from language import answer

global base, cur


def sql_start():
    global base, cur
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    if base:
        print('Database connected.')
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, lang TEXT)')
    base.commit()
    base.execute('CREATE TABLE IF NOT EXISTS language(lang PRIMARY KEY, choose_lang, choosed_lang, hello_info, '
                 'hello_error, cancel_btn, main_menu, test_btn, tst_started, tst_finished, sett_btn, sett_text, '
                 'sett_lang_btn, help_btn, '
                 'help_info, msg_err)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        res = await check_user_lang(data)
        if res is None:
            await add_user_lang(data)
            res = await check_user_lang(data)
        elif data['lang'] != res[1]:
            await update_user_lang(data)
            res = await check_user_lang(data)
        await answer(res[1])
        # await client.translate_client()


async def check_user_lang(data):
    await lang_info_add_am()
    await lang_info_add_ru()
    await lang_info_add_en()
    res = cur.execute('SELECT * FROM users WHERE user_id=?', (data['user_id'],)).fetchone()
    base.commit()
    return res


async def add_user_lang(data):
    cur.execute("INSERT INTO users VALUES (?, ?)", (data['user_id'], data['lang']))
    base.commit()


async def update_user_lang(data):
    cur.execute('UPDATE users SET lang=? WHERE user_id=?', (data['lang'], data['user_id']))
    base.commit()


# Translate
async def lang_info_add_am():
    cur.execute('INSERT OR REPLACE INTO language VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ('AM',
                                                                                            "Ընտրեք լեզուն՝",
                                                                                            "Ընտրված է հայերեն լեզուն։",
                                                                                            "Բարև հարգելի օգտատեր, ես քեզ "
                                                                                            "կօգնեմ IT-մասնագիտություն "
                                                                                            "ընտրելու հարցում։\nՍեղմիր "
                                                                                            "_\'✨ Թեստ\'_ կոճակը թեստը "
                                                                                            "սկսելու համար։",
                                                                                            "Բոտի հետ շփումը անձնական "
                                                                                            "նամակներով, գրեք [նրան]("
                                                                                            "https://t.me"
                                                                                            "/it_prof_choose_bot)",
                                                                                            "⬅ Չեղարկել",
                                                                                            "Գլխավոր մենյու՝",
                                                                                            "✨ Թեստ",
                                                                                            "Թեստը սկսված է՝",
                                                                                            "Թեստը ավարտված է։",
                                                                                            "⚙ Կարգավորումներ",
                                                                                            "Կարգավորումների բաժին՝",
                                                                                            "Լեզու",
                                                                                            "❔ Օգնություն",
                                                                                            "Աշխաեցնելու համար -> "
                                                                                            "/start:\n\n✨ Թեստ - սկսել "
                                                                                            "թեստը։\n\n⚙ Կարգավորումներ - "
                                                                                            "Կարգավորումների բաժին` կարող "
                                                                                            "եք փոխել լեզուն (Русский, "
                                                                                            "English, Հայերեն):",
                                                                                            "⚠ Անհասկանալի հրաման ⚠"))
    base.commit()


async def lang_info_add_en():
    cur.execute('INSERT OR REPLACE INTO language VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ('EN',
                                                                                            "Please select language:",
                                                                                            "English is selected.",
                                                                                            "Welcome dear user, I will "
                                                                                            "guide you in choosing an "
                                                                                            "IT "
                                                                                            "profession։\nClick the "
                                                                                            "_\'✨ "
                                                                                            "Test\'_ button to start "
                                                                                            "the "
                                                                                            "test։",
                                                                                            "Communicating with the bot "
                                                                                            "via private emails,"
                                                                                            "write to [him]("
                                                                                            "https://t.me"
                                                                                            "/it_prof_choose_bot)",
                                                                                            "⬅ Cancel",
                                                                                            "Main menu:",
                                                                                            "✨ Test",
                                                                                            "Test started:",
                                                                                            "Test finished.",
                                                                                            "⚙ Settings",
                                                                                            "Settings section:",
                                                                                            "Language",
                                                                                            "❔ Help",
                                                                                            "To start work -> "
                                                                                            "/start.\n\n✨ Test - start "
                                                                                            "the test.\n\n⚙ Settings - "
                                                                                            "Settings section: you can "
                                                                                            "change the language ("
                                                                                            "Русский, Հայերեն, English).",
                                                                                            " ⚠ Unclear command ⚠ "))
    base.commit()


async def lang_info_add_ru():
    cur.execute('INSERT OR REPLACE INTO language VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', ('RU',
                                                                                            "Выберите язык:",
                                                                                            "Выбран русский язык.",
                                                                                            "Приветствую вас, "
                                                                                            "уважаемый пользователь, "
                                                                                            "я помогу вам в выборе "
                                                                                            "IT-профессии.։\nНажмите "
                                                                                            "кнопку _\'✨ Тест\'_, "
                                                                                            "чтобы начать тест.",
                                                                                            "Общение с ботом через "
                                                                                            "личные сообщения, "
                                                                                            "напишите [ему]("
                                                                                            "https://t.me/it_prof_choose_bot)",
                                                                                            "⬅ Назад",
                                                                                            "Главное меню:",
                                                                                            "✨ Тест",
                                                                                            "Тест начат:",
                                                                                            "Тест закончен.",
                                                                                            "⚙ Настройки",
                                                                                            "Раздел настроек:",
                                                                                            "Язык",
                                                                                            "❔ Помощь",
                                                                                            "Чтобы начать работу -> "
                                                                                            "/start.\n\n✨ Тест - начать "
                                                                                            "тест.\n\n⚙ Настройки - "
                                                                                            "Раздел настроек: вы можете "
                                                                                            "изменить язык ("
                                                                                            "Русский, Հայերեն, English).",
                                                                                            " ⚠ Непонятная команда ⚠ "))
    base.commit()
