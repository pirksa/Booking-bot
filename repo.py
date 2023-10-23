import sqlite3
from transform import *


__select_sql = 'SELECT * FROM'
__delete_sql = 'DELETE FROM'
__insert_sql = 'INSERT OR REPLACE INTO'


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

    def __getitem__(self, key):
        return self.get_by_id(key)

    def __setitem__(self, key, value):
        if key != value['id']:
            raise ValueError
        else:
            self.save(**value)

    def __len__(self):
        pass

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

    def __setitem__(self, key, value):
        if key != value['country_id']:
            raise ValueError
        else:
            self.save(**value)

    def __len__(self):
        cur = self.con.cursor()
        res = cur.execute('SELECT COUNT(*) FROM countries').fetchone()
        return int(res[0])

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return tuple_to_country(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        country = Country(country_id=values['country_id'], country_code=values['country_code'],
                          country_name=values['country_name'])
        data = country_to_tuple(country)
        query = f'{globals()["__insert_sql"]} countries VALUES (?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} countries'
        cur.execute(query)
        res = cur.fetchall()
        return [tuple_to_country(i) for i in res]


class CityRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def __setitem__(self, key, value):
        if key != value['city_id']:
            raise ValueError
        else:
            self.save(**value)

    def __len__(self):
        cur = self.con.cursor()
        res = cur.execute('SELECT COUNT(*) FROM cities').fetchone()
        return int(res[0])

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return tuple_to_city(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        city = City(city_id=values['city_id'], city_code=values['city_code'],
                    city_name=values['city_name'], timezone=values['timezone'], country_id=values['country_id'])
        data = city_to_tuple(city)
        query = f'{globals()["__insert_sql"]} cities VALUES (?, ?, ?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} cities'
        cur.execute(query)
        res = cur.fetchall()
        return [tuple_to_city(i) for i in res]
