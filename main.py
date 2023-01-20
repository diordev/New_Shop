import logging
from aiogram import executor
from bot.handler import *
from db import engine
from db.model import Base

if __name__ == '__main__':
    log = logging.getLogger('broadcast')
    logging.basicConfig(level=logging.INFO)
    Base.metadata.create_all(engine)
    executor.start_polling(dp, skip_updates=True)

print("6+54645hjkhjhkjhjk6456")
