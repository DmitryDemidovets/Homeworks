# Создаем базы данных для магазина
# Магазин shop - товары goods, клиенты clients, покупки purchases
# Товары goods- название title, количество number, цена price
# Клиенты clients- имя name, телефон telephone, код code
# Покупки purchases- название title, количество number, код code

import sqlite3 as sql
# открываем файл с базой данных
con = sql.connect("shop.db")
#создаем первую таблицу для товаров
with con:
    con.execute("""
                CREATE TABLE IF NOT EXISTS goods(
                    product VARCHAR(20) PRIMARY KEY,
                    count INTEGER,
                    price INTEGER
);
    """)
# подготавливаем множественный запрос
add_goods = 'INSERT INTO goods (product, count, price) values(?.?,?)'
# указываем данные для запроса
data = [
    ('spinning', 1, 250),
    ('spinning reel', 2, 200, ),
    ('braided fishing line', 1, 20)
]
#  добавляем с помощью множественного запроса все данные сразу
with con:
    con.executemany(add_goods, data)
# выводим содержимое таблицы на экран
with con:
    data = con.execute('SELECT * FROM goods') 
    for row in data:
        print(row)
# создаем таблицу с клиентами
# открываем базу
with con:
    # получаем количетсво таблиц с нужным нам именем - clients
    data = con.execute('select count(*) from sqlite_master where type = 'tab'')
    for row in data:
        # если таких таблиц нет
        if row[0] == 0 

