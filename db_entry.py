import datetime
import logging

from tsidpy import TSID

from parser import country_pars, city_pars
from repository.repo import CountryRepository, CityRepository
from repository.transform import tuple_to_country, tuple_to_city

db_entry_logger = logging.getLogger(__name__)


def country_save(message: str):
    repo_country = CountryRepository(table='countries', id_field='country_id')
    country_id = TSID.create().number
    repo_country[country_id] = tuple_to_country((country_id,) + country_pars(message) + (datetime.datetime.now(),))
    db_entry_logger.info(f"User's message: {message}")
    db_entry_logger.info(f"User's formatted message: {country_pars(message)}")
    db_entry_logger.info(f"{(country_id,) + country_pars(message) + (datetime.datetime.now(),)}")
    db_entry_logger.info(f"{repo_country[country_id]} saved to DB")


def city_save(message: str):
    repo_city = CityRepository(table='cities', id_field='city_id')
    city_id = TSID.create().number
    repo_country = CountryRepository(table='countries', id_field='country_id')
    country_id = repo_country.get_id_by_value(value_field='country_code', value=city_pars(message)[-1])
    repo_city[city_id] = tuple_to_city((city_id,) + city_pars(message)[:-1] + country_id + (datetime.datetime.now(),))
    db_entry_logger.info(f"User's message: {message}")
    db_entry_logger.info(f"User's formatted message: {city_pars(message)}")
    db_entry_logger.info(f"{(city_id,) + city_pars(message)[:-1] + country_id + (datetime.datetime.now(),)}")
    db_entry_logger.info(f"{repo_city[city_id]} saved to DB")
