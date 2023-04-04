#Найдите номер модели, объем памяти и размеры экранов ноутбуков, цена которых превышает 1000 долларов  


from models.database import engine
from sqlalchemy.orm import Session
from models.laptop import Laptop
from models.product import Product

def get_query2(value):
    with Session(autoflush=False, bind=engine) as db:
        result = db.query(
            Laptop.ram, 
            Laptop.screen, 
            Product.manufacturer,
            Product.model
            ).join(
            Product,
            Product.id == Laptop.model_id,
            isouter = True
            ).filter(
            Laptop.price > value).all()
            
        for u in result:
            print(f'Manufacturer: {u.manufacturer} Model: {u.model} RAM: {u.ram} Screen Size: {u.screen}')