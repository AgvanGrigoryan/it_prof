from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

# from aiogram.dispatcher import FSMContext
from select_lang import lang_set, load_lang, FSMClient, FSMContext

from keyboards import client_kb, test_case_kb

from language import ans_hello_error, ans_help_info
import result


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(message.from_user.id, "Hello")
        await lang_set(message, state)
    except:
        await message.reply(await ans_hello_error(), parse_mode='Markdown')


# @dp.message_handler(commands=['help'])
# @dp.message_handler(Text(equals='❔ Help', ignore_case=True), state='*')
async def command_help(message: types.Message):
    # help_info = await ans_help_info()
    await message.answer(await ans_help_info(), reply_markup=test_case_kb.test_kb)
    # await message.answer("Աշխաեցնելու համար -> /start:\n\n✨ Թեստ - սկսել թեստը։\n\n⚙ Կարգավորումներ - Կարգավորումների բաժին` կարող եք փոխել լեզուն (Русский, English, Հայերեն):")


# @dp.message_handler(lambda message: message.text == "⬅ չեղարկել")
async def action_cancel(message: types.Message):
    types.ReplyKeyboardRemove()
    await message.answer("Գլխավոր մենյու՝", reply_markup=client_kb.main_menu)
    await result.cancel(message)


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(lang_set, commands=['lang'], state='*')
    disp.register_message_handler(load_lang, state=FSMClient.lang)
    disp.register_message_handler(command_start, commands=['start'])
    disp.register_message_handler(command_help, commands=['help'])
    disp.register_message_handler(command_help, Text(equals='❔ Օգնություն', ignore_case=True), state='*')
    disp.register_message_handler(action_cancel, lambda message: message.text == "⬅ չեղարկել")
