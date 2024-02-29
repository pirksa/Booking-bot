import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import db_entry
import keyboards
from parser import country_pars, city_pars
from states import EnterMenu, UserInfo, EnterCompany, EnterBooking

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
    await state.set_state(None)
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
    await state.update_data(country_code=country_pars(message.text)[0])
    db_entry.country_save(message=message.text, user_id=message.from_user.id)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код страны: {country_pars(message.text)[0]}\n'
                              f'Старна: {country_pars(message.text)[1]}')
    await message.answer(text='Теперь, введите город', reply_markup=keyboards.menu)
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите город')
async def chose_cty(message: Message, state: FSMContext):
    await message.answer(text='Введите код города, название города, часовой пояс через пробел\n'
                              'Пример: ALA Almaty UTC+6')
    await state.set_state(EnterMenu.select_city)
    handlers_logger.info("Init button 'Enter city'")


@router.message(EnterMenu.select_city, F.text)
async def fill_city(message: Message, state: FSMContext):
    await state.update_data(city_code=city_pars(message.text)[0])
    user_data = await state.get_data()
    db_entry.city_save(country_code=user_data['country_code'], message=message.text, user_id=message.from_user.id)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код города: {city_pars(message.text)[0]}\n'
                              f'Город: {city_pars(message.text)[1]}\n'
                              f'Часовой пояс: {city_pars(message.text)[2]}')
    await message.answer(text='Теперь, введите здание', reply_markup=keyboards.menu)
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите здание')
async def chose_building_street(message: Message, state: FSMContext):
    await message.answer(text='Введите название улицы и номер здания через пробел\n'
                              'Пример: Baizakov 280')
    await state.set_state(EnterMenu.select_building)


@router.message(StateFilter(EnterMenu.select_building), F.text)
async def fill_building(message: Message, state: FSMContext):
    user_data = await state.get_data()
    db_entry.building_save(city_code=user_data['city_code'], data=message.text, user_id=message.from_user.id)
    await message.answer(text=f'Данные сохранены\n'
                              f'Адресс здания: {message.text}')
    await message.answer(text='Теперь введите компанию', reply_markup=keyboards.menu)
    await state.update_data(address=message.text)
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите компанию')
async def chose_company_name(message: Message, state: FSMContext):
    await message.answer(text='Введите название компании\n'
                              'Пример: Smart.Point')
    await state.set_state(EnterCompany.enter_company_name)
    handlers_logger.info("Init button 'Enter company'")


@router.message(EnterCompany.enter_company_name, F.text)
async def chose_company_floor(message: Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await message.answer(text='Укажите этаж')
    await state.set_state(EnterCompany.enter_floor)


@router.message(StateFilter(EnterCompany.enter_floor), F.text)
async def fill_company(message: Message, state: FSMContext):
    user_data = await state.get_data()
    data = user_data['company_name'], message.text
    db_entry.company_save(data=data, building_address=user_data['address'], user_id=message.from_user.id)
    await message.answer(text=f'Данные сохранены\n'
                              f'Название компании: {data[0]}\n'
                              f'Этаж: {data[1]}')
    await message.answer(text='Теперь введите помещение', reply_markup=keyboards.menu)
    await state.update_data(floor=data[1])
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите помещение')
async def chose_room(message: Message, state: FSMContext):
    await message.answer(text='Введите название помещения\n'
                              'Пример: Meeting room')
    await state.set_state(EnterMenu.select_room)
    handlers_logger.info("Init button 'Enter room'")


@router.message(StateFilter(EnterMenu.select_room), F.text)
async def fill_room(message: Message, state: FSMContext):
    user_data = await state.get_data()
    db_entry.room_save(message=message.text, user_id=message.from_user.id, floor=user_data['floor'])
    await message.answer(text=f'Данные сохранены\n'
                              f'Название помещения: {message.text}')
    await message.answer(text='Теперь введите бронирование', reply_markup=keyboards.menu)
    await state.update_data(room_name=message.text)
    await state.set_state(None)


@router.message(StateFilter(None), F.text == 'Введите бронирование')
async def chose_booking_date(message: Message, state: FSMContext):
    await message.answer(text='Укажите дату бронирования\n'
                              'Пример: 2024-01-01')
    await state.set_state(EnterBooking.enter_date)
    handlers_logger.info("Init button 'Enter booking'")


@router.message(StateFilter(EnterBooking.enter_date), F.text)
async def chose_start_time(message: Message, state: FSMContext):
    await state.update_data(booking_date=message.text)
    await message.answer(text='Укажите время начала\n'
                              'Пример: 11:00')
    await state.set_state(EnterBooking.enter_start_time)


@router.message(StateFilter(EnterBooking.enter_start_time), F.text)
async def chose_end_time(message: Message, state: FSMContext):
    await state.update_data(start_time=message.text)
    await message.answer(text='Укажите время окончания\n'
                              'Пример: 13:00')
    await state.set_state(EnterBooking.enter_end_time)


@router.message(StateFilter(EnterBooking.enter_end_time), F.text)
async def fill_booking(message: Message, state: FSMContext):
    user_data = await state.get_data()
    data = user_data['booking_date'], user_data['start_time'], message.text
    db_entry.booking_save(data=data, room_name=user_data['room_name'], user_id=message.from_user.id)
    await message.answer(text='Данные сохранены\n'
                              f'Дата бронирования: {data[0]}\n'
                              f'Время начала: {data[1]}\n'
                              f'Время окончания: {data[2]}')
    await state.set_state(None)


@router.message(StateFilter(None), F.text)
async def empty_message(message: Message):
    await message.answer('Выбирете действие в меню', reply_markup=keyboards.menu)
    handlers_logger.info('Init empty message')
