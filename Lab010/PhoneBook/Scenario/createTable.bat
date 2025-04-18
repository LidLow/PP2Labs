echo off

set PGPASSWORD=admin
set DBNAME=phonebook

psql -U postgres -c "CREATE DATABASE %DBNAME%;"
psql -U postgres -d %DBNAME% -c "CREATE TABLE contacts (id SERIAL PRIMARY KEY, first_name VARCHAR(100) NOT NULL CHECK (first_name <> ''), last_name VARCHAR(100), phone_number varchar(20) NOT NULL UNIQUE CHECK (phone_number <> ''));"

pause


