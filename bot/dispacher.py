import environ
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = environ.Env(DEBUG =(bool , False))
environ.Env.read_env()
BOT_TOKEN = env('BOT_TOKEN')
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot , storage=MemoryStorage())