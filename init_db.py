import sqlite3


def create_schema():
    con = sqlite3.connect('rooms.sqlite')
    cur = con.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS countries;
    DROP TABLE IF EXISTS cities;
    CREATE TABLE IF NOT EXISTS countries (
        country_id INTEGER PRIMARY KEY,
        country_code VARCHAR(10),
        country_name VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY,
        city_code VARCHAR(10),
        city_name VARCHAR(50),
        timezone VARCHAR(10),
        country_id INTEGER,
    FOREIGN KEY(country_id) REFERENCES countries(country_id)
    );
    DELETE FROM countries;
    DELETE FROM cities;
    INSERT INTO countries (country_id, country_code, country_name) VALUES
        (1, 'KZ', 'Kazakhstan'),
        (2, 'UZ', 'Uzbekistan'),
        (3, 'RU', 'Russia'),
        (4, 'TR', 'Turkey');
    INSERT INTO cities (city_id, city_code, city_name, timezone, country_id) VALUES
        (1, 'ALA', 'Almaty', 'UTC+6', 1),
        (2, 'TSE', 'Astana', 'UTC+6', 1),
        (3, 'TAS', 'Tashkent','UTC+5', 2),
        (4, 'MOW', 'Moscow', 'UTC+3', 3),
        (5, 'IST', 'Istanbul', 'UTC+3', 4);
    ''')
    con.commit()
    cur.close()
    con.close()
