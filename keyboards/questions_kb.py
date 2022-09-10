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
 # Question 7
q7_a1_btn = InlineKeyboardButton(q7_a1, callback_data='3')
q7_a2_btn = InlineKeyboardButton(q7_a2, callback_data='0')
# Question 8
q8_a1_btn = InlineKeyboardButton(q8_a1, callback_data='3')
q8_a2_btn = InlineKeyboardButton(q8_a2, callback_data='0')
# Question 9
q9_a1_btn = InlineKeyboardButton(q9_a1, callback_data='3')
q9_a2_btn = InlineKeyboardButton(q9_a2, callback_data='0')
# Question 10
q10_a1_btn = InlineKeyboardButton(q10_a1, callback_data='3')
q10_a2_btn = InlineKeyboardButton(q10_a2, callback_data='0')
# Question 11
q11_a1_btn = InlineKeyboardButton(q11_a1, callback_data='3')
q11_a2_btn = InlineKeyboardButton(q11_a2, callback_data='0')
# Question 12
q12_a1_btn = InlineKeyboardButton(q12_a1, callback_data='3')
q12_a2_btn = InlineKeyboardButton(q12_a2, callback_data='0')
# Question 13
q13_a1_btn = InlineKeyboardButton(q13_a1, callback_data='3')
q13_a2_btn = InlineKeyboardButton(q13_a2, callback_data='0')
# Question 14
q14_a1_btn = InlineKeyboardButton(q14_a1, callback_data='3')
q14_a2_btn = InlineKeyboardButton(q14_a2, callback_data='0')
# Question 15
q15_a1_btn = InlineKeyboardButton(q15_a1, callback_data='3')
q15_a2_btn = InlineKeyboardButton(q15_a2, callback_data='0')
# Question 16
q16_a1_btn = InlineKeyboardButton(q16_a1, callback_data='3')
q16_a2_btn = InlineKeyboardButton(q16_a2, callback_data='0')
# Question 17
q17_a1_btn = InlineKeyboardButton(q17_a1, callback_data='3')
q17_a2_btn = InlineKeyboardButton(q17_a2, callback_data='0')
# Question 18
q18_a1_btn = InlineKeyboardButton(q18_a1, callback_data='3')
q18_a2_btn = InlineKeyboardButton(q18_a2, callback_data='0',)

question_1_kb = InlineKeyboardMarkup().add(q1_a1_btn).add(q1_a2_btn).add(q1_a3_btn)

question_2_kb = InlineKeyboardMarkup().add(q2_a1_btn).add(q2_a2_btn)

question_3_kb = InlineKeyboardMarkup().add(q3_a1_btn).add(q3_a2_btn)

question_4_kb = InlineKeyboardMarkup().add(q4_a1_btn).add(q4_a2_btn)

question_5_kb = InlineKeyboardMarkup().add(q5_a1_btn).add(q5_a2_btn)

question_6_kb = InlineKeyboardMarkup().add(q6_a1_btn).add(q6_a2_btn)

question_7_kb = InlineKeyboardMarkup().add(q7_a1_btn).add(q7_a2_btn)

question_8_kb = InlineKeyboardMarkup().add(q8_a1_btn).add(q8_a2_btn)

question_9_kb = InlineKeyboardMarkup().add(q9_a1_btn).add(q9_a2_btn)

question_10_kb = InlineKeyboardMarkup().add(q10_a1_btn).add(q10_a2_btn)

question_11_kb = InlineKeyboardMarkup().add(q11_a1_btn).add(q11_a2_btn)

question_12_kb = InlineKeyboardMarkup().add(q12_a1_btn).add(q12_a2_btn)

question_13_kb = InlineKeyboardMarkup().add(q13_a1_btn).add(q13_a2_btn)

question_14_kb = InlineKeyboardMarkup().add(q14_a1_btn).add(q14_a2_btn)

question_15_kb = InlineKeyboardMarkup().add(q15_a1_btn).add(q15_a2_btn)

question_16_kb = InlineKeyboardMarkup().add(q16_a1_btn).add(q16_a2_btn)

question_17_kb = InlineKeyboardMarkup().add(q17_a1_btn).add(q17_a2_btn)

question_18_kb = InlineKeyboardMarkup().add(q18_a1_btn).add(q18_a2_btn)

question_kb = \
    [
        question_1_kb,
        question_2_kb,
        question_3_kb,
        question_4_kb,
        question_5_kb,
        question_6_kb,
        question_7_kb,
        question_8_kb,
        question_9_kb,
        question_10_kb,
        question_11_kb,
        question_12_kb,
        question_13_kb,
        question_14_kb,
        question_15_kb,
        question_16_kb,
        question_17_kb,
        question_18_kb
    ]
