import sqlite3
import sqlite3 as sq


# main_menu, test_btn, sett_btn, sett_text, sett_lang_btn, help_btn, help_info


# global base, cur, trans
trans: tuple
base: sqlite3.Connection
cur: sqlite3.Cursor

choose_lang = ''
choosed_lang = ''
hello_info = ''
hello_error = 'Communicating with the bot via private emails, write to [him](https://t.me/it_prof_choose_bot)'
cancel_btn = ''
main_menu = ''
test_btn = ''
test_started = ''
test_finished = ''
sett_btn = ''
sett_text = ''
sett_lang_btn = ''
help_btn = ''
help_info = ''
msg_err = ''


async def answer(lang):
    global base, cur, trans
    global choose_lang, choosed_lang, hello_info, hello_error, cancel_btn, main_menu, test_btn, test_started, \
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

    # await client.translate_client()
    # await translate_other()


async def ans_choose_lang():
    return choose_lang


async def ans_choosed_lang():
    return choosed_lang


async def ans_hello_info():
    return hello_info


async def ans_hello_error():
    return hello_error


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
