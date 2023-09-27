import sqlite3
from model import Country

con = sqlite3.connect('rooms.sqlite')
cur = con.cursor()


class Repository:
    def __init__(self, id_value):
        self.id_value = id_value

    def get_by_id(self):
        pass

    def delete_by_id(self):
        pass

    def save(self):
        pass

    def tuple_to_class(self, data):
        pass

    def class_to_tuple(self, entity):
        pass


class CountryRepository(Repository):
    def __init__(self, id_value, country_code_value, country_name_value):
        super().__init__(id_value)
        self.country_code_value = country_code_value
        self.country_name_value = country_name_value

    def tuple_to_class(self, data):
        country_id, country_name, country_code = data
        return Country(country_id, country_name, country_code)

    def class_to_tuple(self, country):
        return country.country_id, country.country_name, country.country_code

    def get_by_id(self):
        select_sql_query = "SELECT * FROM countries WHERE country_id = ?"
        cur.execute(select_sql_query, self.id_value)
        res = cur.fetchall()
        return self.tuple_to_class(res)

    def delete_by_id(self):
        delete_sql_query = "DELETE FROM countries WHERE country_id = ?"
        cur.execute(delete_sql_query, self.id_value)

    def save(self):
        country = Country(self.id_value, self.country_code_value, self.country_name_value)
        data = self.class_to_tuple(country)
        insert_sql_query = "INSERT INTO countries VALUES (?, ?, ?)"
        cur.execute(insert_sql_query, data)
        con.commit()


con.close()
