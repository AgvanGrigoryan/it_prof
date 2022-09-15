from aiogram import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вышел в онлайн.')
    sqlite_db.sql_start()



client.register_handlers_client(dp)
other.register_handlers_other(dp)





# @dp.callback_query_handler(func=lambda c: c.date == '1')
# async def process_callback_q1()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
