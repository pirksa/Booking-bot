import datetime
import logging

import psycopg2
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
    con = psycopg2.connect(database='rooms', user='admin', password='root', host='localhost')
    cur = con.cursor()
    query = f"SELECT country_id FROM countries WHERE country_code = '%s'" % (city_pars(message)[-1])
    cur.execute(query)
    res = cur.fetchone()
    repo_city[city_id] = tuple_to_city((city_id,) + city_pars(message)[:-1] + res + (datetime.datetime.now(),))
    db_entry_logger.info(f"User's message: {message}")
    db_entry_logger.info(f"User's formatted message: {city_pars(message)}")
    db_entry_logger.info(f"{(city_id,) + city_pars(message)[:-1] + (res,) + (datetime.datetime.now(),)}")
    db_entry_logger.info(f"{repo_city[city_id]} saved to DB")
