import sqlite3 as sql
from sqlite3 import Error
 
 
def sql_connection():
    try:
        con = sql.connect('office.db')
        return con
    except Error:
        print(Error)
 
 
def sql_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE employee(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()
 
 
def sql_insert(con, data):
    cur = con.cursor()
    cur.execute("INSERT INTO employee(id, name, salary, department, position, hireDate) VALUES(?,?,?,?,?,?)", data)
    con.commit()
 
def sql_update(con):
    cur = con.cursor()
    cur.execute("UPDATE employee SET name='Alex' where id=1")
    con.commit()
 
 
data = (2, 'Andrew', 1900, 'IT', 'Frontend', '2007-02-02' )
 
con = sql_connection()
# sql_table(con)
sql_insert(con, data)
sql_update(con)

resL = [ x.replace('_', ' ') for x in L ]