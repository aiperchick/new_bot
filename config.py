import logging
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(getenv('MY_TOKEN'))
dp = Dispatcher(bot)
