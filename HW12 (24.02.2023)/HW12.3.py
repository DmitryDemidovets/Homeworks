#Cоздать таблицу с животными:
#1) Вывести всех животных старше 2 лет используя LEFT JOIN
#2) Вывести животных старше 3 лет используя INNER JOIN
#3) Вывести животных мужского пола используя любой из джоинов

import sqlite3 as sql
class Database():
    def __init__(self,database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

# Создаем 1-ю таблицу с животными
    def create_table_animals(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS animals
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_name VARCHAR(50),
        gender VARCHAR(50),
        age INTEGER)
        ''')

        self.con.commit()

    def insert_table_animals(self, data):
        self.cur.executemany('''INSERT INTO animals (id, animal_name, gender, age) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()

# Создаем 2-ю таблицу с животными
    def create_table_animals2(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS animals2
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_name VARCHAR(50),
        gender VARCHAR(50),
        age INTEGER)
        ''')

        self.con.commit()

    def insert_table_animals2(self, data):
        self.cur.executemany('''INSERT INTO animals2 (id, animal_name, gender, age) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()

    #Выводим всех животных старше 2 лет используя LEFT JOIN
    def get_all_animals_over_two_years_old(self,age):
        sql_select_query = '''
        SELECT * 
        FROM animals LEFT JOIN animals2 
        ON animals.age > 2 and animals2.age > 2'''
        self.cur.execute(sql_select_query)
        result = self.cur.fetchall()
        return print('Все животные старше 2-х лет', result)

    #Выводим животных старше 3 лет используя INNER JOIN
    def get_all_animals_over_three_years_old(self,age):
        sql_select_query ='''
        SELECT * 
        FROM animals INNER JOIN animals2 
        ON animals.age > 3 and animals2.age > 3'''
        self.cur.execute(sql_select_query)
        result = self.cur.fetchall()
        return print('Все животные старше 3-х лет', result)

    #Выводим животных мужского пола используя любой из джоинов
    def get_male_animals(self, gender):
        sql_select_query ='''
        SELECT * 
        FROM animals INNER JOIN animals2
        ON animals.gender = male and animals2.gender = male'''
        self.cur.execute(sql_select_query)
        result = self.cur.fetchall()
        return print('Все животные мужского пола', result)

    def close(self):
        self.con.close()
def main():

    animals = [
        [1,'Sherry cat', 'female', 6], 
        [2,'Genry cat','male', 1], 
        [3,'Ozzy dog', 'male', 8],
        [4,'Iggy dog', 'male', 10]
        ]

    animals2 = [
        [1,'Texas horse', 'male', 12], 
        [2,'Prada horse','female', 15], 
        [3,'Vardi dog', 'male', 5],
        [4,'Shusha cat', 'female', 4]
        ]

    db1 = Database('animals.db')
    db1.create_table_animals()
    db1.insert_table_animals(animals)

    db2 = Database('animals2.db')
    db2.create_table_animals2()
    db2.insert_table_animals2(animals2)

    db3.get_all_animals_over_two_years_old()
    db3.get_all_animals_over_three_years_old()
    db3.get_male_animals()

if __name__ == '__main__':
    main()