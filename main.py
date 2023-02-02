import asyncio

from aiogram import executor
from aiogram.dispatcher.filters import Text

from config import dp
from handlers import start, help, my_info
from handlers.admin_bot import check_words, ban_user
from parsers.bd import init, create_table
from parsers.cars import cars_command
from schedule import schedule_command, timer, text_remind


async def startup():
    """
    запускаем дополнительные сторонние сервисы
    """
    asyncio.create_task(timer())
    init()
    create_table()


if __name__ == '__main__':
    # начало бота
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(my_info, commands=['my info'])

    # напоминалка
    dp.register_message_handler(schedule_command, Text(equals="напомни"))
    dp.register_message_handler(text_remind, commands=["напоминалка"])

    # mashing.kg
    dp.register_message_handler(cars_command, commands=["cars"])

    # админ бот
    dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(check_words)

    executor.start_polling(
        dp,
        on_startup=startup,
        skip_updates=True)
