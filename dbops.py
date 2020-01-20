from config import config
import psycopg2 as pg
import sqlcmds as sql

def connectdb(name = None):
    '''
        connects to the database from the database.ini file and
        returns the connecton object
    '''
    conn = None
    try:
        params = config()
        if name is not None:
            params['database'] = str(name)
        conn = pg.connect(**params)
        if name is None:
            print('Connected to ', params['database'], " database.")
    except pg.DatabaseError as err:
        print(err)
        exit()
    return conn

def closedb(conn):
    '''
        closes the connection for the passed connection object
    '''
    try:
        conn.close()
    except pg.DatabaseError as err:
        print(err)

def execute_sql(conn, sql, fetch=False):
    '''
        executes the sql cmd passed and the results will be fetched if fetch=True.
    '''
    count = 0
    fetched = {}
    try:
        with conn.cursor() as cur:
            count = cur.execute(sql)
            if fetch:
                fetched = cur.fetchall()
            conn.commit()
    except pg.DatabaseError as err:
        print(err)
    except pg.DataError as err:
        print(err)
    return [count, fetched]