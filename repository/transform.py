from .model import Country, City, Building, Company, Room, User, Booking


def tuple_to_country(data: tuple):
    return Country(country_id=data[0], country_code=data[1], country_name=data[2], last_updated=data[3],
                   last_updated_by=data[4]) if data else None


def country_to_tuple(country: Country):
    return country.country_id, country.country_code, country.country_name, country.last_updated, country.last_updated_by


def tuple_to_city(data: tuple):
    return City(city_id=data[0], city_code=data[1], city_name=data[2], timezone=data[3], country_id=data[4],
                last_updated=data[5], last_updated_by=data[6]) if data else None


def city_to_tuple(city: City):
    return city.city_id, city.city_code, city.city_name, city.timezone, city.country_id, city.last_updated, \
        city.last_updated_by


def tuple_to_building(data: tuple):
    return Building(building_id=data[0], city_id=data[1], address=data[2], last_updated=data[3],
                    last_updated_by=data[4]) if data else None


def building_to_tuple(building: Building):
    return building.building_id, building.city_id, building.address, building.last_updated, building.last_updated_by


def tuple_to_company(data: tuple):
    return Company(company_id=data[0], company_name=data[1], floor=data[2], building_id=data[3], last_updated=data[4],
                   last_updated_by=data[5]) if data else None


def company_to_tuple(company: Company):
    return company.company_id, company.company_name, company.floor, company.building_id, company.last_updated, \
        company.last_updated_by


def tuple_to_room(data: tuple):
    return Room(room_id=data[0], company_id=data[1], room_name=data[2], last_updated=data[3],
                last_updated_by=data[4]) if data else None


def room_to_tuple(room: Room):
    return room.room_id, room.company_id, room.room_name, room.last_updated, room.last_updated_by


def tuple_to_user(data: tuple):
    return User(user_id=data[0], user_name=data[1], phone_number=data[2], join_date=data[3]) if data else None


def user_to_tuple(user: User):
    return user.user_id, user.user_name, user.phone_number, user.join_date


def tuple_to_booking(data: tuple):
    return Booking(booking_id=data[0], user_id=data[1], room_id=data[2], booking_date=data[3], start_time=data[4],
                   end_time=data[5], last_updated=data[6], last_updated_by=data[7]) if data else None


def booking_to_tuple(booking: Booking):
    return booking.booking_id, booking.user_id, booking.room_id, booking.booking_date, booking.start_time, \
        booking.end_time, booking.last_updated, booking.last_updated_by
