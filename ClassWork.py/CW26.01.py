import sqlite3 as sql

class Database():
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)")
        self.con.commit()

    def execute(self, data):
        self.cur.execute(data)
        self.con.commit()

    def execute_many(self, dates):
        self.create_table()
        self.cur.executemany("REPLACE INTO employee VALUES(?,?,?,?)", dates)

    def close(self):
        self.con.close()
    
database = Database('employee.db')
database.create_table()
database.execute("INSERT INTO employee VALUES (0001, 'Vasya', 18);")

