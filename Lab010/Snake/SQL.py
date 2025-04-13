import psycopg2, sys
sys.path.append(r"Lab010\Snake\config")
from config import load_config

config = load_config()

def checkUser(user_name):
    SQL_SEL = "SELECT user_name, level, score FROM users WHERE user_name = %s;"
    SQL_INS = "INSERT INTO users (user_name, level, score) VALUES (%s, 1, 0);"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL_SEL, (user_name,))
            result = curs.fetchone()

            if result:
                return result 
            else:
                curs.execute(SQL_INS, (user_name,))
                conn.commit()
                return (user_name, 1, 0)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
            
def saveScore(user_name, level, score):
    SQL = "UPDATE users SET level=%s, score=%s WHERE user_name=%s;"

    try:
        with psycopg2.connect(**config) as conn, conn.cursor() as curs:
            curs.execute(SQL, (level, score, user_name))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)