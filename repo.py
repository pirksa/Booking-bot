import sqlite3

import transform
from model import Country, City, Building

__select_sql = 'SELECT * FROM'
__delete_sql = 'DELETE FROM'
__insert_sql = 'INSERT OR REPLACE INTO'
__select_count_sql = 'SELECT COUNT(*) FROM'


class Repository:
    con: property

    @property
    def con(self):
        return self.__con

    def __init__(self, **props):
        if props.get('connection'):
            self.__con = props.get('connection')
        else:
            self.__con = sqlite3.connect('rooms.sqlite')

    @staticmethod
    def set_id_field(value: dict):
        return list(value.items())[0][0]

    @staticmethod
    def set_table_name():
        pass

    def __getitem__(self, key):
        return self.get_by_id(key)

    def __setitem__(self, key, value):
        id_field = self.set_id_field(value)
        if not value[id_field]:
            value[id_field] = key
        if key != value[id_field]:
            raise ValueError
        self.save(**value)

    def __len__(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_count_sql"]} {self.set_table_name()}'
        res = cur.execute(query).fetchone()
        return int(res[0])

    def get_by_id(self, *id_value):
        pass

    def delete_by_id(self, *id_value):
        pass

    def save(self, **values):
        pass

    def get_all(self):
        pass


class CountryRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    @staticmethod
    def set_table_name():
        return 'countries'

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_country(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        country = Country(country_id=values['country_id'], country_code=values['country_code'],
                          country_name=values['country_name'])
        data = transform.country_to_tuple(country)
        query = f'{globals()["__insert_sql"]} countries VALUES (?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} countries'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_country(i) for i in res]


class CityRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    @staticmethod
    def set_table_name():
        return 'cities'

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_city(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        city = City(city_id=values['city_id'], city_code=values['city_code'],
                    city_name=values['city_name'], timezone=values['timezone'], country_id=values['country_id'])
        data = transform.city_to_tuple(city)
        query = f'{globals()["__insert_sql"]} cities VALUES (?, ?, ?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} cities'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_city(i) for i in res]


class BuildingRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    @staticmethod
    def set_table_name():
        return 'buildings'

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} buildings WHERE building_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_building(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} buildings WHERE building_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        building = Building(building_id=values['building_id'], city_id=values['city_id'], address=values['address'])
        data = transform.building_to_tuple(building)
        query = f'{globals()["__insert_sql"]} buildings VALUES (?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} buildings'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_building(i) for i in res]
