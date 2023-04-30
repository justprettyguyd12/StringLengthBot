import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


TOKEN = '***'

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


@dp.message_handler()
async def echo(message: Message):
    text = f"{message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=len(text))

if __name__ == "__main__":
    executor.start_polling(dp)



