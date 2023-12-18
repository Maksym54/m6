CREATE DATABASE m6;
CREATE USER SQLite WITH PASSWORD '123098';
ALTER ROLE SQLite SET client_encoding TO 'utf8';
ALTER ROLE SQLite SET default_transaction_isolation TO 'read committed';
ALTER ROLE SQLite SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE m6 TO SQLite;
