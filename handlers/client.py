from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from keyboards.client_kb import main_menu_kb
# from aiogram.dispatcher import FSMContext
from select_lang import lang_set, load_lang, FSMClient, FSMContext

from keyboards import test_case_kb

from language import hello_error, ans_help_btn, ans_cancel_btn, ans_help_info, ans_main_menu
import result


help_btn = ''
help_info = ''
cancel_btn = ''
main_menu = ''

# todoОшибка текстов для проверки хендлерами кнопок меню
# async def translate_client():
#     global help_btn, help_info, cancel_btn, main_menu
#     help_btn = await ans_help_btn()
#     help_info = await ans_help_info()
#     cancel_btn = await ans_cancel_btn()
#     main_menu = await ans_main_menu()


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    try:
        await bot.send_message(message.from_user.id, "Hello")
        await lang_set(message, state)
    except:
        await message.reply(hello_error, parse_mode='Markdown')


# @dp.message_handler(commands=['help'])
# @dp.message_handler(Text(equals='❔ Help', ignore_case=True), state='*')
async def command_help(message: types.Message):
    # help_info = await ans_help_info()
    await message.answer(help_info, reply_markup=test_case_kb.test_kb)


# @dp.message_handler(lambda message: message.text == "⬅ չեղարկել")
async def action_cancel(message: types.Message):
    types.ReplyKeyboardRemove()
    main_menu_kb_case = await main_menu_kb()
    await message.answer(main_menu, reply_markup=main_menu_kb_case)
    await result.cancel(message)


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(lang_set, commands=['lang'], state='*')
    disp.register_message_handler(load_lang, state=FSMClient.lang)
    disp.register_message_handler(command_start, commands=['start'])
    disp.register_message_handler(command_help, commands=['help'])
    disp.register_message_handler(command_help, Text(equals=help_btn, ignore_case=True), state='*')
    disp.register_message_handler(action_cancel, commands=['cancel'], state="*")
    disp.register_message_handler(action_cancel, lambda message: message.text == cancel_btn)
