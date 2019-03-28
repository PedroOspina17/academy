import datetime
import sqlite3

def add_post(content):
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO post VALUES ('{content}','{datetime.datetime.now()}')")
    conn.commit()
    conn.close()


def get_posts():
    conn = sqlite3.connect("forum.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM post ORDER BY time DESC;")
    result = cursor.fetchall()
    print(result)
    conn.close()
    return result

get_posts()