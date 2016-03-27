import psycopg2

conn = psycopg2.connect(user='postgres', database='Chinook', password='pgpass')
conn.autocommit = True

cur = conn.cursor()

def getQuery(query):
    """
    Perform a query on the database and return the results as a list of tuples
    """
    cur.execute(query)
    return cur.fetchall()