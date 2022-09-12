import sqlite3 as sq

# main_menu, test_btn, sett_btn, sett_text, sett_lang_btn, help_btn, help_info

global trans, base, cur


async def answer(lang):
    global base, cur, trans
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    trans = base.execute("SELECT * FROM language WHERE lang=?", (lang,)).fetchone()
    base.commit()
    # if base:
    #     print('Database connected.')


async def ans_choose_lang():
    global trans
    return trans[1]


async def ans_choosed_lang():
    global trans
    return trans[2]


async def ans_hello_info():
    global trans
    return trans[3]


async def ans_hello_error():
    global trans
    return trans[4]


async def ans_cancel_btn():
    global trans
    return trans[5]


async def ans_main_menu():
    global trans
    return trans[6]


async def ans_test_btn():
    global trans
    return trans[7]


async def ans_test_started():
    global trans
    return trans[8]


async def ans_test_finished():
    global trans
    return trans[9]


async def ans_sett_btn():
    global trans
    return trans[8]


async def ans_sett_text():
    global trans
    return trans[9]


async def ans_sett_lang_btn():
    global trans
    return trans[10]


async def ans_help_btn():
    global trans
    return trans[11]


async def ans_help_info():
    global trans
    return trans[12]


async def ans_msg_err():
    global trans
    return trans[13]
