import datetime
import logging

from tsidpy import TSID

from parser import country_pars, city_pars
from repository.repo import CountryRepository, CityRepository, BuildingRepository, CompanyRepository, UserRepository, \
    RoomRepository, BookingRepository
from repository.transform import tuple_to_country, tuple_to_city, tuple_to_user, tuple_to_building, tuple_to_room, \
    tuple_to_company, tuple_to_booking

db_entry_logger = logging.getLogger(__name__)


def country_save(message: str, user_id: int):
    repo_country = CountryRepository(table='countries', id_field='country_id')
    country_id = TSID.create().number
    repo_country[country_id] = tuple_to_country((country_id, *country_pars(message), datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's message: {message}")
    db_entry_logger.info(f"User's formatted message: {country_pars(message)}")
    db_entry_logger.info(f"{(country_id, *country_pars(message), datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_country[country_id]} saved to DB")


def city_save(country_code: str, message: str, user_id: int):
    repo_city = CityRepository(table='cities', id_field='city_id')
    city_id = TSID.create().number
    repo_country = CountryRepository(table='countries', id_field='country_id')
    country_id = repo_country.get_id_by_value(value_field='country_code', value=country_code)
    repo_city[city_id] = tuple_to_city((city_id, *city_pars(message), country_id,
                                        datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's message: {message}")
    db_entry_logger.info(f"User's formatted message: {city_pars(message)}")
    db_entry_logger.info(f"{(city_id, *city_pars(message), country_id, datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_city[city_id]} saved to DB")


def building_save(city_code: str, data: str, user_id: int):
    repo_building = BuildingRepository(table='buildings', id_field='building_id')
    building_id = TSID.create().number
    repo_city = CityRepository(table='cities', id_field='city_id')
    city_id = repo_city.get_id_by_value(value_field='city_code', value=city_code)
    repo_building[building_id] = tuple_to_building((building_id, city_id, data, datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's data: {data}")
    db_entry_logger.info(f"{(building_id, city_id, data, datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_building[building_id]} saved to DB")


def company_save(data: tuple, building_address: str, user_id: int):
    repo_company = CompanyRepository(table='companies', id_field='company_id')
    company_id = TSID.create().number
    repo_building = BuildingRepository(table='buildings', id_field='building_id')
    building_id = repo_building.get_id_by_value(value_field='address', value=building_address)
    repo_company[company_id] = tuple_to_company((company_id, *data, building_id, datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's data: {data}")
    db_entry_logger.info(f"{(company_id, *data, building_id, datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_company[company_id]} saved to DB")


def room_save(message: str, user_id: int, floor: str):
    repo_room = RoomRepository(table='rooms', id_field='room_id')
    room_id = TSID.create().number
    repo_company = CompanyRepository(table='companies', id_field='company_id')
    company_id = repo_company.get_id_by_value(value_field='floor', value=floor)
    repo_room[room_id] = tuple_to_room((room_id, company_id, message, datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's data: {message}")
    db_entry_logger.info(f"{(room_id, company_id, message, datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_room[room_id]} saved to DB")


def booking_save(data: tuple, room_name: str, user_id: int):
    repo_booking = BookingRepository(table='bookings', id_field='booking_id')
    booking_id = TSID.create().number
    repo_room = RoomRepository(table='rooms', id_field='room_id')
    room_id = repo_room.get_id_by_value(value_field='room_name', value=room_name)
    repo_booking[booking_id] = tuple_to_booking((booking_id, user_id, room_id, *data, datetime.datetime.now(), user_id))
    db_entry_logger.info(f"User's data: {data}")
    db_entry_logger.info(f"{(booking_id, user_id, room_id, *data, datetime.datetime.now(), user_id)}")
    db_entry_logger.info(f"{repo_booking[booking_id]} saved to DB")


def user_save(data: tuple):
    repo_user = UserRepository(table='users', id_field='user_id')
    repo_user[data[0]] = tuple_to_user(data + (datetime.datetime.now(),))
    db_entry_logger.info(f"User's data: {data}")
    db_entry_logger.info(f"{repo_user[data[0]]} saved to DB")
