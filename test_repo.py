import unittest

from repo import CountryRepository, CityRepository
from model import Country, City

import sqlite3

from init_db import create_schema


class Test(unittest.TestCase):
    def setUp(self):
        create_schema()
        self.repo_country = CountryRepository()
        self.repo_city = CityRepository()

    def test_get_by_id_country_1(self):
        self.assertEqual(Country(country_id=1, country_code='KZ', country_name='Kazakhstan'), self.repo_country[1])

    def test_get_by_id_country_2(self):
        self.assertEqual(None, self.repo_country[5])

    def test_delete_by_id_country_1(self):
        self.repo_country.delete_by_id(1)
        self.assertEqual(None, self.repo_country[1])

    def test_save_country_1(self):
        self.repo_country[5] = {'country_id': 5, 'country_code': 'DE', 'country_name': 'Germany'}
        self.assertEqual(Country(country_id=5, country_code='DE', country_name='Germany'), self.repo_country[5])

    def test_save_country_2_update(self):
        self.repo_country[1] = {'country_id': 1, 'country_code': 'KZ', 'country_name': 'Kazakhstan'}
        self.assertEqual(Country(country_id=1, country_code='KZ', country_name='Kazakhstan'), self.repo_country[1])

    def test_get_all_country_1(self):
        res = [Country(country_id=1, country_code='KZ', country_name='Kazakhstan'),
               Country(country_id=2, country_code='UZ', country_name='Uzbekistan'),
               Country(country_id=3, country_code='RU', country_name='Russia'),
               Country(country_id=4, country_code='TR', country_name='Turkey')]
        self.assertEqual(res, self.repo_country.get_all())

    def test_number_of_row_country_1(self):
        self.assertEqual(4, len(self.repo_country))

    def test_get_by_id_city_1(self):
        res = City(city_id=1, city_code='ALA', city_name='Almaty', timezone='UTC+6', country_id=1)
        self.assertEqual(res, self.repo_city[1])

    def test_get_by_id_city_2(self):
        self.assertEqual(None, self.repo_city[6])

    def test_delete_by_id_city_1(self):
        self.repo_city.delete_by_id(1)
        self.assertEqual(None, self.repo_city[1])

    def test_save_city_1(self):
        self.repo_city[6] = {'city_id': 6, 'city_code': 'BER', 'city_name': 'Berlin', 'timezone': 'UTC+2',
                             'country_id': 5}
        res = City(city_id=6, city_code='BER', city_name='Berlin', timezone='UTC+2', country_id=5)
        self.assertEqual(res, self.repo_city[6])

    def test_save_city_2_update(self):
        self.repo_city[3] = {'city_id': 3, 'city_code': 'TAS', 'city_name': 'Tashkent', 'timezone': 'UTC+5',
                             'country_id': 2}
        res = City(city_id=3, city_code='TAS', city_name='Tashkent', timezone='UTC+5', country_id=2)
        self.assertEqual(res, self.repo_city[3])

    def test_get_all_city_1(self):
        res = [City(city_id=1, city_code='ALA', city_name='Almaty', timezone='UTC+6', country_id=1),
               City(city_id=2, city_code='TSE', city_name='Astana', timezone='UTC+6', country_id=1),
               City(city_id=3, city_code='TAS', city_name='Tashkent', timezone='UTC+5', country_id=2),
               City(city_id=4, city_code='MOW', city_name='Moscow', timezone='UTC+3', country_id=3),
               City(city_id=5, city_code='IST', city_name='Istanbul', timezone='UTC+3', country_id=4)]
        self.assertEqual(res, self.repo_city.get_all())

    def test_number_of_rows_city(self):
        self.assertEqual(5, len(self.repo_city))


if __name__ == '__main__':
    unittest.main()
