import aiogram.types.reply_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from language import ans_test_btn, ans_help_btn, ans_sett_btn

# from language import test_btn, sett_btn, help_btn

# Main Menu
test: aiogram.types.reply_keyboard.KeyboardButton
sett: aiogram.types.reply_keyboard.KeyboardButton
help_button: aiogram.types.reply_keyboard.KeyboardButton

b4 = KeyboardButton(' Բարեգործություն')


test_btn: str
sett_btn: str
help_btn: str


async def main_menu_kb():
    global test_btn, sett_btn, help_btn
    global test, sett, help_button
    test_btn = await ans_test_btn()
    sett_btn = await ans_sett_btn()
    help_btn = await ans_help_btn()
    test = KeyboardButton(test_btn, callback_data='b')
    sett = KeyboardButton(sett_btn, callback_data='b')
    help_button = KeyboardButton(help_btn, callback_data='b')
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.add(test).row(sett, help_button)
    return main_menu






