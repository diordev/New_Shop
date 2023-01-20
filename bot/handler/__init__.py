from bot.handler.id_filter import *


@dp.message_handler(commands='start')
async def start_handler(msg: types.Message):
    print(msg.chat.id)
    await msg.reply('<b>Assalomu alaykum</b>', 'HTML')
