from aiogram import types
from bot.dispacher import dp

@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    await msg.reply('<b>Successful project 😍💥</b>', 'HTML')
