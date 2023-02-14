# практика
#1. создать скрипт, который берет номер телефона, имя из поля ввода(input)
#  и возраст записывает это сперва в переменные а затем в базу данных Клиенты (имя, номер, возраст)
#1.1  отсортировать клиентов по возрасту(от большего к меньшему) и записать в файл полученные результаты

#1) создаем 3 переменных со значением input()-ок

#2) создаем базу данных и таблицу с полями (id, имя, номер, возраст) ок

#3) инсертим в таблицу значения из переменных

import sqlite3 as sql


# Создаем переменные
name = str(input("Введите имя: "))
number = int(input("Введите номер: "))
age = int(input("Введите возраст: "))

class Database():
    def __init__(self, data_base):
        self.con = sql.connect(data_base)
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number INTEGER, age INTEGER)")
        self.con.commit()

    def execute_data(self,name,number,age):
        self.cur.execute("INSERT INTO clients(name,number,age)VALUES (?,?,?)",(name,number,age))
        self.con.commit()

    def execute_many(self, dates):
        self.create_table()
        self.cur.executemany("REPLACE INTO clients VALUES(?,?,?)", dates)

    def sort_from_largest_to_smallest (self, age):
        sql_select_query ='''SELECT * FROM clients ORDER BY age DESC?'''
        self.cur.execute(sql_select_query, (age,))
        result = self.cur.fetchall()
        return print('Возраст от большего к меньшему', age, ':', result)

    def close(self):
        self.con.close()
    
database = Database('clients.db')
database.create_table()
database.execute_data(name,number,age)


