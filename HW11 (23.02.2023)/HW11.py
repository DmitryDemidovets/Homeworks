#Наша задача — создать таблицу с любимыми книгами только при
#условии ее отсутствия. Для этого потребуется выполнить 2 запроса
#SQL: с помощью первого мы проверим, существует ли таблица с
#данным именем, с помощью второго — создадим таблицу.
#Когда у нас всё настроено, можно переходить к работе с данными.
#Начнем с этапа создания, и здесь нам потребуется функция,
#добавляющая книгу в таблицу. Написать ее не составит труда,
#поскольку необходимо выполнить лишь одну инструкцию INSERT и
#совершить транзакцию.
#Объявим 2 функции: первую — для получения данных обо всех
#книгах, а вторую — для извлечения информации об одной из них на
#основании ее ID. 

import sqlite3 as sql
class Database():
    def __init__(self,database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_books(self):
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS favorite_books
        (id INTEGER PRIMARY KEY,
        book_name VARCHAR(50),
        author VARCHAR(50),
        year_of_publishing INTEGER)
        ''')

        self.con.commit()

    def insert_table_books(self, data):
        self.cur.executemany('''INSERT INTO favorite_books (id, book_name, author, year_of_publishing) VALUES (?, ?, ?, ?)''', data)
        self.con.commit()
    
    def get_all_info(self):
        sql_select_query = '''SELECT * FROM favorite_books'''
        self.cur.execute(sql_select_query)
        result = self.cur.fetchall()
        return print('Данные обо всех книгах', result)

    def get_info_by_id(self, id):
        sql_select_query ='''SELECT * FROM favorite_books WHERE ID = {}'''.format(id)
        self.cur.execute(sql_select_query)
        result = self.cur.fetchall()
        return print('Книга с указанным номером', id ,  ':', result)

    def close(self):
        self.con.close()
def main():

    favorite_books = [
        [1, 'Апгрейд обезьяны', 'Никонов А.П', 2004], 
        [2,'45 татуировок менеджера','Максим Батырев', 2014], 
        [3,'Самый богатый человек в Вавилоне', 'Джордж Клейсон', 1926],
        [4,'Монах, который продал свой феррари', 'Робин Шарма', 1996]
        ]

    db1 = Database('favorite_books.db')
    db1.create_table_books()
    db1.insert_table_books(favorite_books)

    db1.get_all_info()
    db1.get_info_by_id(2)

if __name__ == '__main__':
    main()



