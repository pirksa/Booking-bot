import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import Redis, RedisStorage

import handlers
from repository.init_db import create_schema
from settings import load_config

config = load_config()
redis = Redis(host=config['redis']['host'])
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)
dp.include_routers(handlers.router)


async def main():
    create_schema()
    bot = Bot(token=config['tg']['token'])
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s | %(name)-18s | %(funcName)-15s | %(levelname)s | %(message)s',
                        level=logging.INFO,
                        handlers=[logging.FileHandler('test.log', mode='w'), logging.StreamHandler(sys.stdout)])
    asyncio.run(main())
