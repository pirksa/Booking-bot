class Country:
    country_id: int
    country_code: str
    country_name: str

    def __init__(self, **props):
        self.country_id = props.get('country_id', None)
        self.country_code = props.get('country_code', None)
        self.country_name = props.get('country_name', None)

    def __eq__(self, other):
        if not isinstance(other, Country):
            raise ValueError
        other = other.country_id, other.country_code, other.country_name
        return (self.country_id, self.country_code, self.country_name) == other


class City:
    def __init__(self, city_id, city_code, city_name, timezone):
        self.city_id = city_id
        self.city_code = city_code
        self.city_name = city_name
        self.timezone = timezone


class Building:
    def __init__(self, building_id, address):
        self.building_id = building_id
        self.address = address


class Room:
    def __init__(self, room_id, floor, room_name):
        self.room_id = room_id
        self.floor = floor
        self.room_name = room_name


class Company:
    def __init__(self, company_id, company_name):
        self.company_id = company_id
        self.company_name = company_name


class User:
    def __init__(self, user_id, user_name, department, job_position):
        self.user_id = user_id
        self.user_name = user_name
        self.department = department
        self.job_position = job_position
