from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor

bot = Bot(token='6616305229:AAHj3KN7esge2F2PIDStruPUqXTO1mTQ5Jg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Greetings!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
