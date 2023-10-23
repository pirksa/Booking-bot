from model import Country, City


def tuple_to_country(data):
    if not data:
        return None
    else:
        return Country(country_id=data[0], country_code=data[1], country_name=data[2])


def country_to_tuple(country):
    return country.country_id, country.country_code, country.country_name


def tuple_to_city(data):
    if not data:
        return None
    else:
        return City(city_id=data[0], city_code=data[1], city_name=data[2], timezone=data[3], country_id=data[4])


def city_to_tuple(city):
    return city.city_id, city.city_code, city.city_name, city.timezone, city.country_id

