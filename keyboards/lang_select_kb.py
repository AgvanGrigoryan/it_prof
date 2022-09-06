from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Lang Select kb
ENG = KeyboardButton('🇺🇸 English')
RUS = KeyboardButton('🇷🇺 Русский')
ARM = KeyboardButton('🇦🇲 Հայերեն')

select_lang_kb = ReplyKeyboardMarkup(resize_keyboard=True)
select_lang_kb.row(ENG, RUS, ARM)
