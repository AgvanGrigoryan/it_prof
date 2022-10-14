import sqlite3 as sq


question = []


async def set_questions(lang: str):
    global question
    question.clear()
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    res = list(cur.execute("SELECT `question` FROM `questions` WHERE `lang` = ?", (lang,)).fetchall())
    base.commit()
    for i in range(0, len(res)):
        question.append(res[i][0])


async def get_questions():
    return question
