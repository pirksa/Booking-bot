from repo import CountryRepository, CityRepository


def insert_data():
    repo_country = CountryRepository()
    repo_country[1] = {'country_id': 1, 'country_code': 'KZ', 'country_name': 'Kazakhstan'}
    repo_country[2] = {'country_id': 2, 'country_code': 'UZ', 'country_name': 'Uzbekistan'}
    repo_country[3] = {'country_id': 3, 'country_code': 'RU', 'country_name': 'Russia'}
    repo_country[4] = {'country_id': 4, 'country_code': 'TR', 'country_name': 'Turkey'}

    repo_city = CityRepository()
    repo_city[1] = {'city_id': 1, 'city_code': 'ALA', 'city_name': 'Almaty', 'timezone': 'UTC+6', 'country_id': 1}
    repo_city[2] = {'city_id': 2, 'city_code': 'TSE', 'city_name': 'Astana', 'timezone': 'UTC+6', 'country_id': 1}
    repo_city[3] = {'city_id': 3, 'city_code': 'TAS', 'city_name': 'Tashkent', 'timezone': 'UTC+5', 'country_id': 2}
    repo_city[4] = {'city_id': 4, 'city_code': 'MOW', 'city_name': 'Moscow', 'timezone': 'UTC+3', 'country_id': 3}
    repo_city[5] = {'city_id': 5, 'city_code': 'IST', 'city_name': 'Istanbul', 'timezone': 'UTC+3', 'country_id': 4}
