import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "sales",
    user = "postgres",
    password = "password"
)

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM PRODUCT")

cur.close()

conn.close()