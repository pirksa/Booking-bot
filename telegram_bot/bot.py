import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

import handlers

dp = Dispatcher()
dp.include_routers(handlers.router)


async def main():
    bot = Bot(token='6616305229:AAHj3KN7esge2F2PIDStruPUqXTO1mTQ5Jg')
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
