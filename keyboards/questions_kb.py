from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from answers import *

# QUESTION KB
# Question 1
q1_a1_btn = InlineKeyboardButton(q1_a1, callback_data='3')
q1_a2_btn = InlineKeyboardButton(q1_a2, callback_data='1')
q1_a3_btn = InlineKeyboardButton(q1_a3, callback_data='0')

# Question 2
q2_a1_btn = InlineKeyboardButton(q2_a1, callback_data='3')
q2_a2_btn = InlineKeyboardButton(q2_a2, callback_data='0')

# Question 3
q3_a1_btn = InlineKeyboardButton(q3_a1, callback_data='3')
q3_a2_btn = InlineKeyboardButton(q3_a2, callback_data='0')

# Question 4
q4_a1_btn = InlineKeyboardButton(q4_a1, callback_data='3')
q4_a2_btn = InlineKeyboardButton(q4_a2, callback_data='0')

# Question 5
q5_a1_btn = InlineKeyboardButton(q5_a1, callback_data='3')
q5_a2_btn = InlineKeyboardButton(q5_a2, callback_data='0')

# Question 6
q6_a1_btn = InlineKeyboardButton(q6_a1, callback_data='3')
q6_a2_btn = InlineKeyboardButton(q6_a2, callback_data='0')


question_1_kb = InlineKeyboardMarkup().add(q1_a1_btn).add(q1_a2_btn).add(q1_a3_btn)

question_2_kb = InlineKeyboardMarkup().add(q2_a1_btn).add(q2_a2_btn)

question_3_kb = InlineKeyboardMarkup().add(q3_a1_btn).add(q3_a2_btn)

question_4_kb = InlineKeyboardMarkup().add(q4_a1_btn).add(q4_a2_btn)

question_5_kb = InlineKeyboardMarkup().add(q5_a1_btn).add(q5_a2_btn)

question_6_kb = InlineKeyboardMarkup().add(q6_a1_btn).add(q6_a2_btn)


question_kb =\
[

    question_1_kb,
    question_2_kb,
    question_3_kb,
    question_4_kb,
    question_5_kb,
    question_6_kb

]
