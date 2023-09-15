CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(30),
    company_id INTEGER,
    department VARCHAR(50),
    job_position VARCHAR(50),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
    );

CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name VARCHAR(100),
    building_id INTEGER,
    FOREIGN KEY(building_id) REFERENCES buildings(building_id)
    );

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    building_id INTEGER,
    floor INTEGER,
    room_name VARCHAR(50),
    FOREIGN KEY(building_id) REFERENCES buildings(building_id)
    );

CREATE TABLE buildings (
    building_id INTEGER PRIMARY KEY,
    city_id VARCHAR(50),
    address VARCHAR(50),
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
    );

CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY,
    city_code VARCHAR(10),
    city_name VARCHAR(50),
    timezone VARCHAR(10),
    country_id VARCHAR(50),
    FOREIGN KEY(company_id) REFERENCES countries(country_id)
    );

INSERT INTO cities (city_id, city_code, city_name, timezone)
VALUES
    (1, 'ALA', 'Almaty', 'UTC+6'),
    (2, 'TSE', 'Astana', 'UTC+6'),
    (3, 'TAS', 'Tashkent','UTC+5'),
    (4, 'MOW', 'Moscow', 'UTC+3'),
    (5, 'IST', 'Istanbul', 'UTC+3');

CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY,
    country_code VARCHAR(10),
    country_name VARCHAR(50)
    );

INSERT INTO countries (country_id, country_code, country_name)
VALUES
    (1, 'KZ', 'Kazakhstan'),
    (2, 'US', 'Uzbekistan'),
    (3, 'RU', 'Russia'),
    (4, 'TR', 'Turkey');