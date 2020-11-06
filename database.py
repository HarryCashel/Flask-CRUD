import psycopg2

connection = psycopg2.connect(
    database='library_api',
    user='postgres',
    password='g3t0ffw0w!1',
    host='18.216.231.160',
    port='5432'
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()
