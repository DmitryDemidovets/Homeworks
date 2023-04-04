#Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 долларов. 
# Вывести: model, speed и hd

from models.database import engine
from sqlalchemy.orm import Session
from models.pc import PC
from models.product import Product

def get_query1(value):
    with Session(autoflush=False, bind=engine) as db:
        result = db.query(
            PC.speed, 
            PC.hd, 
            Product.manufacturer,
            Product.model
            ).join(
            Product,
            Product.id == PC.model_id,
            isouter = True
            ).filter(
            PC.price < value).all()
                    
        for u in result:
            print(f'Manufacturer: {u.manufacturer} Model: {u.model} Speed: {u.speed} HDD: {u.hd}')