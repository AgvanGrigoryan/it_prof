import sqlite3 as sq


question_ans_btns = []

# Question 1 answers
async def set_questions_ans_btns(lang: str):
    global question_ans_btns
    question_ans_btns.clear()
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    res = list(cur.execute("SELECT `variant_1`,`variant_2`,`variant_3`,`variant_4`,`variant_5` FROM `questions` WHERE `lang` = ?", (lang,)).fetchall())
    base.commit()
    for q_answers in list(res):
        question_ans_btns.append(q_answers)
