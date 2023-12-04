import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

import handlers
from repository.create_data import insert_data
from repository.init_db import create_schema

dp = Dispatcher()
dp.include_routers(handlers.router)


async def main():
    create_schema()
    insert_data()
    bot = Bot(token='6616305229:AAHj3KN7esge2F2PIDStruPUqXTO1mTQ5Jg')
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s | %(name)-18s | %(funcName)-15s | %(levelname)s | %(message)s',
                        level=logging.INFO,
                        handlers=[logging.FileHandler('test.log', mode='w'), logging.StreamHandler(sys.stdout)])
    asyncio.run(main())
