from tsidpy import TSID

from parser import country_pars
from repository.repo import CountryRepository
from repository.transform import tuple_to_country


def country_save(message: str):
    repo_country = CountryRepository(table='countries', id_field='country_id')
    new_id = TSID.create().number
    repo_country[new_id] = tuple_to_country((new_id,) + country_pars(message))
