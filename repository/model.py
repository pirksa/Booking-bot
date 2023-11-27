from . import transform


class Country:
    def __init__(self, **props):
        self.country_id = props.get('country_id')
        self.country_code = props.get('country_code')
        self.country_name = props.get('country_name')

    def __str__(self):
        return f"Country({self.country_id}, {self.country_code}, {self.country_name})"

    def __eq__(self, other):
        return transform.country_to_tuple(self) == transform.country_to_tuple(other)


class City:
    def __init__(self, **props):
        self.city_id = props.get('city_id')
        self.city_code = props.get('city_code')
        self.city_name = props.get('city_name')
        self.timezone = props.get('timezone')
        self.country_id = props.get('country_id')

    def __str__(self):
        return f'City({self.city_id}, {self.city_code}, {self.city_name}, {self.timezone}, {self.country_id})'

    def __eq__(self, other):
        return transform.city_to_tuple(self) == transform.city_to_tuple(other)


class Building:
    def __init__(self, **props):
        self.building_id = props.get('building_id')
        self.city_id = props.get('city_id')
        self.address = props.get('address')

    def __str__(self):
        return f'Building({self.building_id}, {self.city_id}, {self.address})'

    def __eq__(self, other):
        return transform.building_to_tuple(self) == transform.building_to_tuple(other)


class Room:
    def __init__(self, **props):
        self.room_id = props.get('room_id')
        self.building_id = props.get('building_id')
        self.floor = props.get('floor')
        self.room_name = props.get('room_name')

    def __str__(self):
        return f'Room({self.room_id}, {self.building_id}, {self.floor}, {self.room_name})'

    def __eq__(self, other):
        return transform.room_to_tuple(self) == transform.room_to_tuple(other)
