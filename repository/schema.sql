DROP TABLE IF EXISTS countries CASCADE;

DROP TABLE IF EXISTS cities CASCADE;

DROP TABLE IF EXISTS buildings CASCADE;

DROP TABLE IF EXISTS rooms CASCADE;

DROP TABLE IF EXISTS companies CASCADE;

DROP TABLE IF EXISTS users CASCADE;

DROP TABLE IF EXISTS bookings CASCADE;

CREATE TABLE IF NOT EXISTS countries (
    country_id BIGINT PRIMARY KEY,
    country_code VARCHAR(10),
    country_name VARCHAR(50),
    last_updated TIMESTAMP,
    last_updated_by BIGINT
    );

CREATE TABLE IF NOT EXISTS cities (
    city_id BIGINT PRIMARY KEY,
    city_code VARCHAR(10),
    city_name VARCHAR(50),
    timezone VARCHAR(10),
    country_id BIGINT,
    last_updated TIMESTAMP,
    last_updated_by BIGINT,
    FOREIGN KEY(country_id) REFERENCES countries(country_id) ON UPDATE CASCADE
    );

CREATE TABLE IF NOT EXISTS buildings (
    building_id BIGINT PRIMARY KEY,
    city_id BIGINT,
    address VARCHAR(50),
    last_updated TIMESTAMP,
    last_updated_by BIGINT,
    FOREIGN KEY(city_id) REFERENCES cities(city_id) ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS companies (
    company_id BIGINT PRIMARY KEY,
    company_name VARCHAR(100),
    floor VARCHAR(10),
    building_id BIGINT,
    last_updated TIMESTAMP,
    last_updated_by BIGINT,
    FOREIGN KEY(building_id) REFERENCES buildings(building_id) ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS rooms (
    room_id BIGINT PRIMARY KEY,
    company_id BIGINT,
    room_name VARCHAR(50),
    last_updated TIMESTAMP,
    last_updated_by BIGINT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id) ON DELETE CASCADE
    );

CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name VARCHAR(30),
    phone_number VARCHAR(20),
    join_date TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS bookings (
    booking_id BIGINT PRIMARY KEY,
    user_id INTEGER,
    room_id BIGINT,
    booking_date DATE,
    start_time TIME,
    end_time TIME,
    last_updated TIMESTAMP,
    last_updated_by BIGINT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
    );
