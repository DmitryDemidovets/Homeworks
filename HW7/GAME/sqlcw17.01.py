import sqlite3 as sql
#способ подключения
con = sql.connect("pygame.db")
# управление БД
cur = con.cursor()
# создание базы данных
cur.execute(***
   CREATE TABLE IF NOt ExISTS users (
    name TEXT,
    lvl INTEGER, 
    score INTEGER,
   )***)
con.close
