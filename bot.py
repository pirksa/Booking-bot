import asyncio
import logging
import sys

from aiogram import Bot, types, Dispatcher
from aiogram.filters import CommandStart

dp = Dispatcher()


@dp.message(CommandStart)
async def start_command(message: types.Message):
    await message.answer('Greetings!')


async def main():
    bot = Bot(token='6616305229:AAHj3KN7esge2F2PIDStruPUqXTO1mTQ5Jg')
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
