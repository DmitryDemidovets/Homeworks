import sqlite3 as sql

conn = sql.connect('shop.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT);
    """)
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    date TEXT,
    user_id TEXT,
    total TEXT);
    """)
users = [('00022', 'Lois', 'Griffin', 'female'), ('00033', 'Lois', 'Griffin', 'female'), ('00044', 'Bruce', 'Wayne', 'male')]
cur.executemany("INSERT INTO user VALUES(?, ?, ?, ?);", users)
conn.commit()

