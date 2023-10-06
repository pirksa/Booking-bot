from model import Country


class Repository:
    def __init__(self, con):
        self.con = con

    @staticmethod
    def select_sql_query(table_name, id_name):
        return f"SELECT * FROM {table_name} WHERE {id_name} = "

    @staticmethod
    def delete_sql_query(table_name, id_name):
        return f"DELETE FROM {table_name} WHERE {id_name} = "

    @staticmethod
    def insert_sql_query(table_name):
        return f"INSERT INTO {table_name} VALUES "

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
    def __init__(self, con):
        super().__init__(con)

    def tuple_to_class(self, data):
        country_id, country_code, country_name = data
        return Country(country_id, country_code, country_name)

    def class_to_tuple(self, country):
        return country.country_id, country.country_code, country.country_name

    def get_by_id(self, *id_value):
        cur = self.con.cursor()
        query = self.select_sql_query('countries', 'country_id') + '?'
        cur.execute(query, id_value)
        res = cur.fetchone()
        self.con.close()
        return "Entity doesn't exist" if not res else self.tuple_to_class(res)

    def delete_by_id(self, *id_value):
        cur = self.con.cursor()
        query = self.delete_sql_query('countries', 'country_id') + '?'
        cur.execute(query, id_value)
        self.con.commit()

    def save(self, **country):
        cur = self.con.cursor()
        country = Country(country['country_id'], country['country_code'], country['country_name'])
        data = self.class_to_tuple(country)
        query = self.insert_sql_query('countries') + '(?, ?, ?)'
        cur.execute(query, data)
        self.con.commit()

