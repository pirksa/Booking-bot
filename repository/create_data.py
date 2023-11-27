from .repo import CountryRepository, CityRepository, BuildingRepository, RoomRepository, Country, City, Building, Room


def insert_data():
    repo_country = CountryRepository(table='countries', id_field='country_id')
    repo_country[1] = Country(country_id=1, country_code='KZ', country_name='Kazakhstan')
    repo_country[2] = Country(country_id=2, country_code='UZ', country_name='Uzbekistan')
    repo_country[3] = Country(country_id=3, country_code='RU', country_name='Russia')
    repo_country[4] = Country(country_id=4, country_code='TR', country_name='Turkey')

    repo_city = CityRepository(table='cities', id_field='city_id')
    repo_city[1] = City(city_id=1, city_code='ALA', city_name='Almaty', timezone='UTC+6', country_id=1)
    repo_city[2] = City(city_id=2, city_code='TSE', city_name='Astana', timezone='UTC+6', country_id=1)
    repo_city[3] = City(city_id=3, city_code='TAS', city_name='Tashkent', timezone='UTC+5', country_id=2)
    repo_city[4] = City(city_id=4, city_code='MOW', city_name='Moscow', timezone='UTC+3', country_id=3)
    repo_city[5] = City(city_id=5, city_code='IST', city_name='Istanbul', timezone='UTC+3', country_id=4)

    repo_building = BuildingRepository(table='buildings', id_field='building_id')
    repo_building[1] = Building(building_id=1, city_id=1, address='Khodzhanova str., 2/2')
    repo_building[2] = Building(building_id=2, city_id=2, address='Mangilik El Ave. 55/8, Block C 4.6')
    repo_building[3] = Building(building_id=3, city_id=3, address='Default address')
    repo_building[4] = Building(building_id=4, city_id=4, address='Default address')
    repo_building[5] = Building(building_id=5, city_id=5, address='Default address')

    repo_room = RoomRepository(table='rooms', id_field='room_id')
    repo_room[1] = Room(room_id=1, building_id=1, floor=1, room_name='Meeting room')
