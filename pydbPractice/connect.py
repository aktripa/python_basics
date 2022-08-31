import psycopg2 as pg

def db_conn():
    connection = pg.connect(user='postgres',
                                password='root',
                                host='127.0.0.1',
                                port='5432',
                                database='employee')
    return connection                        
connection = db_conn()                      