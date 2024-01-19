from aiogram.fsm.state import StatesGroup, State


class EnterMenu(StatesGroup):
    select_country = State()
    select_city = State()
    select_room = State()


class UserInfo(StatesGroup):
    user_data = State()


class EnterBuilding(StatesGroup):
    enter_street = State()
    enter_floor = State()
