DELETE FROM countries;

DELETE FROM cities;

INSERT INTO countries (country_id, country_code, country_name)
VALUES
    (1, 'KZ', 'Kazakhstan'),
    (2, 'UZ', 'Uzbekistan'),
    (3, 'RU', 'Russia'),
    (4, 'TR', 'Turkey');

INSERT INTO cities (city_id, city_code, city_name, timezone)
VALUES
    (1, 'ALA', 'Almaty', 'UTC+6'),
    (2, 'TSE', 'Astana', 'UTC+6'),
    (3, 'TAS', 'Tashkent','UTC+5'),
    (4, 'MOW', 'Moscow', 'UTC+3'),
    (5, 'IST', 'Istanbul', 'UTC+3');