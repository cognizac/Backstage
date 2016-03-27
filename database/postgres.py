import psycopg2
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('settings.cfg')

user = config.get('Postgres', 'user')
password = config.get('Postgres', 'password')
database = config.get('Postgres', 'dbname')

conn = psycopg2.connect(user=user, database=database, password=password)
conn.autocommit = True

cur = conn.cursor()

def getQuery(query):
    """
    Perform a query on the database and return the results as a list of tuples
    """
    cur.execute(query)
    return cur.fetchall()