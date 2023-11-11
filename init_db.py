import sqlite3


def create_schema():
    con = sqlite3.connect('rooms.sqlite')
    cur = con.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS countries;
    DROP TABLE IF EXISTS cities;
    DROP TABLE IF EXISTS buildings;
    DROP TABLE IF EXISTS rooms;
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
    CREATE TABLE IF NOT EXISTS buildings (
        building_id INTEGER PRIMARY KEY,
        city_id INTEGER,
        address VARCHAR(50),
        FOREIGN KEY(city_id) REFERENCES cities(city_id)
    );
    CREATE TABLE IF NOT EXISTS rooms (
        room_id INTEGER PRIMARY KEY,
        building_id INTEGER,
        floor INTEGER,
        room_name VARCHAR(50),
        FOREIGN KEY(building_id) REFERENCES buildings(building_id)
    );
    ''')
    con.commit()
    cur.close()
    con.close()
