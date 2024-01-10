import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import db_entry
import keyboards
from parser import country_pars, city_pars
from states import EnterMenu, UserInfo, EnterBuilding

handlers_logger = logging.getLogger(__name__)
router = Router(name=__name__)


@router.message(Command('start'), StateFilter(None))
async def start_command(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Приветствую!')
    await message.answer(text=f'Введите номер телефона')
    await state.set_state(UserInfo.user_data)
    handlers_logger.info("Init Command 'start'")


@router.message(UserInfo.user_data, F.text)
async def fill_user(message: Message, state: FSMContext):
    data = message.from_user.id, message.from_user.username, message.text
    db_entry.user_save(data)
    await message.answer(f'Номер {message.text} сохранен')
    await message.answer(f'Теперь введите страну', reply_markup=keyboards.menu)
    await state.clear()


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


@router.message(EnterMenu.select_country, F.text)
async def fill_country(message: Message, state: FSMContext):
    db_entry.country_save(message.text, message.from_user.id)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код страны: {country_pars(message.text)[0]}\n'
                              f'Старна: {country_pars(message.text)[1]}')
    await message.answer(text='Теперь, введите город', reply_markup=keyboards.menu)
    await state.clear()


@router.message(StateFilter(None), F.text == 'Введите город')
async def chose_cty(message: Message, state: FSMContext):
    await message.answer(text='Введите код города, название города, часовой пояс, код страны через пробел\n'
                              'Пример: ALA Almaty UTC+6 KZ')
    await state.set_state(EnterMenu.select_city)
    handlers_logger.info("Init button 'Enter city'")


@router.message(EnterMenu.select_city, F.text)
async def fill_city(message: Message, state: FSMContext):
    await state.update_data(city_code=city_pars(message.text)[0])
    db_entry.city_save(message.text, message.from_user.id)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код города: {city_pars(message.text)[0]}\n'
                              f'Город: {city_pars(message.text)[1]}\n'
                              f'Часовой пояс: {city_pars(message.text)[2]}\n'
                              f'Код страны: {city_pars(message.text)[3]}')
    await message.answer(text='Теперь, введите здание', reply_markup=keyboards.menu)
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите здание')
async def chose_building_street(message: Message, state: FSMContext):
    await message.answer(text='Введите название улицы и номер здания через пробел\n'
                              'Пример: Baizakov 280\n')
    await state.set_state(EnterBuilding.enter_street)


@router.message(EnterBuilding.enter_street, F.text)
async def chose_building_floor(message: Message, state: FSMContext):
    await state.update_data(street=message.text)
    await message.answer(text='Укажите этаж')
    await state.set_state(EnterBuilding.enter_floor)


@router.message(StateFilter(EnterBuilding.enter_floor), F.text)
async def fill_building(message: Message, state: FSMContext):
    user_data = await state.get_data()
    data = user_data['street'], message.text
    db_entry.building_save(user_data['city_code'], data, message.from_user.id)
    await message.answer(text=f'Данные сохранены\n'
                              f'Адресс здания: {data[0]}\n'
                              f'Этаж: {data[1]}')
    await state.set_state(None)


@router.message(StateFilter(None), F.text)
async def empty_message(message: Message):
    await message.answer('Выбирете действие в меню', reply_markup=keyboards.menu)
    handlers_logger.info('Init empty message')
