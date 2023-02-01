#Используя модуль sqlite3 создать базу данных favorites
#Создать таблицу с любимыми блюдами
#Продумать поля
#Наполнить таблицу рецептами (не более 4)
#_______________________________________________________________
#Создать таблицу в базе данных favorites c любимыми фильмами
#В полях таблицы обязательно должно присутствовать поле “год выпуска”
#Вывести фильмы определенного года выпуска
#_______________________________________________________________
# Создать таблицу техника в базе данных favorites с желаемой техникой
# В полях таблицы обязательно должно быть поле “цена”
# Вывести продукты, цена которых меньше 1200

import sqlite3 as sql
class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_dishes(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS favorite_dishes(
            id INTEGER PRIMARY KEY,
            dish_name VARCHAR(100),
            ingredients TEXT)
        ''')
        self.con.commit()

    def insert_table_dishes(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO favorite_dishes (id, dish_name, ingredients) VALUES(?,?,?)''', data)
        self.con.commit()

    def create_table_films(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS favorite_films(
            id INTEGER PRIMARY KEY,
            film_name VARCHAR(100),
            year_of_release INTEGER,
            rating REAL)      
        ''')

    def insert_table_films(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO favorite_films (id, film_name, year_of_release, rating) VALUES(?,?,?,?)''', data)
        self.con.commit()

    def get_films_of_year(self, year):
        sql_select_query ='''SELECT * FROM favorite_films WHERE year_of_release=?'''
        self.cur.execute(sql_select_query, (year,))
        result = self.cur.fetchall()
        return print('Фильмы', year, 'год выпуска:', result)

    def create_table_technics(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS desired_technics(
            id INTEGER PRIMARY KEY,
            technic_name VARCHAR(100),
            price REAL,
            manufacturer VARCHAR(100))
        ''')

    def insert_table_technics(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO desired_technics (id, technic_name, price, manufacturer) VALUES(?,?,?,?)''', data)
        self.con.commit()

    def get_price_lower_number(self, price):
        sql_select_query ='''SELECT * FROM desired_technics WHERE price<?'''
        self.cur.execute(sql_select_query, (price,))
        result = self.cur.fetchall()
        return print('Техника ниже стоимости', price, ':', result)

    def close(self):
        self.con.close()


def main():

    favorite_dishes = [
        [1, 'Сырники', 'творог, яйца, манная крупа, сахар, соль'], 
        [2, 'Стейк', 'говядина, чеснок, розмарин, масло сливочное'], 
        [3, 'Манник', 'манная крупа, яйца, кефир, сахар, соль, уксус'],
        [4, 'Пицца', 'мука, вода, соль, сахар, дрожжи, оливковое масло, пармезан, ветчина, шампиньоны, помидоры, лук репчатый, кетчуп']
        ]

    
    favorite_films = [
        [1, 'Достучаться до небес', 1997, 8.6], 
        [2, 'Отступники', 2006, 8.5], 
        [3, 'Помни', 2000, 7.9],
        [4, 'Бойцовский клуб', 1999, 8.7],
        [5, 'Невидимый гость', 2016, 7.8]
        ]
    
    desired_technics = [
        [1,'Кинопроектор', 1649, 'Xiaomi'], 
        [2,'Кофемашина', 226, 'Normann' ], 
        [3,'Увлажнитель воздуха', 330, 'Electrolux'],
        [4,'Электрогриль', 1130, 'DeLonghi']
        ]

    db1 = Database('favorites.db')
    db1.create_table_dishes()
    db1.create_table_films()
    db1.create_table_technics()
    
    db1.insert_table_dishes(favorite_dishes)
    db1.insert_table_films(favorite_films)
    db1.insert_table_technics(desired_technics)
    
    db1.get_films_of_year(2006)
    db1.get_price_lower_number(1200)


if __name__ == '__main__':
    main()