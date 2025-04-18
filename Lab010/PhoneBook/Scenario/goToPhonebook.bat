echo off
chcp 1251
set PGPASSWORD=admin
psql -U postgres -d phonebook