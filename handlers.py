from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import db_entry
import keyboards
from parser import country_pars
from states import EnterMenu

router = Router(name=__name__)


@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(f'{message.from_user.first_name}, Приветствую!', reply_markup=keyboards.menu)


@router.message(Command('clear'))
async def clear_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Действие отменено')


@router.message(StateFilter(None), F.text == 'Введите страну')
async def chose_country(message: Message, state: FSMContext):
    await message.answer(text='Введите код страны, название страны через пробел\n'
                              'Пример: KZ Kazakhstan')
    await state.set_state(EnterMenu.select_country)


@router.message(StateFilter(None), F.text == 'Введите город')
async def chose_country(message: Message, state: FSMContext):
    await message.answer(text='Введите код города, название города, часовой пояс через пробел\n'
                              'Пример: ALA Almaty UTC+6')
    await state.set_state(EnterMenu.select_city)


@router.message(EnterMenu.select_country, F.text)
async def fill_country(message: Message, state: FSMContext):
    await state.update_data(country=message.text)
    db_entry.country_save(message.text)
    await message.answer(text=f'Данные сохранены:\n'
                              f'Код страны: {country_pars(message.text)[0]}\n'
                              f'Название старны: {country_pars(message.text)[1]}')
    await state.clear()


@router.message(EnterMenu.select_city, F.text)
async def fill_country(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text=f'Данные сохранены: {message.text}')
    await state.clear()
