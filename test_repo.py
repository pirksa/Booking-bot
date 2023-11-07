import unittest

from tsidpy import TSID

from create_data import insert_data
from init_db import create_schema
from model import Country, City, Building
from repo import CountryRepository, CityRepository, BuildingRepository


class Test(unittest.TestCase):
    def setUp(self):
        create_schema()
        insert_data()
        self.repo_country = CountryRepository(table='countries', id_field='country_id')
        self.repo_city = CityRepository(table='cities', id_field='city_id')
        self.repo_building = BuildingRepository(table='buildings', id_field='building_id')

    def test_get_by_id_country_1(self):
        self.assertEqual(Country(country_id=1, country_code='KZ', country_name='Kazakhstan'), self.repo_country[1])

    def test_get_by_id_country_2(self):
        new_id = TSID.create().number
        self.assertEqual(None, self.repo_country[new_id])

    def test_delete_by_id_country_1(self):
        self.repo_country.delete_by_id(1)
        self.assertEqual(None, self.repo_country[1])

    def test_save_country_1(self):
        new_id = TSID.create().number
        self.repo_country[new_id] = Country(country_id=None, country_code='DE', country_name='Germany')
        self.assertEqual(Country(country_id=new_id, country_code='DE', country_name='Germany'),
                         self.repo_country[new_id])

    def test_save_country_2_update(self):
        self.repo_country[1] = Country(country_id=1, country_code='KZ', country_name='Kazakhstan')
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
        new_id = TSID.create().number
        self.assertEqual(None, self.repo_city[new_id])

    def test_delete_by_id_city_1(self):
        self.repo_city.delete_by_id(1)
        self.assertEqual(None, self.repo_city[1])

    def test_save_city_1(self):
        new_id = TSID.create().number
        self.repo_city[new_id] = City(city_id=new_id, city_code='BER', city_name='Berlin', timezone='UTC+2',
                                      country_id=5)
        res = City(city_id=new_id, city_code='BER', city_name='Berlin', timezone='UTC+2', country_id=5)
        self.assertEqual(res, self.repo_city[new_id])

    def test_save_city_2_update(self):
        self.repo_city[3] = City(city_id=3, city_code='TAS', city_name='Tashkent', timezone='UTC+5', country_id=2)
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

    def test_get_by_id_building_1(self):
        self.assertEqual(Building(building_id=1, city_id=1, address='Khodzhanova str., 2/2'), self.repo_building[1])

    def test_get_by_id_building_2(self):
        new_id = TSID.create().number
        self.assertEqual(None, self.repo_building[new_id])

    def test_delete_by_id_building_1(self):
        self.repo_building.delete_by_id(1)
        self.assertEqual(None, self.repo_building[1])

    def test_save_building_1(self):
        new_id = TSID.create().number
        self.repo_building[new_id] = Building(building_id=new_id, city_id=6, address='Default address')
        self.assertEqual(Building(building_id=new_id, city_id=6, address='Default address'),
                         self.repo_building[new_id])

    def test_save_building_2_update(self):
        self.repo_building[1] = Building(building_id=1, city_id=1, address='Khodzhanova str., 2/2')
        self.assertEqual(Building(building_id=1, city_id=1, address='Khodzhanova str., 2/2'), self.repo_building[1])

    def test_get_all_building_1(self):
        res = [Building(building_id=1, city_id=1, address='Khodzhanova str., 2/2'),
               Building(building_id=2, city_id=2, address='Mangilik El Ave. 55/8, Block C 4.6'),
               Building(building_id=3, city_id=3, address='Default address'),
               Building(building_id=4, city_id=4, address='Default address'),
               Building(building_id=5, city_id=5, address='Default address')]
        self.assertEqual(res, self.repo_building.get_all())

    def test_number_of_row_building_1(self):
        self.assertEqual(5, len(self.repo_building))


if __name__ == '__main__':
    unittest.main()
