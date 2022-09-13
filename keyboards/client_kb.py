from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# from language import ans_test_btn, ans_sett_btn, ans_help_btn
# Main Menu

# test_btn = ans_test_btn()
# sett_btn = ans_sett_btn()
# help_btn = ans_help_btn()
b1 = KeyboardButton('✨ Թեստ')
b2 = KeyboardButton('⚙ Կարգավորումներ')
b3 = KeyboardButton('❔ Օգնություն')
b4 = KeyboardButton(' Բարեգործություն')

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1).row(b2, b3)
