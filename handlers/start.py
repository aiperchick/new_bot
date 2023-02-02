from aiogram import types
from handlers.text import START_TEXT


async def start(messege: types.Message):
    """
    приветствие пользователя
    """
    await messege.answer(text=START_TEXT.format(
        first_name=messege.from_user.first_name)
    )
    await messege.delete()
