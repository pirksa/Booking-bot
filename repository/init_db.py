import psycopg2


def create_schema():
    con = psycopg2.connect(database='rooms', user='admin', password='root', host='localhost')
    cur = con.cursor()
    cur.execute('''
    DROP TABLE IF EXISTS countries CASCADE;
    DROP TABLE IF EXISTS cities CASCADE;
    DROP TABLE IF EXISTS buildings CASCADE;
    DROP TABLE IF EXISTS rooms CASCADE;
    CREATE TABLE IF NOT EXISTS countries (
        country_id BIGINT PRIMARY KEY,
        country_code VARCHAR(10),
        country_name VARCHAR(50),
        last_updated TEXT
    );
    CREATE TABLE IF NOT EXISTS cities (
        city_id BIGINT PRIMARY KEY,
        city_code VARCHAR(10),
        city_name VARCHAR(50),
        timezone VARCHAR(10),
        country_id BIGINT,
        last_updated TEXT,
        FOREIGN KEY(country_id) REFERENCES countries(country_id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS buildings (
        building_id BIGINT PRIMARY KEY,
        city_id BIGINT,
        address VARCHAR(50),
        last_updated TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(city_id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS rooms (
        room_id BIGINT PRIMARY KEY,
        building_id BIGINT,
        floor INTEGER,
        room_name VARCHAR(50),
        last_updated TEXT,
        FOREIGN KEY(building_id) REFERENCES buildings(building_id) ON DELETE CASCADE
    );
    ''')
    con.commit()
    cur.close()
    con.close()
