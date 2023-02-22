#Cоздать базу данных для массажного сервиса с таблицами клиент, услуги, заказ:
# 1) У заказа есть клиент и название услуги (используем Foreign Key)
#2) У клиента и услуги произвольные поля, но важно чтобы присутствовал Primary Key
#Для решения этой задачи используем классовый подход

import sqlite3 as sql
class Database():
    def __init__(self,database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_clients(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS clients
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50),
        gender VARCHAR(50),
        services VARCHAR(50)
        age INTEGER)
        ''')

        self.con.commit()

    def insert_table_clients(self, data):
        self.cur.executemany('''INSERT INTO clients (id, name, gender, services, age) VALUES (?, ?, ?, ?, ?)''', data)
        self.con.commit()

    def create_table_services(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS services
        (id INTEGER PRIMARY KEY,
        service_name VARCHAR(50),
        price INTEGER,
        quantity INTEGER)
        ''')

    def insert_table_services(self, data):
        self.cur.executemany('''INSERT INTO services (id, service_name, price, quantity) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()

    def create_table_orders(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS orders
        (id INTEGER PRIMARY KEY,
        service_name VARCHAR(50),
        price INTEGER,
        quantity INTEGER)
        ''')

    def insert_table_orders(self, data):
        self.cur.executemany('''INSERT INTO orders (id, service_name, price, quantity) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()


    def close(self):
        self.con.close()
def main():

    clients = [
        [1, ], 
        [2,], 
        [3,],
        [4,]
        ]

    services = [
        [1,], 
        [2,], 
        [3,],
        [4,]
        ]

    orders = [
        [1,], 
        [2,], 
        [3,],
        [4,]
        ]

    db1 = Database('clients.db')
    db1.create_table_clients()
    db1.insert_table_clients(clients)

    db1 = Database('services.db')
    db1.create_table_services()
    db1.insert_table_services(services)

    db1 = Database('orders.db')
    db1.create_table_orders()
    db1.insert_table_orders(orders)

if __name__ == '__main__':
    main()