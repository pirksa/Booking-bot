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
    ''')
    con.commit()
    cur.close()
    con.close()
