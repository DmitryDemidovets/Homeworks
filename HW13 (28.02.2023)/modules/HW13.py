#Колонтитул: [СОКРАЩЕННЫЙ ЗАГОЛОВОК ДО 50 СИМВОЛОВ] 1
#Используя sqlAlchemy создать базу и несколько таблиц (любые)
#Реализовать:
#1) Cвязи один к одному
#Многое ко многим
#Один ко многим
# 2) InnerJOIN
#LeftJOIN
#RightJOIN

import sqlalchemy as db

engine = db.create_engine('sqlite:///cars.db')

connection = engine.connect()

metadata = db.MetaData()
# создаем таблицу автомобили

cars = db.Table('cars', metadata
    db.Column('car_id', db.Integer, primary_key=True),
    db.Column(car_model, db.Integer),
    db.Column(car_quantity, db.Integer),
    db.Column(car_price, db.Integer)
)
metadata.create_all(engine)




