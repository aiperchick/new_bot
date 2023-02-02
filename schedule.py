import asyncio
import aioschedule
from aiogram import types
from config import bot


async def text_remind(message: types.Message):
    """
    текст напоминалки
    """
    await message.answer(text=f"что нужно напомнить?")


async def schedule_command(message: types.Message):
    """
    функция запоминает id пользователя
    """
    global chat_id
    global rd
    rd = message.text[8:]
    chat_id = message.from_user.id
    await message.answer(text=f"хорошо")


async def notify():
    """
    напоминалка
    """
    await bot.send_message(
        chat_id=chat_id,
        text=rd
    )


async def timer():
    """
    функия напоминалки
    """
    aioschedule.every(10).seconds.do()

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
