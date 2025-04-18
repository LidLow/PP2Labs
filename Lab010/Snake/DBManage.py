import psycopg2
from config import load_config

def createTables():
    config = load_config()
    SQL1 = "CREATE TABLE users (id SERIAL PRIMARY KEY, user_name VARCHAR(100) NOT NULL UNIQUE CHECK (user_name <> ''), level SMALLINT);"
    SQL2 = "CREATE TABLE user_score (id SERIAL PRIMARY KEY, user_name VARCHAR(100) NOT NULL UNIQUE CHECK (user_name <> ''), score SMALLINT);"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL1)
            curs.execute(SQL2)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error
    
def dropTables():
    config = load_config()
    SQL1 = "DROP TABLE users;"
    SQL2 = "DROP TABLE user_score;"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL1)
            curs.execute(SQL2)
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as Error:
        return Error
    
if __name__ == "__main__":
    dropTables()