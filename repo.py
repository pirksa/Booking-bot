from model import Country


class Repository:
    def __init__(self, con):
        self.con = con

    def get_by_id(self, id_value):
        pass

    def delete_by_id(self):
        pass

    def save(self):
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

    def __init__(self, con):
        super().__init__(con)

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
