CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(30),
    job_position VARCHAR(50),
    department VARCHAR(50)
    );

CREATE TABLE rooms (
    room_id INTEGER PRIMARY KEY,
    room_name VARCHAR(50),
    floor INTEGER,
    building INTEGER
    );

CREATE TABLE buildings (
    building_id INTEGER PRIMARY KEY,
    address VARCHAR(50),
    city VARCHAR(50),
    );

CREATE TABLE cities (
    city_id INTEGER PRIMARY KEY,
    city_code VARCHAR(10),
    city_name VARCHAR(50),
    timezone VARCHAR(10),
    country VARCHAR(50)
    );

INSERT INTO cities (city_id, city_code, city_name, timezone, country)
VALUES
    (1, 'ALA', 'Almaty', 'UTC+6', 'Kazakhstan'),
    (2, 'TSE', 'Astana', 'UTC+6', 'Kazakhstan'),
    (3, 'TAS', 'Tashkent','UTC+5', 'Uzbekistan'),
    (4, 'MOW', 'Moscow', 'UTC+3', 'Russia'),
    (5, 'IST', 'Istanbul', 'UTC+3', 'Turkey');

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