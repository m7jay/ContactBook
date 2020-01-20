from config import config
import psycopg2

def connect():
    conn = None
    try:
        params = config()
        print('Connecting to postgres database....')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print('Database version-\n')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except psycopg2.DatabaseError as err:
        print(err)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.\n')

if __name__ == "__main__":
    connect()