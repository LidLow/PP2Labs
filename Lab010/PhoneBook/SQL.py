import psycopg2
import csv
from config import load_config

config = load_config()

def createTable():
    config = load_config()
    SQL = "CREATE TABLE contacts (id SERIAL PRIMARY KEY, first_name VARCHAR(100) NOT NULL, last_name VARCHAR(100), phone_number varchar(20) NOT NULL UNIQUE CHECK (phone_number <> ''));"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error

def createContact(first_name, last_name, phone_number):
    SQL = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s) ON CONFLICT (phone_number) DO NOTHING;"

    try: 
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (first_name, last_name, phone_number))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def showContacts():
    SQL = "SELECT * FROM contacts;"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)

            row = curs.fetchone()
            while row is not None:
                print(row)
                row = curs.fetchone()
    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def showOrderedContacts(key, order):
    SQL = f"SELECT * FROM contacts ORDER BY {key} {order};"
    
    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
                curs.execute(SQL, (key, order))

                print("\nYour Contacts:", curs.rowcount)

                row = curs.fetchone()
                while row is not None:
                    print(row)
                    row = curs.fetchone()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def deleteContact(name):
    SQL = "DELETE FROM contacts WHERE first_name=%s or last_name=%s;"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (name, name))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def clearContacts():
    config = load_config()
    SQL = "TRUNCATE TABLE contacts;"

    try: 
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def updateContact(id, first_name, last_name, phone_number):
    SQL = "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s;"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (first_name, last_name, phone_number, id))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        print(Error)

def importCSV():
    path = input("Directory of the CSV: ")

    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            createContact(row[0], row[1], row[2])