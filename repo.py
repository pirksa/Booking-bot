import sqlite3
from model import Country, City


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

    def get_by_id(self, *id_value):
        pass

    def delete_by_id(self, *id_value):
        pass

    def save(self, **values):
        pass

    def get_all(self):
        pass

    @staticmethod
    def tuple_to_class(data):
        pass

    @staticmethod
    def class_to_tuple(entity):
        pass


class CountryRepository(Repository):
    __select_sql = 'SELECT * FROM'
    __delete_sql = 'DELETE FROM'
    __insert_sql = 'INSERT INTO'

    def __init__(self, **props):
        super().__init__(**props)

    @staticmethod
    def tuple_to_class(data):
        if not data:
            return None
        else:
            return Country(country_id=data[0], country_code=data[1], country_name=data[2])

    @staticmethod
    def class_to_tuple(country):
        return country.country_id, country.country_code, country.country_name

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{self.__select_sql} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        self.con.close()
        return self.tuple_to_class(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{self.__delete_sql} countries WHERE country_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        country = Country(country_id=values['country_id'], country_code=values['country_code'],
                          country_name=values['country_name'])
        data = self.class_to_tuple(country)
        query = f'{self.__insert_sql} countries VALUES (?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{self.__select_sql} countries'
        cur.execute(query)
        res = cur.fetchall()
        self.con.close()
        return [self.tuple_to_class(i) for i in res]


class CityRepository(Repository):
    __select_sql = 'SELECT * FROM'
    __delete_sql = 'DELETE FROM'
    __insert_sql = 'INSERT INTO'

    def __init__(self, **props):
        super().__init__(**props)

    @staticmethod
    def tuple_to_class(data):
        if not data:
            return None
        else:
            return City(city_id=data[0], city_code=data[1], city_name=data[2], timezone=data[3], country_id=data[4])

    @staticmethod
    def class_to_tuple(city):
        return city.city_id, city.city_code, city.city_name, city.timezone, city.country_id

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{self.__select_sql} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        self.con.close()
        return self.tuple_to_class(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = f'{self.__delete_sql} cities WHERE city_id = ?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **values):
        cur = self.con.cursor()
        city = City(cityy_id=values['city_id'], city_code=values['city_code'],
                    city_name=values['city_name'], timezone=values['timezone'], country_id=values['country_id'])
        data = self.class_to_tuple(city)
        query = f'{self.__insert_sql} cities VALUES (?, ?, ?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{self.__select_sql} cities'
        cur.execute(query)
        res = cur.fetchall()
        self.con.close()
        return [self.tuple_to_class(i) for i in res]
