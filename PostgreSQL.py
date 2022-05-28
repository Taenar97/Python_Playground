# https://www.postgresqltutorial.com/postgresql-python/connect/
# pip install psycopg2 -> database adapter

import psycopg2 as dbcon

conn = dbcon.connect(
    host = "localhost",
    database = "test",
    user = "postgres",
    password = "root"
)


def connect():