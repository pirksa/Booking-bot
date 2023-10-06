class Country:
    def __init__(self, country_id, country_code, country_name):
        self.country_id = country_id
        self.country_code = country_code
        self.country_name = country_name

    def __str__(self):
        return f"Country({self.country_id}, {self.country_code}, {self.country_name})"


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
