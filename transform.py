from model import Country, City, Building, Room


def tuple_to_country(data: tuple):
    return Country(country_id=data[0], country_code=data[1], country_name=data[2]) if data else None


def country_to_tuple(country: Country):
    return country.country_id, country.country_code, country.country_name


def tuple_to_city(data: tuple):
    return City(city_id=data[0], city_code=data[1], city_name=data[2], timezone=data[3], country_id=data[4]) \
        if data else None


def city_to_tuple(city: City):
    return city.city_id, city.city_code, city.city_name, city.timezone, city.country_id


def tuple_to_building(data: tuple):
    return Building(building_id=data[0], city_id=data[1], address=data[2]) if data else None


def building_to_tuple(building: Building):
    return building.building_id, building.city_id, building.address


def tuple_to_room(data: tuple):
    return Room(room_id=data[0], building_id=data[1], floor=data[2], room_name=data[3]) if data else None


def room_to_tuple(room: Room):
    return room.room_id, room.building_id, room.floor, room.room_name
