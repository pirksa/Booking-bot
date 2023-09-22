import sqlite3


class Repository:
    def __init__(self, table_name, id_name, id_value):
        self.table_name = table_name
        self.id_name = id_name
        self.id_value = id_value

    def get_by_id(self):
        con = sqlite3.connect('rooms.sqlite')
        cur = con.cursor()

        cur.execute(f"SELECT * FROM {self.table_name} WHERE {self.id_name} = {self.id_value}")
        result = cur.fetchall()
        con.close()
        return result

    def delete_by_id(self):
        con = sqlite3.connect('rooms.sqlite')
        cur = con.cursor()

        cur.execute(f"DELETE FROM {self.table_name} WHERE {self.id_name} = {self.id_value}")
        con.close()


class CountryRepository(Repository):
    def __init__(self, id_value, country_code_value, country_name_value, table_name='countries', id_name='country_id'):
        super().__init__(table_name, id_name, id_value)
        self.country_code_value = country_code_value
        self.country_name_value = country_name_value

    def save(self):
        con = sqlite3.connect('rooms.sqlite')
        cur = con.cursor()

        data = (self.id_value, self.country_code_value, self.country_name_value)
        insert_sql_query = f"INSERT INTO {self.table_name} VALUES (?, ?, ?)"
        cur.execute(insert_sql_query, data)
        con.commit()
        con.close()
