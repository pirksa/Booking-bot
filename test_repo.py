from unittest import TestCase

from repo import CountryRepository
from model import Country

import sqlite3


class Test(TestCase):
    def test_get_by_id_country_1(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        kz = Country(country_id=1, country_code='KZ', country_name='Kazakhstan')
        self.assertEqual(kz, c.get_by_id(1))

    def test_get_by_id_country_2(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        uz = Country(country_id=2, country_code='UZ', country_name='Uzbekistan')
        self.assertEqual(uz, c.get_by_id(2))

    def test_get_by_id_country_3(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        self.assertEqual(None, c.get_by_id(5))

    def test_save_country_1(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(5)
        c.save(country_id=5, country_code='DE', country_name='Germany')
        self.assertEqual(Country(country_id=5, country_code='DE', country_name='Germany'), c.get_by_id(5))

    def test_delete_by_id_country_1(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(5)
        self.assertEqual(None, c.get_by_id(5))
