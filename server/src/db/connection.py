import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fatms"
    )
    try:
        yield conn
    finally:
        conn.close()