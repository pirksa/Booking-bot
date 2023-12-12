import psycopg2

from . import transform
from .model import Country, City, Building, Room

__select_sql = 'SELECT * FROM'
__delete_sql = 'DELETE FROM'
__insert_sql = 'INSERT INTO'
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
            self.__con = psycopg2.connect(database='rooms', user='admin', password='root', host='localhost')
        self.table = props.get('table')
        self.id_field = props.get('id_field')

    def __getitem__(self, key):
        return self.get_by_id(key)

    def __setitem__(self, key, value):
        if not getattr(value, self.id_field):
            setattr(value, self.id_field, key)
        if getattr(value, self.id_field) != key:
            raise ValueError
        self.save(entity=value)

    def __len__(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_count_sql"]} {self.table}'
        cur.execute(query)
        res = cur.fetchone()
        return int(res[0])

    def delete_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__delete_sql"]} {self.table} WHERE {self.id_field} = %s'
        cur.execute(query, id_value)
        self.con.commit()

    def get_by_id(self, *id_value: int):
        pass

    def save(self, entity: object):
        pass

    def get_all(self):
        pass


class CountryRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} countries WHERE country_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_country(res)

    def save(self, entity: Country):
        cur = self.con.cursor()
        data = transform.country_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} countries VALUES (%s, %s, %s, %s) ON CONFLICT (country_id) DO UPDATE ' \
                f'SET (country_code, country_name, last_updated) = (EXCLUDED.country_code, EXCLUDED.country_name,' \
                f' EXCLUDED.last_updated)'
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

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} cities WHERE city_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_city(res)

    def save(self, entity: City):
        cur = self.con.cursor()
        data = transform.city_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} cities VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (city_id) DO UPDATE ' \
                f'SET (city_code, city_name, timezone, country_id, last_updated) = (EXCLUDED.city_code, ' \
                f' EXCLUDED.city_name, EXCLUDED.timezone, EXCLUDED.country_id, EXCLUDED.last_updated)'
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

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} buildings WHERE building_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_building(res)

    def save(self, entity: Building):
        cur = self.con.cursor()
        data = transform.building_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} buildings VALUES (%s, %s, %s, %s) ON CONFLICT (building_id) DO UPDATE ' \
                f'SET (city_id, address, last_updated) =  (EXCLUDED.city_id, EXCLUDED.address, EXCLUDED.last_updated)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} buildings'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_building(i) for i in res]


class RoomRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} rooms WHERE room_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_room(res)

    def save(self, entity: Room):
        cur = self.con.cursor()
        data = transform.room_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} rooms VALUES (%s, %s, %s, %s, %s) ON CONFLICT (room_id) DO UPDATE ' \
                f' SET (building_id, floor, room_name, last_updated) = (EXCLUDED.building_id, EXCLUDED.floor, ' \
                f' EXCLUDED.last_updated)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_sql"]} rooms'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_room(i) for i in res]
