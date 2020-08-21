from flask import Flask
import psycopg2 as pg
import sys
app = Flask(__name__)


#http://zetcode.com/python/psycopg2/
connection = pg.connect(user="postgres",
                              password="postgres",
                              host="127.0.0.1",
                              port="5432",
                              database="bikes")

cur = connection.cursor()
cur.execute('SELECT version()')

print(cur.fetchone()[0])

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()