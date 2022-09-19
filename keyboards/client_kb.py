import aiogram.types.reply_keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# Main Menu
test: aiogram.types.reply_keyboard.KeyboardButton
sett: aiogram.types.reply_keyboard.KeyboardButton
help_button: aiogram.types.reply_keyboard.KeyboardButton

b4 = KeyboardButton(' Բարեգործություն')
test_button: str
sett_button: str
help_button: str

async def main_menu_kb():
    test = KeyboardButton(test_button, callback_data='b')
    sett = KeyboardButton(sett_button, callback_data='b')
    help = KeyboardButton(help_button, callback_data='b')
    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.add(test).row(sett, help)
    return main_menu






