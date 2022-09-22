import sqlite3 as sq


question = []


async def set_questions(lang: str):
    global  question
    question.clear()
    base = sq.connect("choose_it_prof.db")
    cur = base.cursor()
    res = list(cur.execute("SELECT * FROM questions WHERE lang = ?", (lang,)).fetchone())
    base.commit()
    for i in range(1, len(res)):
        question.append(res[i])


# question = \
#     [
#         question_1,
#         question_2,
#         question_3,
#         question_4,
#         question_5,
#         question_6,
#         question_7,
#         question_8,
#         question_9,
#         question_10,
#         question_11,
#         question_12,
#         question_13,
#         question_14,
#         question_15,
#         question_16,
#         question_17,
#         question_18
#     ]


async def get_questions():
    return question
