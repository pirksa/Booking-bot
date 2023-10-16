from unittest import TestCase

from repo import CountryRepository, CityRepository
from model import Country, City

import sqlite3

from init_db import create_schema


class Test(TestCase):
    def test_get_by_id_country_1(self):
        create_schema()
        c = CountryRepository(connection=sqlite3.connect('rooms.sqlite'))
        res = Country(country_id=1, country_code='KZ', country_name='Kazakhstan')
        self.assertEqual(res, c.get_by_id(1))

    def test_get_by_id_country_2(self):
        create_schema()
        c = CountryRepository(connection=sqlite3.connect('rooms.sqlite'))
        self.assertEqual(None, c.get_by_id(5))

    def test_delete_by_id_country_1(self):
        create_schema()
        c = CountryRepository(connection=sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(1)
        self.assertEqual(None, c.get_by_id(1))

    def test_save_country_1(self):
        create_schema()
        c = CountryRepository(connection=sqlite3.connect('rooms.sqlite'))
        c.save(country_id=5, country_code='DE', country_name='Germany')
        res = Country(country_id=5, country_code='DE', country_name='Germany')
        self.assertEqual(res, c.get_by_id(5))

    def test_get_all_country_1(self):
        create_schema()
        c = CountryRepository(connection=sqlite3.connect('rooms.sqlite'))
        res = [Country(country_id=1, country_code='KZ', country_name='Kazakhstan'),
               Country(country_id=2, country_code='UZ', country_name='Uzbekistan'),
               Country(country_id=3, country_code='RU', country_name='Russia'),
               Country(country_id=4, country_code='TR', country_name='Turkey')]
        self.assertEqual(res, c.get_all())

    def test_get_by_id_city_1(self):
        create_schema()
        c = CityRepository(connection=sqlite3.connect('rooms.sqlite'))
        res = City(city_id=1, city_code='ALA', city_name='Almaty', timezone='UTC+6', country_id=1)
        self.assertEqual(res, c.get_by_id(1))

    def test_get_by_id_city_2(self):
        create_schema()
        c = CityRepository(connection=sqlite3.connect('rooms.sqlite'))
        self.assertEqual(None, c.get_by_id(6))

    def test_delete_by_id_city_1(self):
        create_schema()
        c = CityRepository(connection=sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(1)
        self.assertEqual(None, c.get_by_id(1))

    def test_save_city_1(self):
        create_schema()
        c = CityRepository(connection=sqlite3.connect('rooms.sqlite'))
        c.save(city_id=6, city_code='BER', city_name='Berlin', timezone='UTC+2', country_id=5)
        res = City(city_id=6, city_code='BER', city_name='Berlin', timezone='UTC+2', country_id=5)
        self.assertEqual(res, c.get_by_id(6))

    def test_get_all_city_1(self):
        create_schema()
        c = CityRepository(connection=sqlite3.connect('rooms.sqlite'))
        res = [City(city_id=1, city_code='ALA', city_name='Almaty', timezone='UTC+6', country_id=1),
               City(city_id=2, city_code='TSE', city_name='Astana', timezone='UTC+6', country_id=1),
               City(city_id=3, city_code='TAS', city_name='Tashkent', timezone='UTC+5', country_id=2),
               City(city_id=4, city_code='MOW', city_name='Moscow', timezone='UTC+3', country_id=3),
               City(city_id=3, city_code='IST', city_name='Istanbul', timezone='UTC+3', country_id=4)]
        self.assertEqual(res, c.get_all())
