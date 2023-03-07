#Cоздать базу данных для массажного сервиса с таблицами клиент, услуги, заказ:
#1) У заказа есть клиент и название услуги (используем Foreign Key)
#2) У клиента и услуги произвольные поля, но важно чтобы присутствовал Primary Key
#Для решения этой задачи используем классовый подход

import sqlite3 as sql
class Database():
    def __init__(self,database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

#создаем таблицу клиенты (имя, пол, название услуги, возраст)
    def create_table_clients(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS clients
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name VARCHAR(50),
        gender VARCHAR(50),
        services_name VARCHAR(50)
        )
        ''')

        self.con.commit()

    def insert_table_clients(self, data):
        self.cur.executemany('''INSERT INTO clients (id, client_name, gender, services_name) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()

#создаем таблицу услуги (название услуги, цена, количество)
    def create_table_services(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS services
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_name VARCHAR(50),
        price INTEGER,
        quantity INTEGER)
        ''')

    def insert_table_services(self, data):
        self.cur.executemany('''INSERT INTO services (id, service_name, price, quantity) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()

#создаем таблицу заказ (у заказа есть клиент и название услуги, Foreign Key)
    def create_table_orders(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS orders
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name VARCHAR(50),
        service_name VARCHAR(50),
        price INTEGER,
        FOREIGN KEY (id) REFERENCES clients)
        ''')

    def insert_table_orders(self, data):
        self.cur.executemany('''INSERT INTO orders (id, client_name, service_name, price) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()


    def close(self):
        self.con.close()
def main():

    clients = [
        [1,'Anna', 'female', 'massage1'], 
        [2,'Dmitry','male','massage1'], 
        [3,'Denis', 'male', 'massage2'],
        [4,'Lera', 'female', 'massage2']
        ]

    services = [
        [5,'massage1', 50, 30], 
        [6,'massage2', 25, 30], 
        [7,'massage3', 20, 20],
        [8,'massage4', 15,20]
        ]

    orders = [
        [9,'Anna', 'massage1', 50], 
        [10,'Dmitry','massage1', 50], 
        [11,'Denis', 'massage2', 25],
        [12,'Lera', 'massage2', 25]
        ]

    db1 = Database('massage_service.db')
    db1.create_table_clients()
    db1.insert_table_clients(clients)
    db1.create_table_services()
    db1.insert_table_services(services)
    db1.create_table_orders()
    db1.insert_table_orders(orders)

if __name__ == '__main__':
    main()