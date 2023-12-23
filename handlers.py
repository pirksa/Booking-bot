import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import db_entry
import keyboards
from parser import country_pars, city_pars
from states import EnterMenu

handlers_logger = logging.getLogger(__name__)
router = Router(name=__name__)


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, Приветствую!', reply_markup=keyboards.menu)
    handlers_logger.info("Init Command 'start'")


@router.message(Command('clear'))
async def clear_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Действие отменено', reply_markup=keyboards.menu)
    handlers_logger.info("Init Command 'clear'")


@router.message(StateFilter(None), F.text == 'Введите страну')
async def chose_country(message: Message, state: FSMContext):
    await message.answer(text='Введите код страны, название страны через пробел\n'
                              'Пример: KZ Kazakhstan')
    await state.set_state(EnterMenu.select_country)
    handlers_logger.info("Init button 'Enter country'")


@router.message(StateFilter(None), F.text == 'Введите город')
async def chose_cty(message: Message, state: FSMContext):
    await message.answer(text='Введите код города, название города, часовой пояс, код страны через пробел\n'
                              'Пример: ALA Almaty UTC+6 KZ')
    await state.set_state(EnterMenu.select_city)
    handlers_logger.info("Init button 'Enter city'")


@router.message(StateFilter(None), F.text)
async def empty_message(message: Message):
    await message.answer('Выбирете действие в меню', reply_markup=keyboards.menu)
    handlers_logger.info('Init empty message')


@router.message(EnterMenu.select_country, F.text)
async def fill_country(message: Message, state: FSMContext):
    await state.update_data(country=message.text)
    db_entry.country_save(message.text)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код страны: {country_pars(message.text)[0]}\n'
                              f'Старна: {country_pars(message.text)[1]}')
    await message.answer(text='Теперь, введите город', reply_markup=keyboards.menu)
    await state.clear()


@router.message(EnterMenu.select_city, F.text)
async def fill_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    db_entry.city_save(message.text)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код города: {city_pars(message.text)[0]}\n'
                              f'Город: {city_pars(message.text)[1]}\n'
                              f'Часовой пояс: {city_pars(message.text)[2]}\n'
                              f'Код страны: {city_pars(message.text)[3]}')
    await state.clear()
