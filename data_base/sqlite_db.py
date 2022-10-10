import sqlite3 as sq

from language import answer
from questions import set_questions

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
    base.execute(
        'CREATE TABLE IF NOT EXISTS questions(lang PRIMARY KEY, question_1,question_2,question_3,question_4,'
        'question_5,question_6,question_7,question_8,question_9,question_10,question_11,question_12,question_13,'
        'question_14,question_15,question_16,question_17,question_18)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        res = await check_user_lang(data['user_id'])
        if res is None:
            await add_user_lang(data)
            res = await check_user_lang(data['user_id'])
        elif data['lang'] != res[1]:
            await update_user_lang(data)
            res = await check_user_lang(data['user_id'])
        await answer(res[1])
        await set_questions(res[1])
        # await client.translate_client()


async def check_user_lang(id):
    await lang_info_add_am()
    await lang_info_add_ru()
    await lang_info_add_en()

    await add_am_questions()
    await add_ru_questions()
    await add_en_questions()
    res = cur.execute('SELECT * FROM users WHERE user_id=?', (id,)).fetchone()
    base.commit()
    return res


async def add_user_lang(data):
    cur.execute("INSERT INTO users VALUES (?, ?)", (data['user_id'], data['lang'],))
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
                                                                                            "կօգն եմ IT-մասնագիտություն "
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
                                                                                            "profession.\nClick the "
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
                                                                                            "IT-профессии.\nНажмите "
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


async def add_am_questions():
    cur.execute("INSERT OR REPLACE INTO questions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ('AM',
                                                                                                   'Հետևյալ նշանների համակցություններից ո՞րը պետք է շարունակի այս շարքը՝ 1000011000111\n\n \
                                                                                                    1) 1002\n \
                                                                                                    2) 0111\n \
                                                                                                    3) 1112',
                                                                                                           'Դուք ձգտոու՞մ եք փոխել ձեր շրջապատը և գեղեցկացնել ձեր միջավայրը:\n\n \
                                                                                                    1) Այո, ես դա անում եմ անընդհատ\n \
                                                                                                    2) Ոչ, ինձ չի հետաքրքրում',
                                                                                                           'Ձեզ դուր է գալիս օգնել մարդկանց\n\n \
                                                                                                    1) ստուգել կայքի բոլոր տարրերի և էջերի աշխատանքը\n \
                                                                                                    2) Զարգացնել կայքը ինտերնետում,ներգրավել հանդիսատես գովազդի, նամակագրության և բովանդակության միջոցով',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Տեղադրել համակարգիչներ, հեռախոսակապ, ցանցային երթուղիչներ, միացնել տպիչները, կարգավորել ծրագրերը\n \
                                                                                                    2) Վերլուծել ալգորիթմները, գրել կոդ ծրագրավորման լեզուներով, օգտագործել վերացական հասկացություններ',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ստուգել, արդյոք ծրագիրը տալիս է ճիշտ պատասխանը\n \
                                                                                                    2) Ստուգել ընկերության համակարգչային ցանցը՝ տեղեկատվական հարձակումներին դիմադրության համար',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ստեղծել նոր ալգորիթմներ\n \
                                                                                                    2) Վերապատրաստել աշխատակիցներին, որպեսզի չընկնեն հաքերների թակարդները',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Մասնակցել ծրագրերի մշակմանը, փորձարկելով դրանք աշխատունակության համար\n \
                                                                                                    2) Տեղադրել և կարգավորել ցանցային ծրագրեր, սերվերներ',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ծրագրավորել վեբ հավելվածի տարբեր բաղադրիչների տրամաբանությունն ու վարքը\n \
                                                                                                    2) Նկարել վեբ հավելվածի գրաֆիկական տարրեր (կոճակներ, լոգոներ, մենյու և այլն)',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ուսումնասիրել մարդկանց վարքը սոցիալական ցանցերում, որոնման համակարգերում, կայքերում\n \
                                                                                                    2) Ապահովել կորպորատիվ համակարգիչների անխափան աշխատանքը, գնել և թարմացնել դրանք',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ստուգել՝ արդյոք կայքը կամ հավելվածն աշխատում է ըստ նախատեսվածի\n \
                                                                                                    2) Ստեղծել օգտագործողի համար հարմար և գեղեցիկ ինտերֆեյս',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Մշակել ալգորիթմներ և տրամաբանություն ծրագրի կամ ընկերության կայքի համար\n \
                                                                                                    2) Ինտերնետում ընկերության արտադրանքի կամ ծառայության առաջմղման հայեցակարգ մշակել',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Ամենօր աշխատել տառատեսակների, լուսանկարների, գույների հետ\n \
                                                                                                    2) Ամեն օր ուսումնասիրել օպերացիոն համակարգերը խոցելիության համար',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Դարձրել ընկերությունը գրավիչ հաճախորդների համար\n \
                                                                                                    2) Պաշտպանել ընկերությունը տեղեկատվական սպառնալիքներից',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Անընդհատ ուսումնասիրել ժամանակակից դիզայներների աշխատանքը\n \
                                                                                                    2) Անընդհատ ուսումնասիրել համակարգչային տեխնոլոգիաների վերջին նորությունները',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Հավաքել համակարգիչներ, միացնել դրանք ցանցին և տեղադրել ծրագրեր\n \
                                                                                                    2) Ուսումնասիրել և ընտրել հաքերներից տվյալները պաշտպանելու մեթոդներ',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Կատարել ինտերֆեյսի ձևավորում\n \
                                                                                                    2) Գովազդել կայքը ինտերնետում',
                                                                                                           'Փորձեք ընտրել երկու տարբերակներից որևիցե մեկը\n\n \
                                                                                                    1) Կատարել սարքերի կանխարգելիչ սպասարկում՝ դրանց ցանցի աշխատանքը բարելավելու համար\n \
                                                                                                    2) Փորձարկել ուրիշների կողմից գրված ծրագրեր',
                                                                                                   'Լուծեք խնդիրը՝ a²*a = ?\n\n \
                                                                                                   1) a³\n \
                                                                                                   2) 2a³'
                                                                                                   ))
    base.commit()


async def add_ru_questions():
    cur.execute("INSERT OR REPLACE INTO questions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ('RU',
                                                                                                   'Какой из следующих сочетаний знаков должно продолжить этот ряд: 1000011000111\n\n \
                                                                                                    1) 1002\n \
                                                                                                    2) 0111\n \
                                                                                                    3) 1112',
                                                                                                   'Ты стремишься внести перемены и украсить окружающую тебя среду?\n\n \
                                                                                                    1) Да, постоянно это делаю\n \
                                                                                                    2) Нет, мне всё равно',
                                                                                                   'Вам нравиться помогать людям:\n\n \
                                                                                                    1) Проверять функционирование всех элементов и страниц сайта\n \
                                                                                                    2) Продвигать сайт в интернете, привлекать аудиторию с помощью рекламы, рассылок и содержания',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Настраивать компьютеры, телефонию, сетевые роутеры, подсоединять принтеры, настраивать программы\n \
                                                                                                    2) Анализировать алгоритмы, писать код на языках программирования, изпользуя абстрактные понятия',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Проверять, выдаёт ли программа правильный ответ\n \
                                                                                                    2) Проверять компьютерную сеть компании на устойчивость к информационным атакам',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Создавать новые алгоритмы\n \
                                                                                                    2) Обучать сотрудников не попадаться в ловушки хакеров',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Участвовать в разработке программ, обкатывая их на работоспособность\n \
                                                                                                    2) Устанавливать и настраивать сетевые программы, сервера',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Программировать логику и поведение разных компонентов веб-приложения\n \
                                                                                                    2) Рисовать графические элементы веб-приложения (кнопки, логотипы, меню и т.д.)',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Исследовать поведение людей в социальных сетях, поисковых системах, на сайтах\n \
                                                                                                    2) Обеспечивать бесперебойную работу корпоративных компьютеров, закупать их и обновлять',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Проверять, работает ли сайт или приложение так, как задумано\n \
                                                                                                    2) Создавать удобный и красивый интерфейс',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Разрабатывать алгоритмы и логику программы или сайта компании\n \
                                                                                                    2) Разрабатывать концепцию продвижения товара или услуги компании в интернете',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Ежедневно работать со шрифтами, фотографиями, цветами\n \
                                                                                                    2) Ежедневно изучать операционные системы на предмет наличия в них уязвимостей',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Делать компанию привлекательной для клиентов\n \
                                                                                                    2) Защищать компанию от информационных угроз',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Постоянно изучать работы современных дизайнеров\n \
                                                                                                    2) Постоянно изучать новинки компьютерной техники',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Собирать компьютеры, объединять их в сеть и устанавливать программы\n \
                                                                                                    2) Изучать и подбирать методы защиты данных от хакеров',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Делать дизайн интерфейса\n \
                                                                                                    2) Рекламировать сайт в интернете',
                                                                                                   'Постарайтесь выбрать один из двух предложенных вариантов\n\n \
                                                                                                    1) Выполнять профилактическое обслуживание устройств, чтобы повысить их производительность в сети.\n \
                                                                                                    2) Тестирвоать программы, написанные другими',
                                                                                                   'Решите пример: a²*a = ?\n\n \
                                                                                                    1) a³\n \
                                                                                                    2) 2a³'
                                                                                                   ))
    base.commit()

async def add_en_questions():
    cur.execute("INSERT OR REPLACE INTO questions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ('EN',
                                                                                                   'Which of the following combinations of characters should continue this series: 1000011000111\n\n \
                                                                                                    1) 1002\n \
                                                                                                    2) 0111\n \
                                                                                                    3) 1112',
                                                                                                   'Are you looking to make a difference and beautify your environment?\n\n \
                                                                                                    1) Yes, I do it all the time\n \
                                                                                                    2) No I don\'t care',
                                                                                                   'You like to help people:\n\n \
                                                                                                    1) Check the functioning of all elements and pages of the site\n \
                                                                                                    2) Promote your site on the Internet, attract an audience through advertising, mailing lists and content',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Set up computers, telephony, network routers, connect printers, configure programs\n \
                                                                                                    2) Analyze algorithms, write code in programming languages ​​using abstract concepts',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Check if the program gives the correct answer\n \
                                                                                                    2) Check the company\'s computer network for resistance to information attacks',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Create new algorithms\n \
                                                                                                    2) Train employees not to fall into the traps of hackers',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Participate in the development of programs, testing them for performance\n \
                                                                                                    2) Install and configure network programs, servers',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Program the logic and behavior of different components of a web application\n \
                                                                                                    2) Draw graphical elements of a web application (buttons, logos, menus, etc.)',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Research people\'s behavior in social networks, search engines, websites\n \
                                                                                                    2) Ensure the smooth operation of corporate computers, purchase them and update them',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Check if a site or app is working as intended\n \
                                                                                                    2) Create a user-friendly and beautiful interface',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Develop algorithms and logic for a program or company website\n \
                                                                                                    2) Develop a concept for promoting a company\'s product or service on the Internet',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Daily work with fonts, photos, colors\n \
                                                                                                    2) Examine operating systems daily for vulnerabilities',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Make the company attractive to customers\n \
                                                                                                    2) Protect the company from information threats',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Constantly study the work of contemporary designers\n \
                                                                                                    2) Keep up to date with the latest in computer technology',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Assemble computers, connect them to a network and install programs\n \
                                                                                                    2) Study and select methods to protect data from hackers',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Do interface design\n \
                                                                                                    2) Advertise your site online',
                                                                                                   'Try to choose one of the two options\n\n \
                                                                                                    1) Perform preventive maintenance on devices to improve their network performance.\n \
                                                                                                    2) Test programs written by others',
                                                                                                   'Solve an example: a²*a = ?\n\n \
                                                                                                    1) a³\n \
                                                                                                    2) 2a³'
                                                                                                   ))
    base.commit()