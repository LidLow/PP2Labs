import psycopg2
from config import load_config

def createTable():
    config = load_config()
    SQL = "CREATE TABLE contacts (id SERIAL PRIMARY KEY, first_name VARCHAR(100) NOT NULL CHECK (first_name <> ''), last_name VARCHAR(100), phone_number varchar(20) NOT NULL UNIQUE CHECK (phone_number <> ''));"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error
    
if __name__ == "__main__":
    createTable()