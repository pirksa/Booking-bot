from . import transform


class Country:
    def __init__(self, **props):
        self.country_id = props.get('country_id')
        self.country_code = props.get('country_code')
        self.country_name = props.get('country_name')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f"Country({self.country_id}, {self.country_code}, {self.country_name}, {self.last_updated}," \
               f" {self.last_updated_by})"

    def __eq__(self, other):
        return transform.country_to_tuple(self) == transform.country_to_tuple(other)


class City:
    def __init__(self, **props):
        self.city_id = props.get('city_id')
        self.city_code = props.get('city_code')
        self.city_name = props.get('city_name')
        self.timezone = props.get('timezone')
        self.country_id = props.get('country_id')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f'City({self.city_id}, {self.city_code}, {self.city_name}, {self.timezone}, {self.country_id}, ' \
               f'{self.last_updated}, {self.last_updated_by})'

    def __eq__(self, other):
        return transform.city_to_tuple(self) == transform.city_to_tuple(other)


class Building:
    def __init__(self, **props):
        self.building_id = props.get('building_id')
        self.city_id = props.get('city_id')
        self.address = props.get('address')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f'Building({self.building_id}, {self.city_id}, {self.address}, {self.last_updated}, ' \
               f' {self.last_updated_by})'

    def __eq__(self, other):
        return transform.building_to_tuple(self) == transform.building_to_tuple(other)


class Company:
    def __init__(self, **props):
        self.company_id = props.get('company_id')
        self.company_name = props.get('company_name')
        self.floor = props.get('floor')
        self.building_id = props.get('building_id')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f'Company({self.company_id}, {self.company_name}, {self.floor}), {self.building_id},' \
               f' {self.last_updated}, {self.last_updated_by})'

    def __eq__(self, other):
        return transform.company_to_tuple(self) == transform.company_to_tuple(other)


class Room:
    def __init__(self, **props):
        self.room_id = props.get('room_id')
        self.company_id = props.get('company_id')
        self.room_name = props.get('room_name')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f'Room({self.room_id}, {self.company_id}, {self.room_name}), {self.last_updated},' \
               f' {self.last_updated_by})'

    def __eq__(self, other):
        return transform.room_to_tuple(self) == transform.room_to_tuple(other)


class User:
    def __init__(self, **props):
        self.user_id = props.get('user_id')
        self.user_name = props.get('user_name')
        self.phone_number = props.get('phone_number')
        self.join_date = props.get('join_date')

    def __str__(self):
        return f'User({self.user_id}, {self.user_name}, {self.phone_number}, {self.join_date})'

    def __eq__(self, other):
        return transform.user_to_tuple(self) == transform.user_to_tuple(other)


class Booking:
    def __init__(self, **props):
        self.booking_id = props.get('booking_id')
        self.user_id = props.get('user_id')
        self.room_id = props.get('room_id')
        self.booking_date = props.get('booking_date')
        self.start_time = props.get('start_time')
        self.end_time = props.get('end_time')
        self.last_updated = props.get('last_updated')
        self.last_updated_by = props.get('last_updated_by')

    def __str__(self):
        return f'Booking({self.booking_id}, {self.user_id}, {self.room_id}, {self.booking_date}, {self.start_time},' \
               f'{self.end_time}, {self.last_updated}, {self.last_updated_by})'

    def __eq__(self, other):
        return transform.booking_to_tuple(self) == transform.booking_to_tuple(other)
