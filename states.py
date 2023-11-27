from aiogram.fsm.state import StatesGroup, State


class EnterMenu(StatesGroup):
    select_country = State()
    select_city = State()
