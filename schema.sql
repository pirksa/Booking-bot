DROP TABLE IF EXISTS countries;

DROP TABLE IF EXISTS cities;

DROP TABLE IF EXISTS buildings;

DROP TABLE IF EXISTS rooms;

DROP TABLE IF EXISTS companies;

DROP TABLE IF EXISTS users;

DROP TABLE IF EXISTS bookings;

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

CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name VARCHAR(100),
    building_id INTEGER,
    FOREIGN KEY(building_id) REFERENCES buildings(building_id)
    );

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(30),
    company_id INTEGER,
    department VARCHAR(50),
    job_position VARCHAR(50),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
    );

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    date_time TEXT,
    booking_time INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
