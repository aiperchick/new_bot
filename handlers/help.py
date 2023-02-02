from aiogram import types
from handlers.text import HELP_TEXT


async def help(message: types.Message):
    """
    выводит все команды пользователя
    """
    await message.answer(text=HELP_TEXT)
