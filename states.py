from aiogram.fsm.state import StatesGroup, State


class EnterMenu(StatesGroup):
    select_country = State()
    select_city = State()
    select_building = State()
    select_room = State()


class UserInfo(StatesGroup):
    user_data = State()


class EnterCompany(StatesGroup):
    enter_company_name = State()
    enter_floor = State()


class EnterBooking(StatesGroup):
    enter_date = State()
    enter_start_time = State()
    enter_end_time = State()
