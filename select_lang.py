from create_bot import bot
from aiogram import types

from data_base import sqlite_db

from keyboards.client_kb import main_menu_kb
from keyboards.lang_select_kb import select_lang_kb

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from language import ans_sett_text, ans_hello_info

ID = None


class FSMClient(StatesGroup):
    user_id = State()
    lang = State()


async def lang_code(message):
    match message.text:
        case '🇺🇸 English':
            await message.reply('English is selected.')
            return "EN"
        case '🇷🇺 Русский':
            await message.reply('Выбран русский язык.')
            return "RU"
        case '🇦🇲 Հայերեն':
            await message.reply('Ընտրված է հայերեն լեզուն։')
            return "AM"
        case default:
            await message.reply('Wrong data,selected default: English')
            return "EN"


# Language select dialog start
# @dp.message_handler(commands='setLanguage', state=FSMClient.user_id)
async def lang_set(message: types.Message, state: FSMContext):
    global ID
    ID = message.from_user.id

    await FSMClient.user_id.set()
    async with state.proxy() as data:
        data['user_id'] = message.from_user.id
    # await sqlite_db.sql_add_command(state)
    await FSMClient.next()
    await message.reply("Please select language:", reply_markup=select_lang_kb)


# @dp.message_handler(state=FSMClient.lang)
async def load_lang(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['lang'] = await lang_code(message)
        await sqlite_db.sql_add_command(state)
        hello_info = await ans_hello_info()
        main_menu = await main_menu_kb()
        await bot.send_message(message.from_user.id, hello_info, reply_markup=main_menu, parse_mode="Markdown")

        await state.finish()
