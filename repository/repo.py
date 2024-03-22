import psycopg2

from settings import load_config
from . import transform
from .model import Country, City, Building, Company, Room, User, Booking

config = load_config()
__select_sql = 'SELECT'
__select_all_sql = 'SELECT * FROM'
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
            self.__con = psycopg2.connect(database=config['db']['database'], user=config['db']['user'],
                                          password=config['db']['password'], host=config['db']['host'])
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

    def get_id_by_value(self, value_field: str, value: str):
        cur = self.con.cursor()
        query = f"{globals()['__select_sql']} {self.id_field} FROM {self.table} WHERE {value_field} = '%s'" % value
        cur.execute(query)
        return cur.fetchone()

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
        query = f'{globals()["__select_all_sql"]} countries WHERE country_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_country(res)

    def save(self, entity: Country):
        cur = self.con.cursor()
        data = transform.country_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} countries VALUES (%s, %s, %s, %s, %s) ON CONFLICT (country_id) DO UPDATE' \
                f' SET (country_code, country_name, last_updated, last_updated_by) = (EXCLUDED.country_code,' \
                f' EXCLUDED.country_name, EXCLUDED.last_updated, EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} countries'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_country(i) for i in res]


class CityRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} cities WHERE city_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_city(res)

    def save(self, entity: City):
        cur = self.con.cursor()
        data = transform.city_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} cities VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (city_id) ' \
                f'DO UPDATE SET (city_code, city_name, timezone, country_id, last_updated,' \
                f'last_updated_by) = (EXCLUDED.city_code, EXCLUDED.city_name, EXCLUDED.timezone,' \
                f'EXCLUDED.country_id, EXCLUDED.last_updated, EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} cities'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_city(i) for i in res]


class BuildingRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} buildings WHERE building_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_building(res)

    def save(self, entity: Building):
        cur = self.con.cursor()
        data = transform.building_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} buildings VALUES (%s, %s, %s, %s, %s) ON CONFLICT (building_id) ' \
                f'DO UPDATE SET (city_id, address, last_updated, last_updated_by) =  (EXCLUDED.city_id,' \
                f'EXCLUDED.address, EXCLUDED.last_updated, EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} buildings'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_building(i) for i in res]


class CompanyRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} companies WHERE company_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_company(res)

    def save(self, entity: Company):
        cur = self.con.cursor()
        data = transform.company_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} companies VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (company_id) ' \
                f'DO UPDATE SET (company_name, floor, building_id, last_updated, last_updated_by) = ' \
                f'(EXCLUDED.company_name, EXCLUDED.floor, EXCLUDED.building_id, EXCLUDED.last_updated, ' \
                f'EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} companies'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_company(i) for i in res]


class RoomRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} rooms WHERE room_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_room(res)

    def save(self, entity: Room):
        cur = self.con.cursor()
        data = transform.room_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} rooms VALUES (%s, %s, %s, %s, %s) ON CONFLICT (room_id) DO UPDATE ' \
                f' SET (company_id, room_name, last_updated, last_updated_by) = (EXCLUDED.company_id,' \
                f' EXCLUDED.room_name, EXCLUDED.last_updated, EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} rooms'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_room(i) for i in res]


class BookingRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} bookings WHERE booking_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_booking(res)

    def save(self, entity: Booking):
        cur = self.con.cursor()
        data = transform.booking_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} bookings VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT ' \
                f'(booking_id) DO UPDATE SET (user_id, room_id, booking_date, start_time, end_time, last_updated, ' \
                f'last_updated_by) = (EXCLUDED.user_id, EXCLUDED.room_id, EXCLUDED.booking_date, EXCLUDED.start_time, ' \
                f'EXCLUDED.end_time, EXCLUDED.last_updated, EXCLUDED.last_updated_by)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_count_sql"]} bookings'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_booking(i) for i in res]


class UserRepository(Repository):
    def __init__(self, **props):
        super().__init__(**props)

    def get_by_id(self, *id_value: int):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} users WHERE user_id = %s'
        cur.execute(query, id_value)
        res = cur.fetchone()
        return transform.tuple_to_user(res)

    def save(self, entity: User):
        cur = self.con.cursor()
        data = transform.user_to_tuple(entity)
        query = f'{globals()["__insert_sql"]} users VALUES (%s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE' \
                f' SET (user_name, phone_number, join_date) = (EXCLUDED.user_name, EXCLUDED.phone_number,' \
                f' EXCLUDED.join_date)'
        cur.execute(query, data)
        self.con.commit()

    def get_all(self):
        cur = self.con.cursor()
        query = f'{globals()["__select_all_sql"]} users'
        cur.execute(query)
        res = cur.fetchall()
        return [transform.tuple_to_user(i) for i in res]
