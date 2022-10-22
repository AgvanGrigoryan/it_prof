import sqlite3
import sqlite3 as sq
from time import sleep

import select_lang
from handlers import client, other
from keyboards import settings_case_kb, client_kb, help_case_kb, test_reply_kb

# global base, cur, trans
trans: tuple
base: sqlite3.Connection
cur: sqlite3.Cursor

choose_lang: str
choosed_lang: str
hello_info = "Hello"
hello_err = 'Communicating with the bot via private emails, write to [him](https://t.me/it_prof_choose_bot)'
cancel_btn: str
main_menu: str
test_btn: str
test_started: str
test_finished: str
sett_btn: str
sett_text: str
sett_lang_btn: str
help_btn: str
help_info: str
msg_err: str


async def answer(lang):
    global base, cur, trans
    global choose_lang, choosed_lang, hello_info, hello_err, cancel_btn, main_menu, test_btn, test_started, \
        test_finished, sett_btn, sett_text, sett_lang_btn, help_btn, help_info, msg_err
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    trans = base.execute("SELECT * FROM language WHERE lang=?", (lang,)).fetchone()
    base.commit()


    # if base:
    #     print('Database connected.')
    choose_lang = trans[1]
    choosed_lang = trans[2]
    hello_info = trans[3]
    cancel_btn = trans[5]
    main_menu = trans[6]
    test_btn = trans[7]
    test_started = trans[8]
    test_finished = trans[9]
    sett_btn = trans[10]
    sett_text = trans[11]
    sett_lang_btn = trans[12]
    help_btn = trans[13]
    help_info = trans[14]
    msg_err = trans[15]
    sleep(0.5)

    # client
    client.hello_information = hello_info
    client.hello_error = hello_err
    client.help_button = help_btn
    client.help_information = help_info
    client.cancel_button = cancel_btn
    client.main_menu_text = main_menu
    client.language_button = sett_lang_btn

    # other
    other.cancel_button = cancel_btn
    other.settings_text = sett_text
    other.message_error = msg_err
    other.test_button = test_btn
    other.settings_button = sett_btn
    # other.language_button = sett_lang_btn
    other.test_started = test_started

    # select_lang
    select_lang.hello_information = hello_info

    # keyboards
    test_reply_kb.cancel_button = cancel_btn

    help_case_kb.cancel_button = cancel_btn

    settings_case_kb.lang_button = sett_lang_btn
    settings_case_kb.cancel_button = cancel_btn

    client_kb.test_button = test_btn
    client_kb.sett_button = sett_btn
    client_kb.help_button = help_btn


async def ans_choose_lang():
    return choose_lang


async def ans_choosed_lang():
    return choosed_lang


async def ans_hello_info():
    return hello_info


async def ans_hello_err():
    return hello_err


async def ans_cancel_btn():
    return cancel_btn


async def ans_main_menu():
    return main_menu


async def ans_test_btn():
    return test_btn


async def ans_test_started():
    return test_started


async def ans_test_finished():
    return test_finished


async def ans_sett_btn():
    return sett_btn


async def ans_sett_text():
    return sett_text


async def ans_sett_lang_btn():
    return sett_lang_btn


async def ans_help_btn():
    return help_btn


async def ans_help_info():
    return help_info


async def ans_msg_err():
    return msg_err
