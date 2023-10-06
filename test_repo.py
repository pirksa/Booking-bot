from unittest import TestCase

from repo_temp import CountryRepository

import sqlite3


class Test(TestCase):
    def test_get_by_id_1(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        self.assertEqual("Country(1, KZ, Kazakhstan)", str(c.get_by_id(1)))

    def test_get_by_id_2(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        self.assertEqual("Country(2, UZ, Uzbekistan)", str(c.get_by_id(2)))

    def test_get_by_id_3(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        self.assertEqual("Entity doesn't exist", str(c.get_by_id(5)))

    def test_save_1(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(5)
        c.save(country_id=5, country_code='DE', country_name='Germany')
        self.assertEqual("Country(5, DE, Germany)", str(c.get_by_id(5)))

    def test_delete_by_id(self):
        c = CountryRepository(sqlite3.connect('rooms.sqlite'))
        c.delete_by_id(5)
        self.assertEqual("Entity doesn't exist", str(c.get_by_id(5)))
