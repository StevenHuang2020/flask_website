from configparser import ConfigParser
import psycopg2
from psycopg2.extensions import connection,cursor

def config(filename='database.ini', section='postgresql'):
    """get config from ini file"""
    parser = ConfigParser()

    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

class PsqlConnect():
    """PostgreSQL connect class"""

    conn: connection = None
    cur: cursor = None

    def __init__(self):
        try:
            print('Connecting to the PostgreSQL...........')
            #self.conn = psycopg2.connect("dbname=postgres user=postgres password=123")
            #self.conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="123")
            self.conn = psycopg2.connect(**config())

            # create a cursor
            self.cur = self.conn.cursor()

            print('Connect success, PostgreSQL database version:')
            print(self.exe_sql('SELECT version()'))
            print("Connection successfully..................")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        if self.conn:
            self.conn.close()
        if self.cur:
            self.cur.close()

    def exe_sql(self, sql, query=True):
        assert self.cur is not None
        self.cur.execute(sql)
        self.conn.commit()
        if query:
            return self.cur.fetchall() #fetchone() fetchall()
        return None
