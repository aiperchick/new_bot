from aiogram import types
from handlers.text import MYINFO_TEXT


async def myinfo(message: types.Message):
    """
    выводит инофрмацию
    """
    await message.answer(text=MYINFO_TEXT)
