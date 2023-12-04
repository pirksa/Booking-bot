from tsidpy import TSID

from parser import country_pars
from repository.repo import CountryRepository
from repository.transform import tuple_to_country
import datetime
import logging

db_entry_logger = logging.getLogger(__name__)


def country_save(message: str):
    repo_country = CountryRepository(table='countries', id_field='country_id')
    new_id = TSID.create().number
    repo_country[new_id] = tuple_to_country((new_id,) + country_pars(message) + (datetime.datetime.now(),))
    db_entry_logger.info(f"User's message: {message}, Formatted message: {country_pars(message)}")
    db_entry_logger.info(f"{repo_country[new_id]} saved to DB")
