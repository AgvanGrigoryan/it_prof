from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Main Menu
b1 = KeyboardButton('✨ Test')
b2 = KeyboardButton('⚙ Settings')
b3 = KeyboardButton('❔ Help',)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1).row(b2, b3)
