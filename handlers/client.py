from create_bot import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

# from aiogram.dispatcher import FSMContext
from select_lang import lang_set, load_lang, FSMClient, FSMContext

from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(message.from_user.id, "Welcome 🙂")
        await lang_set(message, state)

    except:
        await message.reply("OԲոտի հետ շփումը անձնական նամակներով,\
         գրեք [նրան](https://t.me/it_prof_choose_bot)", parse_mode='Markdown')


# @dp.message_handler(commands=['help'])
# @dp.message_handler(Text(equals='❔ Help', ignore_case=True), state='*')
async def command_help(message: types.Message):
    await message.answer("Աշխաեցնելու համար -> /start.\n\n✨ Test - սկսել թեստը։\n\n⚙\
     Settings - Կարգավորումների բաժին` կարող եք փոխել լեզուն (Русский,English):")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(lang_set, commands=['lang'], state='*')
    dp.register_message_handler(load_lang, state=FSMClient.lang)
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_help, Text(equals='❔ Help', ignore_case=True), state='*')
